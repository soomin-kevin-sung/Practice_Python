def is_ucpc(s):
    u_idx = s.find('U')
    if u_idx == -1:
        return False

    c_idx = s.find('C', u_idx + 1)
    if c_idx == -1:
        return False

    p_idx = s.find('P', c_idx + 1)
    if p_idx == -1:
        return False

    c_idx = s.find('C', p_idx + 1)
    if c_idx == -1:
        return False

    return True


s = input()
if is_ucpc(s):
    print('I love UCPC')
else:
    print('I hate UCPC')
