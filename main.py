import sys
import time
import os


def clear():
  if os.name == "nt":
    _ = os.system("cls")
  else:
    _ = system("clear")
    
   
def slowprint(str):
  for letter in str:
      sys.stdout.write(letter)
      sys.stdout.flush()
      time.sleep(0.05)
  print()

def mediumprint(str):
  for letter in str:
      sys.stdout.write(letter)
      sys.stdout.flush()
      time.sleep(0.025)
  print()

def fastprint(str):
  for letter in str:
      sys.stdout.write(letter)
      sys.stdout.flush()
      time.sleep(0.000000000000000001)
  print()
