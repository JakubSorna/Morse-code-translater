from alphabet import inverse_morse_code, morse_code
letter_to_morse = morse_code()
morse_to_letter = inverse_morse_code()

def choose():
    choice = input("Insert 'a' to convert letter to morse code and 'm' morse code to letters.")
    return choice