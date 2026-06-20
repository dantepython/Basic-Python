#The goal here is to create a functional yet basic average calculator, that can read at least 2 scores/grades and instantly calculate the average between them. 
n1 = int(input("Please, tell us the first number: "))
#Here, we create the first variable. Using "int" assures that it is going to be an integer number (If you prefer, you can use "float" to receive decimal numbers too). 
#The "input" does so instead of just seeing the text on screen, they can respond to it.
n2 = int(input("Please, tell us the second number: "))
#Now, we'll create a variable to actually calculate the average, just using simple math.
avg = ((n1+n2)/2)
#Now, since we just want to show the result without any further user participation, we use "print" instead of "input".
print(f"The average between {n1} and {n2} results in an {avg} average.")
#Now we used the "f" before the print text so we can put variables in our text, using {variable_name}.
