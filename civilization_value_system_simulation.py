"""
civilization_value_system_simulation.py

Conceptual comparative simulation: how different AI value systems may influence
long-term civilization sustainability.

IMPORTANT DISCLAIMER:
- This is a simplified conceptual simulation.
- All indicators are hypothetical normalized values (0.0–1.0).
- This is NOT empirical data, NOT a scientific prediction, NOT policy advice.
- It does NOT prove that any value system is correct or will inevitably succeed/fail.
- It only illustrates possible tendencies under simplified assumptions.
- Real-world civilization dynamics are far more complex.
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

TOTAL_STEPS = 130   # ~100–150 steps as specified

# Initial civilization state shared across all scenarios (hypothetical baseline)
INITIAL_STATE = {
    "ecological_health": 0.62,
    "carbon_sink_capacity": 0.58,
    "soil_microbiome_health": 0.60,
    "water_cycle_stability": 0.64,
    "resource_circularity": 0.35,
    "technology_capacity": 0.50,
    "human_wellbeing": 0.65,
    "social_harmony": 0.65,
    "governance_quality": 0.58,
    "conflict_pressure": 0.30,
    "thermal_stress": 0.32,
    "sustainability_index": 0.0,  # computed each step
}


def _get_effective_params(params: dict, step: int) -> dict:
    """
    Return the active parameter set for a given step.
    For Transitional Civilization, blend phase-2 params after transition_step.
    """
    transition = params.get("transition_step")
    if transition is None or step < transition:
        return params

    # Post-transition: use phase-2 values where defined
    p = dict(params)
    for key in [
        "tech_growth_rate", "ecology_decay_rate", "circularity_improvement",
        "conflict_growth_rate", "thermal_stress_rate", "harmony_drift",
        "governance_drift",
    ]:
        p2_key = key + "_p2"
        if p2_key in params:
            # Smooth blend: ramp over 20 steps
            progress = min(1.0, (step - transition) / 20.0)
            p[key] = params[key] * (1 - progress) + params[p2_key] * progress
    return p


def step_state(state: dict, params: dict, step: int) -> dict:
    """
    Advance civilization state by one conceptual simulation step.

    Uses simple linear dynamics with coupling terms.
    All dynamics are hypothetical — chosen to illustrate directional tendencies,
    not to model real-world causation with precision.
    """
    p = _get_effective_params(params, step)
    s = dict(state)

    # Small noise to avoid perfectly smooth curves (conceptual variability)
    noise = lambda scale=0.003: np.random.normal(0, scale)

    # --- Ecological subsystem ---
    ecology_pressure = p["ecology_decay_rate"]
    # Circularity partially offsets ecological pressure
    circularity_help = s["resource_circularity"] * 0.010
    s["ecological_health"] = clamp(
        s["ecological_health"] - ecology_pressure + circularity_help + noise()
    )
    s["carbon_sink_capacity"] = clamp(
        s["carbon_sink_capacity"] + 0.7 * (s["ecological_health"] - 0.5) * 0.003
        - ecology_pressure * 0.8 + noise(0.002)
    )
    s["soil_microbiome_health"] = clamp(
        s["soil_microbiome_health"] + 0.6 * (s["ecological_health"] - 0.5) * 0.003
        - ecology_pressure * 0.6 + noise(0.002)
    )
    s["water_cycle_stability"] = clamp(
        s["water_cycle_stability"] + 0.5 * (s["ecological_health"] - 0.5) * 0.002
        - p["thermal_stress_rate"] * 0.5 + noise(0.002)
    )

    # --- Resource & technology ---
    s["resource_circularity"] = clamp(
        s["resource_circularity"] + p["circularity_improvement"] + noise(0.002)
    )
    s["technology_capacity"] = clamp(
        s["technology_capacity"] + p["tech_growth_rate"] * 0.5
        - (1 - s["governance_quality"]) * 0.005 + noise(0.003)
    )

    # --- Social subsystem ---
    s["human_wellbeing"] = clamp(
        s["human_wellbeing"]
        + 0.4 * (s["technology_capacity"] - 0.5) * 0.002
        + 0.3 * (s["ecological_health"] - 0.5) * 0.0015
        - s["conflict_pressure"] * 0.002
        + noise(0.002)
    )
    s["social_harmony"] = clamp(
        s["social_harmony"] + p["harmony_drift"]
        - s["conflict_pressure"] * 0.003 + noise(0.002)
    )
    s["governance_quality"] = clamp(
        s["governance_quality"] + p["governance_drift"]
        + 0.2 * (s["social_harmony"] - 0.5) * 0.001 + noise(0.002)
    )

    # --- Stress indicators (higher = worse) ---
    s["conflict_pressure"] = clamp(
        s["conflict_pressure"] + p["conflict_growth_rate"]
        + (1 - s["governance_quality"]) * 0.001 + noise(0.002)
    )
    s["thermal_stress"] = clamp(
        s["thermal_stress"] + p["thermal_stress_rate"]
        - s["resource_circularity"] * 0.0012 + noise(0.002)
    )

    # --- Composite sustainability index ---
    s["sustainability_index"] = compute_sustainability_index(s)

    return s


def run_scenario(name: str) -> list:
    """
    Run a single scenario for TOTAL_STEPS steps.
    Returns list of state dicts (one per step, including step 0).
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
    """Run all 5 scenarios. Returns dict mapping name → history."""
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
