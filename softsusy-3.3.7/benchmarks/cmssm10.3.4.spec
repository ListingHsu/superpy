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
     3    1.00000000e+01   # tanb
     4    1.00000000e+00   # sign(mu)
     1    4.50000000e+02   # m0
     2    6.75000000e+02   # m12
     5    0.00000000e+00   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    1.77127420e+16   # MX scale
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=2.04536066e-04
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03930649e+01   # MW
        25     1.16896205e+02   # h0
        35     1.02955301e+03   # H0
        36     1.02929708e+03   # A0
        37     1.03273331e+03   # H+
   1000021     1.52386707e+03   # ~g
   1000022     2.81702278e+02   # ~neutralino(1)
   1000023     5.33076026e+02   # ~neutralino(2)
   1000024     5.33322437e+02   # ~chargino(1)
   1000025    -8.26025059e+02   # ~neutralino(3)
   1000035     8.37849132e+02   # ~neutralino(4)
   1000037     8.37705235e+02   # ~chargino(2)
   1000001     1.44817854e+03   # ~d_L
   1000002     1.44617590e+03   # ~u_L
   1000003     1.44817482e+03   # ~s_L
   1000004     1.44617217e+03   # ~c_L
   1000005     1.31700572e+03   # ~b_1
   1000006     1.10245423e+03   # ~t_1
   1000011     6.37604100e+02   # ~e_L
   1000012     6.32479129e+02   # ~nue_L
   1000013     6.37785852e+02   # ~mu_L
   1000014     6.32472049e+02   # ~numu_L
   1000015     5.10123015e+02   # ~stau_1
   1000016     6.30169289e+02   # ~nu_tau_L
   2000001     1.39075791e+03   # ~d_R
   2000002     1.39574641e+03   # ~u_R
   2000003     1.39075407e+03   # ~s_R
   2000004     1.39574238e+03   # ~c_R
   2000005     1.38424973e+03   # ~b_2
   2000006     1.34936414e+03   # ~t_2
   2000011     5.17264906e+02   # ~e_R
   2000013     5.17247363e+02   # ~mu_R
   2000015     6.36547665e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.05289635e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.97501993e-01   # N_{1,1}
  1  2    -1.03320444e-02   # N_{1,2}
  1  3     6.41259399e-02   # N_{1,3}
  1  4    -2.77648441e-02   # N_{1,4}
  2  1     2.40935934e-02   # N_{2,1}
  2  2     9.78817484e-01   # N_{2,2}
  2  3    -1.66652434e-01   # N_{2,3}
  2  4     1.16459422e-01   # N_{2,4}
  3  1    -2.52431364e-02   # N_{3,1}
  3  2     3.64385858e-02   # N_{3,2}
  3  3     7.05003325e-01   # N_{3,3}
  3  4     7.07817296e-01   # N_{3,4}
  4  1    -6.14170717e-02   # N_{4,1}
  4  2     2.01200921e-01   # N_{4,2}
  4  3     6.86356424e-01   # N_{4,3}
  4  4    -6.96175977e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.71741553e-01   # U_{1,1}
  1  2    -2.36047356e-01   # U_{1,2}
  2  1     2.36047356e-01   # U_{2,1}
  2  2     9.71741553e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.86137426e-01   # V_{1,1}
  1  2    -1.65930639e-01   # V_{1,2}
  2  1     1.65930639e-01   # V_{2,1}
  2  2     9.86137426e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.29984757e-01   # F_{11}
  1  2     9.43986261e-01   # F_{12}
  2  1     9.43986261e-01   # F_{21}
  2  2    -3.29984757e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.92000231e-01   # F_{11}
  1  2     1.26236056e-01   # F_{12}
  2  1    -1.26236056e-01   # F_{21}
  2  2     9.92000231e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.03800386e-01   # F_{11}
  1  2     9.94598150e-01   # F_{12}
  2  1     9.94598150e-01   # F_{21}
  2  2    -1.03800386e-01   # F_{22}
Block gauge Q= 1.18405726e+03  # SM gauge couplings
     1     3.62870430e-01   # g'(Q)MSSM DRbar
     2     6.41220986e-01   # g(Q)MSSM DRbar
     3     1.04544721e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.18405726e+03  
  3  3     8.51410214e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.18405726e+03  
  3  3     1.33445997e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.18405726e+03  
  3  3     1.00200619e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.18405726e+03 # Higgs mixing parameters
     1     8.20159176e+02    # mu(Q)MSSM DRbar
     2     9.63744630e+00    # tan beta(Q)MSSM DRbar
     3     2.43742890e+02    # higgs vev(Q)MSSM DRbar
     4     1.09377783e+06    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.18405726e+03  # MSSM DRbar SUSY breaking parameters
     1     2.86443454e+02      # M_1(Q)
     2     5.27790422e+02      # M_2(Q)
     3     1.47073582e+03      # M_3(Q)
    21     3.64915829e+05      # mH1^2(Q)
    22    -6.42942931e+05      # mH2^2(Q)
    31     6.31135510e+02      # meL(Q)
    32     6.31128394e+02      # mmuL(Q)
    33     6.28977275e+02      # mtauL(Q)
    34     5.12681164e+02      # meR(Q)
    35     5.12663468e+02      # mmuR(Q)
    36     5.07294355e+02      # mtauR(Q)
    41     1.40090583e+03      # mqL1(Q)
    42     1.40090201e+03      # mqL2(Q)
    43     1.28028794e+03      # mqL3(Q)
    44     1.35157189e+03      # muR(Q)
    45     1.35156780e+03      # mcR(Q)
    46     1.08876348e+03      # mtR(Q)
    47     1.34553948e+03      # mdR(Q)
    48     1.34553557e+03      # msR(Q)
    49     1.33835424e+03      # mbR(Q)
Block au Q= 1.18405726e+03  
  1  1    -1.49018086e+03      # Au(Q)MSSM DRbar
  2  2    -1.49017425e+03      # Ac(Q)MSSM DRbar
  3  3    -1.15487503e+03      # At(Q)MSSM DRbar
Block ad Q= 1.18405726e+03  
  1  1    -1.81701875e+03      # Ad(Q)MSSM DRbar
  2  2    -1.81701265e+03      # As(Q)MSSM DRbar
  3  3    -1.69933288e+03      # Ab(Q)MSSM DRbar
Block ae Q= 1.18405726e+03  
  1  1    -3.98531114e+02      # Ae(Q)MSSM DRbar
  2  2    -3.98524084e+02      # Amu(Q)MSSM DRbar
  3  3    -3.96401166e+02      # Atau(Q)MSSM DRbar
