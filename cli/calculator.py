# Calculator project start 27 July 2025
# ----------------------------------------------
# 🔍 NOTE: Python uses indentation to control flow
# ----------------------------------------------
# Code that is *inside* the while loop must be indented.
# Anything NOT indented is considered *outside* the loop.
#
# In this calculator:
# - We want to repeatedly ask for input and evaluate it.
# - So the `try` block must be indented inside the loop,
#   otherwise it only runs *after* the user exits, which is wrong.
#
# Example:
# while True:
#     # This is INSIDE the loop
# print("Outside")  <-- This is OUTSIDE the loop
#
# If you accidentally un-indent the `try:` block,
# you'll only evaluate the *last input* (like "q") and may get an error.
# ----------------------------------------------

print("Welcome to the calculator!")
print("Type 'q' or 'quit' to exit.")

while True:
    user_input = input("\nEnter a calculation: ")

    # exit condition — don't evaluate or show other messages
    if user_input.lower() in ["q", "quit"]:
        print("Exiting the calculator. Goodbye!")
        break

    try:
        result = eval(user_input)
        print("Result:", result)
    except Exception as e:
        print("There was an error with your calculation:", e)
