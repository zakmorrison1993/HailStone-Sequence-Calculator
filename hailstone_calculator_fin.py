import math #math library

class operation: #calculators operator
    
  def __init__ (self, inputvar,stepvar): #initalising
    self.inputvar = inputvar #self defined input variable
    self.stepvar = stepvar #self defined step variable 
       
  def function(self): #calculate function
     x = self.inputvar #x variable is number operator
     y = 0 #y variable is loop step variable
     number = [x] #define list, include first number
     while y < self.stepvar: #loop function
       if x%2==1: #if odd (factor of two with remaineder)
          number.append((x*3)+1) #add odd to list
          x = ((x*3)+1) #change number operator
          y += 1 #increase loop step
       elif x%2==0: #if even (factor of two)
          number.append((x/2))#add even to list
          x = (x/2) #change number operator
          y += 1 #increase loop step
     
     if y >= self.stepvar: #if loop step equal to or greater than loop defined max
      rounded = [round(num, 0) for num in number] #round list to no decimal places - don't know why you're not working ¬¬
      return rounded #return list
   
#main
cal = operation(inputvar = int(input("type a number to calculate: ")),stepvar = int(input("enter number of steps: "))) # get input number and step total
cal.function() #performs checks
print("You have chosen number " + str(cal.inputvar) + " to start with and " + str(cal.stepvar) + " amount of steps for me to perform.") #some decoration
print(str(cal.function()))#print sequence
