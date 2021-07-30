def func_fizz_buzz(n):
    
    fizzBuzz = []
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
            fizzBuzz.append("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
            fizzBuzz.append("Fizz")
        elif i % 5 == 0: 
            print("Buzz")
            fizzBuzz.append("Buzz")
        else:
            print(i)
            fizzBuzz.append(i)
    return fizzBuzz

if name == __main__:
    func_fizz_buzz(100)  
