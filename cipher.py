import time
class CaesarCipher:
    # this method encrypt the plain text
    start =time.time()
    def encrypt(plainText,key):
        result = ""
        for char in plainText:
            if char == " ": 
                result += " "
                continue
            if ord(char) > 96 :
                result += chr((ord(char) + key - 97) % 26 + 97)
            else:
                result += chr((ord(char)+ key - 65) % 26 +65)
        return result
    end = time.time()
    # this method decrypt cipher text
    start2 = time.time()
    def decrypt(encryptedText,key):
        result = ""
        for char in encryptedText:
            if char == " ":
                result += " "
                continue
            if ord(char) > 96 :
                result += chr((ord(char) - key - 97) % 26 + 97)
            else:
                result += chr((ord(char) - key -65) % 65 +65)
        return result
    end2 = time.time()
    plainText = input("Enter message you would like to encrypt: \n")
    print("Your message is:",plainText)

    key = int(input("Enter key:"))
    UserInput = input("Type 'encrypt' for encryption and 'decrypt' for decrytion. \n")
    if(UserInput=='encrypt'):
        encrypt_msg=encrypt(plainText,key)
        print("Your encrypted message is:",encrypt_msg)
        print("encryption time is: ", end - start, "seconds")
    elif(UserInput=='decrypt'):
        print("Your decrypted message is:",decrypt(plainText,key))
        print("decryption time is: ", end2 - start2, "seconds")
    else:
        print("Invalid Input")