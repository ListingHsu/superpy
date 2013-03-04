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
     1    2.00000000e+02   # m0
     2    5.00000000e+02   # m12
     5    0.00000000e+00   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    1.90442075e+16   # MX scale
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=5.69565084e-05
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03960777e+01   # MW
        25     1.14918163e+02   # h0
        35     7.34349293e+02   # H0
        36     7.34060156e+02   # A0
        37     7.38734409e+02   # H+
   1000021     1.14926712e+03   # ~g
   1000022     2.04557933e+02   # ~neutralino(1)
   1000023     3.86568026e+02   # ~neutralino(2)
   1000024     3.86758378e+02   # ~chargino(1)
   1000025    -6.35562805e+02   # ~neutralino(3)
   1000035     6.49242442e+02   # ~neutralino(4)
   1000037     6.49158105e+02   # ~chargino(2)
   1000001     1.06658005e+03   # ~d_L
   1000002     1.06378652e+03   # ~u_L
   1000003     1.06657740e+03   # ~s_L
   1000004     1.06378387e+03   # ~c_L
   1000005     9.74266569e+02   # ~b_1
   1000006     8.10441456e+02   # ~t_1
   1000011     3.93657184e+02   # ~e_L
   1000012     3.85496189e+02   # ~nue_L
   1000013     3.93776585e+02   # ~mu_L
   1000014     3.85492252e+02   # ~numu_L
   1000015     2.70928394e+02   # ~stau_1
   1000016     3.84160572e+02   # ~nu_tau_L
   2000001     1.02262163e+03   # ~d_R
   2000002     1.02590540e+03   # ~u_R
   2000003     1.02261887e+03   # ~s_R
   2000004     1.02590257e+03   # ~c_R
   2000005     1.01902590e+03   # ~b_2
   2000006     1.01866843e+03   # ~t_2
   2000011     2.77580267e+02   # ~e_R
   2000013     2.77569155e+02   # ~mu_R
   2000015     3.94440383e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.06644095e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.95799110e-01   # N_{1,1}
  1  2    -1.74981319e-02   # N_{1,2}
  1  3     8.29958075e-02   # N_{1,3}
  1  4    -3.44912008e-02   # N_{1,4}
  2  1     3.81859499e-02   # N_{2,1}
  2  2     9.70343721e-01   # N_{2,2}
  2  3    -1.98482366e-01   # N_{2,3}
  2  4     1.32588259e-01   # N_{2,4}
  3  1    -3.32443947e-02   # N_{3,1}
  3  2     4.84107205e-02   # N_{3,2}
  3  3     7.03441896e-01   # N_{3,3}
  3  4     7.08322463e-01   # N_{3,4}
  4  1    -7.62940041e-02   # N_{4,1}
  4  2     2.36184843e-01   # N_{4,2}
  4  3     6.77411208e-01   # N_{4,3}
  4  4    -6.92466605e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.59474369e-01   # U_{1,1}
  1  2    -2.81795912e-01   # U_{1,2}
  2  1     2.81795912e-01   # U_{2,1}
  2  2     9.59474369e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.81896029e-01   # V_{1,1}
  1  2    -1.89420667e-01   # V_{1,2}
  2  1     1.89420667e-01   # V_{2,1}
  2  2     9.81896029e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     4.19842390e-01   # F_{11}
  1  2     9.07597029e-01   # F_{12}
  2  1     9.07597029e-01   # F_{21}
  2  2    -4.19842390e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.79294137e-01   # F_{11}
  1  2     2.02442567e-01   # F_{12}
  2  1    -2.02442567e-01   # F_{21}
  2  2     9.79294137e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.41712477e-01   # F_{11}
  1  2     9.89907861e-01   # F_{12}
  2  1     9.89907861e-01   # F_{21}
  2  2    -1.41712477e-01   # F_{22}
Block gauge Q= 8.80965363e+02  # SM gauge couplings
     1     3.62367704e-01   # g'(Q)MSSM DRbar
     2     6.42915794e-01   # g(Q)MSSM DRbar
     3     1.06063795e+00   # g3(Q)MSSM DRbar
Block yu Q= 8.80965363e+02  
  3  3     8.61080811e-01   # Yt(Q)MSSM DRbar
Block yd Q= 8.80965363e+02  
  3  3     1.35328846e-01   # Yb(Q)MSSM DRbar
Block ye Q= 8.80965363e+02  
  3  3     1.00503855e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 8.80965363e+02 # Higgs mixing parameters
     1     6.30008032e+02    # mu(Q)MSSM DRbar
     2     9.67255524e+00    # tan beta(Q)MSSM DRbar
     3     2.44102432e+02    # higgs vev(Q)MSSM DRbar
     4     5.58460374e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 8.80965363e+02  # MSSM DRbar SUSY breaking parameters
     1     2.09311712e+02      # M_1(Q)
     2     3.88520242e+02      # M_2(Q)
     3     1.11326687e+03      # M_3(Q)
    21     1.32422095e+05      # mH1^2(Q)
    22    -3.83920856e+05      # mH2^2(Q)
    31     3.86767734e+02      # meL(Q)
    32     3.86763799e+02      # mmuL(Q)
    33     3.85576703e+02      # mtauL(Q)
    34     2.71213702e+02      # meR(Q)
    35     2.71202320e+02      # mmuR(Q)
    36     2.67751674e+02      # mtauR(Q)
    41     1.02952011e+03      # mqL1(Q)
    42     1.02951741e+03      # mqL2(Q)
    43     9.46565547e+02      # mqL3(Q)
    44     9.92030971e+02      # muR(Q)
    45     9.92028094e+02      # mcR(Q)
    46     8.11742989e+02      # mtR(Q)
    47     9.87500727e+02      # mdR(Q)
    48     9.87497915e+02      # msR(Q)
    49     9.82351818e+02      # mbR(Q)
Block au Q= 8.80965363e+02  
  1  1    -1.14047430e+03      # Au(Q)MSSM DRbar
  2  2    -1.14046918e+03      # Ac(Q)MSSM DRbar
  3  3    -8.79886347e+02      # At(Q)MSSM DRbar
Block ad Q= 8.80965363e+02  
  1  1    -1.39539749e+03      # Ad(Q)MSSM DRbar
  2  2    -1.39539275e+03      # As(Q)MSSM DRbar
  3  3    -1.30390278e+03      # Ab(Q)MSSM DRbar
Block ae Q= 8.80965363e+02  
  1  1    -2.99351160e+02      # Ae(Q)MSSM DRbar
  2  2    -2.99345782e+02      # Amu(Q)MSSM DRbar
  3  3    -2.97724347e+02      # Atau(Q)MSSM DRbar
