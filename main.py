# Crude program to check if a number from the user is prime

# function isItValid checks if number is 1. Int, 2. Positive, 3. Greater than 1
# incorporate try: continue
def isItValid(number):
  try:                  # Test if input is int. if not throw execption and return false.
   if (int(number)):
    return(True)
  except ValueError:
    print("User Input Not And Integer")
    return(False)
  

# function isAPrime
# if a number checks as a factor of number other than one and itself it can not be prime.
# see if range 2 - number + 1 check if number mo
def isAPrime(number):
  for loopNumber in range(2,(number)):
    if (number % loopNumber == 0):
                          print(str(number) + ' is not a prime number')
                          return(False)
   
  print(str(number) + ' is a prime number')
  return(True)
                          
 
                          
# Main Execution
usrInput = ""
while (usrInput != "stop"):
  usrInput = input("Enter a Number: ")
  if (isItValid(usrInput)):
    isAPrime(int(usrInput))