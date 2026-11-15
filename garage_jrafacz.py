"""
Author: John Rafacz, Jrafacz@purdue.edu
Assignment: 11.2 - Garage
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
# Create the Garage class
class Garage:
    def __init__(self, name, spaces, cars):
        self.name = name
        self.spaces = spaces
        self.cars = cars

    # Add a car to the garage
    def car_in(self):
        if self.cars < self.spaces:
            self.cars += 1
            print(f"  Added a car to {self.name}")
        else:
            print(f"  {self.name} is full. Can not add another car.")

    # Remove a car from the garage
    def car_out(self):
        if self.cars > 0:
            self.cars -= 1
            print(f"  Removed a car from {self.name}")
        else:
            print(f"  {self.name} is empty. There are no cars to remove.")

    # Print the number of available spaces
    def status(self):
        available = self.spaces - self.cars
        print(f"  {self.name}: {available} out of {self.spaces} spaces are available.")


def main():
    # Create two parking garages
    garage_a = Garage("Lot A", 10, 8)
    garage_b = Garage("Lot B", 15, 1)

    print("Welcome to the Garage Manager!")

    # Display the menu
    def menu():
        print("------------ Menu ------------")
        print("  0. Exit")
        print("  1. Print current status.")
        print("  2. Add a car to A lot.")
        print("  3. Add a car to B lot.")
        print("  4. Remove a car from A lot.")
        print("  5. Remove a car from B lot.")

    menu()

    # Allow the user to choose an option
    while True:
        choice = input("Please choose an option (0-5): ")

        if choice == "0":
            print("End of the Day Garage Status:")
            garage_a.status()
            garage_b.status()
            break

        elif choice == "1":
            print("Current Garage Status:")
            garage_a.status()
            garage_b.status()

        elif choice == "2":
            garage_a.car_in()

        elif choice == "3":
            garage_b.car_in()

        elif choice == "4":
            garage_a.car_out()

        elif choice == "5":
            garage_b.car_out()

        else:
            print("Invalid choice!")
            menu()

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
