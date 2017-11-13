def fizzbuzz():
    i = 1
    while (i <= 100):
        if i % 3 == 0 and i % 5 == 0:
            print ("fizzbuzz")
        else:
            if i % 3 == 0:
                print("fizz")
            elif i % 5 == 0:
                print("buzz")
            else:
                print(str(i))
        i = i + 1
        
        
fizzbuzz()