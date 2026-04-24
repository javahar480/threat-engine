MAP = {
    "beaconing": "T1071",
    "multi_stage_attack": "T1071"
}

def map_to_mitre(t):
    return MAP.get(t, "unknown")
