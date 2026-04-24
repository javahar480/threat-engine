def calculate_score(data, flags):
    score = 0

    if flags.get("new_ip"):
        score += 20
    if flags.get("beaconing"):
        score += 40
    if flags.get("unknown_process"):
        score += 40

    return score
