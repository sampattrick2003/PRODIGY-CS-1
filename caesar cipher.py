def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_amount + shift) % 26 + shift_amount)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def main():
    while True:
        print("Caesar Cipher Program")
        choice = input("Would you like to (e)ncrypt or (d)ecrypt a message? (Enter 'q' to quit): ").lower()
        
        if choice == 'q':
            print("Exiting the program.")
            break
        
        if choice in ['e', 'd']:
            text = input("Enter your message: ")
            shift = int(input("Enter the shift value: "))

            if choice == 'e':
                encrypted_text = caesar_cipher_encrypt(text, shift)
                print(f"Encrypted message: {encrypted_text}")
            elif choice == 'd':
                decrypted_text = caesar_cipher_decrypt(text, shift)
                print(f"Decrypted message: {decrypted_text}")
        else:
            print("Invalid choice. Please enter 'e' to encrypt, 'd' to decrypt, or 'q' to quit.")
        
        print()

if __name__ == "__main__":
    main()
