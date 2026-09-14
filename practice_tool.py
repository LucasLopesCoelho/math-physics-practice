print("Math & Physics Practice Tool")

score = 0

print("\nQuestion 1 - Math")
answer = float(input("What is 12 x 8? "))

if answer == 96:
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is 96.")

print("\nQuestion 2 - Physics")
answer = float(input("A car travels 100 meters in 5 seconds. What is its average speed in m/s? "))

if answer == 20:
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is 20 m/s.")

print("\nFinal score:", score, "/ 2")
