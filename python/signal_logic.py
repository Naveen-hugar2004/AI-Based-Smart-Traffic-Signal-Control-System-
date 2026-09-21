def decide_signal(vehicle_count: int, low_threshold: int = 5, high_threshold: int = 15) -> str:
    if vehicle_count < low_threshold:
        return "GREEN"
    if vehicle_count < high_threshold:
        return "YELLOW"
    return "RED"
