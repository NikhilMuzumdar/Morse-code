import json

# Morse code dictionary is saved as a text file
# Read the file and use json.loads to store it as a dict variable
with open('morse.txt', mode="r") as file:
    content = file.read()
morse_dict = json.loads(content)

def morse_encode(string):
    output = ""
    for _ in string:
        if _.lower() in morse_dict.keys():
            output += " "+morse_dict[_.lower()]
    return output


def morse_decode(morse_string):
    # reverse the morse code dictionary (using dict comprehension) and save it as decode dict.
    decode_dict = {v: k for k, v in morse_dict.items()}
    output = ""
    for _ in morse_string.split(" "):
        if _ == " ":
            output += " "
        elif _ in decode_dict.keys():
            output += decode_dict[_].upper()
    return output

def test_function(string):
    e = morse_encode(string)
    d = morse_decode(e)
    print(f"Morse Code: {e}\nCoded and Decoded String: {d}\nEntered string: {string}")
