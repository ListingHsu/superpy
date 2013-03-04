# SOFTSUSY3.3.7 SLHA compliant output
# B.C. Allanach, Comput. Phys. Commun. 143 (2002) 305-331, hep-ph/0104145
Block SPINFO          # Program information
     1    SOFTSUSY    # spectrum calculator
     2    3.3.7       # version number
Block MODSEL  # Select model
     1    0   # nonUniversal
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
Block EXTPAR               # non-universal SUSY breaking parameters
     0    -1.00000000e+00  # Set MX=MSUSY
     1     7.00000000e+02  # M_1(MX)
     2     2.50000000e+03  # M_2(MX)
     3     8.40000000e+02  # M_3(MX)
     11    0.00000000e+00  # At(MX)
     12    0.00000000e+00  # Ab(MX)
     13    0.00000000e+00  # Atau(MX)
     23    2.50000000e+03  # mu(MX)
     26    2.50000000e+03  # mA(pole)
     31    2.50000000e+03  # meL(MX)
     32    2.50000000e+03  # mmuL(MX)
     33    2.50000000e+03  # mtauL(MX)
     34    2.50000000e+03  # meR(MX)
     35    2.50000000e+03  # mmuR(MX)
     36    2.50000000e+03  # mtauR(MX)
     41    8.40000000e+02  # mqL1(MX)
     42    8.40000000e+02  # mqL2(MX)
     43    2.50000000e+03  # mqL3(MX)
     44    8.40000000e+02  # muR(MX)
     45    8.40000000e+02  # mcR(MX)
     46    2.50000000e+03  # mtR(MX)
     47    8.40000000e+02  # mdR(MX)
     48    8.40000000e+02  # msR(MX)
     49    2.50000000e+03  # mbR(MX)
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=1.69817371e-04
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.04625197e+01   # MW
        25     1.16788556e+02   # h0
        35     2.50009687e+03   # H0
        36     2.49998971e+03   # A0
        37     2.50164792e+03   # H+
   1000021     9.59646133e+02   # ~g
   1000022     6.90289321e+02   # ~neutralino(1)
   1000023     2.43158887e+03   # ~neutralino(2)
   1000024     2.43270794e+03   # ~chargino(1)
   1000025    -2.50015774e+03   # ~neutralino(3)
   1000035     2.55158879e+03   # ~neutralino(4)
   1000037     2.55047926e+03   # ~chargino(2)
   1000001     9.36297492e+02   # ~d_L
   1000002     9.33243377e+02   # ~u_L
   1000003     9.36297492e+02   # ~s_L
   1000004     9.33243377e+02   # ~c_L
   1000005     2.52295191e+03   # ~b_1
   1000006     2.52596706e+03   # ~t_1
   1000011     2.51892348e+03   # ~e_L
   1000012     2.51740325e+03   # ~nue_L
   1000013     2.51892351e+03   # ~mu_L
   1000014     2.51740325e+03   # ~numu_L
   1000015     2.49941934e+03   # ~stau_1
   1000016     2.51718148e+03   # ~nu_tau_L
   2000001     9.03506503e+02   # ~d_R
   2000002     9.00925523e+02   # ~u_R
   2000003     9.03506503e+02   # ~s_R
   2000004     9.00925523e+02   # ~c_R
   2000005     2.55187931e+03   # ~b_2
   2000006     2.55415508e+03   # ~t_2
   2000011     2.50377602e+03   # ~e_R
   2000013     2.50377602e+03   # ~mu_R
   2000015     2.52265044e+03   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.04719598e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.99778383e-01   # N_{1,1}
  1  2    -3.91071977e-04   # N_{1,2}
  1  3     1.97352859e-02   # N_{1,3}
  1  4    -7.31787483e-03   # N_{1,4}
  2  1     1.15797881e-02   # N_{2,1}
  2  2     8.10942322e-01   # N_{2,2}
  2  3    -4.19277712e-01   # N_{2,3}
  2  4     4.07976297e-01   # N_{2,4}
  3  1    -8.77436178e-03   # N_{3,1}
  3  2     9.85050225e-03   # N_{3,2}
  3  3     7.06919490e-01   # N_{3,3}
  3  4     7.07170992e-01   # N_{3,4}
  4  1    -1.52349868e-02   # N_{4,1}
  4  2     5.85043045e-01   # N_{4,2}
  4  3     5.69281611e-01   # N_{4,3}
  4  4    -5.77417507e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     7.54673459e-01   # U_{1,1}
  1  2    -6.56100579e-01   # U_{1,2}
  2  1     6.56100579e-01   # U_{2,1}
  2  2     7.54673459e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     7.67152877e-01   # V_{1,1}
  1  2    -6.41464311e-01   # V_{1,2}
  2  1     6.41464311e-01   # V_{2,1}
  2  2     7.67152877e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.65161616e-01   # F_{11}
  1  2     9.30944141e-01   # F_{12}
  2  1     9.30944141e-01   # F_{21}
  2  2    -3.65161616e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     4.03430466e-01   # F_{11}
  1  2     9.15010306e-01   # F_{12}
  2  1     9.15010306e-01   # F_{21}
  2  2    -4.03430466e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     4.06599444e-01   # F_{11}
  1  2     9.13606530e-01   # F_{12}
  2  1     9.13606530e-01   # F_{21}
  2  2    -4.06599444e-01   # F_{22}
