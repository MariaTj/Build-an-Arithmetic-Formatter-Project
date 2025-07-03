def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: too many problems"
    for problem in problems:
        parts = problem.split()

        first, operator, second = parts
        if not first.isdigit() or not second.isdigit(): 
            print("Error: Numbers must only contain digits.")
        
        if operator not in ["+", "-"]:
            print("Error: Operator must be '+' or '-'.")
        
        if len(first) > 4  or len(second) > 4:
            print('Error: Numbers cannot be more than four digits.')



    return problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
