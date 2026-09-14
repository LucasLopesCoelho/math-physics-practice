import random
import time
from datetime import datetime


# --------------------------------------------------
# UTILITIES
# --------------------------------------------------

def get_number(prompt):
    """Keeps asking until the user enters a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def get_choice(prompt, valid_choices):
    """Keeps asking until the user enters a valid option."""
    while True:
        choice = input(prompt).strip().lower()

        if choice in valid_choices:
            return choice

        print("Invalid option. Please try again.")


def answers_match(user_answer, correct_answer):
    """Allows a small difference for decimal answers."""
    return abs(user_answer - correct_answer) < 0.02


# --------------------------------------------------
# MATH QUESTION GENERATORS
# --------------------------------------------------

def math_arithmetic(difficulty):
    if difficulty == "easy":
        a = random.randint(2, 20)
        b = random.randint(2, 20)

    elif difficulty == "medium":
        a = random.randint(10, 100)
        b = random.randint(5, 50)

    else:
        a = random.randint(50, 500)
        b = random.randint(10, 100)

    operation = random.choice(["+", "-", "*"])

    if operation == "+":
        answer = a + b
    elif operation == "-":
        answer = a - b
    else:
        answer = a * b

    question = f"What is {a} {operation} {b}?"

    explanation = f"{a} {operation} {b} = {answer}"

    return question, answer, explanation, "Arithmetic"


def math_percentage(difficulty):
    if difficulty == "easy":
        percentage = random.choice([10, 20, 25, 50])
        number = random.choice([40, 80, 100, 120, 200])

    elif difficulty == "medium":
        percentage = random.choice([15, 20, 30, 35, 40])
        number = random.randint(100, 500)

    else:
        percentage = random.randint(5, 75)
        number = random.randint(100, 1000)

    answer = number * percentage / 100

    question = f"What is {percentage}% of {number}?"

    explanation = (
        f"{percentage}% of {number} = "
        f"{percentage}/100 × {number} = {answer:.2f}"
    )

    return question, answer, explanation, "Percentages"


def math_algebra(difficulty):
    if difficulty == "easy":
        x = random.randint(1, 15)
        a = random.randint(1, 10)

    elif difficulty == "medium":
        x = random.randint(5, 30)
        a = random.randint(5, 20)

    else:
        x = random.randint(10, 50)
        a = random.randint(10, 40)

    result = x + a

    question = f"Solve for x: x + {a} = {result}"

    explanation = (
        f"x = {result} - {a}\n"
        f"x = {x}"
    )

    return question, x, explanation, "Algebra"


def generate_math_question(difficulty):
    generator = random.choice([
        math_arithmetic,
        math_percentage,
        math_algebra
    ])

    return generator(difficulty)


# --------------------------------------------------
# PHYSICS QUESTION GENERATORS
# --------------------------------------------------

def physics_speed(difficulty):
    if difficulty == "easy":
        distance = random.randint(50, 300)
        time_value = random.randint(2, 15)

    elif difficulty == "medium":
        distance = random.randint(100, 1000)
        time_value = random.randint(5, 40)

    else:
        distance = random.randint(500, 5000)
        time_value = random.randint(10, 120)

    answer = distance / time_value

    question = (
        f"An object travels {distance} meters in "
        f"{time_value} seconds.\n"
        "What is its average speed in m/s?"
    )

    explanation = (
        "Speed = Distance ÷ Time\n"
        f"Speed = {distance} ÷ {time_value}\n"
        f"Speed = {answer:.2f} m/s"
    )

    return question, answer, explanation, "Speed"


def physics_force(difficulty):
    if difficulty == "easy":
        mass = random.randint(2, 20)
        acceleration = random.randint(1, 10)

    elif difficulty == "medium":
        mass = random.randint(10, 100)
        acceleration = random.randint(2, 20)

    else:
        mass = random.randint(50, 500)
        acceleration = random.randint(5, 30)

    answer = mass * acceleration

    question = (
        f"An object has a mass of {mass} kg and accelerates "
        f"at {acceleration} m/s².\n"
        "What force is acting on it in newtons?"
    )

    explanation = (
        "Force = Mass × Acceleration\n"
        f"F = {mass} × {acceleration}\n"
        f"F = {answer} N"
    )

    return question, answer, explanation, "Force"


def physics_work(difficulty):
    if difficulty == "easy":
        force = random.randint(5, 30)
        distance = random.randint(2, 15)

    elif difficulty == "medium":
        force = random.randint(20, 100)
        distance = random.randint(5, 50)

    else:
        force = random.randint(50, 500)
        distance = random.randint(10, 100)

    answer = force * distance

    question = (
        f"A force of {force} N moves an object "
        f"{distance} meters.\n"
        "How much work is done in joules?"
    )

    explanation = (
        "Work = Force × Distance\n"
        f"W = {force} × {distance}\n"
        f"W = {answer} J"
    )

    return question, answer, explanation, "Work"


def physics_kinetic_energy(difficulty):
    if difficulty == "easy":
        mass = random.randint(1, 10)
        velocity = random.randint(2, 8)

    elif difficulty == "medium":
        mass = random.randint(5, 30)
        velocity = random.randint(5, 20)

    else:
        mass = random.randint(20, 100)
        velocity = random.randint(10, 40)

    answer = 0.5 * mass * velocity ** 2

    question = (
        f"An object has a mass of {mass} kg and moves at "
        f"{velocity} m/s.\n"
        "What is its kinetic energy in joules?"
    )

    explanation = (
        "Kinetic Energy = ½ × mass × velocity²\n"
        f"KE = 0.5 × {mass} × {velocity}²\n"
        f"KE = {answer:.2f} J"
    )

    return question, answer, explanation, "Kinetic Energy"


def generate_physics_question(difficulty):
    available_generators = [
        physics_speed,
        physics_force,
        physics_work
    ]

    if difficulty != "easy":
        available_generators.append(physics_kinetic_energy)

    generator = random.choice(available_generators)

    return generator(difficulty)


# --------------------------------------------------
# QUESTION SELECTION
# --------------------------------------------------

def generate_question(subject, difficulty):
    if subject == "math":
        return generate_math_question(difficulty)

    elif subject == "physics":
        return generate_physics_question(difficulty)

    else:
        random_subject = random.choice(["math", "physics"])

        if random_subject == "math":
            return generate_math_question(difficulty)

        return generate_physics_question(difficulty)


# --------------------------------------------------
# RESULTS HISTORY
# --------------------------------------------------

def save_result(subject, difficulty, score, total, percentage):
    date = datetime.now().strftime("%Y-%m-%d %H:%M")

    result = (
        f"{date} | "
        f"Subject: {subject.title()} | "
        f"Difficulty: {difficulty.title()} | "
        f"Score: {score}/{total} | "
        f"{percentage:.1f}%\n"
    )

    with open("practice_history.txt", "a") as file:
        file.write(result)


# --------------------------------------------------
# QUIZ
# --------------------------------------------------

def run_quiz():

    print("\n====================================")
    print("      MATH & PHYSICS PRACTICE")
    print("====================================")

    print("\nChoose a subject:")
    print("1 - Math")
    print("2 - Physics")
    print("3 - Mixed")

    subject_choice = get_choice(
        "\nYour choice: ",
        ["1", "2", "3"]
    )

    subjects = {
        "1": "math",
        "2": "physics",
        "3": "mixed"
    }

    subject = subjects[subject_choice]

    print("\nChoose difficulty:")
    print("1 - Easy")
    print("2 - Medium")
    print("3 - Hard")

    difficulty_choice = get_choice(
        "\nYour choice: ",
        ["1", "2", "3"]
    )

    difficulties = {
        "1": "easy",
        "2": "medium",
        "3": "hard"
    }

    difficulty = difficulties[difficulty_choice]

    print("\nHow many questions?")
    print("1 - 5 questions")
    print("2 - 10 questions")
    print("3 - 15 questions")

    amount_choice = get_choice(
        "\nYour choice: ",
        ["1", "2", "3"]
    )

    question_amounts = {
        "1": 5,
        "2": 10,
        "3": 15
    }

    total_questions = question_amounts[amount_choice]

    score = 0
    streak = 0
    best_streak = 0

    category_results = {}

    start_time = time.time()

    print("\n------------------------------------")
    print("Practice session started!")
    print("------------------------------------")

    for question_number in range(1, total_questions + 1):

        question, correct_answer, explanation, category = generate_question(
            subject,
            difficulty
        )

        print(
            f"\nQuestion {question_number}/{total_questions}"
        )

        print(f"Category: {category}")

        print("\n" + question)

        user_answer = get_number("\nYour answer: ")

        if category not in category_results:
            category_results[category] = {
                "correct": 0,
                "total": 0
            }

        category_results[category]["total"] += 1

        if answers_match(user_answer, correct_answer):

            print("\n✓ Correct!")

            score += 1
            streak += 1

            category_results[category]["correct"] += 1

            if streak > best_streak:
                best_streak = streak

            if streak >= 3:
                print(f"🔥 {streak} correct answers in a row!")

        else:

            print("\n✗ Incorrect.")

            print(
                f"Correct answer: {correct_answer:.2f}"
            )

            streak = 0

        print("\nExplanation:")
        print(explanation)

        if question_number != total_questions:
            input("\nPress Enter for the next question...")


    # --------------------------------------------------
    # FINAL RESULTS
    # --------------------------------------------------

    end_time = time.time()

    elapsed_seconds = end_time - start_time

    percentage = (score / total_questions) * 100

    average_time = elapsed_seconds / total_questions

    print("\n\n====================================")
    print("            RESULTS")
    print("====================================")

    print(
        f"\nScore: {score}/{total_questions}"
    )

    print(
        f"Percentage: {percentage:.1f}%"
    )

    print(
        f"Best streak: {best_streak}"
    )

    print(
        f"Total time: {elapsed_seconds:.1f} seconds"
    )

    print(
        f"Average time per question: "
        f"{average_time:.1f} seconds"
    )


    # --------------------------------------------------
    # PERFORMANCE FEEDBACK
    # --------------------------------------------------

    print("\nPerformance:")

    if percentage == 100:
        print("Outstanding! Perfect score.")

    elif percentage >= 90:
        print("Excellent performance!")

    elif percentage >= 80:
        print("Great job!")

    elif percentage >= 70:
        print("Good work. A little more practice will help.")

    elif percentage >= 60:
        print("You're improving. Keep practicing.")

    else:
        print("Keep going. Practice makes progress.")


    # --------------------------------------------------
    # CATEGORY ANALYSIS
    # --------------------------------------------------

    print("\nPerformance by category:")

    weakest_category = None
    weakest_percentage = 101

    for category, results in category_results.items():

        category_percentage = (
            results["correct"] /
            results["total"] *
            100
        )

        print(
            f"- {category}: "
            f"{results['correct']}/{results['total']} "
            f"({category_percentage:.0f}%)"
        )

        if category_percentage < weakest_percentage:

            weakest_percentage = category_percentage
            weakest_category = category


    if weakest_category:

        print(
            f"\nRecommended focus area: "
            f"{weakest_category}"
        )


    # --------------------------------------------------
    # SAVE RESULTS
    # --------------------------------------------------

    save_result(
        subject,
        difficulty,
        score,
        total_questions,
        percentage
    )

    print(
        "\nYour result has been saved "
        "to practice_history.txt"
    )


# --------------------------------------------------
# MAIN PROGRAM
# --------------------------------------------------

while True:

    run_quiz()

    again = get_choice(
        "\nWould you like to practice again? (yes/no): ",
        ["yes", "no", "y", "n"]
    )

    if again in ["no", "n"]:
        print("\nThanks for practicing!")
        print("See you next time.")
        break
