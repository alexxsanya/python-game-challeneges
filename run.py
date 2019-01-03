import lib
import testLib
ass = lib.AndelaAssign()  
print("Select from the menu below to run my attempted questions :".title())
print("> 1. Rolling Dice Game\n> 2. Magic 8 Ball Game") 
try:
  option = int(raw_input())
  if option == 1:
    ass.rollingDice()
  elif option == 2:
    ass.magicBall() 
  else:
    print("Err: Try Again & Enter a correct integer option value")
    SystemExit()

except Exception:
  print("Err: None Integer Value Entered")
  SystemExit()