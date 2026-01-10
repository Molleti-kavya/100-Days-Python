logo = """ 
   ____                              ____ _       _               
  / ___|__ _  ___  ___  __ _ _ __   / ___(_)_ __ | |__   ___ _ __ 
 | |   / _` |/ _ \/ __|/ _` | '__| | |   | | '_ \| '_ \ / _ \ '__|
 | |__| (_| |  __/\__ \ (_| | |    | |___| | |_) | | | |  __/ |   
  \____\__,_|\___||___/\__,_|_|     \____|_| .__/|_| |_|\___|_|   
                                           |_|                 
"""
print(logo)
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
should_continue = True

def caesar(original_text, shift_amount,encode_or_decode):
    output_text = ""
    if encode_or_decode == "decrypt":
        shift_amount *= -1
    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print  (f"Here is the {encode_or_decode}ed result : {output_text}")

while should_continue:
        direction = input("Type 'Encrypt' to encrypt and 'Decrypt' to decrypt : \n ").lower()
        text = input("Type your message : \n").lower()
        shift = int(input("Type the shift number : \n"))

        caesar(text,shift,direction)
        restart = input("Type 'Yes' to continue. otherwise, type 'No' :\n").lower()
        if restart == "no":
            should_continue = False