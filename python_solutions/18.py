with open("input_18.txt", "r") as f:
    lines = f.readlines()

val_stack  = [None]
mode_stack = ["NONE"]

def evaluate(val):
    if mode_stack[-1] == "MULT":
        val_stack[-1] *= val
    elif mode_stack[-1] == "DIV":
        val_stack[-1] /= val
    elif mode_stack[-1] == "ADD":
        val_stack[-1] += val
    elif mode_stack[-1] == "SUB":
        val_stack[-1] -= val
    elif mode_stack[-1] == "NONE":
        val_stack[-1] = val

final_ans = 0
for line in lines:
    simple_line = line.strip().replace(" ", "")
    
    for char in simple_line:
        if char == '(':
            val_stack.append(None) # create a new context
            mode_stack.append("NONE") # create a new context
        elif char == ')':
            final_val = val_stack.pop() # create a new context
            mode_stack.pop() # create a new context
            evaluate(final_val)
        elif char == '*':
            mode_stack[-1] = "MULT"
        elif char == '/':
            mode_stack[-1] = "DIV"
        elif char == '+':
            mode_stack[-1] = "ADD"
        elif char == '-':
            mode_stack[-1] = "SUB"
        else:
            evaluate(int(char))
    final_ans += val_stack[0]
    val_stack  = [None]
    mode_stack = ["NONE"]
print(final_ans)