import random

# Initial permutation IP
__ip = [
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7,
    56, 48, 40, 32, 24, 16, 8, 0,
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6
]

def get_user_input_64_bit():
    while True:
        try:
            user_input = int(input("Enter a 64-bit plaintext (as a binary): "))
            if all(c in "01" for c in bin(user_input)[2:]) and len(str(user_input)) == 64:
                return user_input
            else:
                print("Invalid input. Please enter a valid 64-bit binary.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def generate_random_64_bit_number():
    return random.getrandbits(64)

def ip(user_plaintext):
  print("Performing the initial permutation...")
  binary_representation = format(user_plaintext, '064b')
  initial_permutation = [int(binary_representation[i - 1]) for i in __ip]
  print("Initial permutation result:", initial_permutation)

def menu():
    print("""--------- WELCOME! ---------
  Program Description: The initial permutation (IP) is a cryptographic operation used in the Data Encryption Standard (DES) algorithm. It is the first step in the encryption process and is applied to the 64-bit plaintext before further processing. The purpose of the initial permutation is to shuffle the bits of the plaintext to introduce confusion and diffusion, which are essential properties in cryptographic algorithms.
  --------------------------------------------------
  Menu:
  1. Generate a 64-bit plaintext
  2. Enter a 64-bit plaintext
  3. Exit""")

    user_choice = int(input("Pick an option: "))

    match user_choice:
        case 1:
            print("Generating a random 64-bit plaintext...\n")
            generated_plaintext = generate_random_64_bit_number()
            print("Generated plaintext:", bin(generated_plaintext)[2:])
            user_input = input("Would you like to perform the initial permutation? (y/n)")

            if user_input.lower() == "y":
                ip(generated_plaintext)
            else:
                menu()

        case 2:
            user_given_plaintext = get_user_input_64_bit()
            user_input = input("Would you like to perform the initial permutation? (y/n)")

            if user_input.lower() == "y":
                ip(user_given_plaintext)
            else:
                menu()

        case 3:
            print("Exiting the program.")
            exit()

menu()
