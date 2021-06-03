def arithmetic_arranger(problems, solution = False):
    if len(problems) > 5: return "Error: Too many problems."
    arr = []
    for p in problems:
        vals = p.split()
        n1, op, n2 = vals[0], vals[1], vals[2]
        width = max(len(n1), len(n2)) + 2

        try: int(n1), int(n2)
        except: return "Error: Numbers must only contain digits."
        if len(n1) > 4 or len(n2) > 4: return "Error: Numbers cannot be more than four digits."
        if not(op == '+' or op == "-"): return "Error: Operator must be '+' or '-'."

        eq = [n1.rjust(width), op + n2.rjust(width - 1), "-" * width]
        if solution:
            ans = str(eval(n1 + op + n2))
            eq.append(ans.rjust(width))
        arr.append(eq)

    print(arr)
    arr = zip(*arr)
    for index, elem in enumerate(arr):
        arr[index] = "    ".join(elem)
    return "\n".join(arr)
