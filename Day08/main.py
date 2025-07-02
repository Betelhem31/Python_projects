import math
from art import logo
#function defination
def greet():
    print('Hello Welcome!')
    print('Hello Welcome!')
    print('Hello Welcome!')

greet()

def greet_with_name(name):
    print(f'Helo {name}')

greet_with_name('PAul') 

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with(name= 'SElam', location = "Ethiopia")

# #calculate area
# def paint_calc(height, width, cover):
#    result = math.ceil((height * width) / coverage)
   
#    print(f"you will need to buy {result} cans of paint!")

# test_h =int(input("Height of wall:  "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height= test_h, width=test_w, cover=coverage)

#prime number
# def prime_checker(number):
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#     if is_prime:
#         print("it is a prime number.")
#     else:
#         print("it is a not prime number.")
    

# n = int(input("Check this number: "))
# prime_checker(number=n)

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26



    def caesar(plain_text, shift_amount, location):
        cipher_text = ''
        for letter in plain_text:
            if letter in alphabet:
                position = alphabet.index(letter)
                if location =='encode':
                    new_poition = position + shift_amount
                elif location == 'decode':
                        new_poition = position - shift_amount
                else:
                    print("Wrng key word")

                new_letter = alphabet[new_poition]
                cipher_text = cipher_text + new_letter
            else:
                cipher_text += letter
        print(f"The {location} text is {cipher_text}.")

    caesar(plain_text=text, shift_amount= shift, location= direction)

    result = input("Wanna go again? 'yes' or 'no'")
    if result == 'no':
        should_continue = False
        print("ok then see you!")





    