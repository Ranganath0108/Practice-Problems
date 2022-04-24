def BalanceParenthesis(s):
    stack = []

    for i in s:
        if(i == '[' or i == '(' or i == '{'):
            stack.append(i)
        if(i == ']' or i == ')' or i == '}'):
            if((i == ']' and stack[-1] == '[') or (i == ')' and stack[-1] == '(') or (i == '}' and stack[-1] == '{')):
                stack.pop()
    if(len(stack) == 0):
        return True
    return False


print(BalanceParenthesis("{([])}"))
print(BalanceParenthesis("()"))
print(BalanceParenthesis("([]"))
print(BalanceParenthesis("[()]{}{[()()]()}"))
print(BalanceParenthesis("[(])"))
