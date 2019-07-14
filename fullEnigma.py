#!/usr/bin/env python3

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphaList = list(alphabet)
list_step = []

class Rotor:

    def __init__(self,charStr):
        self.charList = list(charStr)
        self.lastChar = self.charList[len(self.charList)-1]
        self.i = 0
        count_Rot_1 = 0
        count_Rot_2 = 0
    def encryptLetter(self,letter): #returns rotor's encoding of the character
        index = alphaList.index(letter)
        encryptedLetter = self.charList[index]
        return encryptedLetter

    def decryptLetter(self,letter): #returns rotor's decoding of the character
        index = self.charList.index(letter)
        decryptedLetter = alphaList[index]
        return decryptedLetter

    def click(self): #turns rotor one click
        self.charList = self.charList[1:]+self.charList[:1]
        if self.charList.index(self.lastChar) == 0:
            self.i = 1
            return False
        if self.i == 1:
            self.i = 0
            return True
        else:
            return False

class Reflector: #Combines letters pairwise. Every letter has a partner
    def __init__(self):
        self.pairs =['EW', 'OG', 'DM', 'BC', 'TI', 'VJ', 'PA', 'LH', 'YQ', 'UR', 'XF', 'NS', 'ZK']
        self.List1 = []
        self.List2 = []
        for pairs in self.pairs:
            self.List1.append(pairs[0])
            self.List2.append(pairs[1])

    def reflect(self,letter):
        if letter in self.List1:
            position = self.List1.index(letter)
            return self.List2[position]
        elif letter in self.List2:
            position = self.List2.index(letter)
            return self.List1[position]

class Plugboard: #Pairwise substitution for 12 of the letters(chosen by the user)
    def __init__(self,List):
        self.pairs = List
        self.List1 = []
        self.List2 = []
        for pairs in self.pairs:
            self.List1.append(pairs[0])
            self.List2.append(pairs[1])

    def plug(self,letter):
        if letter in self.List1:
            position = self.List1.index(letter)
            return self.List2[position]
        elif letter in self.List2:
            position = self.List2.index(letter)
            return self.List1[position]
        else:
            return letter

class Enigma:

    message_list_encrypted = []
    message_list_decrypted = []

    def __init__(self,Plugboard_Settings,Rotor_1_Settings,Rotor_2_Settings,Rotor_3_Settings):
        self.Rotor_1_Settings = Rotor(str(Rotor_1_Settings))
        self.Rotor_2_Settings = Rotor(str(Rotor_2_Settings))
        self.Rotor_3_Settings = Rotor(str(Rotor_3_Settings))
        self.Plugboard_Settings = Plugboard(Plugboard_Settings)
        self.Reflector = Reflector()

    def crypt(self,message):
        message_list_encrypted = []
        message_list = list(str(message))
        for char in message_list:
            plug_Return = self.Plugboard_Settings.plug(char)
            message_char_encrypt_1 = self.Rotor_1_Settings.encryptLetter(plug_Return)
            message_char_encrypt_2 = self.Rotor_2_Settings.encryptLetter(message_char_encrypt_1)
            message_char_encrypt_3 = self.Rotor_3_Settings.encryptLetter(message_char_encrypt_2)
            reflect_Return = self.Reflector.reflect(message_char_encrypt_3)
            message_char_encrypt_3 = self.Rotor_3_Settings.decryptLetter(reflect_Return)
            message_char_encrypt_2 = self.Rotor_2_Settings.decryptLetter(message_char_encrypt_3)
            message_char_encrypt_1 = self.Rotor_1_Settings.decryptLetter(message_char_encrypt_2)
            plug_Return = self.Plugboard_Settings.plug(message_char_encrypt_1)
            message_list_encrypted.append(plug_Return)
            if self.Rotor_3_Settings.click() is True:
                if self.Rotor_2_Settings.click() is True:
                    if self.Rotor_1_Settings.click() is True:
                        break
                    else:
                        continue
                else:
                    continue
            else:
                continue
        message_str_encrypted = "".join(message_list_encrypted)
        print(message_str_encrypted)
        return(message_list_encrypted)

if ( __name__ == "__main__" ):
    main()
