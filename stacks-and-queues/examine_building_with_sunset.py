def examine_building_with_sunset(it):
    stack = []
    while True:
        height = next(it, None)
        if height is not None:
            while stack and stack[-1] <= height:
                stack.pop()
            stack.append(height)
        else:
            break
    return stack
