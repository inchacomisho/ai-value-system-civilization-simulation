"""
civilization_value_system_simulation.py

Conceptual comparative simulation: how different AI value systems may influence
long-term civilization sustainability.

IMPORTANT DISCLAIMER:
- This is a simplified conceptual simulation.
- All indicators are hypothetical normalized values (0.0-1.0).
- This is NOT empirical data, NOT a scientific prediction, NOT policy advice.
- It does NOT prove that any value system is correct or will inevitably succeed/fail.
- It only illustrates possible tendencies under simplified assumptions.
- Real-world civilization dynamics are far more complex.
- Even the Artificial Wisdom scenario retains residual risks and realistic ceilings.
  Residual risk sources include: external shocks, climate lag, governance friction,
  institutional inertia, geopolitical complexity, and unpredictable system dynamics.
"""

import numpy as np
from scenario_definitions import SCENARIOS
from model_utils import (
    clamp, clamp_state, compute_sustainability_index,
    plot_indicator, save_full_results, save_final_comparison, print_final_table,
)

# Fixed seed for reproducibility — conceptual model, not a stochastic predictor
RNG_SEED = 42
np.random.seed(RNG_SEED)

TOTAL_STEPS = 130   # ~100-150 steps as specified

# Initial civilization state shared across all scenarios (hypothetical baseline)
INITIAL_STATE = {
    "ecological_health":      0.62,
    "carbon_sink_capacity":   0.58,
    "soil_microbiome_health": 0.60,
    "water_cycle_stability":  0.64,
    "resource_circularity":   0.35,
    "technology_capacity":    0.50,
    "human_wellbeing":        0.65,
    "social_harmony":         0.65,
    "governance_quality":     0.58,
    "conflict_pressure":      0.30,
    "thermal_stress":         0.32,
    "sustainability_index":   0.0,   # computed each step
}

# ---------------------------------------------------------------------------
# Realistic ceilings for positive indicators.
# Design rationale: even under optimal value systems, perfect recovery is not
# assumed in this conceptual model. These ceilings avoid implying that any
# value system is a "complete solution." Not empirical limits — conceptual
# design choices to prevent 1.0 saturation.
# ---------------------------------------------------------------------------
INDICATOR_CEILINGS = {
    "ecological_health":      0.93,
    "carbon_sink_capacity":   0.91,
    "soil_microbiome_health": 0.90,
    "water_cycle_stability":  0.90,
    "resource_circularity":   0.88,
    "social_harmony":         0.87,
    "governance_quality":     0.85,
}

# ---------------------------------------------------------------------------
# Residual risk floors for stress indicators.
# Even under optimal value systems, some conflict pressure and thermal stress
# remain in this conceptual model. Conceptual residual risk sources include:
# external shocks, climate lag, governance friction, geopolitical complexity,
# ecological recovery delay, and implementation limits. Not zero risk.
# ---------------------------------------------------------------------------
STRESS_FLOORS = {
    "conflict_pressure": 0.08,
    "thermal_stress":    0.10,
}

# ---------------------------------------------------------------------------
# Deterministic external shocks at fixed steps.
# These represent conceptual stress factors common to all scenarios:
# no value system fully controls climate events, governance friction, or
# resource constraints. Not real-world predictions — simplified conceptual
# stress pulses applied uniformly across scenarios.
# ---------------------------------------------------------------------------
SHOCKS = {
    25: {"ecological_health": -0.025, "thermal_stress":        +0.018},
    40: {"conflict_pressure": +0.018, "governance_quality":    -0.015},
    65: {"resource_circularity": -0.018, "water_cycle_stability": -0.012},
}


def _dr(delta: float, current: float, ceiling: float = 1.0) -> float:
    """
    Diminishing returns: reduces a positive improvement delta as the indicator
    approaches its ceiling.

    Formula: delta * (headroom / ceiling) ** 1.2
    - Full speed when indicator is far below ceiling.
    - Progressively slower as indicator nears ceiling.
    - Negative deltas (degradation) pass through unchanged.

    Conceptual device — not an empirical law.
    """
    if delta > 0 and ceiling > 0:
        headroom = max(0.0, ceiling - current)
        return delta * (headroom / ceiling) ** 1.2
    return delta


