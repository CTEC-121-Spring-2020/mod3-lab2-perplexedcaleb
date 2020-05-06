"""
CTEC 121
Caleb Howard
Module 3 Lab 2
<assignment/lab description
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""

def main():
    try:
        print(4/0)
    except ZeroDivisionError:
        print("\nThere was a divide by zero error. Exiting\n")
        exit
    except:
        print("\nUnknown exception\n")
        exit
     

main()    