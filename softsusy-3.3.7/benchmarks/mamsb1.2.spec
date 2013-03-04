# SOFTSUSY3.3.7 SLHA compliant output
# B.C. Allanach, Comput. Phys. Commun. 143 (2002) 305-331, hep-ph/0104145
Block SPINFO          # Program information
     1    SOFTSUSY    # spectrum calculator
     2    3.3.7       # version number
Block MODSEL  # Select model
     1    3   # amsb
Block SMINPUTS             # Standard Model inputs
     1    1.27934000e+02   # alpha_em^(-1)(MZ) SM MSbar
     2    1.16637000e-05   # G_Fermi
     3    1.17200000e-01   # alpha_s(MZ)MSbar
     4    9.11876000e+01   # MZ(pole)
     5    4.25000000e+00   # mb(mb)
     6    1.73300000e+02   # Mtop(pole)
     7    1.77700000e+00   # Mtau(pole)
Block MINPAR               # SUSY breaking input parameters
     3    1.00000000e+01   # tanb
     4    1.00000000e+00   # sign(mu)
     1    3.75000000e+02   # m0
     2    5.00000000e+04   # m3/2
Block EXTPAR               # scale of SUSY breaking BCs
     0    2.44383050e+16   # MX scale
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=4.73294582e-04
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03945537e+01   # MW
        25     1.14138823e+02   # h0
        35     8.96362054e+02   # H0
        36     8.96177081e+02   # A0
        37     9.00002206e+02   # H+
   1000021    -1.08704799e+03   # ~g
   1000022     1.64195953e+02   # ~neutralino(1)
   1000023     4.56142464e+02   # ~neutralino(2)
   1000024     1.64387284e+02   # ~chargino(1)
   1000025    -8.62660282e+02   # ~neutralino(3)
   1000035     8.69334469e+02   # ~neutralino(4)
   1000037     8.68192209e+02   # ~chargino(2)
   1000039     5.00000000e+04   # ~gravitino
   1000001     1.07981124e+03   # ~d_L
   1000002     1.07706740e+03   # ~u_L
   1000003     1.07980474e+03   # ~s_L
   1000004     1.07706088e+03   # ~c_L
   1000005     9.38461508e+02   # ~b_1
   1000006     7.80252397e+02   # ~t_1
   1000011     3.23409952e+02   # ~e_L
   1000012     3.13390969e+02   # ~nue_L
   1000013     3.23400213e+02   # ~mu_L
   1000014     3.13376439e+02   # ~numu_L
   1000015     2.87183437e+02   # ~stau_1
   1000016     3.08923101e+02   # ~nu_tau_L
   2000001     1.09077202e+03   # ~d_R
   2000002     1.08264412e+03   # ~u_R
   2000003     1.09076503e+03   # ~s_R
   2000004     1.08263816e+03   # ~c_R
   2000005     1.07629992e+03   # ~b_2
   2000006     9.78135510e+02   # ~t_2
   2000011     3.13331427e+02   # ~e_R
   2000013     3.13302239e+02   # ~mu_R
   2000015     3.34562032e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.06403509e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1    -5.33078752e-03   # N_{1,1}
  1  2     9.95024737e-01   # N_{1,2}
  1  3    -9.57809685e-02   # N_{1,3}
  1  4     2.68953779e-02   # N_{1,4}
  2  1     9.96224637e-01   # N_{2,1}
  2  2     1.36040490e-02   # N_{2,2}
  2  3     7.34685063e-02   # N_{2,3}
  2  4    -4.42015997e-02   # N_{2,4}
  3  1    -2.12455016e-02   # N_{3,1}
  3  2     4.86009483e-02   # N_{3,2}
  3  3     7.04737277e-01   # N_{3,3}
  3  4     7.07482824e-01   # N_{3,4}
  4  1    -8.40040734e-02   # N_{4,1}
  4  2     8.58990701e-02   # N_{4,2}
  4  3     6.99123562e-01   # N_{4,3}
  4  4    -7.04833960e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.91085012e-01   # U_{1,1}
  1  2    -1.33230997e-01   # U_{1,2}
  2  1     1.33230997e-01   # U_{2,1}
  2  2     9.91085012e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.99283541e-01   # V_{1,1}
  1  2    -3.78471181e-02   # V_{1,2}
  2  1     3.78471181e-02   # V_{2,1}
  2  2     9.99283541e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1    -4.03397199e-01   # F_{11}
  1  2     9.15024972e-01   # F_{12}
  2  1     9.15024972e-01   # F_{21}
  2  2     4.03397199e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.98256599e-01   # F_{11}
  1  2     5.90234121e-02   # F_{12}
  2  1    -5.90234121e-02   # F_{21}
  2  2     9.98256599e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     5.86416866e-01   # F_{11}
  1  2     8.10009419e-01   # F_{12}
  2  1     8.10009419e-01   # F_{21}
  2  2    -5.86416866e-01   # F_{22}
