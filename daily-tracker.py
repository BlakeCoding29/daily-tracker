day = input("What day is it? ")
coded = input("Did you code today? yes/no: ")

if coded.lower() == "yes":
    print(f"Good work. You coded on {day}.")
else:
    print("Do 10 minutes. Keep the streak alive.")