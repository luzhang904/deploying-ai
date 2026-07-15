def calculate(expression):

    try:
        result=eval(expression)

        return f"The answer is {result}"

    except:

        return "I cannot calculate this expression."