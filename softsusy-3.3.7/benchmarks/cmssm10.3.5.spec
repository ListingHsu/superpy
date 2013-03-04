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
     1    5.00000000e+02   # m0
     2    7.50000000e+02   # m12
     5    0.00000000e+00   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    1.71306936e+16   # MX scale
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=2.83575750e-04
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03926088e+01   # MW
        25     1.17527573e+02   # h0
        35     1.13477652e+03   # H0
        36     1.13455786e+03   # A0
        37     1.13767456e+03   # H+
   1000021     1.68018680e+03   # ~g
   1000022     3.14733715e+02   # ~neutralino(1)
   1000023     5.95354460e+02   # ~neutralino(2)
   1000024     5.95611204e+02   # ~chargino(1)
   1000025    -9.05522986e+02   # ~neutralino(3)
   1000035     9.16744744e+02   # ~neutralino(4)
   1000037     9.16593802e+02   # ~chargino(2)
   1000001     1.59620944e+03   # ~d_L
   1000002     1.59440901e+03   # ~u_L
   1000003     1.59620535e+03   # ~s_L
   1000004     1.59440491e+03   # ~c_L
   1000005     1.45210962e+03   # ~b_1
   1000006     1.21849038e+03   # ~t_1
   1000011     7.07447201e+02   # ~e_L
   1000012     7.02805671e+02   # ~nue_L
   1000013     7.07629814e+02   # ~mu_L
   1000014     7.02797863e+02   # ~numu_L
   1000015     5.66701494e+02   # ~stau_1
   1000016     7.00255811e+02   # ~nu_tau_L
   2000001     1.53219010e+03   # ~d_R
   2000002     1.53794177e+03   # ~u_R
   2000003     1.53218589e+03   # ~s_R
   2000004     1.53793734e+03   # ~c_R
   2000005     1.52485070e+03   # ~b_2
   2000006     1.48162953e+03   # ~t_2
   2000011     5.74251907e+02   # ~e_R
   2000013     5.74232543e+02   # ~mu_R
   2000015     7.06006131e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.05087166e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.97909100e-01   # N_{1,1}
  1  2    -8.60436551e-03   # N_{1,2}
  1  3     5.86553280e-02   # N_{1,3}
  1  4    -2.57477292e-02   # N_{1,4}
  2  1     2.05343328e-02   # N_{2,1}
  2  2     9.81171366e-01   # N_{2,2}
  2  3    -1.56661905e-01   # N_{2,3}
  2  4     1.11077177e-01   # N_{2,4}
  3  1    -2.29164641e-02   # N_{3,1}
  3  2     3.29880806e-02   # N_{3,2}
  3  3     7.05374244e-01   # N_{3,3}
  3  4     7.07696120e-01   # N_{3,4}
  4  1    -5.68384115e-02   # N_{4,1}
  4  2     1.90106554e-01   # N_{4,2}
  4  3     6.88813310e-01   # N_{4,3}
  4  4    -6.97255417e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.75102592e-01   # U_{1,1}
  1  2    -2.21754222e-01   # U_{1,2}
  2  1     2.21754222e-01   # U_{2,1}
  2  2     9.75102592e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.87418229e-01   # V_{1,1}
  1  2    -1.58130453e-01   # V_{1,2}
  2  1     1.58130453e-01   # V_{2,1}
  2  2     9.87418229e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.05641793e-01   # F_{11}
  1  2     9.52146572e-01   # F_{12}
  2  1     9.52146572e-01   # F_{21}
  2  2    -3.05641793e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.93316216e-01   # F_{11}
  1  2     1.15424846e-01   # F_{12}
  2  1    -1.15424846e-01   # F_{21}
  2  2     9.93316216e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     9.29455257e-02   # F_{11}
  1  2     9.95671195e-01   # F_{12}
  2  1     9.95671195e-01   # F_{21}
  2  2    -9.29455257e-02   # F_{22}
Block gauge Q= 1.30491921e+03  # SM gauge couplings
     1     3.63073612e-01   # g'(Q)MSSM DRbar
     2     6.40701405e-01   # g(Q)MSSM DRbar
     3     1.04051839e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.30491921e+03  
  3  3     8.48204256e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.30491921e+03  
  3  3     1.32796580e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.30491921e+03  
  3  3     1.00127852e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.30491921e+03 # Higgs mixing parameters
     1     8.99472330e+02    # mu(Q)MSSM DRbar
     2     9.62629804e+00    # tan beta(Q)MSSM DRbar
     3     2.43635210e+02    # higgs vev(Q)MSSM DRbar
     4     1.32845409e+06    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.30491921e+03  # MSSM DRbar SUSY breaking parameters
     1     3.19733615e+02      # M_1(Q)
     2     5.87648105e+02      # M_2(Q)
     3     1.62241687e+03      # M_3(Q)
    21     4.50343342e+05      # mH1^2(Q)
    22    -7.71703099e+05      # mH2^2(Q)
    31     7.00513061e+02      # meL(Q)
    32     7.00505205e+02      # mmuL(Q)
    33     6.98127812e+02      # mtauL(Q)
    34     5.69545982e+02      # meR(Q)
    35     5.69526463e+02      # mmuR(Q)
    36     5.63598116e+02      # mtauR(Q)
    41     1.54467542e+03      # mqL1(Q)
    42     1.54467124e+03      # mqL2(Q)
    43     1.41196918e+03      # mqL3(Q)
    44     1.48960751e+03      # muR(Q)
    45     1.48960300e+03      # mcR(Q)
    46     1.20031585e+03      # mtR(Q)
    47     1.48284011e+03      # mdR(Q)
    48     1.48283582e+03      # msR(Q)
    49     1.47496871e+03      # mbR(Q)
Block au Q= 1.30491921e+03  
  1  1    -1.63774591e+03      # Au(Q)MSSM DRbar
  2  2    -1.63773869e+03      # Ac(Q)MSSM DRbar
  3  3    -1.27125757e+03      # At(Q)MSSM DRbar
Block ad Q= 1.30491921e+03  
  1  1    -1.99454467e+03      # Ad(Q)MSSM DRbar
  2  2    -1.99453800e+03      # As(Q)MSSM DRbar
  3  3    -1.86593331e+03      # Ab(Q)MSSM DRbar
Block ae Q= 1.30491921e+03  
  1  1    -4.40698614e+02      # Ae(Q)MSSM DRbar
  2  2    -4.40690889e+02      # Amu(Q)MSSM DRbar
  3  3    -4.38355709e+02      # Atau(Q)MSSM DRbar
