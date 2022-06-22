# """
#  *****************************************************************************
#    FILE:        functions.py
#
#    AUTHOR:      {Fatima Cortinas}
#
#    ASSIGNMENT:  Magic 8 Ball fortune teller and Eli's Shipping
#
#    DATE:         {06/18/2022}
#
#    DESCRIPTION: {For the magic 8-ball: ask the user for their full name and their question in the main function, pass he variables to the fortune function, create a list with the possible answers, choose a random answer from the list of possible answers, by importing random,then use random.choice(). The choice method returns a randomly selected element from the specific sequence; the sequence can be a string, a range, a list, a tuplet or any other kind of sequence. Find the index of the first name that the user input. Return a print statement where it says their first name and question, and the random answer. For Eli's shipping: ask the user for the weight of their package. For ground shipping convert the kg into lbs and then if the kg converted to lbs are 2 lbs or less multiply by 1.50, if it's over over 2 lbs but less than or equal to 6 lbs multiply by 3.00, if it's over 6 lbs but no more than 10 multiply it by 4, if it's over 10 lbs multiply it by 4.75 and the same thing for drone shipping. No matter how many lbs the ground shipping premium is always the same. Write a useful message that tells the user which method of shipping they should choose to save the most money. }
#
#  *****************************************************************************
import random

def fortune(name,question):
  
  #Possible answers for the magic 8-Ball
    possible_answers=["Yes - definitely.", "It is decidedly so.", "Without a doubt.","Reply hazy, try again.","Ask again later.","Better not tell you now.","My sources say no.","Outlook not so good.","Very doubtful."]
  #final answer
    best_answer=random.choice(possible_answers)
  
  #find the first name 
    name_index=name.find(" " )
    first_name=name[0:name_index]
  
  #final output
    return print(f"{first_name}' Question: {question}\nMagic 8-Ball's answer: {best_answer}")


def shipping(weight):

  #kg to lbs
    lbs_in_one_kg=2.20462
    lbs=(weight * lbs_in_one_kg)
  
  #Ground Shipping
    if (lbs <= 2):
      ground_shipping=(weight * 1.50) + 20
      print(f"The price of ground shipping is ${ground_shipping:.2f}.")
    elif (lbs > 2 and lbs <= 6):
      ground_shipping_2=(weight*3) + 20
      print(f"The price of ground shipping is ${ground_shipping_2:.2f}.")
    elif(lbs > 6 and lbs <= 10):
      ground_shipping_3=(weight*4) + 20
      print(f"The price of ground shipping is ${ground_shipping_3:.2f}.")
    else:
      ground_shipping_4=(weight*4.75) + 20
      print(f"The price of ground shipping is ${ground_shipping_4:.2f}.")
    

  #Ground Shipping Premium
    ground_shipping_premium=125
    print(f"The price of premium ground shipping is ${ground_shipping_premium:.2f}.")


  #Drone Shipping 
    if (lbs <= 2):
      drone_shipping=(weight*4.50)
      print(f"The price of drone shipping is ${drone_shipping:,.2f}.")
    elif (lbs >= 2 and lbs <= 6):
      drone_shipping_2=(weight*9)
      print(f"The price of drone shipping is ${drone_shipping_2:,.2f}.")
    elif(lbs > 6 and lbs <= 10):
      drone_shipping_3=(weight*12)
      print(f"The price of drone shipping is ${drone_shipping_3:,.2f}.")
    else:
      drone_shipping_4=(weight*14.25)
      print(f"The price of drone shipping is ${drone_shipping_4:,.2f}.")

    ground_shipping_=ground_shipping_4
    premium_shipping=125
    drone_shipping_=drone_shipping_4
    if ground_shipping_ < premium_shipping and ground_shipping_ < drone_shipping_:
      print(f"To save the most money, you should choose ground shipping!")
    elif drone_shipping_ < ground_shipping_ and drone_shipping_ < premium_shipping:
      print(f"To save the most money, you should choose drone shipping!")
    else:
      print(f"To save the most money, you should choose premium ground shipping!")

  
          
def main():

  #collecting input from the user for Magic 8-Ball
  name=input("What is your full name? ")
  question=input("What is your question you would like to answer? ")
  fortune(name,question)
  print()
  print()
  
  #collecting input from the user for Eli's Shipping
  kg=int(input("What is your pacakge weight in kg? "))
  print() 
  weight=shipping(kg)


##################DO NOT EDIT BELOW THIS LINE################
# This invokes the main function.  It is always included in our
# python programs. 
if __name__ == "__main__":
    main()
