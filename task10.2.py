def function(a=input("Please, input a: "), b=input("Please, input b: ")):
    try:
        a, b = int(a), int(b)
        return a**2/b
    except ZeroDivisionError:
        return "You cannot divide by zero"
    except ValueError:
        return "You can only use numbers"


print(function())


