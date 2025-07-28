import ast             # ast: used for converting the input expression into structured tree(AST: Abstract Syntax Tree)..
import operator        # Providing the ready-made functions like +,-,*,/ etc.

# Supported Operators:

ops = {
    ast.Add: ('+', operator.add),               # ast.Add, ast.Sub are the classes.
    ast.Sub: ('-', operator.sub),               # For each operator we store its symbol(+,-,*,/) and its function(operator.add, operator.sub).
    ast.Mult: ('*', operator.mul),
    ast.Div: ('/', operator.truediv),
    ast.Pow: ('**', operator.pow),
    ast.USub: ('-', operator.neg)
}

steps = []              # It is a Global List that is used to store the each step, whatever the operation we perform we will append the to this list.

# Recursive evaluator with step tracking:

def evaluate(node):                         # Here we use evalution() for Recursive evalution.
    if isinstance(node, ast.BinOp):         # we use Binary Operations, Unary Operations and Numbers(three types of nodes).
        left = evaluate(node.left)
        right = evaluate(node.right)
        op_symbol, op_func = ops[type(node.op)]
        result = op_func(left, right)
        steps.append(f"{left} {op_symbol} {right} = {result}")
        return result
    elif isinstance(node, ast.UnaryOp):
        operand = evaluate(node.operand)
        op_symbol, op_func = ops[type(node.op)]
        result = op_func(operand)
        steps.append(f"{op_symbol}{operand} = {result}")
        return result
    elif isinstance(node, ast.Num):
        return node.n
    
    else:                                           # If the expression has something unexpected, raise an error then Anything else is used.
        raise ValueError("Unsupported expression element.")

# Input and parse
def step_by_step_calculator(expression):            # ast.parse takes the input string and creates an expression tree.
    global steps                                    # We pass the root node (tree.body) to evaluate().
    steps = []                                      # After evaluation, we print all steps and the final result.
    try:
        tree = ast.parse(expression, mode='eval')
        result = evaluate(tree.body)
        print("\nStep-by-step evaluation:")
        for step in steps:
            print(step)
        print(f"\nFinal Result: {result}")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    expr = input("Enter a math expression: ")
    step_by_step_calculator(expr)
