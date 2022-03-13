def check_numbers(Number1, Number2):
    return result

Number1 = 20
Number2 = 60
print("Number1: ", Number1)
print("Number2: ", Number2)

if Number1 or Number2 % 6 ==0:
    print("One number is divisible by 6")
    
if Number1 and Number2 % 10 ==0:
    print("Both numbers are divisible by 10")

if Number1 % 6 ==0 and Number1 % 10 ==0 and Number2 % 10 ==0:
    print("True")
else:
    print("False")

if Number2 % 6 ==0 and Number1 % 10 ==0 and Number2 % 10 ==0:
    print("True")
else:
    print("False")    
    
    
