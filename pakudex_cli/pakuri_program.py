from pakuri import *
from pakudex import *
def main():
    print("Welcome to Pakudex: Tracker Extraordinaire!")
    while True:
        try:
            max_capacity = int(input("Enter max capacity of the Pakudex: "))
            if max_capacity < 1:
                print("Please enter a valid size.")
            else:
                break
        except ValueError:
            print("Please enter a valid size.") 
    pakudex = Pakudex(max_capacity)
    print(f"The Pakudex can hold {max_capacity} species of Pakuri.")
    condition = True
    while condition == True:
        print("""
Pakudex Main Menu
-----------------
1. List Pakuri
2. Show Pakuri
3. Add Pakuri
4. Evolve Pakuri
5. Sort Pakuri
6. Exit
""")
        option = input("What would you like to do? ")
        if option == "1":
            species_array = pakudex.get_species_array()
            if species_array is None:
                print("No Pakuri in Pakudex yet!")
            else:
                print("Pakuri In Pakudex:")
                for i,species in enumerate(species_array, start=1):
                    print(f"{i}. {species}")
        elif option == "2":
            species = input("Enter the name of the species to display: ")
            stats = pakudex.get_stats(species)
            if stats is None:
                print("Error: No such Pakuri!")
            else:
                print(f"\nSpecies: {species}")
                print(f"Attack: {stats[0]}")
                print(f"Defense: {stats[1]}")
                print(f"Speed: {stats[2]}")
        elif option == "3":
            if pakudex.get_size() == pakudex.get_capacity():
                    print("Error: Pakudex is full!")
            else:
                species = input("Enter the name of the species to add: ")
                added = pakudex.add_pakuri(species)
                if added:
                    print(f"Pakuri species {species} successfully added!")
                else:
                    print("Error: Pakudex already contains this species!")
        elif option == "4":
            species = input("Enter the name of the species to evolve: ")
            evolved = pakudex.evolve_species(species)
            if evolved:
                print(f"{species} has evolved!")
            else:
                print("Error: No such Pakuri!")
        elif option == "5":
            pakudex.sort_pakuri()
            print("Pakuri have been sorted!")
        elif option == "6":
            print("Thanks for using Pakudex! Bye!")
            condition = False
        else:
            print("Unrecognized menu selection!")

if __name__ == "__main__":
    main()