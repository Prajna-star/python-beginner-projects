# this is the caeser cipher problem!
alphabet = list("abcdefghijklmnopqrstuvwxyz")
direction = input("Type 'encode' to encrypt and 'decode' to decrypt the message. ").lower()

def code(direction):
    if direction == 'encode' or direction == 'decode':
        text = input("The message you want to send or decrypt: ").lower()
        shift = int(input("The number of letters you want to shift: "))
        if shift > len(alphabet):
            shift = shift % len(alphabet)
        if direction == 'decode':
            shift *= -1
        new_text =''
        for i in text:
            if i in alphabet:    
                n = alphabet.index(i) + shift
                new_text += alphabet[n]
            else:
                new_text += i
        print(f"Your {direction}d message is {new_text}")
    else:
        print("Please check your wording it should either be 'encode' or 'decode'!")
code(direction)
