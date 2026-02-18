from caeser_cipher_art import logo


alphabet = ["a" , "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

print(logo)

direction = input("Type 'encode' to encrypt, 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caeser(plain_text, shift_amount,choice):
  cipher_text = ""
  if choice == "encode":
    for letter in plain_text:
      if letter in alphabet:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        if new_position > 25:
          new_position = (new_position % 25 - 1)
        new_letter = alphabet[new_position]
      elif letter not in alphabet:
        new_letter = letter
      cipher_text += new_letter
    print(f"The {choice}d text is {cipher_text}")
  elif choice == "decode":
    for letter in plain_text:
      if letter in alphabet:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        if new_position < 0:
          new_position = (new_position + 26)
        new_letter = alphabet[new_position]
      elif letter not in alphabet:
        new_letter = letter
      cipher_text += new_letter
    print(f"The {choice}d text is {cipher_text}")
  else:
    print("Pls choose between 'encode' and 'decode'")
  game_status = input("Type 'yes' if you want to go again, Otherwise type 'no'\n").lower()
  if game_status == "yes":
    direction = input("Type 'encode' to encrypt, 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caeser(shift_amount =  shift, plain_text = text, choice = direction)
  elif game_status == 'no':
    print("Goodbye")

  
    
caeser(shift_amount =  shift, plain_text = text, choice = direction)

