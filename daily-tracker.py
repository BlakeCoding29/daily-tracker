day = input("What day is it? ")
coded = input("Did you code today? yes/no: ")

entry = f"{day}: {coded}\n"

with open("log.txt", "a") as file:
    file.write(entry)

if coded.lower() == "yes":
    print(f"Logged. You coded on {day}.")
else:
    print("Logged. Do 10 minutes next time.")