Block gauge Q= 8.41434117e+02  # SM gauge couplings
     1     3.62168636e-01   # g'(Q)MSSM DRbar
     2     6.44985805e-01   # g(Q)MSSM DRbar
     3     1.06272964e+00   # g3(Q)MSSM DRbar
Block yu Q= 8.41434117e+02  
  3  3     8.63494518e-01   # Yt(Q)MSSM DRbar
Block yd Q= 8.41434117e+02  
  3  3     1.49018770e-01   # Yb(Q)MSSM DRbar
Block ye Q= 8.41434117e+02  
  3  3     9.93541702e-02   # Ytau(Q)MSSM DRbar
Block hmix Q= 8.41434117e+02 # Higgs mixing parameters
     1     8.61465195e+02    # mu(Q)MSSM DRbar
     2     9.67927809e+00    # tan beta(Q)MSSM DRbar
     3     2.44436401e+02    # higgs vev(Q)MSSM DRbar
     4     8.03303712e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 8.41434117e+02  # MSSM DRbar SUSY breaking parameters
     1     4.65558441e+02      # M_1(Q)
     2     1.59472822e+02      # M_2(Q)
     3    -1.03437810e+03      # M_3(Q)
    21     4.93756603e+04      # mH1^2(Q)
    22    -7.27136520e+05      # mH2^2(Q)
    31     3.19021116e+02      # meL(Q)
    32     3.19006831e+02      # mmuL(Q)
    33     3.14812459e+02      # mtauL(Q)
    34     3.06005913e+02      # meR(Q)
    35     3.05976115e+02      # mmuR(Q)
    36     2.97156888e+02      # mtauR(Q)
    41     1.04655478e+03      # mqL1(Q)
    42     1.04654807e+03      # mqL2(Q)
    43     9.07849722e+02      # mqL3(Q)
    44     1.05268641e+03      # muR(Q)
    45     1.05268026e+03      # mcR(Q)
    46     7.69257317e+02      # mtR(Q)
    47     1.06023129e+03      # mdR(Q)
    48     1.06022406e+03      # msR(Q)
    49     1.04518947e+03      # mbR(Q)
Block au Q= 8.41434117e+02  
  1  1     1.62907216e+03      # Au(Q)MSSM DRbar
  2  2     1.62905845e+03      # Ac(Q)MSSM DRbar
  3  3     9.24480563e+02      # At(Q)MSSM DRbar
Block ad Q= 8.41434117e+02  
  1  1     2.30319609e+03      # Ad(Q)MSSM DRbar
  2  2     2.30318338e+03      # As(Q)MSSM DRbar
  3  3     2.05129085e+03      # Ab(Q)MSSM DRbar
Block ae Q= 8.41434117e+02  
  1  1     4.90572455e+02      # Ae(Q)MSSM DRbar
  2  2     4.90540711e+02      # Amu(Q)MSSM DRbar
  3  3     4.81178731e+02      # Atau(Q)MSSM DRbar
