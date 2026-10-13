def simple_interest(si,p,t,r):
    si = (p*t*r)/100
    return si

if __name__ == "__main__":
    p = int(input("Enter principal amount: "))
    t = int(input("Enter time period: "))
    r = int(input("Enter rate of interest: "))
    si = simple_interest(0, p, t, r)
    print("Simple interest is:", si)