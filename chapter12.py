# Exception Handling

"""try is used when we are not sure if that part of the code will throw an exception or not
    If the part of code throws exception, we go to the except block where we can show the message
    We can specifically declare different blocks for different blocks as NameError, TypeError, ZeroDivisionError, etc"""

try:
    a = int(input("Enter anything: "))  # This will work when int is entered, but throw an exception otherwise
    print(f"You entered {a}")
except Exception as e:
    # Here we declare what all types of errors will be caught in this block, this one catches all Exception.
    print(f"You got the exception message: {e}")



# Handling different errors
try:
    num = int(input("Enter a number: "))
    num = 1 / num
    print(f"Your result is {num}")

except ZeroDivisionError:
    print("You are dividing by zero")
except ValueError:
    print("You did not enter a number")
except Exception:
    print("Any other type of error occurred")
    exit()

else:
    print("This part will be printed if the try part is successfully executed without and exceptions.")

finally:
    print("This part will be executed irrespective of the execution of the code, will run whether error occurs or not.")
    '''This is always executed, even if the program exits if an error occurs (like in the 3rd except block)
        If we wrote this part of code after the except, then it will not be executed after exit() is called'''



# Raising errors
def increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("ValueError occurred")


print(f"Calling increment function on 5: {increment(5)}")
# print(f"Calling increment function on 's': {increment('s')}") --> This raises ValueError
