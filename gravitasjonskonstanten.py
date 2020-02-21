from numpy import *

def gravitasjonskonstanten(ekstra):

    print("r = ", r, "+-", delta_r)


    M_gjennomsnitt = (M1 + M2)/2

    O_M = sqrt((M1-M_gjennomsnitt)**2+(M2-M_gjennomsnitt)**2)
    O_M_gjennomsnitt = O_M/sqrt(2)
    print("M =", M_gjennomsnitt, "+-", O_M_gjennomsnitt)


    print("L =", L, "+-", deltaL)


    print("t_kammer =", t_kammer, "+-", delta_t_kammer)



    d_gjennomsnitt = (d1+d2+d3+d4)/4
    O_d = sqrt((d1-d_gjennomsnitt)**2+(d2-d_gjennomsnitt)**2+(d3-d_gjennomsnitt)**2+(d4-d_gjennomsnitt)**2)
    O_d_gjennomsnitt = O_d/sqrt(4)
    print("d =", d_gjennomsnitt, "+-", O_d_gjennomsnitt)

    b = t_kammer/2+d_gjennomsnitt/2+ekstra
    delta_b = sqrt((O_d_gjennomsnitt/2)**2+(delta_t_kammer/2)**2)
    print("b =", b, "+-", delta_b)

    T_gjennomsnitt = (T1+T2)/2
    O_T = sqrt((T1-T_gjennomsnitt)**2+(T2-T_gjennomsnitt)**2)
    O_T_gjennomsnitt = O_T/sqrt(2)
    print("T = ", T_gjennomsnitt, "+-", O_T_gjennomsnitt)

    S = abs(S1-S2)
    delta_S = sqrt(deltaS1**2+deltaS2**2)
    print("S = ", S, "+-", delta_S)

    beta = (b**3)/((b**2+4*r**2)**1.5)


    G = (pi**2)/(1-beta)*(S*b**2*r)/(T_gjennomsnitt**2*L*M_gjennomsnitt)

    dGdS = (pi**2)/(1-beta)*1/L*(b**2*r)/(T_gjennomsnitt**2*M_gjennomsnitt)

    dGdL = -(pi**2)/(1-beta)*(S*b**2*r)/(T_gjennomsnitt**2*L**2*M_gjennomsnitt)

    dGdM = -(pi**2)/(1-beta)*(S*b**2*r)/(T_gjennomsnitt**2*L*M_gjennomsnitt**2)

    dGdT = -2*(pi**2)/(1-beta)*(S*b**2*r)/(T_gjennomsnitt**3*L*M_gjennomsnitt)

    dbetadr = - 3/2 * (b**3)/sqrt(b**2+4*r**2)*8*r
    dGdr = (pi**2)/((1-beta)**2)*(S*b**2*r)/(T_gjennomsnitt**2*L*M_gjennomsnitt)*dbetadr + (pi**2)/(1-beta)*(S*b**2)/(T_gjennomsnitt**2*L*M_gjennomsnitt)

    dbetadb = (3*b**2*(b**2+4*r**2)**1.5-b**3*3/2*sqrt(b**2+4*r*2)*2*b)/((b**2+4*r**2)**3)
    dGdb = (pi**2)/((1-beta)**2)*(S*b**2*r)/(T_gjennomsnitt**2*L*M_gjennomsnitt)*dbetadb + 2*(pi**2)/(1-beta)*(S*b*r)/(T_gjennomsnitt**2*L*M_gjennomsnitt)

    deltaG = sqrt((dGdb*delta_b)**2+(dGdS*delta_S)**2+(dGdr*delta_r)**2+(dGdL*deltaL)**2+(dGdM*O_M_gjennomsnitt)**2+(dGdT*O_T_gjennomsnitt)**2)

    print("G =", G, "+-", deltaG)

    deltaG2G = deltaG/G
    print("eller", deltaG2G*100, "% av G")
    print("deltaS/S = ", delta_S/S*100, "% av G")
    print("deltaL/L = ", deltaL/L*100, "% av G")
    print("deltab/b = ", delta_b/b*100, "% av G")
    print("deltaT/T = ", O_T_gjennomsnitt/T_gjennomsnitt*100, "% av G")
    print("deltar/r = ", delta_r/r*100, "% av G")
    print("deltaM/M = ", O_M_gjennomsnitt/M_gjennomsnitt*100, "% av G")


S1 = 432.2048e-3
deltaS1 = 1.094190e-3
S2 = 448.5159e-3
deltaS2 = 0.1838761e-3
T1 = 654.6693
T2 = 643.5912
M1 = 1504.8e-3
M2 = 1507.3e-3
r = 50.0e-3
delta_r = 0.05e-3
L = 211.5e-2
deltaL = 1e-2
t_kammer = 30.25e-3
delta_t_kammer = 0.0001e-3
d1 = 63.40e-3
d2 = 63.80e-3
d3 = 63.50e-3
d4 = 63.60e-3

gravitasjonskonstanten(0)
print("noe ekstra")
gravitasjonskonstanten(1e-3)
print("NY S1")
S1 = 425.5859e-3
gravitasjonskonstanten(0)
print("noe ekstra og NY S1")
gravitasjonskonstanten(1e-3)