# My first time messing around with Functions
def first_function():
    numero = int(input("Hello there, this is a function called first_funcion, select a number to begin: "))
    if numero == 18 :
        print("GGs")
    else:
        first_function()
first_function()