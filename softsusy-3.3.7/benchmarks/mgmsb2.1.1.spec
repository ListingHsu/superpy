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
     1    7.20000000e+04   # lambda
     2    8.00000000e+04   # M_mess
     5    1.00000000e+00   # N5
     6    1.00000000e+00   # cgrav
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=1.16829274e-04
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.04112038e+01   # MW
        25     1.10612250e+02   # h0
        35     3.73635036e+02   # H0
        36     3.73218805e+02   # A0
        37     3.82168569e+02   # H+
   1000021     7.07369877e+02   # ~g
   1000022     1.14265310e+02   # ~neutralino(1)
   1000023     2.06540637e+02   # ~neutralino(2)
   1000024     2.05681345e+02   # ~chargino(1)
   1000025    -3.04618659e+02   # ~neutralino(3)
   1000035     3.38714961e+02   # ~neutralino(4)
   1000037     3.38313900e+02   # ~chargino(2)
   1000039     1.36512000e-09   # ~gravitino
   1000001     8.40571024e+02   # ~d_L
   1000002     8.36984877e+02   # ~u_L
   1000003     8.40569873e+02   # ~s_L
   1000004     8.36983721e+02   # ~c_L
   1000005     7.95939321e+02   # ~b_1
   1000006     7.47814119e+02   # ~t_1
   1000011     2.56407176e+02   # ~e_L
   1000012     2.43498000e+02   # ~nue_L
   1000013     2.56452488e+02   # ~mu_L
   1000014     2.43496864e+02   # ~numu_L
   1000015     1.22809744e+02   # ~stau_1
   1000016     2.42995657e+02   # ~nu_tau_L
   2000001     8.04159414e+02   # ~d_R
   2000002     8.05699276e+02   # ~u_R
   2000003     8.04157812e+02   # ~s_R
   2000004     8.05698461e+02   # ~c_R
   2000005     8.11584408e+02   # ~b_2
   2000006     8.27439195e+02   # ~t_2
   2000011     1.29436852e+02   # ~e_R
   2000013     1.29432524e+02   # ~mu_R
   2000015     2.58336359e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -7.96324025e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.75215330e-01   # N_{1,1}
  1  2    -6.35499282e-02   # N_{1,2}
  1  3     1.93876766e-01   # N_{1,3}
  1  4    -8.56052945e-02   # N_{1,4}
  2  1     1.61792211e-01   # N_{2,1}
  2  2     8.50465775e-01   # N_{2,2}
  2  3    -4.05487295e-01   # N_{2,3}
  2  4     2.93447270e-01   # N_{2,4}
  3  1    -6.88338633e-02   # N_{3,1}
  3  2     9.77375508e-02   # N_{3,2}
  3  3     6.92437926e-01   # N_{3,3}
  3  4     7.11504736e-01   # N_{3,4}
  4  1    -1.34313960e-01   # N_{4,1}
  4  2     5.12949065e-01   # N_{4,2}
  4  3     5.64377155e-01   # N_{4,3}
  4  4    -6.32709605e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     8.01915278e-01   # U_{1,1}
  1  2    -5.97437769e-01   # U_{1,2}
  2  1     5.97437769e-01   # U_{2,1}
  2  2     8.01915278e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.00782493e-01   # V_{1,1}
  1  2    -4.34270537e-01   # V_{1,2}
  2  1     4.34270537e-01   # V_{2,1}
  2  2     9.00782493e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.27995810e-01   # F_{11}
  1  2     9.44679178e-01   # F_{12}
  2  1     9.44679178e-01   # F_{21}
  2  2    -3.27995810e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     5.41216298e-01   # F_{11}
  1  2     8.40883416e-01   # F_{12}
  2  1     8.40883416e-01   # F_{21}
  2  2    -5.41216298e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.54146853e-01   # F_{11}
  1  2     9.88047948e-01   # F_{12}
  2  1     9.88047948e-01   # F_{21}
  2  2    -1.54146853e-01   # F_{22}
Block gauge Q= 7.68693764e+02  # SM gauge couplings
     1     3.62512224e-01   # g'(Q)MSSM DRbar
     2     6.46107285e-01   # g(Q)MSSM DRbar
     3     1.07638113e+00   # g3(Q)MSSM DRbar
Block yu Q= 7.68693764e+02  
  3  3     8.73707032e-01   # Yt(Q)MSSM DRbar
Block yd Q= 7.68693764e+02  
  3  3     2.06921218e-01   # Yb(Q)MSSM DRbar
Block ye Q= 7.68693764e+02  
  3  3     1.51625159e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 7.68693764e+02 # Higgs mixing parameters
     1     2.95114950e+02    # mu(Q)MSSM DRbar
     2     1.45437300e+01    # tan beta(Q)MSSM DRbar
     3     2.43902587e+02    # higgs vev(Q)MSSM DRbar
     4     1.54862060e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 7.68693764e+02  # MSSM DRbar SUSY breaking parameters
     1     1.21037431e+02      # M_1(Q)
     2     2.29808727e+02      # M_2(Q)
     3     6.41114032e+02      # M_3(Q)
    21     5.42287749e+04      # mH1^2(Q)
    22    -7.85626841e+04      # mH2^2(Q)
    31     2.49846914e+02      # meL(Q)
    32     2.49845802e+02      # mmuL(Q)
    33     2.49507368e+02      # mtauL(Q)
    34     1.18261005e+02      # meR(Q)
    35     1.18256261e+02      # mmuR(Q)
    36     1.16803628e+02      # mtauR(Q)
    41     8.15912977e+02      # mqL1(Q)
    42     8.15911784e+02      # mqL2(Q)
    43     7.87292147e+02      # mqL3(Q)
    44     7.83708463e+02      # muR(Q)
    45     7.83707617e+02      # mcR(Q)
    46     7.25286532e+02      # mtR(Q)
    47     7.80682968e+02      # mdR(Q)
    48     7.80681302e+02      # msR(Q)
    49     7.77420871e+02      # mbR(Q)
Block au Q= 7.68693764e+02  
  1  1    -1.99092972e+02      # Au(Q)MSSM DRbar
  2  2    -1.99092686e+02      # Ac(Q)MSSM DRbar
  3  3    -1.87348527e+02      # At(Q)MSSM DRbar
Block ad Q= 7.68693764e+02  
  1  1    -2.12230081e+02      # Ad(Q)MSSM DRbar
  2  2    -2.12229681e+02      # As(Q)MSSM DRbar
  3  3    -2.07802469e+02      # Ab(Q)MSSM DRbar
Block ae Q= 7.68693764e+02  
  1  1    -1.94809064e+01      # Ae(Q)MSSM DRbar
  2  2    -1.94807620e+01      # Amu(Q)MSSM DRbar
  3  3    -1.94368326e+01      # Atau(Q)MSSM DRbar
