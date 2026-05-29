"""
model_utils.py
Utility functions for the civilization value system conceptual simulation.

NOTE: All functions operate on hypothetical normalized indicators (0.0–1.0).
Not empirical data. Not predictions. Not policy recommendations.
"""

import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


# ---------------------------------------------------------------------------
# Indicator helpers
# ---------------------------------------------------------------------------

def clamp(value: float, lo: float = 0.0, hi: float = 1.0) -> float:
    """Clamp a hypothetical indicator to [lo, hi]."""
    return float(np.clip(value, lo, hi))


def clamp_state(state: dict) -> dict:
    """Clamp all indicators in a state dict to [0.0, 1.0]."""
    return {k: clamp(v) for k, v in state.items()}


# ---------------------------------------------------------------------------
# Sustainability index
# ---------------------------------------------------------------------------

def compute_sustainability_index(state: dict) -> float:
    """
    Compute a composite sustainability index from civilization state indicators.

    sustainability_index is the weighted mean of positive indicators minus a
    penalty for high-stress indicators.

    This is a simplified conceptual formula — not an empirical metric.
    """
    positive = [
        state["ecological_health"],
        state["carbon_sink_capacity"],
        state["soil_microbiome_health"],
        state["water_cycle_stability"],
        state["resource_circularity"],
        state["technology_capacity"],
        state["human_wellbeing"],
        state["social_harmony"],
        state["governance_quality"],
    ]
    # Higher is worse for stress indicators
    stress_penalty = (state["thermal_stress"] + state["conflict_pressure"]) / 2.0

    raw = np.mean(positive) - 0.5 * stress_penalty
    return clamp(raw)


# ---------------------------------------------------------------------------
# Plotting
# ---------------------------------------------------------------------------

SCENARIO_COLORS = {
    "Human-Centered Growth": "#e07b39",
    "Dualistic Power Optimization": "#c0392b",
    "Techno-Optimism Without Wisdom": "#8e44ad",
    "Artificial Wisdom Civilization": "#27ae60",
    "Transitional Civilization": "#2980b9",
}


def plot_indicator(results_by_scenario: dict, indicator: str,
                   output_path: str, steps: int) -> None:
    """
    Plot a single indicator across all scenarios and save to output_path.

    results_by_scenario: dict mapping scenario name → list of state dicts
    """
    fig, ax = plt.subplots(figsize=(10, 6))

    for name, history in results_by_scenario.items():
        values = [s[indicator] for s in history]
        color = SCENARIO_COLORS.get(name, "#555555")
        ax.plot(range(len(values)), values, label=name, color=color, linewidth=2)

    # Annotate direction of "good"
    if indicator in ("thermal_stress", "conflict_pressure"):
        direction_note = "lower is better"
    else:
        direction_note = "higher is better"

    ax.set_title(
        f"Conceptual Simulation — {indicator.replace('_', ' ').title()}\n"
        f"({direction_note}) | hypothetical normalized indicators only",
        fontsize=12,
    )
    ax.set_xlabel("Simulation Step")
    ax.set_ylabel("Indicator Value (0.0–1.0, hypothetical)")
    ax.set_ylim(0.0, 1.0)
    ax.legend(loc="best", fontsize=9)
    ax.grid(True, alpha=0.3)

    fig.tight_layout()
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    fig.savefig(output_path, dpi=150)
    plt.close(fig)
    print(f"  Saved figure: {output_path}")


# ---------------------------------------------------------------------------
# Results persistence
# ---------------------------------------------------------------------------

def save_full_results(results_by_scenario: dict, output_path: str) -> None:
    """Save step-by-step simulation results to CSV."""
    rows = []
    for name, history in results_by_scenario.items():
        for step, state in enumerate(history):
            row = {"scenario": name, "step": step}
            row.update(state)
            rows.append(row)

    df = pd.DataFrame(rows)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"  Saved CSV: {output_path}")


def save_final_comparison(results_by_scenario: dict, output_path: str) -> None:
    """Save only the final-step state of each scenario to CSV."""
    rows = []
    for name, history in results_by_scenario.items():
        final = history[-1].copy()
        final["scenario"] = name
        rows.append(final)

    df = pd.DataFrame(rows).set_index("scenario")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path)
    print(f"  Saved final comparison CSV: {output_path}")


def print_final_table(results_by_scenario: dict) -> None:
    """Print a formatted final-state comparison table to stdout."""
    indicators = [
        "ecological_health", "carbon_sink_capacity", "soil_microbiome_health",
        "water_cycle_stability", "resource_circularity", "technology_capacity",
        "human_wellbeing", "social_harmony", "governance_quality",
        "conflict_pressure", "thermal_stress", "sustainability_index",
    ]
    header = f"{'Scenario':<40}" + "".join(f"{ind[:8]:>10}" for ind in indicators)
    print("\n" + "=" * len(header))
    print("CONCEPTUAL SIMULATION - FINAL STATE COMPARISON (hypothetical indicators)")
    print("Not empirical data. Not predictions. Not policy recommendations.")
    print("=" * len(header))
    print(header)
    print("-" * len(header))
    for name, history in results_by_scenario.items():
        final = history[-1]
        row = f"{name:<40}" + "".join(f"{final[ind]:>10.3f}" for ind in indicators)
        print(row)
    print("=" * len(header))
