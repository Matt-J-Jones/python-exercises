def commands(binary_str):
    actions = ['wink', 'double blink', 'close your eyes', 'jump', 'R']
    if binary_str[1:len(binary_str)] == '0000':
        return []

    return_actions = []
    for x in range(5):
        if binary_str[x] == '1':
            return_actions.append(actions[len(actions)-1-x])

    if return_actions[0] != 'R':
        return_actions.reverse()
    else:
        return_actions.remove('R')

    return return_actions
