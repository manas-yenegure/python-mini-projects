alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    # Convert large shift values
    shift_amount %= len(alphabet)

    # Reverse the shift for decoding
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        # Encrypt/decrypt only letters
        if letter in alphabet:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
        else:
            # Keep numbers, spaces, and symbols unchanged
            output_text += letter

    print(f"Here is the {encode_or_decode}d result: {output_text}")


should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    if direction not in ["encode", "decode"]:
        print("Invalid choice. Please type 'encode' or 'decode'.")
        continue

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(
        original_text=text,
        shift_amount=shift,
        encode_or_decode=direction
    )

    restart = input("\nType 'yes' if you want to go again. Otherwise type 'no': ").lower()

    if restart == "no":
        should_continue = False
        print("Goodbye!")