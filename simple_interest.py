import sys

def simple_interest(p,t,r):
    si = (p*t*r)/100
    return si

if __name__ == "__main__":
    p = float(sys.argv[1])
    t = float(sys.argv[2])
    r = float(sys.argv[3])

print("Simple interest is:", simple_interest(p,t,r))
