# SOFTSUSY3.3.7 SLHA compliant output
# B.C. Allanach, Comput. Phys. Commun. 143 (2002) 305-331, hep-ph/0104145
Block SPINFO          # Program information
     1    SOFTSUSY    # spectrum calculator
     2    3.3.7       # version number
Block MODSEL  # Select model
     1    1   # sugra
Block SMINPUTS             # Standard Model inputs
     1    1.27934000e+02   # alpha_em^(-1)(MZ) SM MSbar
     2    1.16637000e-05   # G_Fermi
     3    1.17200000e-01   # alpha_s(MZ)MSbar
     4    9.11876000e+01   # MZ(pole)
     5    4.25000000e+00   # mb(mb)
     6    1.73300000e+02   # Mtop(pole)
     7    1.77700000e+00   # Mtau(pole)
Block MINPAR               # SUSY breaking input parameters
     3    4.00000000e+01   # tanb
     4    1.00000000e+00   # sign(mu)
     1    1.15000000e+03   # m0
     2    4.25000000e+02   # m12
     5   -5.00000000e+02   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    2.11822633e+16   # MX scale
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=3.34330700e-05
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.04541468e+01   # MW
        25     1.16571218e+02   # h0
        35     9.02091213e+02   # H0
        36     9.02201706e+02   # A0
        37     9.06459491e+02   # H+
   1000021     1.04501472e+03   # ~g
   1000022     1.77574812e+02   # ~neutralino(1)
   1000023     3.39312735e+02   # ~neutralino(2)
   1000024     3.39405338e+02   # ~chargino(1)
   1000025    -5.96236496e+02   # ~neutralino(3)
   1000035     6.06779372e+02   # ~neutralino(4)
   1000037     6.07627463e+02   # ~chargino(2)
   1000001     1.43783712e+03   # ~d_L
   1000002     1.43578267e+03   # ~u_L
   1000003     1.43778710e+03   # ~s_L
   1000004     1.43573257e+03   # ~c_L
   1000005     1.12643161e+03   # ~b_1
   1000006     9.33634580e+02   # ~t_1
   1000011     1.18109803e+03   # ~e_L
   1000012     1.17809881e+03   # ~nue_L
   1000013     1.18084318e+03   # ~mu_L
   1000014     1.17780699e+03   # ~numu_L
   1000015     9.52409194e+02   # ~stau_1
   1000016     1.08259843e+03   # ~nu_tau_L
   2000001     1.41774783e+03   # ~d_R
   2000002     1.41882613e+03   # ~u_R
   2000003     1.41765223e+03   # ~s_R
   2000004     1.41881961e+03   # ~c_R
   2000005     1.25098507e+03   # ~b_2
   2000006     1.15880972e+03   # ~t_2
   2000011     1.16036968e+03   # ~e_R
   2000013     1.15977478e+03   # ~mu_R
   2000015     1.08899369e+03   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -2.59457757e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.95885405e-01   # N_{1,1}
  1  2    -1.38322800e-02   # N_{1,2}
  1  3     8.51496880e-02   # N_{1,3}
  1  4    -2.77571410e-02   # N_{1,4}
  2  1     3.30699902e-02   # N_{2,1}
  2  2     9.74413558e-01   # N_{2,2}
  2  3    -1.91892801e-01   # N_{2,3}
  2  4     1.12257503e-01   # N_{2,4}
  3  1    -3.95197645e-02   # N_{3,1}
  3  2     5.80991792e-02   # N_{3,2}
  3  3     7.02508272e-01   # N_{3,3}
  3  4     7.08198278e-01   # N_{3,4}
  4  1    -7.45441090e-02   # N_{4,1}
  4  2     2.16682651e-01   # N_{4,2}
  4  3     6.80006479e-01   # N_{4,3}
  4  4    -6.96478997e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.62263921e-01   # U_{1,1}
  1  2    -2.72117889e-01   # U_{1,2}
  2  1     2.72117889e-01   # U_{2,1}
  2  2     9.62263921e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.86958260e-01   # V_{1,1}
  1  2    -1.60976377e-01   # V_{1,2}
  2  1     1.60976377e-01   # V_{2,1}
  2  2     9.86958260e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.06529272e-01   # F_{11}
  1  2     9.51861232e-01   # F_{12}
  2  1     9.51861232e-01   # F_{21}
  2  2    -3.06529272e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.82548624e-01   # F_{11}
  1  2     1.86005919e-01   # F_{12}
  2  1    -1.86005919e-01   # F_{21}
  2  2     9.82548624e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.58008248e-01   # F_{11}
  1  2     9.87437792e-01   # F_{12}
  2  1     9.87437792e-01   # F_{21}
  2  2    -1.58008248e-01   # F_{22}
Block gauge Q= 1.01596526e+03  # SM gauge couplings
     1     3.62152581e-01   # g'(Q)MSSM DRbar
     2     6.41936999e-01   # g(Q)MSSM DRbar
     3     1.05666062e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.01596526e+03  
  3  3     8.55904191e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.01596526e+03  
  3  3     5.16787775e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.01596526e+03  
  3  3     4.12740102e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.01596526e+03 # Higgs mixing parameters
     1     5.88385791e+02    # mu(Q)MSSM DRbar
     2     3.92188927e+01    # tan beta(Q)MSSM DRbar
     3     2.43674418e+02    # higgs vev(Q)MSSM DRbar
     4     9.80337067e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.01596526e+03  # MSSM DRbar SUSY breaking parameters
     1     1.79432929e+02      # M_1(Q)
     2     3.32941599e+02      # M_2(Q)
     3     9.45465756e+02      # M_3(Q)
    21     4.89993403e+05      # mH1^2(Q)
    22    -3.31661658e+05      # mH2^2(Q)
    31     1.17826024e+03      # meL(Q)
    32     1.17796924e+03      # mmuL(Q)
    33     1.08516303e+03      # mtauL(Q)
    34     1.15825149e+03      # meR(Q)
    35     1.15765638e+03      # mmuR(Q)
    36     9.57647430e+02      # mtauR(Q)
    41     1.41173958e+03      # mqL1(Q)
    42     1.41168870e+03      # mqL2(Q)
    43     1.10914885e+03      # mqL3(Q)
    44     1.39583074e+03      # muR(Q)
    45     1.39582410e+03      # mcR(Q)
    46     9.19971091e+02      # mtR(Q)
    47     1.39406570e+03      # mdR(Q)
    48     1.39396829e+03      # msR(Q)
    49     1.22579590e+03      # mbR(Q)
Block au Q= 1.01596526e+03  
  1  1    -1.30188289e+03      # Au(Q)MSSM DRbar
  2  2    -1.30185027e+03      # Ac(Q)MSSM DRbar
  3  3    -8.79603097e+02      # At(Q)MSSM DRbar
Block ad Q= 1.01596526e+03  
  1  1    -1.50805914e+03      # Ad(Q)MSSM DRbar
  2  2    -1.50797607e+03      # As(Q)MSSM DRbar
  3  3    -1.24463828e+03      # Ab(Q)MSSM DRbar
Block ae Q= 1.01596526e+03  
  1  1    -5.82789657e+02      # Ae(Q)MSSM DRbar
  2  2    -5.82488120e+02      # Amu(Q)MSSM DRbar
  3  3    -4.88632296e+02      # Atau(Q)MSSM DRbar
