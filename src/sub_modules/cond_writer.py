# def writeFunc(s):
#     script = f"return "

ss = 123


def cond(a, conditions):
    try:
        # Evaluate the condition string
        result = eval(conditions)
        if isinstance(result, bool):
            return result
        else:
            raise ValueError("Condition does not evaluate to a boolean value.")
    except Exception as e:
        print(f"Error occurred while evaluating the condition: {e}")
        return False
a = [1]
condition = "a[0] == 1"
print(cond(a, condition))