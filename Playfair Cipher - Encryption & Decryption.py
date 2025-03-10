import re


def generate_playfair_matrix(keyword):
    keyword = keyword.upper().replace("J", "I")
    seen = set()
    matrix = []

    for char in keyword:
        if char not in seen and char.isalpha():
            seen.add(char)
            matrix.append(char)

    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in seen:
            seen.add(char)
            matrix.append(char)

    return [matrix[i:i + 5] for i in range(0, 25, 5)]


def locate_letter(matrix, letter):
    for i, row in enumerate(matrix):
        if letter in row:
            return i, row.index(letter)
    return None


def prepare_text(text):
    text = re.sub(r'[^A-Z]', '', text.upper().replace("J", "I"))
    prepared = ""
    i = 0
    while i < len(text):
        if i == len(text) - 1:
            prepared += text[i] + "X"
            break
        if text[i] == text[i + 1]:
            prepared += text[i] + "X"
            i += 1
        else:
            prepared += text[i] + text[i + 1]
            i += 2
    return prepared


def playfair_cipher(text, matrix, mode="encrypt"):
    text = prepare_text(text)
    result = ""

    for i in range(0, len(text), 2):
        row1, col1 = locate_letter(matrix, text[i])
        row2, col2 = locate_letter(matrix, text[i + 1])

        if row1 == row2:
            col1 = (col1 + 1) % 5 if mode == "encrypt" else (col1 - 1) % 5
            col2 = (col2 + 1) % 5 if mode == "encrypt" else (col2 - 1) % 5
        elif col1 == col2:
            row1 = (row1 + 1) % 5 if mode == "encrypt" else (row1 - 1) % 5
            row2 = (row2 + 1) % 5 if mode == "encrypt" else (row2 - 1) % 5
        else:
            col1, col2 = col2, col1

        result += matrix[row1][col1] + matrix[row2][col2]

    return result


keyword = input("Enter keyword: ")
matrix = generate_playfair_matrix(keyword)

print("\nPlayfair Matrix:")
for row in matrix:
    print(" ".join(row))

while True:
    choice = input("\nEnter 'e' to encrypt, 'd' to decrypt, or 'q' to quit: ").lower()
    if choice == 'q':
        break
    text = input("Enter text: ")
    if choice == 'e':
        print("Encrypted text:", playfair_cipher(text, matrix, "encrypt"))
    elif choice == 'd':
        print("Decrypted text:", playfair_cipher(text, matrix, "decrypt"))
    else:
        print("Invalid choice.")



