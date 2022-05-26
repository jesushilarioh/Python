# 4. 
# Starting with a variable (text) containing an empty string,
# write a loop that prompts the user to type a word. Add
# the user's input to the end of (text) and then print the
# variable. The loop should repeat while the length of (text) 
# is less than 10 characters.

text = ""

while len(text) < 10:
    text += input("Type a word:")
    print(text)
