#!/usr/bin/env python3

import itertools
from enigma import *

def cracker(rot1,rot1_List,rot2,rot2_List,rot3,rot3_List):
    counter = 0
    decrypted_List = []
    while (counter<=26**3):
        #setting the rotors
        rotor_Settings = Enigma(rot1,rot2,rot3)
        #decrypt with current settings
        decrypted_message = rotor_Settings.decrypt("PZYGMGKHIZLLYVPMIDETWKXQCLRUNAHHCFAJSUVDZUODBTTXQDQZYMVNQXOKCNPQVLRKESAHBOEWZUKTWBQCWYEXJZTTUUHTMTERAQBDYFORQWLJCHYDRCQAZOKLBRSXHIICTUVPWAICHCSWXEDWOMPAORENVFNKDGSWXXEDSEQKTPVDHVCWHOMQPXNUBGULWWHANHETUJYITZVJYOERHVMYTRZCMALJASOGHHMGJXMWFLKFQBWPKMNOEVYWUWBVXXGHFYFRYKOQYZRGMDYUVQMLQFPFYTZWUKHAZTXYNNMEHARLWOATYKOYEJMLCOHWYPC")
        decrypted_List.append(decrypted_message)
        rot3_List = rot3_List[1:]+rot3_List[:1]
        rot3 = "".join(rot3_List)
        if ((counter%26)==0):
            rot2_List = rot2_List[1:]+rot2_List[:1]
            rot2 = "".join(rot2_List)
            if ((counter%(26**2))==0):
                rot1_List = rot1_List[1:]+rot1_List[:1]
                rot1 = "".join(rot1_List)
                counter+=1
                continue
            counter+=1
            continue
        counter+=1

    for item in decrypted_List:
        if ("MINE" in item): #Search words that are likely to be in cyphertext
            if ("ONE" in item):
                print(item)
                print("\n")

def main():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphaList = list(alphabet)
    Rotor_1_Settings="SHBMFWEIQRODTAVXCPYZUJKGNL"
    Rotor_1_Settings_List = list(Rotor_1_Settings)
    Rotor_2_Settings="GYRFNUCZLQDWMKHSJOEPBVITXA"
    Rotor_2_Settings_List = list(Rotor_2_Settings)
    Rotor_3_Settings="MSEWGQHDPRFNXATOIBUJLCZVYK"
    Rotor_3_Settings_List = list(Rotor_3_Settings)

    cracker(Rotor_1_Settings,Rotor_1_Settings_List,Rotor_2_Settings,Rotor_2_Settings_List,Rotor_3_Settings,Rotor_3_Settings_List)
    cracker(Rotor_1_Settings,Rotor_1_Settings_List,Rotor_3_Settings,Rotor_3_Settings_List,Rotor_2_Settings,Rotor_2_Settings_List)
    cracker(Rotor_2_Settings,Rotor_2_Settings_List,Rotor_3_Settings,Rotor_3_Settings_List,Rotor_1_Settings,Rotor_1_Settings_List)
    cracker(Rotor_2_Settings,Rotor_2_Settings_List,Rotor_1_Settings,Rotor_1_Settings_List,Rotor_3_Settings,Rotor_3_Settings_List)
    cracker(Rotor_3_Settings,Rotor_3_Settings_List,Rotor_2_Settings,Rotor_2_Settings_List,Rotor_1_Settings,Rotor_1_Settings_List)
    cracker(Rotor_3_Settings,Rotor_3_Settings_List,Rotor_1_Settings,Rotor_1_Settings_List,Rotor_2_Settings,Rotor_2_Settings_List)

main()
