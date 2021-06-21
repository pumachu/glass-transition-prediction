B2nm = 0.0529177
H2kJ = 2625.5
Vf = {'H':7.842800,'C':34.939018,'N':25.922105}
Bf = {'H':6.5,'C':46.6,'N':24.2}
Rf = {'H':3.099151,'C':3.93063,'N':3.250329}

f = open('DDEC_atomic_Rcubed_moments.xyz','r')
lines = f.readlines()

natom = int(lines[0].split()[0])
SYMB = []
Vi = []
for i in range(2,natom+2):
    SYMB.append(lines[i].split()[0])
    Vi.append(float(lines[i].split()[-1]))
Bi = []
for i, V in enumerate(Vi):
    Bi.append((V/Vf[SYMB[i]])**2.0*Bf[SYMB[i]])
Ai = []
for i, B in enumerate(Bi):
    Ri = (Vi[i]/Vf[SYMB[i]])**(1.0/3.0)*Rf[SYMB[i]]
    Ai.append(0.5*B*(2*Ri)**6.0)

fo = open('VDW_parameters.txt','w')
fo.write( 'index  element  sigma(nm) epsilon(kJ/mol) \n')
for i in range(len(Bi)):
    sigma = (Ai[i]/Bi[i])**(1.0/6.0)*B2nm
    eps = Bi[i]**2.0/(4.0*Ai[i])*H2kJ
    fo.write( str(i+1) + '  '+ SYMB[i] + '  '+ str(sigma) + '  ' + str(eps) + '\n')

