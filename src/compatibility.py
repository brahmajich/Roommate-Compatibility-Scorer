def calculate_compatibility(roommate1, roommate2):
    score = 0

    # Sleep Time Compatibility
    if roommate1['sleep_time'] == roommate2['sleep_time']:
        score += 25
    else:
        score += 10

    # Cleanliness Compatibility
    if roommate1['cleanliness'] == roommate2['cleanliness']:
        score += 25
    else:
        score += 10

    # Work Schedule Compatibility
    if roommate1['work_schedule'] == roommate2['work_schedule']:
        score += 25
    else:
        score += 10

    # Food Habits Compatibility
    if roommate1['food_habits'] == roommate2['food_habits']:
        score += 25
    else:
        score += 10

    return min(score, 100)  # Ensure the score doesn't exceed 100
