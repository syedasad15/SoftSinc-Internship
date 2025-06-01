import operator

def calculate():
    expr = input("Enter expression (e.g., 2 + 2): ")
    try:
        result = eval(expr)
        print("Result:", result)
    except Exception as e:
        print("Error:", e)