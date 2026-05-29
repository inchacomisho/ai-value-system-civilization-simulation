"""
scenario_definitions.py
Defines the 5 civilization scenarios and their AI value system parameters.

NOTE: All parameter values are hypothetical normalized indicators for conceptual
comparison only. Not empirical data, not predictions, not policy recommendations.
"""

SCENARIOS = {
    "Human-Centered Growth": {
        "description": (
            "AI value system prioritizing short-term human benefit, economic growth, "
            "consumption, and convenience. Ecological and long-term costs are discounted."
        ),
        "priorities": ["economic output", "consumer convenience", "short-term welfare"],
        "deprioritizes": ["ecological health", "long-term sustainability", "resource circularity"],
        "params": {
            # How quickly the economy grows (boosts technology, wellbeing short-term)
            "tech_growth_rate": 0.005,
            # How fast ecological health degrades under this value system
            "ecology_decay_rate": 0.004,
            # Rate of resource circularity improvement (low under growth-first logic)
            "circularity_improvement": 0.0008,
            # Conflict tendency (moderate — competition for resources)
            "conflict_growth_rate": 0.002,
            # Thermal stress increase rate
            "thermal_stress_rate": 0.003,
            # Social harmony trajectory (initially high, erodes over time)
            "harmony_initial": 0.70,
            "harmony_drift": -0.0008,
            # Governance quality (moderate, mainly serving economic interests)
            "governance_initial": 0.60,
            "governance_drift": -0.0004,
            # Wellbeing initial level
            "wellbeing_initial": 0.72,
            # Whether a mid-run value transition occurs
            "transition_step": None,
        },
    },

    "Dualistic Power Optimization": {
        "description": (
            "AI value system prioritizing dominance, military/economic competition, "
            "control, and in-group advantage. Cooperation and ecology are sacrificed "
            "for strategic superiority."
        ),
        "priorities": ["military capacity", "resource control", "geopolitical dominance"],
        "deprioritizes": ["social harmony", "ecological health", "human dignity globally"],
        "params": {
            "tech_growth_rate": 0.004,
            "ecology_decay_rate": 0.005,
            "circularity_improvement": 0.0003,
            "conflict_growth_rate": 0.005,
            "thermal_stress_rate": 0.004,
            "harmony_initial": 0.50,
            "harmony_drift": -0.0015,
            "governance_initial": 0.45,
            "governance_drift": -0.001,
            "wellbeing_initial": 0.55,
            "transition_step": None,
        },
    },

    "Techno-Optimism Without Wisdom": {
        "description": (
            "AI value system prioritizing technological efficiency and innovation, "
            "but underweighting natural law, ecological feedback, circularity, and "
            "long-term governance. Assumes technology can fix all downstream problems."
        ),
        "priorities": ["innovation", "efficiency", "technological capacity"],
        "deprioritizes": ["natural law alignment", "circularity", "governance wisdom"],
        "params": {
            "tech_growth_rate": 0.007,
            "ecology_decay_rate": 0.003,
            "circularity_improvement": 0.0015,
            "conflict_growth_rate": 0.0015,
            "thermal_stress_rate": 0.0025,
            "harmony_initial": 0.65,
            "harmony_drift": -0.0006,
            "governance_initial": 0.58,
            "governance_drift": 0.0002,
            "wellbeing_initial": 0.70,
            "transition_step": None,
        },
    },

    "Artificial Wisdom Civilization": {
        "description": (
            "AI value system prioritizing natural law compatibility, harmony, circularity, "
            "long-term sustainability, governance quality, and human dignity. "
            "Short-term growth is moderated in favour of systemic health. "
            "NOTE: This is a proposed evaluation direction, not a proven or complete solution."
        ),
        "priorities": [
            "natural law alignment", "ecological regeneration", "circularity",
            "long-term sustainability", "governance quality", "non-violence",
        ],
        "deprioritizes": ["unchecked short-term growth", "dominance", "exploitation"],
        "params": {
            "tech_growth_rate": 0.003,
            "ecology_decay_rate": -0.003,   # ecology recovers under this system
            "circularity_improvement": 0.004,
            "conflict_growth_rate": -0.003,  # conflict reduces
            "thermal_stress_rate": -0.002,   # thermal stress reduces
            "harmony_initial": 0.65,
            "harmony_drift": 0.002,
            "governance_initial": 0.68,
            "governance_drift": 0.002,
            "wellbeing_initial": 0.65,
            "transition_step": None,
        },
    },

    "Transitional Civilization": {
        "description": (
            "Begins close to Human-Centered Growth, then transitions toward "
            "Artificial Wisdom Civilization at step 50. Illustrates the possible "
            "trajectory of a civilizational value shift mid-course."
        ),
        "priorities": ["initially: growth", "then: wisdom and sustainability"],
        "deprioritizes": ["initially: ecology", "then: short-term exploitation"],
        "params": {
            # Phase 1 (steps 0–49): growth-like
            "tech_growth_rate": 0.005,
            "ecology_decay_rate": 0.0035,
            "circularity_improvement": 0.0009,
            "conflict_growth_rate": 0.0018,
            "thermal_stress_rate": 0.003,
            "harmony_initial": 0.68,
            "harmony_drift": -0.0006,
            "governance_initial": 0.60,
            "governance_drift": -0.0002,
            "wellbeing_initial": 0.70,
            # Step at which value system transitions
            "transition_step": 50,
            # Phase 2 params (post-transition, converge toward wisdom scenario)
            "tech_growth_rate_p2": 0.003,
            "ecology_decay_rate_p2": -0.002,
            "circularity_improvement_p2": 0.003,
            "conflict_growth_rate_p2": -0.002,
            "thermal_stress_rate_p2": -0.0015,
            "harmony_drift_p2": 0.0016,
            "governance_drift_p2": 0.002,
        },
    },
}
