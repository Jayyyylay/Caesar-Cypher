from arttss import logo
print(logo)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' ','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' ','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' ','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' ']



def caesar(e_direction):

  text = input("Type your message: ").lower()
  shift = int(input("Type the shift number: "))
  if shift > 26:
    shift %= 26
  if e_direction == "encode":
    cipher_text = ""
    for letter in text:
      position = alphabet.index(letter)
      new_position = position + shift
      cipher_text += alphabet[new_position]
    print(f"The {e_direction} text is: {cipher_text}")

  elif e_direction == "decode":
    cipher_text = ""
    for letter in text:
      position = alphabet.index(letter)
      new_position = position - shift
      cipher_text += alphabet[new_position]
    print(f"The {e_direction} text is: {cipher_text}")

def main():
  again = False
  while not again:
    direc = False
    while not direc:
      direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt: ").lower()
      if direction != "encode" and direction != "decode":
        print("PLEASE INPUT THE RIGHT ONE!")
      else:
        caesar(e_direction=direction)
        direc = True
    again = True

def play_again():
  again2 = True
  while again2:
    ask = input("\nDo you want to start again? 'yes'or 'no': ").lower()
    if ask != "yes" and ask != "no":
      print("Please type Yes or No only!")
    elif ask == "no":
      again2 = False
      print("GOODBYE!")
    else:
      main()

main()
play_again()



