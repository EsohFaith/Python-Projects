import math

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

ch = 0

while ch < 5:
    print ("1. Add(+)")
    print ("2. Subtract(-)")
    print ("3. Multiply(*)")
    print ("4. Division(/)")
    print ("5. Exist")
    
    ch = int (input("Enter your choice"))

    if ch == 1:
       sum = num1 + num2
       print("sum=", sum)

    elif ch == 2:
       Diff = num1 - num2  
       print ("Difference=", Diff)

    elif ch == 3:
       Mul = num1 * num2          
       print ("prodcut=", Mul)

    elif ch == 4:
         if num2 == 0:
             print ("Cannot divide by zero!")
         else: 
          Div = num1 / num2
         print ("Quotient=", Div)

    elif ch == 5:
     break   
    else:
        print ("Invalid choice")