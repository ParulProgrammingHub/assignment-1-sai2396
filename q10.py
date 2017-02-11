p = float(input("Principal Amount: "))
t = int(input("Time: "))
r = int(input("Interest rate: "))


def interest(p, t, r):
    si = p * (1 + ((r * t) / 100))
    print ("Simple interest: ", si)
interest(p, t, r)
