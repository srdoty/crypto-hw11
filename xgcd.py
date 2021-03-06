# This file implements the Euclidean Algorithm and the Extended EA.

# Euclidean Algorithm

def gcd(a,b):
    """returns g = gcd(a,b)"""
    while b != 0:
        q, r = divmod(a,b)
        a,b = b, r
    return a # when b is zero


# Extended Euclidean Algorithm

def xgcd(a,b):
    """returns the gcd and the numbers x,y such that gcd = ax+by"""
    prevx, x = 1, 0;  prevy, y = 0, 1
    while b != 0:
        q, r = divmod(a,b)
        x, prevx = prevx - q*x, x  
        y, prevy = prevy - q*y, y
        a, b = b, r
    return a, prevx, prevy



# EXPLANATION:
# Mathematical analysis reveals that at each stage in the calculation
# the current remainder can be expressed in the form ax + by for some
# integers x, y.  Moreover, the x-sequence and y-sequence are
# generated by the recursion (where q is the integer quotient of the
# current division):
#
#         new x = prev x - q * x;   new y = prev y - q * y
#
# and where the initial values are x = 0, prev x = 1, y = 1, prev y = 0.
# Finally, upon termination the x and y sequences have gone one step
# too far (as has the remainder) so return the previous x, y values. 
