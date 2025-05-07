from src.compatibility import calculate_compatibility


def rank_roommate_pairs(profiles):
    results = []

    for i in range(len(profiles)):
        for j in range(i + 1, len(profiles)):
            compatibility_score = calculate_compatibility(profiles[i], profiles[j])
            results.append({
                'Roommate1': profiles[i]['name'],
                'Roommate2': profiles[j]['name'],
                'Compatibility_Score': compatibility_score
            })

    return sorted(results, key=lambda x: x['Compatibility_Score'], reverse=True)
