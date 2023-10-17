from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

while True:
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    new_text = []

    def encrypt(plain_text,shift_amount):
        new_text = []

        for char in plain_text:
            if char in alphabet:
                index = alphabet.index(char)
                new_index = (index + shift_amount) % len(alphabet)
                new_char = alphabet[new_index]
                new_text.append(new_char)
            else:
                new_text.append(char)

        return ''.join(new_text)

    def decrypt(cipher_text,shift_amount):
        new_text = []

        for char in cipher_text:
            if char in alphabet:
                index = alphabet.index(char)
                new_index = (index - shift_amount) % len(alphabet)
                new_char = alphabet[new_index]
                new_text.append(new_char)
        else:
            new_text.append(char)

        return ''.join(new_text)

    if direction == "encode":
        result = encrypt(plain_text=text, shift_amount=shift)
        print(f"The encoded text is {result}")
    elif direction == "decode":
        result = decrypt(cipher_text=text, shift_amount=shift)
        print(f"The decoded text is {result}")

    choice = input("Type 'N' if you want to finish the program or type anything!")

    if choice.lower() == "n":
        break


 