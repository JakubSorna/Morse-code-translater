

def alphabet_list():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    list = []
    for letter in alphabet:
        list.append(letter)
    return list

def morse():
    morse =""".- # -... # -.-. # -.. # . # ..-. # --. # .... # .. # .--- # 
    -.- # .-.. # -- # -. # --- # .--. # --.- # .-. # ... # - # ..- # ...- # .-- #
     -..- # -.-- # --..""".replace("\n","").replace(" ", "")
    morse = morse.split("#")

    return morse

def morse_code():
    keys = alphabet_list()
    values = morse()
    dict={}
    for i in range(26):
        dict.update({keys[i]:values[i]})
    return dict

def inverse_morse_code():
    keys = morse()
    values = alphabet_list()
    dict={}
    for i in range(26):
        dict.update({keys[i]:values[i]})
    return dict

