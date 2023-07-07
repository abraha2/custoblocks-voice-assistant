"""
this module accepts input in the form of a verbal math equation, i.e.
"add 42 and 85," and it spits out the answer.
you may use add, multiply, divide, and subtract
"""

import math # I'll deal with this later, to make more complicated operations

operators = {"add":"+",
            "subtract":"-",
            "divide":"/",
            "multiply":"*"}

def math_module(text):
    if text.split(" ")[0] not in operators:
        return "Sorry, " + text.split(" ")[0] + " is not an operator I know of."
    for each_operator in operators:
        if each_operator in text:
            if not text.split(" ")[2].isalpha():
                return "invalid command syntax, please try again"
                 #later, use return, its perfect in this application.
            text = text.replace(each_operator + " ", "")
            operation = operators[each_operator]
            text_list = text.split(" ")
            equation = f"{text_list[0]} {operation} {text_list[2]}"
            return "\nThe answer is " + str(eval(equation))

if __name__ == '__main__':
    print(math_module(input('Type here: ')))
