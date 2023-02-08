# def isValid(s: str) -> bool:
#     small, medium, large = 0,  0,  0
#     for ch in s:
#         if ch == '(': small = small + 1
#         elif ch == '[': medium = medium + 1
#         elif ch == '{': large = large + 1
#         elif ch == ')': small = small - 1
#         elif ch == ']': medium = medium - 1
#         elif ch == '}': large = large - 1
#     if small == 0 and medium == 0 and large == 0: return True
#     else: return False

def isValid(s: str) -> bool:
    if s[0] in [')', ']', '}']: return False
    stack = []
    for ch in s:
        if len(stack) == 0 and ch in [')', ']', '}']: return False
        if ch in ['(', '[', '{']:
            stack.append(ch)
        elif ch in [')', ']', '}'] and len(stack) > 0:
            if stack[len(stack)-1] == '(' and ch == ')':
                stack.pop()
            elif stack[len(stack)-1] == '[' and ch == ']':
                stack.pop()
            elif stack[len(stack)-1] == '{' and ch == '}':
                stack.pop()
            else: stack.append(ch)
    if len(stack) == 0: return True
    else: return False