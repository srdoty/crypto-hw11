# Stand alone implementation of the modpower function,
# without any classes. Return value is always an integer.

def modpower(x,e,n):
  """returns the value of x to the e-th power mod n 
  computed by the method of successive squaring"""
  result = 1 # to get started
  s,q = x,e  # s=current square, q=current quotient
  while q > 0:
    if q%2 == 1: 
      result = (s * result) % n
    s = (s * s) % n  # compute the next square
    q = q//2         # compute the next quotient
  return result


