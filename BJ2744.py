s = input()
print(''.join([c.lower() if c.isupper() else c.upper() for c in s]))
