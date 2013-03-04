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
     1    9.00000000e+04   # lambda
     2    1.00000000e+05   # M_mess
     5    1.00000000e+00   # N5
     6    1.00000000e+00   # cgrav
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=7.04154054e-04
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.04019759e+01   # MW
        25     1.12333395e+02   # h0
        35     4.62238735e+02   # H0
        36     4.61905125e+02   # A0
        37     4.69165123e+02   # H+
   1000021     8.64571817e+02   # ~g
   1000022     1.45061996e+02   # ~neutralino(1)
   1000023     2.65587016e+02   # ~neutralino(2)
   1000024     2.65155525e+02   # ~chargino(1)
   1000025    -3.68279933e+02   # ~neutralino(3)
   1000035     4.01185441e+02   # ~neutralino(4)
   1000037     4.00603219e+02   # ~chargino(2)
   1000039     2.13300000e-09   # ~gravitino
   1000001     1.03055650e+03   # ~d_L
   1000002     1.02767053e+03   # ~u_L
   1000003     1.03055509e+03   # ~s_L
   1000004     1.02766912e+03   # ~c_L
   1000005     9.76735134e+02   # ~b_1
   1000006     9.13287012e+02   # ~t_1
   1000011     3.17781927e+02   # ~e_L
   1000012     3.07431257e+02   # ~nue_L
   1000013     3.17807772e+02   # ~mu_L
   1000014     3.07429855e+02   # ~numu_L
   1000015     1.52911247e+02   # ~stau_1
   1000016     3.06809723e+02   # ~nu_tau_L
   2000001     9.85001491e+02   # ~d_R
   2000002     9.87536370e+02   # ~u_R
   2000003     9.84999535e+02   # ~s_R
   2000004     9.87535370e+02   # ~c_R
   2000005     9.93582282e+02   # ~b_2
   2000006     1.00616228e+03   # ~t_2
   2000011     1.58936459e+02   # ~e_R
   2000013     1.58930969e+02   # ~mu_R
   2000015     3.19061082e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -7.59172359e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.83920353e-01   # N_{1,1}
  1  2    -4.32756028e-02   # N_{1,2}
  1  3     1.57601575e-01   # N_{1,3}
  1  4    -7.20396036e-02   # N_{1,4}
  2  1     1.21871744e-01   # N_{2,1}
  2  2     8.64347978e-01   # N_{2,2}
  2  3    -3.88750587e-01   # N_{2,3}
  2  4     2.94826782e-01   # N_{2,4}
  3  1    -5.62187916e-02   # N_{3,1}
  3  2     7.93578974e-02   # N_{3,2}
  3  3     6.97354718e-01   # N_{3,3}
  3  4     7.10097295e-01   # N_{3,4}
  4  1    -1.17845086e-01   # N_{4,1}
  4  2     4.94704072e-01   # N_{4,2}
  4  3     5.81146385e-01   # N_{4,3}
  4  4    -6.35334003e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     8.25120752e-01   # U_{1,1}
  1  2    -5.64956410e-01   # U_{1,2}
  2  1     5.64956410e-01   # U_{2,1}
  2  2     8.25120752e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.02601487e-01   # V_{1,1}
  1  2    -4.30477125e-01   # V_{1,2}
  2  1     4.30477125e-01   # V_{2,1}
  2  2     9.02601487e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     2.77254458e-01   # F_{11}
  1  2     9.60796527e-01   # F_{12}
  2  1     9.60796527e-01   # F_{21}
  2  2    -2.77254458e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     4.75782518e-01   # F_{11}
  1  2     8.79562957e-01   # F_{12}
  2  1     8.79562957e-01   # F_{21}
  2  2    -4.75782518e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.22936863e-01   # F_{11}
  1  2     9.92414494e-01   # F_{12}
  2  1     9.92414494e-01   # F_{21}
  2  2    -1.22936863e-01   # F_{22}
Block gauge Q= 9.37890932e+02  # SM gauge couplings
     1     3.62940310e-01   # g'(Q)MSSM DRbar
     2     6.44933056e-01   # g(Q)MSSM DRbar
     3     1.06542074e+00   # g3(Q)MSSM DRbar
Block yu Q= 9.37890932e+02  
  3  3     8.66444268e-01   # Yt(Q)MSSM DRbar
Block yd Q= 9.37890932e+02  
  3  3     2.04723041e-01   # Yb(Q)MSSM DRbar
Block ye Q= 9.37890932e+02  
  3  3     1.51457247e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 9.37890932e+02 # Higgs mixing parameters
     1     3.59466667e+02    # mu(Q)MSSM DRbar
     2     1.45087504e+01    # tan beta(Q)MSSM DRbar
     3     2.43643842e+02    # higgs vev(Q)MSSM DRbar
     4     2.36664299e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 9.37890932e+02  # MSSM DRbar SUSY breaking parameters
     1     1.51689372e+02      # M_1(Q)
     2     2.86309955e+02      # M_2(Q)
     3     7.85300394e+02      # M_3(Q)
    21     8.47388832e+04      # mH1^2(Q)
    22    -1.13708321e+05      # mH2^2(Q)
    31     3.11340415e+02      # meL(Q)
    32     3.11339027e+02      # mmuL(Q)
    33     3.10914970e+02      # mtauL(Q)
    34     1.48353636e+02      # meR(Q)
    35     1.48347749e+02      # mmuR(Q)
    36     1.46539938e+02      # mtauR(Q)
    41     1.00167384e+03      # mqL1(Q)
    42     1.00167239e+03      # mqL2(Q)
    43     9.66800863e+02      # mqL3(Q)
    44     9.60963980e+02      # muR(Q)
    45     9.60962944e+02      # mcR(Q)
    46     8.89687334e+02      # mtR(Q)
    47     9.57082614e+02      # mdR(Q)
    48     9.57080584e+02      # msR(Q)
    49     9.53122413e+02      # mbR(Q)
Block au Q= 9.37890932e+02  
  1  1    -2.41593596e+02      # Au(Q)MSSM DRbar
  2  2    -2.41593251e+02      # Ac(Q)MSSM DRbar
  3  3    -2.27468749e+02      # At(Q)MSSM DRbar
Block ad Q= 9.37890932e+02  
  1  1    -2.57312939e+02      # Ad(Q)MSSM DRbar
  2  2    -2.57312457e+02      # As(Q)MSSM DRbar
  3  3    -2.51992311e+02      # Ab(Q)MSSM DRbar
Block ae Q= 9.37890932e+02  
  1  1    -2.43963498e+01      # Ae(Q)MSSM DRbar
  2  2    -2.43961693e+01      # Amu(Q)MSSM DRbar
  3  3    -2.43410690e+01      # Atau(Q)MSSM DRbar
