import numpy as np
from scipy.optimize import fsolve
import sympy as sym

def myFunction(z):
   x = z[0]
   y = z[1]

   F = np.empty((2))
   F[0] = ((x + 18930450466.13127)**2 + (y + 2610440131.656021)**2)**0.5
   F[1] = ((x + 18930447543.615204)**2 + (y + 2610439189.706784)**2)**0.5
   return F

#zGuess = np.array([1,1])
#z = fsolve(myFunction,zGuess)

#sym.init_printing()
#x,y = sym.symbols('x,y')
#f = sym.Eq(((x + 18930450466.13127)**2 + (y + 2610440131.656021)**2)**0.5, ((x + 18930447543.615204)**2 + (y + 2610439189.706784)**2)**0.5)
#g = sym.Eq(((x + 18930447543.615204)**2 + (y + 2610439189.706784)**2)**0.5, ((x + 18930450466.13127)**2 + (y + 2610440131.656021)**2)**0.5)

#result = sym.solve([f],(x,y))
#print(result)

print(-18930450466.13127**2)
print(-2610440131.656021**2)
print(-18930447543.615204**2)
print(-2610439189.706784**2)
print(-18930435776.34452**2)
print(-2610435051.919005**2)


#eq1= ((x + 18930450466.13127)**2 + (y + 2610440131.656021)**2)**0.5
#eq2= ((x + 18930447543.615204)**2 + (y - -2610439189.706784)**2)**0.5
