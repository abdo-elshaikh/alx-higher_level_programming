#!/usr/bin/python3
""" writes a string to a text file (UTF8) """


def write_file(filename="", text=""):
    """ writes a string to a text file (UTF8)
        and returns the number of characters written

        args:
            filename: name of the file
            text: text to write

        return: number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
        return len(text)
