#from forces import force_d
from math import sqrt, cos, sin, pi
"""
Ay: the y-component of the force at support A.
Cx: the x-component of the force at support C.
Cy: the y-component of the force at support C.
Tab: the tension in member AB.
Tad: the tension in member AD.
Tbc: the tension in member BC.
Tbd: the tension in member BD.
Tcd: the tension in member CD.
"""
force_d = 98
fd = force_d
Cx = -fd
Ay = .5 * fd
Cy = -Ay
Tcd = -Cy / sin(pi/4)
Tcb = Cx - sin(pi/4) * Tcd
Tad = -Ay / sin(pi/4)
Tab = -Tcb
Tbd = 0