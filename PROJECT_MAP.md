# Project Map

This document lists every file in the repository and its role.

---

## Parent Framework

This simulation repository is connected to the broader theoretical framework:

- **Will Superintelligent AI Cause Human Extinction?**  
  https://github.com/InchaComisho/Will-Superintelligent-AI-Cause-Human-Extinction-

That repository provides the conceptual foundation for reframing AI, AGI, and ASI risk through value systems, objective functions, Natural Law, the Six Principles, and Artificial Wisdom.

This repository provides a simplified conceptual simulation that explores how different AI value systems may influence civilization sustainability indicators under simplified assumptions.

Important note: this simulation does not provide empirical proof, real-world prediction, or policy recommendations. It uses hypothetical normalized indicators for conceptual comparison only.

---

## Recommended Reading Order

For someone new to this project:

1. [README.md](README.md) — Start here: overview, purpose, and how to run
2. [MODEL_DESCRIPTION.md](MODEL_DESCRIPTION.md) — Plain-language explanation of what the model does
3. [VALUE_SYSTEMS.md](VALUE_SYSTEMS.md) — Detailed description of the five scenarios
4. [ARTIFICIAL_WISDOM_METRICS.md](ARTIFICIAL_WISDOM_METRICS.md) — Proposed evaluation axes for the wisdom scenario
5. [SIMULATION_LIMITATIONS.md](SIMULATION_LIMITATIONS.md) — Important disclaimers — read before drawing conclusions
6. [scenario_definitions.py](scenario_definitions.py) — Scenario parameters (Python)
7. [model_utils.py](model_utils.py) — Utility functions (Python)
8. [civilization_value_system_simulation.py](civilization_value_system_simulation.py) — Main simulation logic (Python)
9. [run_all.py](run_all.py) — Entry point to run the simulation

---

## File Index

### Documentation

| File | Type | Role |
|------|------|------|
| [README.md](README.md) | Markdown | Project overview, scenarios, indicators, how to run, license |
| [MODEL_DESCRIPTION.md](MODEL_DESCRIPTION.md) | Markdown | Plain-language model explanation for non-technical readers |
| [VALUE_SYSTEMS.md](VALUE_SYSTEMS.md) | Markdown | Detailed description of all five AI value system scenarios |
| [ARTIFICIAL_WISDOM_METRICS.md](ARTIFICIAL_WISDOM_METRICS.md) | Markdown | Proposed evaluation axes for the Artificial Wisdom scenario |
| [SIMULATION_LIMITATIONS.md](SIMULATION_LIMITATIONS.md) | Markdown | Full disclaimer and limitations of this conceptual model |
| [PROJECT_MAP.md](PROJECT_MAP.md) | Markdown | This file — index of all files and recommended reading order |

### Python Source

| File | Role |
|------|------|
| [run_all.py](run_all.py) | Entry point — `python run_all.py` to run everything |
| [civilization_value_system_simulation.py](civilization_value_system_simulation.py) | Main simulation: runs all scenarios, saves CSV and figures |
| [scenario_definitions.py](scenario_definitions.py) | Defines the 5 scenario parameter sets and descriptions |
| [model_utils.py](model_utils.py) | Shared utilities: clamping, sustainability index, plotting, CSV export |

### Configuration

| File | Role |
|------|------|
| [requirements.txt](requirements.txt) | Python package dependencies (numpy, pandas, matplotlib) |

### Generated Output (created when simulation is run)

| Path | Description |
|------|-------------|
| `results/civilization_simulation_results.csv` | Full step-by-step results for all scenarios |
| `results/final_scenario_comparison.csv` | Final-step comparison table |
| `figures/sustainability_index_comparison.png` | Composite sustainability over time |
| `figures/ecological_health_comparison.png` | Ecological health over time |
| `figures/human_wellbeing_comparison.png` | Human wellbeing over time |
| `figures/conflict_pressure_comparison.png` | Conflict pressure over time |
| `figures/thermal_stress_comparison.png` | Thermal stress over time |

---

## Cooperation Credit

Conceptual development supported by:
- Cruz: Claude by Anthropic

---

## License

CC BY-SA 4.0
This work is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License.
You are free to share and adapt this material, including for commercial purposes, under the following terms:

* Attribution is required.
* Derivative works must be distributed under the same license.

License details: https://creativecommons.org/licenses/by-sa/4.0/
