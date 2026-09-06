"""Unit tests for p5_solution.py."""

import unittest

from P5_Connor_Delk import caesar_cipher, caesar_decipher, letter_frequency


class TestCaesarCipher(unittest.TestCase):
    """Tests for Caesar-cipher encryption."""

    def test_basic_lowercase_shift(self) -> None:
        self.assertEqual(caesar_cipher("abc xyz", 3), "def abc")

    def test_preserves_case_spaces_and_punctuation(self) -> None:
        self.assertEqual(caesar_cipher("Hello, World!", 5), "Mjqqt, Btwqi!")

    def test_wraps_uppercase_letters(self) -> None:
        self.assertEqual(caesar_cipher("XYZ", 4), "BCD")

    def test_accepts_negative_shift(self) -> None:
        self.assertEqual(caesar_cipher("Abc", -1), "Zab")

    def test_normalizes_large_shift(self) -> None:
        self.assertEqual(caesar_cipher("Az", 55), "Dc")

    def test_zero_shift_and_empty_text(self) -> None:
        self.assertEqual(caesar_cipher("No change 123!", 0), "No change 123!")
        self.assertEqual(caesar_cipher("", 10), "")


class TestCaesarDecipher(unittest.TestCase):
    """Tests for Caesar-cipher decryption."""

    def test_decrypts_known_ciphertext(self) -> None:
        self.assertEqual(caesar_decipher("Mjqqt, Btwqi!", 5), "Hello, World!")

    def test_round_trip_for_varied_shifts(self) -> None:
        message = "Attack at Dawn: 06:30!"
        for shift in (-53, -1, 0, 1, 13, 26, 81):
            with self.subTest(shift=shift):
                encrypted = caesar_cipher(message, shift)
                self.assertEqual(caesar_decipher(encrypted, shift), message)


class TestLetterFrequency(unittest.TestCase):
    """Tests for case-insensitive English-letter counting."""

    def test_counts_letters_ignoring_case(self) -> None:
        frequencies = letter_frequency("AaBbB c")
        self.assertEqual(frequencies["a"], 2)
        self.assertEqual(frequencies["b"], 3)
        self.assertEqual(frequencies["c"], 1)

    def test_ignores_non_alphabetic_characters(self) -> None:
        frequencies = letter_frequency("A-1 a! 23?")
        self.assertEqual(frequencies["a"], 2)
        self.assertEqual(sum(frequencies.values()), 2)

    def test_contains_every_letter_in_alphabetical_order(self) -> None:
        frequencies = letter_frequency("")
        self.assertEqual(list(frequencies), list("abcdefghijklmnopqrstuvwxyz"))
        self.assertTrue(all(count == 0 for count in frequencies.values()))

    def test_counts_a_pangram(self) -> None:
        frequencies = letter_frequency("The quick brown fox jumps over the lazy dog")
        self.assertEqual(frequencies["o"], 4)
        self.assertEqual(frequencies["t"], 2)
        self.assertEqual(frequencies["z"], 1)
        self.assertEqual(sum(frequencies.values()), 35)


if __name__ == "__main__":
    unittest.main()
