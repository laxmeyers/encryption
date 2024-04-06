##############################################################################
# COMPONENT:
#    CIPHER01
# Author:
#    Br. Helfrich, Kyle Mueller, <your name here if you made a change>
# Summary:
#    Implement your cipher here. You can view 'example.py' to see the
#    completed Caesar Cipher example.
##############################################################################


##############################################################################
# CIPHER
##############################################################################
class Cipher:
    def __init__(self):
        # TODO: Insert anything you need for your cipher here
        self.encryption = ""
        pass

    def get_author(self):
        # TODO: Return your name
        return "Andrew Meyers"

    def get_cipher_name(self):
        # TODO: Return the cipher name
        return "Monoalphabetic cipher"

    ##########################################################################
    # GET CIPHER CITATION
    # Returns the citation from which we learned about the cipher
    ##########################################################################
    def get_cipher_citation(self):
        # TODO: This function should return your citation(s)
        return "Security For Software Engineers by James N. Helfrich"

    ##########################################################################
    # GET PSEUDOCODE
    # Returns the pseudocode as a string to be used by the caller
    ##########################################################################
    def get_pseudocode(self):
        # TODO: This function should return your psuedocode, neatly formatted

        # The encrypt pseudocode
        pc = "encrypt(plainText, password)\n" \
             "   offset <- offsetFromPassword(password)\n" \
             "   FOR p is all values of plainText\n" \
             "      asciiOfPlainText <- (getAsciiOfCharacter(*p))\n" \
             "      asciiOfPassword <- (getAsciiOfpassword(*password[index]))\n" \
             "      asciiOfPlainText -= asciiOfPassword\n" \
             "      if bigger than 256 then take 256 away\n" \
             "   RETURN cipherText\n\n"

        # The decrypt pseudocode
        pc += "encrypt(plainText, password)\n" \
             "   offset <- offsetFromPassword(password)\n" \
             "   FOR p is all values of plainText\n" \
             "      asciiOfCipherText <- (getAsciiOfCharacter(*p))\n" \
             "      asciiOfPassword <- (getAsciiOfpassword(*password[index]))\n" \
             "      asciiOfCipherText += asciiOfPassword\n" \
             "      if smaller than 0 then add 256\n" \
             "   RETURN cipherText\n\n"

        return pc

    ##########################################################################
    # ENCRYPT
    # TODO: This takes the password and test and changes the text using the password.
    ##########################################################################
    def encrypt(self, plaintext, password):
        ciphertext = plaintext
        
        count = 0
        length = len(password)
        for c in ciphertext:
            if count >= length:
                count = 0
            passAscii1 = ord(password[count])
            cipherAscii2 = ord(c)
            cipherAscii2 += passAscii1
            if cipherAscii2 > 256:
                cipherAscii2 -= 256
            count += 1
            self.encryption += chr(cipherAscii2)
            
        # TODO - Add your code here
        return self.encryption

    ##########################################################################
    # DECRYPT
    # TODO: takes the password and uses the ascii as the numbers to then move over how many to change the letters.
    ##########################################################################
    def decrypt(self, ciphertext, password):
        plaintext = ciphertext
        decryption = ""
        count = 0
        length = len(password)
        for p in plaintext:
            if count >= length:
                count = 0
            passAscii1 = ord(password[count])
            plainAscii2 = ord(p)
            plainAscii2 -= passAscii1
            if plainAscii2 < 0:
                plainAscii2 += 256
            count += 1
            decryption += chr(plainAscii2)
            
        # TODO - Add your code here
        return decryption