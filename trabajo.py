def add(x,y):
    print(f"{num1} + {num2} = {num1+num2}")
    #print(f"{num1}+{num2}"), es igual a poner print(num1,"+",num2)

def subtract(x,y):
    print(f"{num1} - {num2} = {num1-num2}")

def multiply(x,y):
    print(f"{num1} * {num2} = {num1*num2}")

def divide(x,y):
    print(f"{num1} / {num2} = {num1/num2}")

def power(x,y):
    print(f"{num1} ^ {num2} = {num1**num2}")

def Logaritmo(num1,num2=10):
    import math
    print(math.log(num1,num2))
    #mat.log es logaritmos naturales, el primer numero es num1 = el primer argumento y el num2 = base
    
num1= 2
num2= 3
Logaritmo(num1, num2)
def menu():
    print("Select operation.")
    print("1.Suma           : + ")
    print("2.Resta          : - ")
    print("3.Multiplicacion : * ")
    print("4.Division       : / ")
    print("5.Potencia       : ^ ")
    print("6.Logaritmo      : $ ")
    print("7.Cerrar         : # ")
    choice = input("Enter Choice : ")
    return choice

def clearscreen():
    #clear screen borra todo lo que se encuentra antes de la definicion
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def wait():
    #wait espera 4 segundos antes de continuar con el codigo
    import time
    time.sleep(4)

clearscreen()

while True:
    choice = menu()
    if choice in ('1','2','3','4','5','6','7'):
        num1 = int(input("Enter First Number = "))
        num2 = int(input("Enter 2nd Number = "))

        if choice == '1':
            add(num1,num2)
        elif choice == '2':
            subtract(num1,num2)
        elif choice == '3':
            multiply(num1,num2)
        elif choice == '4':
            divide(num1,num2)
        elif choice == '5':
            power(num1,num2)
        elif choice == "6":
            Logaritmo(num1,num2)
        elif choice == '7':
            print("Saliendo del programa....")
            wait()
            break    
        wait()