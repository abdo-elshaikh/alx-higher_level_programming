#!/usr/bin/python3
def text_indentation(text):
    """prints a text with 2 new lines """
    if type(text) != str:
        raise TypeError("text must be a string")
    for char in ".:?":
        text = text.replace(char, (char + "\n\n"))
    print(text, end="")
