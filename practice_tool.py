import streamlit as st
import random
import time

st.set_page_config(
    page_title="Math & Physics Practice",
    page_icon="📚",
    layout="centered"
)

st.title("📚 Math & Physics Practice")
st.write("Practice math and physics with randomly generated questions.")

subject = st.selectbox(
    "Choose a subject:",
    ["Math", "Physics", "Mixed"]
)

difficulty = st.selectbox(
    "Choose difficulty:",
    ["Easy", "Medium", "Hard"]
)

total_questions = st.selectbox(
    "Number of questions:",
    [5, 10, 15]
)

if "score" not in st.session_state:
    st.session_state.score = 0

if "question_number" not in st.session_state:
    st.session_state.question_number = 1

if "current_question" not in st.session_state:
    st.session_state.current_question = None

if "correct_answer" not in st.session_state:
    st.session_state.correct_answer = None

if "answered" not in st.session_state:
    st.session_state.answered = False


def generate_math_question():
    if difficulty == "Easy":
        a = random.randint(2, 20)
        b = random.randint(2, 20)

    elif difficulty == "Medium":
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

    return question, answer


def generate_physics_question():
    if difficulty == "Easy":
        distance = random.randint(50, 300)
        time_value = random.randint(2, 15)

    elif difficulty == "Medium":
        distance = random.randint(100, 1000)
        time_value = random.randint(5, 40)

    else:
        distance = random.randint(500, 5000)
        time_value = random.randint(10, 120)

    answer = distance / time_value

    question = (
        f"An object travels {distance} meters in "
        f"{time_value} seconds. What is its average speed in m/s?"
    )

    return question, answer


def generate_question():
    selected_subject = subject

    if subject == "Mixed":
        selected_subject = random.choice(["Math", "Physics"])

    if selected_subject == "Math":
        return generate_math_question()

    return generate_physics_question()


if st.session_state.current_question is None:
    question, answer = generate_question()

    st.session_state.current_question = question
    st.session_state.correct_answer = answer


st.subheader(
    f"Question {st.session_state.question_number} of {total_questions}"
)

st.write(st.session_state.current_question)

user_answer = st.number_input(
    "Your answer:",
    value=0.0,
    step=0.1
)

if st.button("Submit Answer") and not st.session_state.answered:

    correct_answer = st.session_state.correct_answer

    if abs(user_answer - correct_answer) < 0.02:
        st.success("Correct! 🎉")
        st.session_state.score += 1

    else:
        st.error(
            f"Incorrect. Correct answer: {correct_answer:.2f}"
        )

    st.session_state.answered = True


if st.session_state.answered:

    if st.session_state.question_number < total_questions:

        if st.button("Next Question"):

            st.session_state.question_number += 1
            st.session_state.answered = False

            question, answer = generate_question()

            st.session_state.current_question = question
            st.session_state.correct_answer = answer

            st.rerun()

    else:

        percentage = (
            st.session_state.score /
            total_questions *
            100
        )

        st.subheader("Results")

        st.write(
            f"Score: {st.session_state.score}/{total_questions}"
        )

        st.write(
            f"Percentage: {percentage:.1f}%"
        )

        if percentage == 100:
            st.success("Perfect score!")

        elif percentage >= 80:
            st.success("Great job!")

        elif percentage >= 60:
            st.info("Good effort. Keep practicing!")

        else:
            st.warning("Keep practicing!")

        if st.button("Restart Quiz"):

            st.session_state.score = 0
            st.session_state.question_number = 1
            st.session_state.current_question = None
            st.session_state.correct_answer = None
            st.session_state.answered = False

            st.rerun()
