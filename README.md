Roommate Compatibility Scorer
Welcome to the Roommate Compatibility Scorer project! This Python-based application helps you find the best roommate match based on their preferences. The idea is to rate how compatible two roommates are with each other, considering factors like sleep time, cleanliness, work schedule, and food habits.

This is a Python-based application designed to help individuals or systems recommend the best roommates based on their preferences. The application allows users to input various factors such as sleep schedules, cleanliness habits, work hours, and food preferences. It then calculates a compatibility score to assess how well two people would get along as roommates.

Whether you are a landlord looking for the perfect roommate match, building a roommate-finding app, or simply curious about roommate compatibility, this project provides a simple yet effective way to calculate compatibility based on different preferences.

Table of Contents
Project Overview

Features

Technologies Used

Setup Instructions

Usage

File Structure

Example

Contributing

License

Project Overview
The Roommate Compatibility Scorer is designed to help individuals or systems recommend compatible roommates based on shared preferences. Whether you're moving into a new apartment, creating a roommate-finding app, or just curious about roommate compatibility, this project offers a simple yet effective solution.

By inputting a roommate's sleep schedule, cleanliness habits, work schedule, and food preferences, the algorithm calculates a compatibility score ranging from 0 to 100. The closer the score is to 100, the more compatible the roommates are.
The Roommate Compatibility Scorer takes in roommate profiles with preferences such as sleep time, cleanliness, work schedule, and food habits. It then compares each pair of roommates based on how similar these preferences are and calculates a compatibility score from 0 to 100. The higher the score, the more compatible the roommates are likely to be.

This project is useful for:

Finding the ideal roommate based on shared preferences.

Roommate-matching applications that need to recommend roommates based on compatibility.

Landlords and rental agencies who want to ensure good matches between tenants.




Features
Roommate Profile Creation: Each roommate can have a profile with their preferences (sleep time, cleanliness, work schedule, food habits).

Compatibility Calculation: The algorithm compares two roommates' preferences and generates a compatibility score.

Ranking: Roommate pairs are ranked based on their compatibility scores, providing a list of the best matches.

CSV Integration: Roommate profiles can be stored and loaded from CSV files.

Extensible: You can easily add more preferences or scoring rules to improve the matching algorithm.
Profile Creation: Users can create profiles by entering preferences such as sleep time, cleanliness, work schedule, and food habits.

Compatibility Scoring: The algorithm calculates compatibility based on the input preferences. The closer the score is to 100, the better the match.

Roommate Pair Ranking: The program ranks pairs of roommates based on their compatibility scores.

CSV Integration: Roommate profiles are stored in CSV format, allowing easy access, editing, and export of data.

Flexible Matching Algorithm: The program can be easily customized to include more preferences or alter the scoring criteria.

Data Visualization (Optional): You can extend the project to visualize roommate matches or provide more insightful metrics.

Technologies Used
Python 3.x: The primary programming language.

Pandas: A powerful library for handling and processing CSV data.

NumPy: (Optional) For numerical operations (if needed for advanced scoring).

Setup Instructions
1. Clone the Repository
To get started, clone the project repository to your local machine.

bash
git clone https://github.com/brahmajich/roommate-compatibility-scorer.git
cd roommate-compatibility-scorer
2. Install Dependencies
Ensure you have Python 3.x installed on your machine. After that, install the required dependencies using the requirements.txt file.

bash
pip install -r requirements.txt
This will install Pandas and any other dependencies necessary to run the project.

3. Prepare Data
The program expects a CSV file (roommates.csv) that contains the roommate profiles. You can either edit the mock data already provided or add your own roommate data.

Here is a sample format for the CSV:

csv
name,sleep_time,cleanliness,work_schedule,food_habits
Roommate1,early,very clean,9-5,vegetarian
Roommate2,late,average,flexible,non-vegetarian
Roommate3,early,not clean,9-5,vegetarian
Roommate4,late,very clean,night shift,non-vegetarian
You can modify this file or add more roommates as needed.

4. Running the Project
Once everything is set up, you can run the program by executing the following command:

bash
python main.py
This will:

Load the roommate data from the CSV file.

Compare each pair of roommates.

Calculate the compatibility scores.

Rank and display the best roommate matches.

Usage
Example of Matching Roommates
Let’s assume you have the following roommates:

Roommate1: Early sleeper, very clean, 9-5 job, vegetarian.

Roommate2: Late sleeper, average cleanliness, flexible work schedule, non-vegetarian.

When you run the program, it calculates their compatibility score, which will be based on their matching preferences (e.g., sleep schedule, cleanliness, etc.).

Output
After executing python main.py, the output will show the compatibility score for all roommate pairs. For example:

bash
Ranked Matches based on Compatibility Score:
Roommate1 & Roommate3 - Score: 85
Roommate2 & Roommate4 - Score: 80
Roommate1 & Roommate2 - Score: 50
This shows the best roommate pairs, ranked by their compatibility score.

File Structure
Here’s a quick overview of the project file structure:

bash
roommate-compatibility-scorer/
│
├── data/                          # Contains CSV files with roommate profiles
│   ├── roommates.csv              # Main roommate data file
│   └── mock_profiles.csv          # (Optional) A mock profile file for testing
│
├── src/                           # Source code for the project
│   ├── __init__.py                # Marks directory as a Python package
│   ├── compatibility.py           # Contains the core logic for compatibility calculation
│   ├── data_loader.py             # Code to load data from CSV files
│   ├── profile_manager.py         # Functions for managing roommate profiles
│   └── ranking.py                 # Code for ranking and displaying best matches
│
├── requirements.txt               # Python dependencies
├── main.py                        # Entry point for running the compatibility model
├── README.md                      # Project overview and instructions
└── .gitignore                     # Git ignore file
Example
The roommates.csv file might look like this:

csv
name,sleep_time,cleanliness,work_schedule,food_habits
Roommate1,early,very clean,9-5,vegetarian
Roommate2,late,average,flexible,non-vegetarian
Roommate3,early,not clean,9-5,vegetarian
Roommate4,late,very clean,night shift,non-vegetarian
After Running the Program
The program will compare every pair of roommates and display the compatibility scores, such as:

bash
Roommate1 & Roommate3 - Score: 85
Roommate2 & Roommate4 - Score: 80
Roommate1 & Roommate2 - Score: 50
Contributing
We welcome contributions to improve this project. To contribute:

Fork the repository.

Create a new branch (git checkout -b feature-name).

Make your changes.

Commit your changes (git commit -am 'Add feature').

Push to the branch (git push origin feature-name).

Create a new pull request.

Feel free to open issues or submit pull requests with bug fixes, enhancements, or suggestions.
