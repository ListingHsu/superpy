# SOFTSUSY3.3.7 SLHA compliant output
# B.C. Allanach, Comput. Phys. Commun. 143 (2002) 305-331, hep-ph/0104145
Block SPINFO          # Program information
     1    SOFTSUSY    # spectrum calculator
     2    3.3.7       # version number
     3   # Warning: stau LSP
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
     1    3.90000000e+02   # m0
     2    7.00000000e+02   # m12
     5   -5.00000000e+02   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    1.67470597e+16   # MX scale
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=5.77897078e-04
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03878829e+01   # MW
        25     1.18671457e+02   # h0
        35     8.06871077e+02   # H0
        36     8.06789289e+02   # A0
        37     8.11061228e+02   # H+
   1000021     1.57094967e+03   # ~g
   1000022     2.94215885e+02   # ~neutralino(1)
   1000023     5.59327580e+02   # ~neutralino(2)
   1000024     5.59484268e+02   # ~chargino(1)
   1000025    -9.12551611e+02   # ~neutralino(3)
   1000035     9.20032105e+02   # ~neutralino(4)
   1000037     9.20552194e+02   # ~chargino(2)
   1000001     1.47781433e+03   # ~d_L
   1000002     1.47580966e+03   # ~u_L
   1000003     1.47777462e+03   # ~s_L
   1000004     1.47576988e+03   # ~c_L
   1000005     1.25303372e+03   # ~b_1
   1000006     1.08845888e+03   # ~t_1
   1000011     6.10378245e+02   # ~e_L
   1000012     6.04956283e+02   # ~nue_L
   1000013     6.10395696e+02   # ~mu_L
   1000014     6.04811508e+02   # ~numu_L
   1000015     2.93100842e+02   # ~stau_1
   1000016     5.54501442e+02   # ~nu_tau_L
   2000001     1.41691503e+03   # ~d_R
   2000002     1.42223517e+03   # ~u_R
   2000003     1.41683600e+03   # ~s_R
   2000004     1.42223013e+03   # ~c_R
   2000005     1.31882195e+03   # ~b_2
   2000006     1.31753521e+03   # ~t_2
   2000011     4.71620300e+02   # ~e_R
   2000013     4.71242865e+02   # ~mu_R
   2000015     5.78438918e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -2.59709527e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.98236669e-01   # N_{1,1}
  1  2    -6.14356360e-03   # N_{1,2}
  1  3     5.57102804e-02   # N_{1,3}
  1  4    -1.95492623e-02   # N_{1,4}
  2  1     1.53966269e-02   # N_{2,1}
  2  2     9.86734907e-01   # N_{2,2}
  2  3    -1.36971780e-01   # N_{2,3}
  2  4     8.57665413e-02   # N_{2,4}
  3  1    -2.52713085e-02   # N_{3,1}
  3  2     3.67775965e-02   # N_{3,2}
  3  3     7.05185577e-01   # N_{3,3}
  3  4     7.07617179e-01   # N_{3,4}
  4  1    -5.14573339e-02   # N_{4,1}
  4  2     1.57999649e-01   # N_{4,2}
  4  3     6.93432332e-01   # N_{4,3}
  4  4    -7.01099033e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.81099721e-01   # U_{1,1}
  1  2    -1.93502811e-01   # U_{1,2}
  2  1     1.93502811e-01   # U_{2,1}
  2  2     9.81099721e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.92477347e-01   # V_{1,1}
  1  2    -1.22428408e-01   # V_{1,2}
  2  1     1.22428408e-01   # V_{2,1}
  2  2     9.92477347e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     4.01230501e-01   # F_{11}
  1  2     9.15977120e-01   # F_{12}
  2  1     9.15977120e-01   # F_{21}
  2  2    -4.01230501e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     8.06052871e-01   # F_{11}
  1  2     5.91843535e-01   # F_{12}
  2  1    -5.91843535e-01   # F_{21}
  2  2     8.06052871e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     2.87596081e-01   # F_{11}
  1  2     9.57751791e-01   # F_{12}
  2  1     9.57751791e-01   # F_{21}
  2  2    -2.87596081e-01   # F_{22}
Block gauge Q= 1.16478203e+03  # SM gauge couplings
     1     3.62839455e-01   # g'(Q)MSSM DRbar
     2     6.40795196e-01   # g(Q)MSSM DRbar
     3     1.04507434e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.16478203e+03  
  3  3     8.45801469e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.16478203e+03  
  3  3     4.89466401e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.16478203e+03  
  3  3     4.27977253e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.16478203e+03 # Higgs mixing parameters
     1     9.09612250e+02    # mu(Q)MSSM DRbar
     2     3.91596088e+01    # tan beta(Q)MSSM DRbar
     3     2.43663008e+02    # higgs vev(Q)MSSM DRbar
     4     8.26579152e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.16478203e+03  # MSSM DRbar SUSY breaking parameters
     1     2.98754682e+02      # M_1(Q)
     2     5.50315513e+02      # M_2(Q)
     3     1.52737976e+03      # M_3(Q)
    21    -1.79452743e+05      # mH1^2(Q)
    22    -8.09987881e+05      # mH2^2(Q)
    31     6.03179874e+02      # meL(Q)
    32     6.03034179e+02      # mmuL(Q)
    33     5.56018528e+02      # mtauL(Q)
    34     4.66341047e+02      # meR(Q)
    35     4.65959267e+02      # mmuR(Q)
    36     3.26010432e+02      # mtauR(Q)
    41     1.43152521e+03      # mqL1(Q)
    42     1.43148474e+03      # mqL2(Q)
    43     1.24318064e+03      # mqL3(Q)
    44     1.37921689e+03      # muR(Q)
    45     1.37921177e+03      # mcR(Q)
    46     1.08720700e+03      # mtR(Q)
    47     1.37283920e+03      # mdR(Q)
    48     1.37275890e+03      # msR(Q)
    49     1.25719162e+03      # mbR(Q)
Block au Q= 1.16478203e+03  
  1  1    -1.88757424e+03      # Au(Q)MSSM DRbar
  2  2    -1.88753053e+03      # Ac(Q)MSSM DRbar
  3  3    -1.33467556e+03      # At(Q)MSSM DRbar
Block ad Q= 1.16478203e+03  
  1  1    -2.17631874e+03      # Ad(Q)MSSM DRbar
  2  2    -2.17620746e+03      # As(Q)MSSM DRbar
  3  3    -1.84324042e+03      # Ab(Q)MSSM DRbar
Block ae Q= 1.16478203e+03  
  1  1    -7.06491546e+02      # Ae(Q)MSSM DRbar
  2  2    -7.06152097e+02      # Amu(Q)MSSM DRbar
  3  3    -5.92036243e+02      # Atau(Q)MSSM DRbar
