p = float(input('Principal Amount: '))
t = int(input('Time: '))
r = int(input('Interest Percentage: '))


def ci(p, t, r):
    x = (1 + (r / 100))**t
    i = (pr * x - pl)
    return i
print('Compound Interest: ', ci(p, t, r))
