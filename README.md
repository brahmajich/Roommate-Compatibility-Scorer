# Roommate Compatibility Scorer

Welcome to the **Roommate Compatibility Scorer** project! This Python-based application helps you find the best roommate match based on their preferences. The idea is to rate how compatible two roommates are with each other, considering factors like sleep time, cleanliness, work schedule, and food habits.

Whether you are moving into a new apartment, creating a roommate-finding app, or just curious about roommate compatibility, this project offers a simple yet effective solution.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Installation & Setup](#installation--setup)
5. [Usage Instructions](#usage-instructions)
6. [Committing Changes to GitHub](#committing-changes-to-github)
7. [Detailed Explanation of Components](#detailed-explanation-of-components)
8. [File Structure](#file-structure)
9. [Example](#example)
10. [Contributing](#contributing)
11. [License](#license)

---

## Project Overview

The **Roommate Compatibility Scorer** takes in roommate profiles with preferences such as sleep time, cleanliness, work schedule, and food habits. It then compares each pair of roommates based on how similar these preferences are and calculates a compatibility score from **0 to 100**. The higher the score, the more compatible the roommates are likely to be.

This project is useful for:
- **Finding the ideal roommate** based on shared preferences.
- **Roommate-matching applications** that need to recommend roommates based on compatibility.
- **Landlords and rental agencies** who want to ensure good matches between tenants.

---

## Features

- **Profile Creation**: Users can create profiles by entering preferences such as sleep time, cleanliness, work schedule, and food habits.
- **Compatibility Scoring**: The algorithm calculates compatibility based on the input preferences. The closer the score is to 100, the better the match.
- **Roommate Pair Ranking**: The program ranks pairs of roommates based on their compatibility scores.
- **CSV Integration**: Roommate profiles are stored in CSV format, allowing easy access, editing, and export of data.
- **Flexible Matching Algorithm**: The program can be easily customized to include more preferences or alter the scoring criteria.
- **Data Visualization (Optional)**: You can extend the project to visualize roommate matches or provide more insightful metrics.

---

## Technologies Used

This project is built using Python, and the following libraries are used:

- **Python 3.x**: The core programming language for this application.
- **Pandas**: A powerful library for data manipulation and analysis, especially useful for handling CSV files.
- **NumPy**: Optional (you may use this for advanced numerical computations if needed).
- **CSV Files**: The data is stored in CSV files for easy import/export.

---

## Installation & Setup

Follow these steps to set up the **Roommate Compatibility Scorer** on your local machine.

### 1. Clone the Repository

To get started, clone this project to your local machine:

```bash
git clone https://github.com/brahmaji-ch/roommate-compatibility-scorer.git
cd roommate-compatibility-scorer
