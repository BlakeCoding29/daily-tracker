from datetime import date
from pathlib import Path


LOG_FILE = Path(__file__).with_name("log.txt")


def ask_day():
    today = date.today().strftime("%A %m/%d/%y")
    day = input(f"What day is it? [{today}] ").strip()
    return day.title() if day else today


def ask_yes_no(prompt):
    answers = {
        "y": "yes",
        "yes": "yes",
        "n": "no",
        "no": "no",
    }

    answer = input(prompt).strip().lower()
    while answer not in answers:
        answer = input("Please enter yes or no: ").strip().lower()

    return answers[answer]


def current_streak():
    if not LOG_FILE.exists():
        return 0

    streak = 0
    for line in reversed(LOG_FILE.read_text().splitlines()):
        if not line.strip():
            continue

        coded = line.rsplit(":", 1)[-1].strip().lower()
        if coded == "yes":
            streak += 1
        else:
            break

    return streak


def main():
    day = ask_day()
    coded = ask_yes_no("Did you code today? yes/no: ")

    entry = f"{day}: {coded}\n"

    with LOG_FILE.open("a") as file:
        file.write(entry)

    if coded == "yes":
        print(f"Logged. You coded on {day}.")
        print(f"Current coding streak: {current_streak()} day(s).")
    else:
        print("Logged. Do 10 minutes next time.")


if __name__ == "__main__":
    main()
