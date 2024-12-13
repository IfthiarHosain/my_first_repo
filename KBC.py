Questions= (
   "what is the capital of bangladesh",
   "what is the name of the river that flows near postogola?",
   "what is the meaning of phone",
   "where is mirpur stadium?",
  "who is the father of the nation?"
  )

Answers=("Dhaka","Buriganga","mobile phone","In Mirpur","Hazrat Adam (AS)")

Options=(
    {"a":"Dhaka","b":"dehli","c":"chittagong","d":"sidney"},
    {"a":"Buriganga","b":"Padma","c":"Jamuna","d":"Meghna"},
    {"a":"Vodaphone","b":"mobile phone","c":"Grameenphone","d":"headphone"},
    {"a":"khulna","b":"demra","c":"In Mirpur","d":"jatrabari"},
    {"a":"prophet Mohammad","b":"Alauddin khilji","c":"Hazrat Adam(AS)"}
    )

def run_quiz():
    total_price = 0
    for i, question  in enumerate(Questions):
      print(Questions)
      for option, Answer in Options[i].items():
         print(f"{Options}:{Answers}")

      User_input=(input("choose the correct answer  (a/b/c/d)")).strip().lower()
      
      if Options(i).get(User_input)== Answers[i]:
       prize= (i+1)*5000
       total_price += prize
       print(f"you have won the [prize]")
      else:
       print("wrong answer go and fuck yourself")
      break
      
    print(f"totall prize won:[total_prize]")     
run_quiz()
   tui khankir pola,
tui khankirpola