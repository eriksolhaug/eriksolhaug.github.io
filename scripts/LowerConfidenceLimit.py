# LowerConfidenceLimit.py
# Find the LOWER confidence limit of a Poisson Distribution given number of events, n, and single-sided confidence limit, CL.
import cgi, cgitb
form = cgi.FieldStorage()
n =  form.getvalue('n_input')
cl =  form.getvalue('CL_input')

import numpy as np

def S(cl):
    if cl == 0.8413:
        return 1.000
    elif cl == 0.900:
        return 1.282
    elif cl == 0.950:
        return 1.645
    elif cl == 0.975:
        return 1.960
    elif cl == 0.9772:
        return 2.000
    elif cl == 0.990:
        return 2.326
    elif cl == 0.995:
        return 2.576
    elif cl == 0.9987:
        return 3.000
    elif cl == 0.999:
        return 3.090
    elif cl == 0.9995:
        return 3.291

def beta(cl):
    if cl == 0.8413:
        return 0.0
    elif cl == 0.900:
        return 0.010
    elif cl == 0.950:
        return 0.031
    elif cl == 0.975:
        return 0.058
    elif cl == 0.9772:
        return 0.062
    elif cl == 0.990:
        return 0.103
    elif cl == 0.995:
        return 0.141
    elif cl == 0.9987:
        return 0.222
    elif cl == 0.999:
        return 0.241
    elif cl == 0.9995:
        return 0.287

def gamma(cl):
    # No case for cl == 0.8413!
    if cl == 0.900:
        return -4.00
    elif cl == 0.950:
        return -2.50
    elif cl == 0.975:
        return -2.22
    elif cl == 0.9772:
        return -2.19
    elif cl == 0.990:
        return -2.07
    elif cl == 0.995:
        return -2.00
    elif cl == 0.9987:
        return -1.88
    elif cl == 0.999:
        return -1.85
    elif cl == 0.9995:
        return -1.80

def lam_l(cl, n):
#     return (n - S(cl)*np.sqrt(n - 1/4) + (S(cl)**2 - 1)/4) # Eqn 11
#     return n*(1 - 1/(9*n) - S(cl)/(3*np.sqrt(n)))**3 # Eqn 12
#     return (n - S(cl)*np.sqrt(n) + (S(cl)**2 - 1)/3) # Eqn 13
    return n*(1 - 1/(9*n) - S(cl)/(3*np.sqrt(n)) + beta(cl)*(n**gamma(cl)))**3 # Eqn 14

value = lam_l(cl, n)

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Hello - Second CGI Program</title>"
print "</head>"
print "<body>"
print "<h3>Lower Limit: %s </h3>" % (value)
print "</body>"
print "</html>"