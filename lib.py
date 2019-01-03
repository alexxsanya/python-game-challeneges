import random, sys, itertools
from time import sleep 

ANSWERS = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it", "As I see it yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"] 

class AndelaAssign: 

  def tossMagicBall(self):
    return random.choice(ANSWERS).title()

  def magicBall(self): 

    ask_again = 'yes'

    while ask_again == 'yes' or ask_again == 'y':

      question =  raw_input('\nEnter Your Question ? : ')

      self.processing() #setting up the waiting 

      print("\n\n>>>"+self.tossMagicBall())

      ask_again =  raw_input('\nWould You Like to Ask Again ? : yes/no ')

      if ask_again == 'no' or ask_again == 'n':

        print("Good Bye !!!")

        SystemExit()
 
  def tossDice(self):
    #setting dice ranges
    min = 1
    max = 6
    return random.randint(min,max) 

  def rollingDice(self):

    roll_again = "yes"

    while roll_again == 'yes' or roll_again == 'y':

      self.processing()

      dice_value =  self.tossDice()

      print("\n\n>>> Dice Value is  "+str(dice_value) )

      roll_again = raw_input("\nWould You Like to Roll the Dice Again ? - yes/no : ")
      
      if roll_again == 'no' or roll_again == 'n':

        print("Good Bye !!!")

        SystemExit()
  
  def processing(self):
    count = 1
    for i in itertools.cycle(['|','+','/','~']):
      if count == 6:
        break
      sys.stdout.write('\rProcessing '+ i) 
      sys.stdout.flush()
      sleep(0.1)
      count += 1