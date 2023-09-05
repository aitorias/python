# Conditionals

## `if()` statements

We can use the concept of **branching** to alter code execution sequence depending on the values of variables. We can use an if statement to evaluate a comparison. We start with the `if` keyword, followed by our comparison. We end the line with a colon. The body of the if statement is then indented to the right. If the comparison is `True`, the code inside the `if())` body is executed. If the comparison evaluates to `False`, then the code block is skipped and will not be run.

## `else` statements

The `else` statement follows an if block, and is composed of the keyword `else` followed by a colon. The body of the `else` statement is indented to the right, and will be executed if the above if statement doesn’t execute.

We also touched on the modulo operator, which is represented by the percent sign: `%`. This operator performs integer division, but only returns the remainder of this division operation. If we're dividing 5 by 2, the quotient is 2, and the remainder is 1. Two 2s can go into 5, leaving 1 left over. So 5%2 would return 1. Dividing 10 by 5 would give us a quotient of 2 with no remainder, since 5 can go into 10 twice with nothing left over. In this case, 10%5 would return 0, as there is no remainder.

# `elif()` statement

The `elif()` statement allows us even more comparisons to perform more complex branching. Very similar to the if statements, an `elif()` statement starts with the e`elif`lif keyword, followed by a comparison to be evaluated. This is followed by a colon, and then the code block on the next line, indented to the right. An elif statement must follow an if statement, and will only be evaluated if the if statement was evaluated as false. You can include multiple elif statements to build complex branching.
