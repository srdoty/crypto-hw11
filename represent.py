# Convert strings to integer representations and back again to
# strings. This is needed for implementing all public-key
# cryptosystems, which assume the plaintext is representated by
# some integer.

URADIX = 1114112 # The unicode upper range limit (CONSTANT)

def rep(string):
    """returns an integer representation of the input string string"""
    k = 0; num = 0
    for char in string:
        num = num + ord(char) * URADIX**k
        k = k+1
    return num

def unrep(num):
    """returns the string that the input num represents"""
    output = '' # empty string to start
    q = num
    while q > 0:
        q,r = divmod(q,URADIX)
        output = output + chr(r)
    return output

# The above functions are inverses of one another, in the sense
# that
#
#    unrep(rep(s)) == s
#
# returns True for any input string s of any length.

# Sometimes we have a restriction on the length of the input strings,
# called its blocksize (call it B for short). In that case, we convert
# each B characters of the string to its integer representation and
# return a list of the resulting integers. This leads to

def replist(str,blocksize):
    """returns a list of integer representations of blocks of 
    length given by the blocksize"""
    B = blocksize
    return [rep(str[i:i+B]) for i in range(0, len(str), B)]

def unreplist(lst):
    """returns the string that produced lst as its replist"""
    out = '' # empty string to start
    for item in lst:
        out = out + unrep(item)
    return out

# The above functions are inverses of one another, in the sense
# that
#
#    unreplist(replist(s,B)) == s
#
# returns True for any input string s of any length, for a given
# blocksize B. 
