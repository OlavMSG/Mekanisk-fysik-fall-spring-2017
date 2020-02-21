#importerer biblotek
import numpy as np
import sympy as sp

#Variabler, kan endres
S, b, r, T, L, M = sp.symbols('S b r T L M')

#Generell formel, ender til d hvis f. eks b = d/2,d for diamter
Ghhs = np.pi**2/(1-b**3/(b**2+4*r**2)**(3/2))*S*b**2*r/(T**2*L*M)
#Derivasjon, bestem hvilke variabler som er aktuelle
dGbd = [sp.diff(Ghhs, S), sp.diff(Ghhs, b), sp.diff(Ghhs, r), sp.diff(Ghhs, T), sp.diff(Ghhs, L), sp.diff(Ghhs, M)]

#Regner ut G, legg inn verdier (disse verdiene er fra mitt forsøk, avgrenset til 4 desimaler, hadde mer python skript til å regne de ut.
#Alt er i SI-enheter
G = Ghhs.subs([(S, 0.02293), (b, 0.04791), (r, 0.05), (T, 649.13), (L, 2.115), (M,1.506)])

#Usikkerheter, må evt regnes ut, lykke til :), 4 desimaler fra mitt forsøk
deltaS = 0.001109 #Må regnes ut #Jeg Brukte delta_S = sqrt(deltaS1**2+deltaS2**2)
deltab = 7.3951e-5 #Må regnes ut #Jeg brukte  b = t_kammer/2+d_gjennomsnitt/2+ og delta_b = sqrt((O_d_gjennomsnitt/2)**2+(delta_t_kammer/2)**2), t_kammer = bredden på kammeret
deltar = 5e-5 #Må bestemmes 0.5 mm vanlig
deltaT = 5.539 #Må beregnes #Jeg Brukte O_T = sqrt((T1-T_gjennomsnitt)**2+(T2-T_gjennomsnitt)**2) og O_T_gjennomsnitt = O_T/sqrt(2)
deltaL = 0.01 #Må bestemme, her 1 cm
deltaM = 0.00125 #Må beregnes # Jeg Brukte  O_M = sqrt((M1-M_gjennomsnitt)**2+(M2-M_gjennomsnitt)**2) og O_M_gjennomsnitt = O_M/sqrt(2)

deltas = [deltaS, deltab, deltar, deltaT, deltaL, deltaM] # lage liste over deltas

#Gauss feilforplantning (∆f)**2 = (∂f/∂a * ∆a)**2 +(∂f/∂b*∆b)**2 +(∂f/∂c*∆c)**2 +... = C
#Dette er bakt inn her. ->
deltaG = np.sum([(dGbd[j].subs([(S, 0.02293), (b, 0.04791), (r, 0.05), (T, 649.13), (L, 2.115), (M,1.506)])*deltas[j])**2 for j in range(len(deltas))])
#Gauss feilforplantning ∆f = C ** (1/2)
deltaG = (deltaG)**(1/2)

#skriver ut
print('G = ', G, 'deltaG = ', deltaG)