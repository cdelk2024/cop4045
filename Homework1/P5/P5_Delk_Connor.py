"""Interactive Caesar cipher and letter-frequency analyzer.

This module provides reusable functions for encryption, decryption, and
frequency analysis.  Run the file directly to use the terminal menu.
"""

LOWERCASE_ALPHABET = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def caesar_cipher(text: str, shift: int) -> str:
    """Return *text* with each English letter shifted by *shift* positions.

    Uppercase and lowercase letters retain their original casing. Spaces,
    punctuation, numbers, and all other characters are left unchanged.
    Positive shifts move forward through the alphabet; negative shifts move
    backward. Shifts wrap around at either end of the alphabet.
    """
    shifted_text = ""

    for character in text:
        if character in LOWERCASE_ALPHABET:
            old_index = LOWERCASE_ALPHABET.index(character)
            new_index = (old_index + shift) % len(LOWERCASE_ALPHABET)
            shifted_text += LOWERCASE_ALPHABET[new_index]
        elif character in UPPERCASE_ALPHABET:
            old_index = UPPERCASE_ALPHABET.index(character)
            new_index = (old_index + shift) % len(UPPERCASE_ALPHABET)
            shifted_text += UPPERCASE_ALPHABET[new_index]
        else:
            shifted_text += character

    return shifted_text


def caesar_decipher(cyphertext: str, shift: int) -> str:
    """Decrypt Caesar-*cyphertext* that was encrypted using *shift*."""
    return caesar_cipher(cyphertext, -shift)


def letter_frequency(text: str) -> dict[str, int]:
    """Return case-insensitive counts for every English letter in *text*.

    The returned dictionary always contains the keys ``a`` through ``z`` in
    alphabetical order. Non-alphabetic and non-English characters are ignored.
    """
    frequencies = {}

    for letter in LOWERCASE_ALPHABET:
        frequencies[letter] = 0

    for character in text:
        lowercase_character = character.lower()
        if lowercase_character in LOWERCASE_ALPHABET:
            frequencies[lowercase_character] += 1

    return frequencies


def _read_shift() -> int:
    """Prompt until the user enters a valid integer shift."""
    while True:
        shift_text = input("Enter an integer shift value: ").strip()
        try:
            return int(shift_text)
        except ValueError:
            print("Invalid shift. Please enter a whole number, such as 3 or -2.")


def _display_frequencies(frequencies: dict[str, int]) -> None:
    """Print a compact alphabetical frequency table."""
    print("\nLetter frequencies in the encrypted text:")
    for start in range(0, len(LOWERCASE_ALPHABET), 6):
        letters = LOWERCASE_ALPHABET[start : start + 6]
        row = []
        for letter in letters:
            row.append(f"{letter}: {frequencies[letter]}")
        print("  ".join(row))


def main() -> None:
    """Run the interactive Caesar-cipher terminal menu."""
    while True:
        print("\nCaesar Cipher Menu")
        print("1. Encrypt and analyze a message")
        print("2. Quit")
        choice = input("Choose an option (1-2): ").strip()

        if choice == "1":
            message = input("Enter a message: ")
            shift = _read_shift()

            encrypted_text = caesar_cipher(message, shift)
            frequencies = letter_frequency(encrypted_text)
            decrypted_text = caesar_decipher(encrypted_text, shift)

            print(f"\nEncrypted text: {encrypted_text}")
            _display_frequencies(frequencies)
            print(f"\nDecrypted text: {decrypted_text}")
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please enter 1 or 2.")


if __name__ == "__main__":
    main()
