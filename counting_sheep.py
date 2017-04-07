#!/usr/local/bin/python


def as_digits(n):
    """ Function that convert an integer as a set of digit
        :param n: input integer
    """

    l = []
    s = str(n)
    size = len(s)
    for i in range(size):
        l.append(int(s[i]))
    return set(l)

def is_betw_limits(n, large):
    if large :
        return n >= 0 and n <= pow(10,6)
    else :
        return n >= 0 and n <= 200


def sheep(n, large) :
    """ Function that return the last computed integer if available 
        or return "INSOMNIA" if the ten digits are not found within 
        the 100 loops
        :param n: input integer
        :param t: number of test cases to perform
        :param large: boolean to set the large dataset option
                      if true 0 <= N <= 10^6
                      else 0 <= N <= 200
    """
    try:
        int(n)
    except:
        print  (n+" is not an int or is not between limits")  

    if not is_betw_limits(n, large):
        raise Exception("N not between limits")

    if n == 0:
        # 0 is the only one integer for which insomia is reached
        return "INSOMNIA"

    m = n
    final = set(range(10))
    digit = as_digits(m)
    step = 0
    while digit != final:
        step = step + 1
        m = step*n
        digit = digit.union(as_digits(m))

    return str(m)


def counting_sheep(t, large):
    """ For each case T, call sheep(n) with n as user input
        :param t: number of test cases to perform
        :param large: boolean to set the large dataset option
                      if true 0 <= N <= 10^6
                      else 0 <= N <= 200
    """
    try:
        int(t)
    except:
        print ("T is not an integer")
    if 1 > t or t > 100 :
        raise Exception("T is not between 1 and 100")

    for i in range (t):
        print ("Enter the wanted number :")
        n = input ()
        sheeps = sheep(n, large)
        print (str(n) + " Case #" + str(i+1) + ": "+ sheeps)




# Input : T : number of test cases
# 1 <= T <= 100
if __name__ == "__main__":
    print ("Enter the number of test cases to perform : ")
    t = input()
    counting_sheep(t, True)