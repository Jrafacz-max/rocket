"""
Author: John Rafacz, Jrafacz@purdue.edu
Assignment: 11.3 - Rockets
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


"""Write new functions below this line (starting with unit 4)."""
# Create the Rocket class
class Rocket:
    def __init__(self, name, booster_cost, upper_stage_cost, fuel_cost):
        self.name = name
        self.booster_cost = booster_cost
        self.upper_stage_cost = upper_stage_cost
        self.fuel_cost = fuel_cost

    # Calculate the cost per launch
    def cost_per_launch(self):
        cost = self.booster_cost + self.upper_stage_cost + self.fuel_cost
        print(f"This {self.name} cost ${cost:.2f} million per launch.")


# Create the ReusableRocket class
class ReusableRocket(Rocket):
    def __init__(self, name, booster_cost, upper_stage_cost, fuel_cost, uses):
        super().__init__(name, booster_cost, upper_stage_cost, fuel_cost)
        self.uses = uses

    # Calculate the reusable rocket launch cost
    def cost_per_launch(self):
        cost = (self.booster_cost / self.uses) + self.upper_stage_cost + self.fuel_cost
        print(f"This {self.name} cost ${cost:.2f} million per launch.")


def main():
     # Create five rockets
    atlas = Rocket("Atlas V", 65.4, 42.6, 0.23)
    ariane = Rocket("Ariane 5", 83.5, 55.6, 0.69)
    long_march = Rocket("Long March 3B", 28.5, 19.0, 2.38)
    soyuz = Rocket("Soyuz 2", 20.9, 13.9, 0.24)
    falcon = ReusableRocket("Falcon 9", 43.0, 18.6, 0.45, 23)

    # Display the cost per launch for each rocket
    atlas.cost_per_launch()
    ariane.cost_per_launch()
    long_march.cost_per_launch()
    soyuz.cost_per_launch()
    falcon.cost_per_launch()


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
