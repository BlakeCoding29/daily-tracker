def main():
    day = input("What day is it? ").strip().title()
    coded = input("Did you code today? yes/no: ").strip().lower()

    while coded not in ["yes", "no"]:
        coded = input("Please enter yes or no: ").strip().lower()

    entry = f"{day}: {coded}\n"

    with open("log.txt", "a") as file:
        file.write(entry)

    if coded == "yes":
        print(f"Logged. You coded on {day}.")
    else:
        print("Logged. Do 10 minutes next time.")


if __name__ == "__main__":
    main()
