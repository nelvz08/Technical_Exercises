import sys
import random
import json

# Get user input numbers 6 times
numbers = []
while len(numbers) < 6:
    try:
        num = int(input(f"Enter number {len(numbers)+1}: "))
        numbers.append(num)
    except ValueError:
        print("Invalid input. Please enter integers.")

print("You provided the following 6 numbers:", numbers)
print("\n")

# Display the Choices
print("Please select your proccess to execute:")
print("1. Perform subtraction and show output on screen comma separated.")
print("2. Perform multiplication and store result in a JSON file.")
print("3. Pick randomly a number and show it on screen.")
print("4. Print sorted (highest to lowest) array/list numbers.")
print("5. Print sorted (lowest to highest) array/list numbers.")
print("\n")

# Get user choice
choice = input("Enter your choice (1-5): ")

# Perform operation based on user choice:
if choice == "1":
        
        subtractionResult = []
        for i in range(len(numbers)):
            if i == 0:
                result = numbers[i]
            else:
                result -= numbers[i]

            subtractionResult.append(str(result))

        # Convert the list of subtraction results to a string with commas
        subtractionOutput = ", ".join(subtractionResult)
        
        # Display the result 
        print("Subtraction result:", subtractionOutput)

elif choice == "2":
    productResult = 1
    for num in numbers:
        productResult *= num
    
    # Store result in json file
    with open("productResult.json", "w") as jsonFile:
        jsonData = {}
        for i, num in enumerate(numbers):
            jsonData[f"InputNumber{i+1}"] = num
        jsonData["MultiplicationResult"] = productResult
        json.dump(jsonData, jsonFile)

    print("Multiplication result can be seen on produckResult.json file.")

elif choice == "3":
    randomNumber = random.choice(numbers)
    print("Randomly picked number: ", randomNumber)

elif choice == "4":
    sortedNumber = sorted(numbers, reverse=True)
    print("Sorted number (highest to lowest): ", sortedNumber)

elif choice == "5":
    sortedNumber = sorted(numbers)
    print("Sorted number (lowest to highest): ", sortedNumber)

else:
    print("Invalid choice. Please enter a number between 1 and 5.")