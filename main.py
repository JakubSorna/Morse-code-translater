from alphabet import inverse_morse_code, morse_code, alphabet_list, morse
letter_to_morse = morse_code()
morse_to_letter = inverse_morse_code()

def choose():
    choice = input("Insert 'w' to convert word to morse code and 'm' morse code to word.")
    for char in choice:
        if char not in "wm":
            print("Wrong choice!")
            return choose()
        else:
            return choice

def Input():
    word = input("Insert word:")
    word = word.lower()
    return word
def word_to_morse():
    word = Input()
    for letter in word:
        if letter not in alphabet_list():
            print("You must use only letters!")
            return word_to_morse()
        else:
            continue
    morse = []
    for letter in word:
        morse.append(letter_to_morse[letter])
    print(" ".join(morse))

def morse_to_word():
    code = input("Insert your code by '.' and '-' and put ',' between each letter:")
    for char in code:
        if char not in "-.,":
            print("Wrong char!")
            return morse_to_word()
        else:
            continue
    code = code.split(",")
    for letter in code:
        if letter not in morse():
            print("Your morse code is not valid!")
            return morse_to_word()
        else:
            continue
    word = []
    for letter in code:
        word.append(morse_to_letter[letter])
    print("".join(word))

def main():
    choice = choose()
    if choice=="w":
        word_to_morse()
    else:
        morse_to_word()

main()