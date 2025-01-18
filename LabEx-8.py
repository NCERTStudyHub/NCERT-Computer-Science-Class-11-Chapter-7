# Lab Exercises - 8
# Write a program that creates a GK quiz consisting of any five questions of your choice. The questions should be displayed randomly. 
# Create a user defined function score() to calculate the score of the quiz and another user defined function remark (scorevalue) that 
# accepts the final score to display remarks as follows:

# 5: "Outstanding", 
# 4: "Excellent", 
# 3: "Good", 
# 2: "Read more to score more", 
# 1: "Needs to take interest", 
# 0: "General knowledge will always help you."


import random

def score(correct_answers, user_answers):
    """
    Calculate the score based on correct answers.

    Parameters:
    correct_answers (list): List of correct answers.
    user_answers (list): List of user's answers.

    Returns:
    int: The total score.
    """
    return sum(1 for correct, user in zip(correct_answers, user_answers) if correct == user)

def remark(score_value):
    """
    Provide remarks based on the score.

    Parameters:
    score_value (int): The final score.

    Returns:
    str: The remark corresponding to the score.
    """
    remarks = {
        5: "Outstanding",
        4: "Excellent",
        3: "Good",
        2: "Read more to score more",
        1: "Needs to take interest",
        0: "General knowledge will always help you."
    }
    return remarks.get(score_value, "Invalid score")

def main():
    # Questions and answers
    questions = [
        ("What is the capital of France?", "Paris"),
        ("Who wrote 'Romeo and Juliet'?", "Shakespeare"),
        ("What is the largest planet in our solar system?", "Jupiter"),
        ("What is the chemical symbol for water?", "H2O"),
        ("Who painted the Mona Lisa?", "Da Vinci")
    ]

    # Shuffle questions
    random.shuffle(questions)

    # Store user's answers
    user_answers = []

    # Ask questions
    for question, answer in questions:
        user_answer = input(f"{question} ")
        user_answers.append(user_answer.strip())

    # Correct answers
    correct_answers = [answer for _, answer in questions]

    # Calculate score
    total_score = score(correct_answers, user_answers)

    # Display results
    print(f"\nYour total score is: {total_score}")
    print(remark(total_score))

# Run the program
if __name__ == "__main__":
    main()
