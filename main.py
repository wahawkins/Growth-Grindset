import random

# Function to load workouts from a text file
def load_workouts(file_path):
    workouts = {}
    current_category = None

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            # If the line ends with ":", it's a category header
            if line.endswith(":"):
                current_category = line[:-1]  # Remove the colon
                workouts[current_category] = []
            elif current_category:
                workouts[current_category].append(line)

    return workouts

# Function to generate a workout plan
def generate_workout_plan(workouts):
    workout_plan = {}
    for category, exercises in workouts.items():
        if category == "Cardio":
            workout_plan[category] = [random.choice(exercises)]  # Only 1 cardio exercise
        elif len(exercises) >= 2:
            workout_plan[category] = random.sample(exercises, 2)
        else:
            workout_plan[category] = exercises  # Keep whatever is available
    return workout_plan

# Function to swap a workout
def swap_exercise(workouts, workout_plan, category, index):
    available_exercises = [ex for ex in workouts[category] if ex not in workout_plan[category]]
    
    if available_exercises:
        new_exercise = random.choice(available_exercises)
        workout_plan[category][index] = new_exercise
        print(f"✅ Swapped! New exercise for {category}: {new_exercise}")
    else:
        print(f"⚠️ No alternative exercises available for {category}.")

# Main function
def main():
    gym_choice = input("Do you have access to a gym? (yes/no): ").strip().lower()
    file_path = "with_gym.txt" if gym_choice == "yes" else "without_gym.txt"

    workouts = load_workouts(file_path)
    workout_plan = generate_workout_plan(workouts)

    print("\n💪 Your Initial Workout Plan:\n")
    for category, exercises in workout_plan.items():
        print(f"{category}: {', '.join(exercises)}")

    while True:
        swap = input("\nDo you want to swap an exercise? (yes/no): ").strip().lower()
        if swap != "yes":
            break

        category = input("Enter the category (Chest, Back, Shoulders, etc.): ").strip().title()
        if category not in workout_plan:
            print("⚠️ Invalid category. Try again.")
            continue

        print(f"Current exercises for {category}:")
        for i, exercise in enumerate(workout_plan[category]):
            print(f"{i + 1}. {exercise}")

        try:
            index = int(input("Enter the number of the exercise to swap: ")) - 1
            if index not in range(len(workout_plan[category])):
                print("⚠️ Invalid choice. Try again.")
                continue
            swap_exercise(workouts, workout_plan, category, index)
        except ValueError:
            print("⚠️ Please enter a valid number.")

    print("\n🏋️‍♂️ Final Workout Plan:\n")
    for category, exercises in workout_plan.items():
        print(f"{category}: {', '.join(exercises)}")

if __name__ == "__main__":
    main()
