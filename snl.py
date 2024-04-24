import random
import streamlit as st

# Constants for the game
LADDERS = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
SNAKES = {98: 78, 95: 75, 93: 73, 87: 24, 64: 60, 62: 19, 56: 53, 49: 11, 47: 26, 16: 6}

def roll_dice():
    """Simulate rolling a six-sided dice."""
    return random.randint(1, 6)

def move_player(player, position):
    """Move the player according to the dice roll and check for snakes/ladders."""
    roll = roll_dice()
    position += roll
    st.write(f"Player {player} rolled a {roll}.")

    if position in SNAKES:
        st.write(f"Oh no! Player {player} got bitten by a snake and is now on square {SNAKES[position]}.")
        position = SNAKES[position]

    elif position in LADDERS:
        st.write(f"Great! Player {player} climbed a ladder and is now on square {LADDERS[position]}.")

    return position

def play_game():
    """Main function to play the Snake and Ladder game."""
    player1_position = 0
    player2_position = 0

    while True:
        # Player 1's turn
        st.text_input("Player 1 press Enter to roll the dice...", key='input_player1')
        if st.session_state.input_player1:
            player1_position = move_player(1, player1_position)
            if player1_position >= 100:
                st.write("Player 1 wins!")
                break

        # Player 2's turn
        st.text_input("Player 2 press Enter to roll the dice...", key='input_player2')
        if st.session_state.input_player2:
            player2_position = move_player(2, player2_position)
            if player2_position >= 100:
                st.write("Player 2 wins!")
                break

def main():
    st.title("Snake and Ladder Game")
    st.write("Welcome to the Snake and Ladder game.")
    st.write("Rules:")
    st.write("  1. The game will be played by two players.")
    st.write("  2. Players take turns to roll a 6-sided dice.")
    st.write("  3. If a player lands at the bottom of a ladder, they climb to the top of the ladder.")
    st.write("  4. If a player lands on the head of a snake, they slide down to the tail of the snake.")
    st.write("  5. First player to reach or pass 100 wins.")
    st.write("Let's begin!")
    play_game()

if __name__ == "__main__":
    main()
