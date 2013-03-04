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
     1    3.60000000e+02   # m0
     2    6.00000000e+02   # m12
     5   -5.00000000e+02   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    1.76223363e+16   # MX scale
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=6.84606401e-05
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03891570e+01   # MW
        25     1.17912423e+02   # h0
        35     7.08993532e+02   # H0
        36     7.09000613e+02   # A0
        37     7.14120378e+02   # H+
   1000021     1.36311067e+03   # ~g
   1000022     2.50491228e+02   # ~neutralino(1)
   1000023     4.76950056e+02   # ~neutralino(2)
   1000024     4.77094977e+02   # ~chargino(1)
   1000025    -8.08653774e+02   # ~neutralino(3)
   1000035     8.16410179e+02   # ~neutralino(4)
   1000037     8.17037360e+02   # ~chargino(2)
   1000001     1.28923397e+03   # ~d_L
   1000002     1.28691111e+03   # ~u_L
   1000003     1.28919749e+03   # ~s_L
   1000004     1.28687455e+03   # ~c_L
   1000005     1.08360424e+03   # ~b_1
   1000006     9.34124314e+02   # ~t_1
   1000011     5.41148852e+02   # ~e_L
   1000012     5.35055399e+02   # ~nue_L
   1000013     5.41182795e+02   # ~mu_L
   1000014     5.34914997e+02   # ~numu_L
   1000015     2.51517989e+02   # ~stau_1
   1000016     4.86678047e+02   # ~nu_tau_L
   2000001     1.23763327e+03   # ~d_R
   2000002     1.24187337e+03   # ~u_R
   2000003     1.23756072e+03   # ~s_R
   2000004     1.24186878e+03   # ~c_R
   2000005     1.15104263e+03   # ~b_2
   2000006     1.15361641e+03   # ~t_2
   2000011     4.26418761e+02   # ~e_R
   2000013     4.26060832e+02   # ~mu_R
   2000015     5.13636869e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -2.60393621e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.97789562e-01   # N_{1,1}
  1  2    -7.78861502e-03   # N_{1,2}
  1  3     6.25059454e-02   # N_{1,3}
  1  4    -2.11738956e-02   # N_{1,4}
  2  1     1.88504606e-02   # N_{2,1}
  2  2     9.84769883e-01   # N_{2,2}
  2  3    -1.47917961e-01   # N_{2,3}
  2  4     8.94047753e-02   # N_{2,4}
  3  1    -2.87915309e-02   # N_{3,1}
  3  2     4.21311211e-02   # N_{3,2}
  3  3     7.04606442e-01   # N_{3,3}
  3  4     7.07761103e-01   # N_{3,4}
  4  1    -5.68480208e-02   # N_{4,1}
  4  2     1.68500988e-01   # N_{4,2}
  4  3     6.91189588e-01   # N_{4,3}
  4  4    -7.00451764e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.77908890e-01   # U_{1,1}
  1  2    -2.09031582e-01   # U_{1,2}
  2  1     2.09031582e-01   # U_{2,1}
  2  2     9.77908890e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.91809150e-01   # V_{1,1}
  1  2    -1.27728660e-01   # V_{1,2}
  2  1     1.27728660e-01   # V_{2,1}
  2  2     9.91809150e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     4.35441938e-01   # F_{11}
  1  2     9.00216817e-01   # F_{12}
  2  1     9.00216817e-01   # F_{21}
  2  2    -4.35441938e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     8.09644409e-01   # F_{11}
  1  2     5.86920719e-01   # F_{12}
  2  1    -5.86920719e-01   # F_{21}
  2  2     8.09644409e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     3.19168826e-01   # F_{11}
  1  2     9.47697874e-01   # F_{12}
  2  1     9.47697874e-01   # F_{21}
  2  2    -3.19168826e-01   # F_{22}
Block gauge Q= 1.00889475e+03  # SM gauge couplings
     1     3.62517640e-01   # g'(Q)MSSM DRbar
     2     6.41504712e-01   # g(Q)MSSM DRbar
     3     1.05239344e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.00889475e+03  
  3  3     8.50573371e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.00889475e+03  
  3  3     4.90342553e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.00889475e+03  
  3  3     4.27717004e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.00889475e+03 # Higgs mixing parameters
     1     8.05565439e+02    # mu(Q)MSSM DRbar
     2     3.91934202e+01    # tan beta(Q)MSSM DRbar
     3     2.43821349e+02    # higgs vev(Q)MSSM DRbar
     4     6.36175761e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.00889475e+03  # MSSM DRbar SUSY breaking parameters
     1     2.54466568e+02      # M_1(Q)
     2     4.70473236e+02      # M_2(Q)
     3     1.32360804e+03      # M_3(Q)
    21    -1.47200364e+05      # mH1^2(Q)
    22    -6.37527176e+05      # mH2^2(Q)
    31     5.34816737e+02      # meL(Q)
    32     5.34675767e+02      # mmuL(Q)
    33     4.89457827e+02      # mtauL(Q)
    34     4.21534329e+02      # meR(Q)
    35     4.21172244e+02      # mmuR(Q)
    36     2.88560424e+02      # mtauR(Q)
    41     1.24858782e+03      # mqL1(Q)
    42     1.24855061e+03      # mqL2(Q)
    43     1.07783590e+03      # mqL3(Q)
    44     1.20437334e+03      # muR(Q)
    45     1.20436867e+03      # mcR(Q)
    46     9.40037415e+02      # mtR(Q)
    47     1.19903066e+03      # mdR(Q)
    48     1.19895691e+03      # msR(Q)
    49     1.09398706e+03      # mbR(Q)
Block au Q= 1.00889475e+03  
  1  1    -1.68706366e+03      # Au(Q)MSSM DRbar
  2  2    -1.68702354e+03      # Ac(Q)MSSM DRbar
  3  3    -1.17940783e+03      # At(Q)MSSM DRbar
Block ad Q= 1.00889475e+03  
  1  1    -1.95299193e+03      # Ad(Q)MSSM DRbar
  2  2    -1.95288976e+03      # As(Q)MSSM DRbar
  3  3    -1.64810929e+03      # Ab(Q)MSSM DRbar
Block ae Q= 1.00889475e+03  
  1  1    -6.66168446e+02      # Ae(Q)MSSM DRbar
  2  2    -6.65841715e+02      # Amu(Q)MSSM DRbar
  3  3    -5.56359661e+02      # Atau(Q)MSSM DRbar
