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
     1    6.00000000e+02   # m0
     2    5.50000000e+02   # m12
     5   -5.00000000e+02   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    1.88685226e+16   # MX scale
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=1.87013948e-04
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03893111e+01   # MW
        25     1.17595339e+02   # h0
        35     7.31032340e+02   # H0
        36     7.30996883e+02   # A0
        37     7.35761841e+02   # H+
   1000021     1.27465442e+03   # ~g
   1000022     2.29837038e+02   # ~neutralino(1)
   1000023     4.38017637e+02   # ~neutralino(2)
   1000024     4.38152396e+02   # ~chargino(1)
   1000025    -7.50592784e+02   # ~neutralino(3)
   1000035     7.58919964e+02   # ~neutralino(4)
   1000037     7.59601680e+02   # ~chargino(2)
   1000001     1.28682170e+03   # ~d_L
   1000002     1.28452737e+03   # ~u_L
   1000003     1.28678336e+03   # ~s_L
   1000004     1.28448894e+03   # ~c_L
   1000005     1.06726205e+03   # ~b_1
   1000006     9.07732708e+02   # ~t_1
   1000011     7.03582120e+02   # ~e_L
   1000012     6.98787995e+02   # ~nue_L
   1000013     7.03510121e+02   # ~mu_L
   1000014     6.98608613e+02   # ~numu_L
   1000015     4.72318704e+02   # ~stau_1
   1000016     6.37449635e+02   # ~nu_tau_L
   2000001     1.24463261e+03   # ~d_R
   2000002     1.24794521e+03   # ~u_R
   2000003     1.24455684e+03   # ~s_R
   2000004     1.24794031e+03   # ~c_R
   2000005     1.14105303e+03   # ~b_2
   2000006     1.12643016e+03   # ~t_2
   2000011     6.35100889e+02   # ~e_R
   2000013     6.34702156e+02   # ~mu_R
   2000015     6.55496264e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -2.59913503e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.97437340e-01   # N_{1,1}
  1  2    -8.97858357e-03   # N_{1,2}
  1  3     6.73107973e-02   # N_{1,3}
  1  4    -2.25254203e-02   # N_{1,4}
  2  1     2.15724808e-02   # N_{2,1}
  2  2     9.82863990e-01   # N_{2,2}
  2  3    -1.57132505e-01   # N_{2,3}
  2  4     9.39275339e-02   # N_{2,4}
  3  1    -3.11257684e-02   # N_{3,1}
  3  2     4.56191499e-02   # N_{3,2}
  3  3     7.04199636e-01   # N_{3,3}
  3  4     7.07850940e-01   # N_{3,4}
  4  1    -6.07006390e-02   # N_{4,1}
  4  2     1.78372240e-01   # N_{4,2}
  4  3     6.89116467e-01   # N_{4,3}
  4  4    -6.99726569e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.74968006e-01   # U_{1,1}
  1  2    -2.22345198e-01   # U_{1,2}
  2  1     2.22345198e-01   # U_{2,1}
  2  2     9.74968006e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.90922769e-01   # V_{1,1}
  1  2    -1.34432384e-01   # V_{1,2}
  2  1     1.34432384e-01   # V_{2,1}
  2  2     9.90922769e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     4.16083116e-01   # F_{11}
  1  2     9.09326586e-01   # F_{12}
  2  1     9.09326586e-01   # F_{21}
  2  2    -4.16083116e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     8.87026257e-01   # F_{11}
  1  2     4.61718983e-01   # F_{12}
  2  1    -4.61718983e-01   # F_{21}
  2  2     8.87026257e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     2.82689774e-01   # F_{11}
  1  2     9.59211391e-01   # F_{12}
  2  1     9.59211391e-01   # F_{21}
  2  2    -2.82689774e-01   # F_{22}
Block gauge Q= 9.81990703e+02  # SM gauge couplings
     1     3.62276504e-01   # g'(Q)MSSM DRbar
     2     6.41583169e-01   # g(Q)MSSM DRbar
     3     1.05451264e+00   # g3(Q)MSSM DRbar
Block yu Q= 9.81990703e+02  
  3  3     8.52297677e-01   # Yt(Q)MSSM DRbar
Block yd Q= 9.81990703e+02  
  3  3     4.95393367e-01   # Yb(Q)MSSM DRbar
Block ye Q= 9.81990703e+02  
  3  3     4.24549046e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 9.81990703e+02 # Higgs mixing parameters
     1     7.46408473e+02    # mu(Q)MSSM DRbar
     2     3.92051451e+01    # tan beta(Q)MSSM DRbar
     3     2.43877847e+02    # higgs vev(Q)MSSM DRbar
     4     6.83750671e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 9.81990703e+02  # MSSM DRbar SUSY breaking parameters
     1     2.32714735e+02      # M_1(Q)
     2     4.30921124e+02      # M_2(Q)
     3     1.21818888e+03      # M_3(Q)
    21    -1.33772513e+04      # mH1^2(Q)
    22    -5.46569744e+05      # mH2^2(Q)
    31     6.99421553e+02      # meL(Q)
    32     6.99242195e+02      # mmuL(Q)
    33     6.40418396e+02      # mtauL(Q)
    34     6.32007445e+02      # meR(Q)
    35     6.31607153e+02      # mmuR(Q)
    36     4.89446373e+02      # mtauR(Q)
    41     1.24911320e+03      # mqL1(Q)
    42     1.24907356e+03      # mqL2(Q)
    43     1.05429658e+03      # mqL3(Q)
    44     1.21281792e+03      # muR(Q)
    45     1.21281289e+03      # mcR(Q)
    46     9.08908744e+02      # mtR(Q)
    47     1.20848831e+03      # mdR(Q)
    48     1.20841048e+03      # msR(Q)
    49     1.09288293e+03      # mbR(Q)
Block au Q= 9.81990703e+02  
  1  1    -1.58112308e+03      # Au(Q)MSSM DRbar
  2  2    -1.58108496e+03      # Ac(Q)MSSM DRbar
  3  3    -1.09682141e+03      # At(Q)MSSM DRbar
Block ad Q= 9.81990703e+02  
  1  1    -1.83181022e+03      # Ad(Q)MSSM DRbar
  2  2    -1.83171315e+03      # As(Q)MSSM DRbar
  3  3    -1.53901305e+03      # Ab(Q)MSSM DRbar
Block ae Q= 9.81990703e+02  
  1  1    -6.43334698e+02      # Ae(Q)MSSM DRbar
  2  2    -6.43014737e+02      # Amu(Q)MSSM DRbar
  3  3    -5.37432165e+02      # Atau(Q)MSSM DRbar
