import math

def find_hypotenuse(a,b):
    c = (a ** 2) + (b ** 2)
    hypotenuse = math.sqrt(c)
    return hypotenuse

a = int(input("what is one side of the right tringle?"))
b = int(input("what is the other side of the right tringle?"))
hypotenuse = find_hypotenuse(a,b)
print(f"the hypotenuse is {hypotenuse}.")