Block gauge Q= 2.50364659e+03  # SM gauge couplings
     1     3.64547432e-01   # g'(Q)MSSM DRbar
     2     6.36924083e-01   # g(Q)MSSM DRbar
     3     1.03873368e+00   # g3(Q)MSSM DRbar
Block yu Q= 2.50364659e+03  
  3  3     8.31433344e-01   # Yt(Q)MSSM DRbar
Block yd Q= 2.50364659e+03  
  3  3     1.28257248e-01   # Yb(Q)MSSM DRbar
Block ye Q= 2.50364659e+03  
  3  3     9.96739438e-02   # Ytau(Q)MSSM DRbar
Block hmix Q= 2.50364659e+03 # Higgs mixing parameters
     1     2.50000000e+03    # mu(Q)MSSM DRbar
     2     9.54747534e+00    # tan beta(Q)MSSM DRbar
     3     2.43755428e+02    # higgs vev(Q)MSSM DRbar
     4     6.16359563e+06    # mA^2(Q)MSSM DRbar
Block msoft Q= 2.50364659e+03  # MSSM DRbar SUSY breaking parameters
     1     7.00000000e+02      # M_1(Q)
     2     2.50000000e+03      # M_2(Q)
     3     8.40000000e+02      # M_3(Q)
    21    -1.69279452e+05      # mH1^2(Q)
    22    -6.07133814e+06      # mH2^2(Q)
    31     2.50000000e+03      # meL(Q)
    32     2.50000000e+03      # mmuL(Q)
    33     2.50000000e+03      # mtauL(Q)
    34     2.50000000e+03      # meR(Q)
    35     2.50000000e+03      # mmuR(Q)
    36     2.50000000e+03      # mtauR(Q)
    41     8.39999998e+02      # mqL1(Q)
    42     8.39999998e+02      # mqL2(Q)
    43     2.50000000e+03      # mqL3(Q)
    44     8.39999998e+02      # muR(Q)
    45     8.39999998e+02      # mcR(Q)
    46     2.50000000e+03      # mtR(Q)
    47     8.39999998e+02      # mdR(Q)
    48     8.39999998e+02      # msR(Q)
    49     2.50000000e+03      # mbR(Q)
Block au Q= 2.50364659e+03  
  1  1     2.89757158e-06      # Au(Q)MSSM DRbar
  2  2     2.89759092e-06      # Ac(Q)MSSM DRbar
  3  3     4.36764905e-06      # At(Q)MSSM DRbar
Block ad Q= 2.50364659e+03  
  1  1     1.52571759e-06      # Ad(Q)MSSM DRbar
  2  2     1.52573498e-06      # As(Q)MSSM DRbar
  3  3     1.95760484e-06      # Ab(Q)MSSM DRbar
Block ae Q= 2.50364659e+03  
  1  1     0.00000000e+00      # Ae(Q)MSSM DRbar
  2  2     4.19000342e-08      # Amu(Q)MSSM DRbar
  3  3     4.18460998e-08      # Atau(Q)MSSM DRbar
