import streamlit as st
import random

st.title("🎯 Number Guessing Game")

# session state variables
if 'targetnumber' not in st.session_state:
    st.session_state.targetnumber = None
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
if 'max_attempts' not in st.session_state:
    st.session_state.max_attempts = None
if 'game_active' not in st.session_state:
    st.session_state.game_active = False
if 'guessed_numbers' not in st.session_state:
    st.session_state.guessed_numbers = []

# disable input fields if game is active
disable_inputs = st.session_state.game_active

with st.form("game_settings"): 
    # difficulty level
    difficulty = st.selectbox(
        'Select Difficulty Level',
        ['Easy (10 attempts)', 'Medium (5 attempts)', 'Hard (3 attempts)'],
        disabled=disable_inputs
    )
    level_mapping = {'Easy (10 attempts)': 10, 'Medium (5 attempts)': 5, 'Hard (3 attempts)': 3}
    st.session_state.max_attempts = level_mapping[difficulty]

   # taking range of numbers from user
    col1, col2 = st.columns(2)
    with col1:
        st.session_state.min_val = st.number_input(
            'Enter minimum value', value=1, step=1, disabled=disable_inputs
        )
    with col2:
        st.session_state.max_val = st.number_input(
            'Enter maximum value', value=100, step=1, disabled=disable_inputs
        )

    # start game
    start_button = st.form_submit_button("Start Game", disabled=disable_inputs)

if start_button:
    if st.session_state.min_val < st.session_state.max_val:
        st.session_state.targetnumber = random.randint(st.session_state.min_val, st.session_state.max_val)
        st.session_state.attempts = 0
        st.session_state.guessed_numbers = []  # Reset guesses on new game start
        st.session_state.game_active = True
        st.rerun()  # Refresh UI state
    else:
        st.error('Minimum value must be less than maximum value.')

# game input
if st.session_state.game_active:
    guess = st.number_input(
        'Enter your guess',
        min_value=st.session_state.min_val,
        max_value=st.session_state.max_val,
        step=1
    )

    if st.button('Submit Guess'):
        if guess in st.session_state.guessed_numbers:
            st.warning("⚠️ You've already guessed this number! Try a different one.")
        else:
            st.session_state.guessed_numbers.append(guess)
            st.session_state.attempts += 1

            if guess == st.session_state.targetnumber:
                st.success(f'🎉 Correct! You guessed the number in {st.session_state.attempts} attempts.')
                st.session_state.game_active = False
            elif st.session_state.attempts >= st.session_state.max_attempts:
                st.error(f'☠️ Game Over! The number was {st.session_state.targetnumber}. Better luck next time.')
                st.session_state.game_active = False
            elif guess < st.session_state.targetnumber:
                st.warning('❌ Too low! Try again.')
            elif guess > st.session_state.targetnumber:
                st.warning('❌ Too high! Try again.')

if st.session_state.game_active:
    st.write(f'##### Attempts: {st.session_state.attempts}/{st.session_state.max_attempts}')

# guessed numbers
if st.session_state.guessed_numbers and st.session_state.game_active:
    st.subheader("📌 Guessed Numbers:")
    st.write(", ".join(map(str, st.session_state.guessed_numbers)))

# reset game
if st.button('Reset Game'):
    st.session_state.targetnumber = None
    st.session_state.attempts = 0
    st.session_state.game_active = False
    st.session_state.guessed_numbers = []
    st.rerun()
