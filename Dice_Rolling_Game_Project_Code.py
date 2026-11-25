# Dice Rolling Game

def calculate_frequency(rolls):
    frequency = {}

    for i in range(1, 7):
        frequency[i] = rolls.count(i)

    return frequency


def display_results(rolls):

    frequency = calculate_frequency(rolls)

    total = sum(rolls)
    average = total / len(rolls)

    max_frequency = max(frequency.values())

    most_frequent = []

    for face in range(1, 7):
        if frequency[face] == max_frequency:
            most_frequent.append(face)

    print("\nFrequency:", end=" ")

    for face in range(1, 7):
        print(f"{face}:{frequency[face]}", end=" | ")

    print("\nTotal:", total)
    print("Average: {:.2f}".format(average))

    print("Most frequent:", end=" ")

    for face in most_frequent:
        print(face, end=" ")

    print(f"({max_frequency} times)")


def main():

    print("===== DICE ROLLING GAME =====")

    while True:

        # Validate number of rolls
        while True:
            try:
                n = int(input("\nNumber of rolls: "))

                if 1 <= n <= 1000:
                    break
                else:
                    print("Invalid input. Enter a whole number from 1 to 1000.")

            except ValueError:
                print("Invalid input. Enter a whole number from 1 to 1000.")

        # Accept dice values
        while True:
            try:
                values = input("Rolls: ")

                rolls = list(map(int, values.replace(",", " ").split()))

                if len(rolls) != n:
                    print("Please enter exactly", n, "rolls.")
                    continue

                if any(x < 1 or x > 6 for x in rolls):
                    print("Invalid dice value. Enter values from 1 to 6.")
                    continue

                break

            except ValueError:
                print("Invalid input. Enter numbers only.")

        # Display statistics
        display_results(rolls)

        # Play again
        choice = input("\nPlay again? (y/n): ").lower()

        if choice != 'y':
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()