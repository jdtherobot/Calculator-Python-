# Calculator project start 27 July 2025

user_input = input("Welcome to the calculator! "
                   "\n Please enter a calculation to begin. "
                   "\n Type 'q' or 'quit' to exit. "
                   "\n Enter a calculation: ")

while true:
    user_input = input("Enter a calculation: ")

    #exit conditional statement
    if user_input.lower() in ["q", "quit"]:
        print("Exiting the calculator. Goodbye!")
        break
#print user input
print("You entered: ", user_input)

# evaluate the operation
try:
    result = eval(user_input)
    print("Result: ", result)
except Exception as e:
    print("There was an error with your calculation:", e)
