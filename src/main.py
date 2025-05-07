import pandas as pd
from src.data_loader import load_roommate_data
from src.ranking import rank_roommate_pairs


def main():
    # Load the roommate data
    df = load_roommate_data('data/roommates.csv')

    # Convert data to a list of profiles
    profiles = df.to_dict(orient='records')

    # Rank roommate pairs based on compatibility scores
    ranked_matches = rank_roommate_pairs(profiles)

    # Display the ranked results
    print("Ranked Matches based on Compatibility Score:")
    for match in ranked_matches:
        print(f"{match['Roommate1']} & {match['Roommate2']} - Score: {match['Compatibility_Score']}")


if __name__ == "__main__":
    main()
