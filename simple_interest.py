import sys

def simple_interest(si,p,t,r):
    si = (p*t*r)/100
    return si

if __name__ == "__main__":
    p = int(sys.argv[1])
    t = int(sys.argv[2])
    r = int(sys.argv[3])
    si = simple_interest(0, p, t, r)


    print("Simple interest is:", si)