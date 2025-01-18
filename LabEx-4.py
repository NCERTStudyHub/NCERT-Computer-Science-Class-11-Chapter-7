# Lab Exercises - 4
# ABC School has allotted unique token IDs from (1 to 600) to all the parents for facilitating a lucky draw on the day of their Annual day function. 
# The winner would receive a special prize. Write a program using Python that helps to automate the task.


import random

def lucky_draw():
    # Define the range of token IDs
    token_ids = list(range(1, 601))
    
    # Randomly select one token ID
    winner_token_id = random.choice(token_ids)
    
    # Display the winner
    print(f"The winner of the lucky draw is token ID: {winner_token_id}")

# Run the lucky draw
if __name__ == "__main__":
    lucky_draw()
