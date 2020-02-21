from numpy import *

print("Kollisjoner i 2D")

m1 = 29.8e-3
m2 = 31.6e-3
M1 = 44.9e-3
M2 = 47.1e-3

print("Eleatisk, m1 og M1")

v1x = 0.10
v1y = -0.40
v2x = 0.10
v2y = 1.06
V1x = -0.68
V1y = 0.85
V2x = -0.68
V2y = -0.09

p_forx = m1*v1x + M1*V1x
p_etterx = m1*v2x + M1*V2x
print("p_forx =", p_forx, "=", p_etterx, "= p_etterx")

p_fory = m1*v1y + M1*V1y
p_ettery = m1*v2y + M1*V2y
print("p_fory =", p_fory, "=", p_ettery, "= p_ettery")

E_for = 1/2 * m1*(v1x**2+v1y**2) + 1/2 * M1*(V1x**2+V1y**2)
E_etter = 1/2 * m1*(v2x**2+v2y**2) + 1/2 * M1*(V2x**2+V2y**2)
print("E_for = ", E_for, ". E_etter = ", E_etter)

print("Fullstendig Uelastisk")

v1x = -0.19
v1y = 0.14
v2x = 0.05
v2y = 0.14
V1x = 0.23
V1y = -0.17
V2x = 0.06
V2y = -0.17
x1 = 0.52
y1 = 0.26
x2 = 0.51
y2 = 0.28
X1 = 0.41
Y1 = 0.30
X2 = 0.43
Y2 = 0.29

p_forx = m2*v1x + M2*V1x
p_etterx = (m2+M2)*(v2x+V2x)/2
print("p_forx =", p_forx, "=", p_etterx, "= p_etterx")

p_fory = m2*v1y + M2*V1y
p_ettery = (m2+M2)*(v2y+V2y)/2
print("p_fory =", p_fory, "=", p_ettery, "= p_ettery")