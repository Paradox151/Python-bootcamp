# #stepehen ceaser cipher 


import string

alphabet_list = list(string.ascii_lowercase)
alphabet = alphabet_list

print('''
,adPPYba, ,adPPYYba, ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,
a8" "8a I8[ "" I8[ "" a8" "8a I8[ "" 88P' "Y8
88 88 `"Y8ba, `"Y8ba, 88 88 `"Y8ba, 88
88 88 aa ]8I aa ]8I 88 88 aa ]8I 88
"8a, ,d88 `"YbbdP"' `"YbbdP"' "8a, ,d88 `"YbbdP"' 88
`"8bbdP"Y8
      ''')
user_input=input("Type 'encode' to encrypt, 'decode' to decrypt\n").lower()
orignal_text=input("type your message\n").lower()
shift=int(input("type the shift number\n"))


def ceasar(orignal_text, shift_amount, encode_or_decode):
    output_text=""
    for letter in orignal_text:

        if encode_or_decode== "decode":
            shift_amount *= -1
        
        shif
        
 