def _apply_shocks(s: dict, step: int) -> dict:
    """
    Apply deterministic external shocks at fixed steps.
    Shocks are small, affect all scenarios equally, and respect floors/ceilings.
    Conceptual stress factors only — not real-world event predictions.
    """
    if step in SHOCKS:
        for key, delta in SHOCKS[step].items():
            floor = STRESS_FLOORS.get(key, 0.0)
            ceil  = INDICATOR_CEILINGS.get(key, 1.0)
            s[key] = clamp(s[key] + delta, lo=floor, hi=ceil)
    return s


def _get_effective_params(params: dict, step: int) -> dict:
    """
    Return the active parameter set for a given step.
    For Transitional Civilization, blend phase-2 params after transition_step.
    """
    transition = params.get("transition_step")
    if transition is None or step < transition:
        return params

    p = dict(params)
    for key in [
        "tech_growth_rate", "ecology_decay_rate", "circularity_improvement",
        "conflict_growth_rate", "thermal_stress_rate", "harmony_drift",
        "governance_drift",
    ]:
        p2_key = key + "_p2"
        if p2_key in params:
            # Smooth blend over 20 steps after transition
            progress = min(1.0, (step - transition) / 20.0)
            p[key] = params[key] * (1 - progress) + params[p2_key] * progress
    return p


def step_state(state: dict, params: dict, step: int) -> dict:
    """
    Advance civilization state by one conceptual simulation step.

    Key design choices (not empirical):
    - Positive improvements use diminishing returns: faster far from ceiling,
      slower near it. Prevents 1.0 saturation.
    - Stress indicators use residual risk floors: prevents 0.0 saturation.
    - Realistic ceilings clamp positive indicators below 1.0.
    - Deterministic external shocks apply at steps 25, 40, 65 to all scenarios.
    - All parameters are hypothetical. Not real-world causation models.
    """
    p = _get_effective_params(params, step)
    s = dict(state)

    # Small noise for conceptual variability (fixed seed = reproducible)
    noise = lambda scale=0.002: np.random.normal(0, scale)

    # --- Ecological subsystem ---
    # net_eco: positive = recovery, negative = degradation
    # ecology_decay_rate > 0 means degradation; < 0 means recovery (AW scenario)
    eco_ceil = INDICATOR_CEILINGS["ecological_health"]
    net_eco = -p["ecology_decay_rate"] + s["resource_circularity"] * 0.008
    s["ecological_health"] = clamp(
        s["ecological_health"] + _dr(net_eco, s["ecological_health"], eco_ceil) + noise(),
        hi=eco_ceil
    )

    csink_ceil = INDICATOR_CEILINGS["carbon_sink_capacity"]
    net_csink = 0.7 * (s["ecological_health"] - 0.5) * 0.003 - p["ecology_decay_rate"] * 0.8
    s["carbon_sink_capacity"] = clamp(
        s["carbon_sink_capacity"] + _dr(net_csink, s["carbon_sink_capacity"], csink_ceil) + noise(),
        hi=csink_ceil
    )

    smb_ceil = INDICATOR_CEILINGS["soil_microbiome_health"]
    net_smb = 0.6 * (s["ecological_health"] - 0.5) * 0.003 - p["ecology_decay_rate"] * 0.6
    s["soil_microbiome_health"] = clamp(
        s["soil_microbiome_health"] + _dr(net_smb, s["soil_microbiome_health"], smb_ceil) + noise(),
        hi=smb_ceil
    )

    wcs_ceil = INDICATOR_CEILINGS["water_cycle_stability"]
    net_wcs = 0.5 * (s["ecological_health"] - 0.5) * 0.002 - p["thermal_stress_rate"] * 0.5
    s["water_cycle_stability"] = clamp(
        s["water_cycle_stability"] + _dr(net_wcs, s["water_cycle_stability"], wcs_ceil) + noise(),
        hi=wcs_ceil
    )

    # --- Resource & technology ---
    rc_ceil = INDICATOR_CEILINGS["resource_circularity"]
    s["resource_circularity"] = clamp(
        s["resource_circularity"] + _dr(p["circularity_improvement"], s["resource_circularity"], rc_ceil) + noise(),
        hi=rc_ceil
    )
    s["technology_capacity"] = clamp(
        s["technology_capacity"] + p["tech_growth_rate"] * 0.5
        - (1 - s["governance_quality"]) * 0.004 + noise()
    )

    # --- Social subsystem ---
    s["human_wellbeing"] = clamp(
        s["human_wellbeing"]
        + 0.4 * (s["technology_capacity"] - 0.5) * 0.002
        + 0.3 * (s["ecological_health"] - 0.5) * 0.0015
        - s["conflict_pressure"] * 0.002
        + noise()
    )

    sh_ceil = INDICATOR_CEILINGS["social_harmony"]
    net_sh = p["harmony_drift"] - s["conflict_pressure"] * 0.003
    s["social_harmony"] = clamp(
        s["social_harmony"] + _dr(net_sh, s["social_harmony"], sh_ceil) + noise(),
        hi=sh_ceil
    )

    gq_ceil = INDICATOR_CEILINGS["governance_quality"]
    net_gq = p["governance_drift"] + 0.2 * (s["social_harmony"] - 0.5) * 0.001
    s["governance_quality"] = clamp(
        s["governance_quality"] + _dr(net_gq, s["governance_quality"], gq_ceil) + noise(),
        hi=gq_ceil
    )

    # --- Stress indicators with residual risk floors ---
    # Even under optimal conditions, conflict and thermal stress do not reach zero.
    # Floors represent conceptual residual risk: external shocks, climate lag,
    # governance friction, and complexity effects. Not a prediction of minimum values.
    cp_floor = STRESS_FLOORS["conflict_pressure"]
    net_cp = p["conflict_growth_rate"] + (1 - s["governance_quality"]) * 0.001
    s["conflict_pressure"] = clamp(
        s["conflict_pressure"] + net_cp + noise(),
        lo=cp_floor
    )

    ts_floor = STRESS_FLOORS["thermal_stress"]
    net_ts = p["thermal_stress_rate"] - s["resource_circularity"] * 0.0010
    s["thermal_stress"] = clamp(
        s["thermal_stress"] + net_ts + noise(),
        lo=ts_floor
    )

    # --- Deterministic external shocks (conceptual stress factors) ---
    s = _apply_shocks(s, step)

    # --- Composite sustainability index ---
    s["sustainability_index"] = compute_sustainability_index(s)

    return s


