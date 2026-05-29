# AI Value System Civilization Simulation

This repository presents a conceptual comparative simulation exploring how different AI value systems and objective functions may influence long-term civilization sustainability.

This model does not provide empirical proof, real-world prediction, or policy recommendations.

---

## Purpose

As AI, AGI, and ASI systems become increasingly capable, the question of *what they are asked to optimize* becomes critically important. This repository offers a simplified conceptual model to explore how different AI evaluation axes — what an AI is told to value — may shape the long-term trajectory of civilization.

This simulation does **not** argue that AI is inherently safe or dangerous. It treats the danger question as one of **value alignment**: not merely "how intelligent is the AI?" but "what is it optimizing for, and on what timescale?"

---

## Scenarios

Five hypothetical AI value system scenarios are compared:

| # | Scenario | Core Priority |
|---|----------|--------------|
| 1 | **Human-Centered Growth** | Short-term utility, economic growth, consumer convenience |
| 2 | **Dualistic Power Optimization** | Dominance, military/economic competition, in-group control |
| 3 | **Techno-Optimism Without Wisdom** | Innovation and efficiency, without ecological or governance grounding |
| 4 | **Artificial Wisdom Civilization** | Natural law, harmony, circularity, long-term sustainability, governance |
| 5 | **Transitional Civilization** | Begins near scenario 1, transitions toward scenario 4 at mid-run |

See [VALUE_SYSTEMS.md](VALUE_SYSTEMS.md) for detailed descriptions of each scenario.

---

## Indicators

All indicators are **hypothetical normalized values (0.0–1.0)**. They are not measured data.

| Indicator | Direction | Meaning |
|-----------|-----------|---------|
| ecological_health | higher = better | Overall ecological system health |
| carbon_sink_capacity | higher = better | Carbon fixation and absorption capacity |
| soil_microbiome_health | higher = better | Soil and microbial ecosystem health |
| water_cycle_stability | higher = better | Stability of water circulation systems |
| resource_circularity | higher = better | Resource recycling and circular economy |
| technology_capacity | higher = better | Technological capability |
| human_wellbeing | higher = better | Human welfare and quality of life |
| social_harmony | higher = better | Social cohesion and cooperation |
| governance_quality | higher = better | Quality of governance and oversight |
| conflict_pressure | **lower = better** | Conflict and domination pressure |
| thermal_stress | **lower = better** | Thermal/climate stress |
| sustainability_index | higher = better | Composite sustainability (computed) |

---

## Output Files

### Figures (`figures/`)

| File | Description |
|------|-------------|
| `sustainability_index_comparison.png` | Composite sustainability over time by scenario |
| `ecological_health_comparison.png` | Ecological health trajectory |
| `human_wellbeing_comparison.png` | Human wellbeing trajectory |
| `conflict_pressure_comparison.png` | Conflict pressure trajectory (lower = better) |
| `thermal_stress_comparison.png` | Thermal stress trajectory (lower = better) |

### Data (`results/`)

| File | Description |
|------|-------------|
| `civilization_simulation_results.csv` | Full step-by-step results for all scenarios |
| `final_scenario_comparison.csv` | Final-step state comparison across scenarios |

---

## How to Run

```bash
pip install -r requirements.txt
python run_all.py
```

---

## Important Notices

- All output values are **hypothetical normalized indicators**, not real-world measurements.
- This model **may suggest** possible directional tendencies under simplified assumptions.
- This model **does not prove** that any value system will succeed or fail.
- This model **does not predict** future civilization trajectories.
- This model **does not recommend** specific policies or AI designs.
- Real-world dynamics are far more complex than this simplified model.
- Further interdisciplinary validation is required before drawing any practical conclusions.
- See [SIMULATION_LIMITATIONS.md](SIMULATION_LIMITATIONS.md) for the full disclaimer.

> **Note on the Artificial Wisdom scenario:** Even in the Artificial Wisdom Civilization scenario, the model should not be interpreted as suggesting perfect safety, complete ecological recovery, or zero conflict. Residual risks, external shocks, implementation limits, governance friction, and complex-system uncertainty remain in all scenarios. Artificial Wisdom is represented here as a proposed value-system direction that may improve long-term sustainability under simplified assumptions, not as a guaranteed solution.

---

## File Overview

See [PROJECT_MAP.md](PROJECT_MAP.md) for a complete file listing and recommended reading order.

---

## Keywords / Hashtags

`#AIValueAlignment` `#CivilizationSimulation` `#AGISafety` `#ArtificialWisdom`
`#ConceptualModel` `#Sustainability` `#EcologicalHealth` `#LongTermThinking`
`#ValueSystems` `#AIEthics` `#GovernanceQuality` `#HypotheticalIndicators`

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
