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
     1    1.20000000e+05   # lambda
     2    1.00000000e+09   # M_mess
     5    1.00000000e+00   # N5
     6    1.00000000e+00   # cgrav
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=7.99223118e-05
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03995919e+01   # MW
        25     1.13648325e+02   # h0
        35     7.55830483e+02   # H0
        36     7.55717421e+02   # A0
        37     7.60222048e+02   # H+
   1000021     9.32918254e+02   # ~g
   1000022     1.60214181e+02   # ~neutralino(1)
   1000023     3.10279269e+02   # ~neutralino(2)
   1000024     3.10457607e+02   # ~chargino(1)
   1000025    -6.28409041e+02   # ~neutralino(3)
   1000035     6.37685105e+02   # ~neutralino(4)
   1000037     6.38275761e+02   # ~chargino(2)
   1000039     2.84400000e-05   # ~gravitino
   1000001     1.19298077e+03   # ~d_L
   1000002     1.19049777e+03   # ~u_L
   1000003     1.19297730e+03   # ~s_L
   1000004     1.19049430e+03   # ~c_L
   1000005     1.09042137e+03   # ~b_1
   1000006     9.33014784e+02   # ~t_1
   1000011     4.67115655e+02   # ~e_L
   1000012     4.60048099e+02   # ~nue_L
   1000013     4.67143238e+02   # ~mu_L
   1000014     4.60042404e+02   # ~numu_L
   1000015     2.48021872e+02   # ~stau_1
   1000016     4.58040837e+02   # ~nu_tau_L
   2000001     1.10934067e+03   # ~d_R
   2000002     1.11760151e+03   # ~u_R
   2000003     1.10933572e+03   # ~s_R
   2000004     1.11759900e+03   # ~c_R
   2000005     1.11166806e+03   # ~b_2
   2000006     1.12036170e+03   # ~t_2
   2000011     2.58432864e+02   # ~e_R
   2000013     2.58412404e+02   # ~mu_R
   2000015     4.67043200e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -7.12176727e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.96417045e-01   # N_{1,1}
  1  2    -1.53270439e-02   # N_{1,2}
  1  3     7.91812329e-02   # N_{1,3}
  1  4    -2.54654151e-02   # N_{1,4}
  2  1     3.05939550e-02   # N_{2,1}
  2  2     9.81525465e-01   # N_{2,2}
  2  3    -1.66069914e-01   # N_{2,3}
  2  4     8.99586293e-02   # N_{2,4}
  3  1    -3.69131168e-02   # N_{3,1}
  3  2     5.51827413e-02   # N_{3,2}
  3  3     7.02941599e-01   # N_{3,3}
  3  4     7.08142214e-01   # N_{3,4}
  4  1    -6.96742780e-02   # N_{4,1}
  4  2     1.82558780e-01   # N_{4,2}
  4  3     6.87040192e-01   # N_{4,3}
  4  4    -6.99852529e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.72000770e-01   # U_{1,1}
  1  2    -2.34977665e-01   # U_{1,2}
  2  1     2.34977665e-01   # U_{2,1}
  2  2     9.72000770e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.91728431e-01   # V_{1,1}
  1  2    -1.28353883e-01   # V_{1,2}
  2  1     1.28353883e-01   # V_{2,1}
  2  2     9.91728431e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     2.30326311e-01   # F_{11}
  1  2     9.73113452e-01   # F_{12}
  2  1     9.73113452e-01   # F_{21}
  2  2    -2.30326311e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     6.53985039e-01   # F_{11}
  1  2     7.56507481e-01   # F_{12}
  2  1     7.56507481e-01   # F_{21}
  2  2    -6.53985039e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.05626108e-01   # F_{11}
  1  2     9.94405916e-01   # F_{12}
  2  1     9.94405916e-01   # F_{21}
  2  2    -1.05626108e-01   # F_{22}
Block gauge Q= 9.98328803e+02  # SM gauge couplings
     1     3.62766270e-01   # g'(Q)MSSM DRbar
     2     6.43403030e-01   # g(Q)MSSM DRbar
     3     1.06114331e+00   # g3(Q)MSSM DRbar
Block yu Q= 9.98328803e+02  
  3  3     8.61411764e-01   # Yt(Q)MSSM DRbar
Block yd Q= 9.98328803e+02  
  3  3     1.99688735e-01   # Yb(Q)MSSM DRbar
Block ye Q= 9.98328803e+02  
  3  3     1.50921995e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 9.98328803e+02 # Higgs mixing parameters
     1     6.21293574e+02    # mu(Q)MSSM DRbar
     2     1.44999107e+01    # tan beta(Q)MSSM DRbar
     3     2.43889063e+02    # higgs vev(Q)MSSM DRbar
     4     6.02175588e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 9.98328803e+02  # MSSM DRbar SUSY breaking parameters
     1     1.63983396e+02      # M_1(Q)
     2     3.06651895e+02      # M_2(Q)
     3     8.44108704e+02      # M_3(Q)
    21     1.80507227e+05      # mH1^2(Q)
    22    -3.69089365e+05      # mH2^2(Q)
    31     4.62963013e+02      # meL(Q)
    32     4.62957343e+02      # mmuL(Q)
    33     4.61229706e+02      # mtauL(Q)
    34     2.50797180e+02      # meR(Q)
    35     2.50776090e+02      # mmuR(Q)
    36     2.44275948e+02      # mtauR(Q)
    41     1.16509049e+03      # mqL1(Q)
    42     1.16508694e+03      # mqL2(Q)
    43     1.07973993e+03      # mqL3(Q)
    44     1.09143623e+03      # muR(Q)
    45     1.09143364e+03      # mcR(Q)
    46     9.07008989e+02      # mtR(Q)
    47     1.08159054e+03      # mdR(Q)
    48     1.08158543e+03      # msR(Q)
    49     1.07202737e+03      # mbR(Q)
Block au Q= 9.98328803e+02  
  1  1    -5.61117732e+02      # Au(Q)MSSM DRbar
  2  2    -5.61115831e+02      # Ac(Q)MSSM DRbar
  3  3    -4.83606562e+02      # At(Q)MSSM DRbar
Block ad Q= 9.98328803e+02  
  1  1    -6.38609922e+02      # Ad(Q)MSSM DRbar
  2  2    -6.38607280e+02      # As(Q)MSSM DRbar
  3  3    -6.09415599e+02      # Ab(Q)MSSM DRbar
Block ae Q= 9.98328803e+02  
  1  1    -8.31171815e+01      # Ae(Q)MSSM DRbar
  2  2    -8.31155329e+01      # Amu(Q)MSSM DRbar
  3  3    -8.26140381e+01      # Atau(Q)MSSM DRbar