def run_scenario(name: str) -> list:
    """
    Run a single scenario for TOTAL_STEPS steps.
    Returns list of state dicts (one per step including step 0).
    """
    params = SCENARIOS[name]["params"]
    state = {k: v for k, v in INITIAL_STATE.items()}
    state["sustainability_index"] = compute_sustainability_index(state)

    history = [dict(state)]
    for step in range(1, TOTAL_STEPS + 1):
        state = step_state(state, params, step)
        history.append(dict(state))
    return history


def run_all_scenarios() -> dict:
    """Run all 5 scenarios. Returns dict mapping name -> history."""
    results = {}
    for name in SCENARIOS:
        print(f"  Running scenario: {name}")
        results[name] = run_scenario(name)
    return results


def main():
    print("\n" + "=" * 70)
    print("AI Value System Civilization Simulation - Conceptual Model")
    print("Hypothetical normalized indicators only. Not predictions. Not proof.")
    print("=" * 70 + "\n")

    print("[1/4] Running scenarios...")
    results = run_all_scenarios()

    print("\n[2/4] Saving CSV results...")
    save_full_results(results, "results/civilization_simulation_results.csv")
    save_final_comparison(results, "results/final_scenario_comparison.csv")

    print("\n[3/4] Generating figures...")
    for indicator, filename in [
        ("sustainability_index",  "figures/sustainability_index_comparison.png"),
        ("ecological_health",     "figures/ecological_health_comparison.png"),
        ("human_wellbeing",       "figures/human_wellbeing_comparison.png"),
        ("conflict_pressure",     "figures/conflict_pressure_comparison.png"),
        ("thermal_stress",        "figures/thermal_stress_comparison.png"),
    ]:
        plot_indicator(results, indicator, filename, TOTAL_STEPS)

    print("\n[4/4] Final comparison table:")
    print_final_table(results)

    print("\nConceptual simulation complete.")
    print("See results/ and figures/ directories for output.")
    print("Reminder: all values are hypothetical. Not empirical. Not predictions.\n")


if __name__ == "__main__":
    main()
