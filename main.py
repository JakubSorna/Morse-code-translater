from alphabet import inverse_morse_code, morse_code
letter_to_morse = morse_code()
morse_to_letter = inverse_morse_code()

def choose():
    choice = input("Insert 'a' to convert letter to morse code and 'm' morse code to letters.")
    return choice

def Input():
    word = input("Insert word:")
    word = word.lower()
    return word
def word_to_morse():
    word = Input()
    morse = []
    for letter in word:
        morse.append(letter_to_morse[letter])
    print(" ".join(morse))

def morse_to_word():
    code = input("Insert your code by '.' and '-' and put ',' between each letter:")
    code = code.split(",")
    word = []
    for letter in code:
        word.append(morse_to_letter[letter])
    print("".join(word))

