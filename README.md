# Build-an-Arithmetic-Formatter-Project
First project from FreeCodeCamp.org in the Scientific Computing with Python curriculum. 

## The rules of the project (Copy from FreeCodeCamp.org):
The function will return the correct conversion if the supplied problems are properly formatted, otherwise, it will return a string that describes an error that is meaningful to the user.

- Situations that will return an error:
    - If there are too many problems supplied to the function. The limit is five, anything more will return: 'Error: Too many problems.'
    - The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error returned will be: "Error: Operator must be '+' or '-'."
    - Each number (operand) should only contain digits. Otherwise, the function will return: 'Error: Numbers must only contain digits.'
    - Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be: 'Error: Numbers cannot be more than four digits.'
- If the user supplied the correct format of problems, the conversion you return will follow these rules:
    - There should be a single space between the operator and the longest of the two operands, the operator will be on the same line as the second operand, both operands will be in the same order as provided (the first will be the top one and the second will be the bottom).
    - Numbers should be right-aligned.
    - There should be four spaces between each problem.
    - There should be dashes at the bottom of each problem. The dashes should run along the entire length of each problem individually. 

## Example of output: 
By default, `show_answers` is set to `False` in the function, if you want to show the answers; change `show_answer = False` to `show_answer = True`.

 ```
    32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
  730      3799      88      172
