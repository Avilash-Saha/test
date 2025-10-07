hungry = input("Are you hungry? (yes/no): ").strip().lower()
if hungry == "yes":
    print("Eat something!")
else:
    thrirsty = input("Are you thirsty? (yes/no): ").strip().lower()
    if thrirsty == "yes":
        print("Drink something!")
    else:
        print("Keep working!")