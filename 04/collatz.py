def collatz():
    while (True):    
        number = 0
        temp = input('Enter number:\n')
        if not(temp.isdigit()):
            print("Please enter an integer")
        else:
            break

    number = int(temp)
    while (number != 1):
        if number % 2 == 1:
            number *= 3
            number += 1
            print(number)
        else:
            number = int(number / 2)
            print(number)
    

collatz()
        
        