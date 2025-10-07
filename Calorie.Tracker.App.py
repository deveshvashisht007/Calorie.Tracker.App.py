
print("\t\t\twelcome to the daily calorie tracker!")
print()

print("this progrms helps you keep track of your daily colorie intake and maintain a healthy diet")
print()

print("let's get started by entering your meals for the day and their calorie counts.")
print()

meals = []
calories = []

NUM_Meals = int(input("how many meals did you have today?"))
print("--------------------------------------------------")

for i in range(NUM_Meals):
    meal_name=input(f"enter the name of meal {i+1}:")

    cal = int(input(f"enter the calorie count for{meal_name}:"))

    meals.append(meal_name)

    calories.append(cal)

    total_calories = sum(calories)

    avg_calories =total_calories/NUM_Meals
    print()

Daily_calorie_limit =float(input("enter your daily calorie limit:"))

print("\nDaily calorie intake summary:")
print("-------------------------------")

print("Meal\t\tCalories")
print("-------------------------------")

for i in range(len(meals)):
    print(meals[i],"\t\t",calories[i])
    print("---------------------------")

print(f"total calories consumed: {total_calories} calories")
print("----------------------------------------------------")

print(f"Average calories consumed: {avg_calories}")
print("----------------------------------------------------")

if total_calories>=Daily_calorie_limit:
    print("you have exceeded your daily calorie limit.try to eat healthier tomorrow!")
else:
    print("great job! you have stayed within your daily calorie limit.keep it up!")
print()



print("thank you for using the daily calorie tracker. stay healthy!")