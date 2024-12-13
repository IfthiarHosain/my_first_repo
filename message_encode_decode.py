import random
import string
def encode(user_input):
 if (len(user_input)<=3):
   reversed_str =(user_input[::-1])
   print (f"Encoded message:{reversed_str}")
 else:
     random_letters= "".join(random.choices(string.ascii_letters,k=3))
     modified_string= random_letters+user_input+random_letters
     b= modified_string+user_input[:1]
     print(f"Encoded message:{b}")
def decode(user_input): 
 if (len(user_input)<=3):
  reversed_str=(user_input[::-1])
  print(f"Decoded message:{reversed_str}")
 else:
  num_letters_to_remove= 3
  num_letters_to_remove= min(num_letters_to_remove,len(user_input))
  random_indices =random.sample(range(len(user_input)),num_letters_to_remove)
  modified_str="".join([char for idx,char in enumerate(user_input)if idx not in random_indices])
  print(f"original message :{user_input}")
  print(f"Decoded Message:{user_input[:1]+modified_str}")
user_input = str(input("if you want to Encode press: a,\n if you want to decode press: b "))
if user_input =="a":
 message= input("Enter the message to Encode: ")
 encode(message)
elif user_input=="b" :
 message= input("Enter the message to Decode: ")
 decode(message)
else: 
  print("Invalid Input\n please enter a or b")
