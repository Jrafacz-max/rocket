"""
Author: John Rafacz, Jrafacz@purdue.edu
Assignment: 11.1 - Dice
Date: 11/14/2026

Description:
    Describe your program here.

Contributors:
    John Rafacz, Jrafacz@purdue.edu

My contributor(s) helped me:
    [X] understand the assignment expectations without
        telling me how they will approach it.
    [X] understand different ways to think about a solution
        without helping me plan my solution.
    [X] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

"""Import additional modules below this line (starting with unit 6)."""
import random

"""Write new functions below this line (starting with unit 4)."""
# Create the Dice class
class Dice:
    def __init__(self, sides):
        self.sides = sides

    # Roll the die once
    def roll(self):
        return random.randint(1, self.sides)

    # Roll the die n times and print the results
    def n_rolls(self, n):
        results = []

        for i in range(n):
            results.append(str(self.roll()))

        print(f"Rolling a {self.sides} sided die {n} times: {', '.join(results)}")



def main():
    # Create three dice
    die6 = Dice(6)
    die10 = Dice(10)
    die20 = Dice(20)

    # Roll each die 10 times
    die6.n_rolls(10)
    die10.n_rolls(10)
    die20.n_rolls(10)
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
