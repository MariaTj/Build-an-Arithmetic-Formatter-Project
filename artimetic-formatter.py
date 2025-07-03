def arithmetic_arranger(problems, show_answers=False):
    top_line = []
    bottom_line = []
    dashes_line = []
    answers_line = []
    if len(problems) > 5:
        return "Error: Too many problems."
    for problem in problems:
        
        parts = problem.split(' ')
        first, operator, second = parts
        
        if not first.isdigit() or not second.isdigit(): 
            return("Error: Numbers must only contain digits.")
        
        if operator not in ["+", "-"]:
            return("Error: Operator must be '+' or '-'.")
        
        if len(first) > 4  or len(second) > 4:
            return('Error: Numbers cannot be more than four digits.')

        right_aligned = problem.rjust(4)
        width = max(len(first), len(second)) + 2

        top_line.append(first.rjust(width))
        bottom_line.append(operator + second.rjust(width - 1))
        dashes_line.append('-'*width)

        if operator == '+':
            result = str(int(first) + int(second))
        else:
            result = str(int(first) - int(second))

        answers_line.append(result.rjust(width))

    line1 = "    ".join(top_line)
    line2 = "    ".join(bottom_line)
    line3 = "    ".join(dashes_line)
    line4 = "    ".join(answers_line)
    
    if show_answers:
        return line1 + "\n" + line2 + "\n" + line3 + "\n" + line4
    else:
        return line1 + "\n" + line2 + "\n" + line3

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')