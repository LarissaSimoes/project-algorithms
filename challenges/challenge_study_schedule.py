def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    
    if permanence_period is None or any(
        (start is None or not isinstance(start, int)) or 
        (end is None or not isinstance(end, int)) or 
        (end < start) 
        for start, end in permanence_period
    ):
        return None
    
    count = 0
    for start, end in permanence_period:
        if start is not None and end is not None and start <= target_time <= end:
            count += 1
    
    return count
