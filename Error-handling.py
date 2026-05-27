
try:
    number = int(input("Enter number:"))
    print(1 / number)
except ZeroDivisionError:
    print("No divide by zero")
except ValueError:
    print("Enter only numbers")
except Exception:
    print("Something went wrong")

finally:
    print("Do some cleaning")