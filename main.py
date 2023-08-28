
from math import *

vars = {}



def evaluate(expr):
    # ugly
    if expr[0] == "POINT":
        if len(expr) > 3:
            vars[expr[1]] = {"values": [int(x) for x in expr[2:]]}
            return "SUCESS"
        else: 
            return "YOU SHOULD PROVIDE MORE INFORMATION"


    elif expr[0] == "EQQ":
        pointA = vars[expr[1]]["values"]
        pointB = vars[expr[2]]["values"]
        m = coAngular(pointA, pointB) 
        n = coLinear(m, pointA)

        return f"{m:.2f}x {n:+.2f}"


    
        


    else:
        try: 
            print(vars[expr[0]])
        except:

            return "SOMETHING HAS FAILED"



while True:        
    repl = input(">> ").upper()

    
    expr = repl.split(" ")
    
    if repl == "EXIT": 
        break

    print(evaluate(expr))
    
  

