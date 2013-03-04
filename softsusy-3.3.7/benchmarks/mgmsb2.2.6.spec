# SOFTSUSY3.3.7 SLHA compliant output
# B.C. Allanach, Comput. Phys. Commun. 143 (2002) 305-331, hep-ph/0104145
Block SPINFO          # Program information
     1    SOFTSUSY    # spectrum calculator
     2    3.3.7       # version number
Block MODSEL  # Select model
     1    2   # gmsb
Block SMINPUTS             # Standard Model inputs
     1    1.27934000e+02   # alpha_em^(-1)(MZ) SM MSbar
     2    1.16637000e-05   # G_Fermi
     3    1.17200000e-01   # alpha_s(MZ)MSbar
     4    9.11876000e+01   # MZ(pole)
     5    4.25000000e+00   # mb(mb)
     6    1.73300000e+02   # Mtop(pole)
     7    1.77700000e+00   # Mtau(pole)
Block MINPAR               # SUSY breaking input parameters
     3    1.50000000e+01   # tanb
     4    1.00000000e+00   # sign(mu)
     1    1.70000000e+05   # lambda
     2    1.00000000e+14   # M_mess
     5    1.00000000e+00   # N5
     6    1.00000000e+00   # cgrav
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=3.81320632e-04
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.04569865e+01   # MW
        25     1.16190753e+02   # h0
        35     1.11957755e+03   # H0
        36     1.11953496e+03   # A0
        37     1.12273478e+03   # H+
   1000021     1.26309079e+03   # ~g
   1000022     2.27580106e+02   # ~neutralino(1)
   1000023     4.38321101e+02   # ~neutralino(2)
   1000024     4.38517189e+02   # ~chargino(1)
   1000025    -8.78055396e+02   # ~neutralino(3)
   1000035     8.84611627e+02   # ~neutralino(4)
   1000037     8.85153018e+02   # ~chargino(2)
   1000039     4.02900000e+00   # ~gravitino
   1000001     1.55531197e+03   # ~d_L
   1000002     1.55345523e+03   # ~u_L
   1000003     1.55530582e+03   # ~s_L
   1000004     1.55344908e+03   # ~c_L
   1000005     1.37507734e+03   # ~b_1
   1000006     1.09374677e+03   # ~t_1
   1000011     7.52602294e+02   # ~e_L
   1000012     7.48126295e+02   # ~nue_L
   1000013     7.52688458e+02   # ~mu_L
   1000014     7.48110358e+02   # ~numu_L
   1000015     4.95125920e+02   # ~stau_1
   1000016     7.42911379e+02   # ~nu_tau_L
   2000001     1.39757632e+03   # ~d_R
   2000002     1.42655355e+03   # ~u_R
   2000003     1.39756720e+03   # ~s_R
   2000004     1.42654903e+03   # ~c_R
   2000005     1.40793077e+03   # ~b_2
   2000006     1.41876450e+03   # ~t_2
   2000011     5.12001275e+02   # ~e_R
   2000013     5.11954350e+02   # ~mu_R
   2000015     7.48590020e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -7.00210816e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.98214746e-01   # N_{1,1}
  1  2    -8.06840178e-03   # N_{1,2}
  1  3     5.62697060e-02   # N_{1,3}
  1  4    -1.83287272e-02   # N_{1,4}
  2  1     1.60199359e-02   # N_{2,1}
  2  2     9.90368567e-01   # N_{2,2}
  2  3    -1.20732056e-01   # N_{2,3}
  2  4     6.58576779e-02   # N_{2,4}
  3  1    -2.64275970e-02   # N_{3,1}
  3  2     3.93088000e-02   # N_{3,2}
  3  3     7.04963457e-01   # N_{3,3}
  3  4     7.07660176e-01   # N_{3,4}
  4  1    -5.11103212e-02   # N_{4,1}
  4  2     1.32513473e-01   # N_{4,2}
  4  3     6.96623295e-01   # N_{4,3}
  4  4    -7.03238153e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.85384142e-01   # U_{1,1}
  1  2    -1.70346975e-01   # U_{1,2}
  2  1     1.70346975e-01   # U_{2,1}
  2  2     9.85384142e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.95606597e-01   # V_{1,1}
  1  2    -9.36349506e-02   # V_{1,2}
  2  1     9.36349506e-02   # V_{2,1}
  2  2     9.95606597e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     1.76710042e-01   # F_{11}
  1  2     9.84262953e-01   # F_{12}
  2  1     9.84262953e-01   # F_{21}
  2  2    -1.76710042e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     3.91357827e-01   # F_{11}
  1  2     9.20238584e-01   # F_{12}
  2  1     9.20238584e-01   # F_{21}
  2  2    -3.91357827e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     7.40923315e-02   # F_{11}
  1  2     9.97251386e-01   # F_{12}
  2  1     9.97251386e-01   # F_{21}
  2  2    -7.40923315e-02   # F_{22}
Block gauge Q= 1.21064471e+03  # SM gauge couplings
     1     3.62931267e-01   # g'(Q)MSSM DRbar
     2     6.41403828e-01   # g(Q)MSSM DRbar
     3     1.04842907e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.21064471e+03  
  3  3     8.52153793e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.21064471e+03  
  3  3     1.96450247e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.21064471e+03  
  3  3     1.50625108e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.21064471e+03 # Higgs mixing parameters
     1     8.71603488e+02    # mu(Q)MSSM DRbar
     2     1.44703599e+01    # tan beta(Q)MSSM DRbar
     3     2.43748672e+02    # higgs vev(Q)MSSM DRbar
     4     1.30809931e+06    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.21064471e+03  # MSSM DRbar SUSY breaking parameters
     1     2.31061440e+02      # M_1(Q)
     2     4.26844070e+02      # M_2(Q)
     3     1.16096964e+03      # M_3(Q)
    21     4.80525438e+05      # mH1^2(Q)
    22    -7.33146588e+05      # mH2^2(Q)
    31     7.48808148e+02      # meL(Q)
    32     7.48792223e+02      # mmuL(Q)
    33     7.43928850e+02      # mtauL(Q)
    34     5.06941690e+02      # meR(Q)
    35     5.06894327e+02      # mmuR(Q)
    36     4.92261356e+02      # mtauR(Q)
    41     1.52036374e+03      # mqL1(Q)
    42     1.52035743e+03      # mqL2(Q)
    43     1.37300861e+03      # mqL3(Q)
    44     1.39181079e+03      # muR(Q)
    45     1.39180612e+03      # mcR(Q)
    46     1.05714616e+03      # mtR(Q)
    47     1.36061074e+03      # mdR(Q)
    48     1.36060128e+03      # msR(Q)
    49     1.34335596e+03      # mbR(Q)
Block au Q= 1.21064471e+03  
  1  1    -1.07293083e+03      # Au(Q)MSSM DRbar
  2  2    -1.07292546e+03      # Ac(Q)MSSM DRbar
  3  3    -8.55283464e+02      # At(Q)MSSM DRbar
Block ad Q= 1.21064471e+03  
  1  1    -1.27991954e+03      # Ad(Q)MSSM DRbar
  2  2    -1.27991213e+03      # As(Q)MSSM DRbar
  3  3    -1.19800646e+03      # Ab(Q)MSSM DRbar
Block ae Q= 1.21064471e+03  
  1  1    -2.40098345e+02      # Ae(Q)MSSM DRbar
  2  2    -2.40090169e+02      # Amu(Q)MSSM DRbar
  3  3    -2.37600238e+02      # Atau(Q)MSSM DRbar
