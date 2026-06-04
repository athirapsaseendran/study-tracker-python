import matplotlib.pyplot as plt

subjects = {}
goal = 0


def load_data():
    try:
        with open("subjects.txt", "r") as file:
            for line in file:
                line = line.strip()

                if line:
                    subject, hours = line.split(",")
                    subjects[subject] = int(hours)

    except FileNotFoundError:
        pass


def save_data():
    with open("subjects.txt", "w") as file:
        for subject, hours in subjects.items():
            file.write(f"{subject},{hours}\n")


def load_goal():
    global goal

    try:
        with open("goal.txt", "r") as file:
            goal = int(file.read().strip())

    except (FileNotFoundError, ValueError):
        goal = 0


def save_goal():
    with open("goal.txt", "w") as file:
        file.write(str(goal))


def get_level(hours):
    if hours <= 4:
        return "Beginner"
    elif hours <= 9:
        return "Intermediate"
    else:
        return "Advanced"


def add_subject():
    subject = input("Enter subject name: ").strip()

    if not subject:
        print("Subject name cannot be empty!")

    elif subject in subjects:
        print("Subject already exists!")

    else:
        subjects[subject] = 0
        save_data()
        print("Subject added successfully!")


def view_subjects():
    if not subjects:
        print("No subjects added yet!")
        return

    print("\n===== SUBJECTS =====")

    sorted_subjects = sorted(
        subjects.items(),
        key=lambda item: item[1],
        reverse=True
    )

    for subject, hours in sorted_subjects:
        level = get_level(hours)
        print(f"{subject} : {hours} hours [{level}]")


def add_hours():
    subject = input("Enter subject name: ").strip()

    if subject not in subjects:
        print("Subject not found!")
        return

    try:
        hours = int(input("Enter hours studied: "))

        if hours < 0:
            print("Hours cannot be negative!")
        else:
            subjects[subject] += hours
            save_data()
            print("Study hours updated!")

    except ValueError:
        print("Please enter a valid number!")


def delete_subject():
    subject = input("Enter subject name to delete: ").strip()

    if subject in subjects:
        del subjects[subject]
        save_data()
        print("Subject deleted successfully!")
    else:
        print("Subject not found!")


def view_statistics():
    if not subjects:
        print("No data available for statistics!")
        return

    total_subjects = len(subjects)
    total_hours = sum(subjects.values())
    most_studied = max(subjects, key=subjects.get)
    average_hours = total_hours / total_subjects

    print("\n===== STATISTICS =====")
    print(f"Total Subjects: {total_subjects}")
    print(f"Total Hours Studied: {total_hours}")
    print(
        f"Most Studied Subject: {most_studied} "
        f"({subjects[most_studied]} hours)"
    )
    print(f"Average Hours Per Subject: {average_hours:.2f}")


def weekly_report():
    if not subjects:
        print("No study data available!")
        return

    total_hours = sum(subjects.values())
    top_subject = max(subjects, key=subjects.get)

    print("\n===== WEEKLY REPORT =====")
    print(f"Total Study Hours: {total_hours}\n")

    sorted_subjects = sorted(
        subjects.items(),
        key=lambda item: item[1],
        reverse=True
    )

    for subject, hours in sorted_subjects:
        print(f"{subject} : {hours} hours")

    print(f"\nTop Subject: {top_subject}")


def set_goal():
    global goal

    try:
        target = int(input("Enter target study hours: "))

        if target <= 0:
            print("Goal must be greater than 0!")
        else:
            goal = target
            save_goal()
            print(f"Study goal set to {goal} hours!")

    except ValueError:
        print("Please enter a valid number!")


def view_goal_progress():
    if goal == 0:
        print("No study goal set yet!")
        return

    current_hours = sum(subjects.values())

    progress = (current_hours / goal) * 100
    display_progress = min(progress, 100)

    print("\n===== GOAL PROGRESS =====")
    print(f"Goal: {goal} hours")
    print(f"Current: {current_hours} hours")
    print(f"Progress: {display_progress:.2f}%")

    if current_hours >= goal:
        print("🎉 Goal Achieved!")


def show_chart():
    if not subjects:
        print("No study data available!")
        return

    sorted_subjects = sorted(
        subjects.items(),
        key=lambda item: item[1],
        reverse=True
    )

    labels = [subject for subject, hours in sorted_subjects]
    values = [hours for subject, hours in sorted_subjects]

    plt.figure(figsize=(8, 5))
    plt.bar(labels, values)

    plt.title("Study Hours by Subject")
    plt.xlabel("Subjects")
    plt.ylabel("Hours Studied")

    plt.tight_layout()
    plt.show()


load_data()
load_goal()

while True:
    print("\n===== STUDY TRACKER =====")
    print("1. Add Subject")
    print("2. View Subjects")
    print("3. Add Study Hours")
    print("4. Delete Subject")
    print("5. Exit")
    print("6. View Statistics")
    print("7. Weekly Report")
    print("8. Set Study Goal")
    print("9. View Goal Progress")
    print("10. Show Progress Chart")

    choice = input("Enter choice: ")

    if choice == "1":
        add_subject()

    elif choice == "2":
        view_subjects()

    elif choice == "3":
        add_hours()

    elif choice == "4":
        delete_subject()

    elif choice == "5":
        save_data()
        save_goal()
        print("Data saved successfully!")
        print("Goodbye!")
        break

    elif choice == "6":
        view_statistics()

    elif choice == "7":
        weekly_report()

    elif choice == "8":
        set_goal()

    elif choice == "9":
        view_goal_progress()

    elif choice == "10":
        show_chart()

    else:
        print("Invalid choice!")