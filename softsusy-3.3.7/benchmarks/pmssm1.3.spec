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
     1     5.00000000e+02  # M_1(MX)
     2     2.50000000e+03  # M_2(MX)
     3     6.00000000e+02  # M_3(MX)
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
     41    6.00000000e+02  # mqL1(MX)
     42    6.00000000e+02  # mqL2(MX)
     43    2.50000000e+03  # mqL3(MX)
     44    6.00000000e+02  # muR(MX)
     45    6.00000000e+02  # mcR(MX)
     46    2.50000000e+03  # mtR(MX)
     47    6.00000000e+02  # mdR(MX)
     48    6.00000000e+02  # msR(MX)
     49    2.50000000e+03  # mbR(MX)
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=7.45950594e-04
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.04024217e+01   # MW
        25     1.16452209e+02   # h0
        35     2.50009919e+03   # H0
        36     2.49999189e+03   # A0
        37     2.50164566e+03   # H+
   1000021     7.00895052e+02   # ~g
   1000022     4.91904111e+02   # ~neutralino(1)
   1000023     2.43297598e+03   # ~neutralino(2)
   1000024     2.43412332e+03   # ~chargino(1)
   1000025    -2.50030289e+03   # ~neutralino(3)
   1000035     2.55283165e+03   # ~neutralino(4)
   1000037     2.55176860e+03   # ~chargino(2)
   1000001     6.95224456e+02   # ~d_L
   1000002     6.91074918e+02   # ~u_L
   1000003     6.95224456e+02   # ~s_L
   1000004     6.91074918e+02   # ~c_L
   1000005     2.51998575e+03   # ~b_1
   1000006     2.52347480e+03   # ~t_1
   1000011     2.51889832e+03   # ~e_L
   1000012     2.51738082e+03   # ~nue_L
   1000013     2.51889834e+03   # ~mu_L
   1000014     2.51738082e+03   # ~numu_L
   1000015     2.49924714e+03   # ~stau_1
   1000016     2.51715896e+03   # ~nu_tau_L
   2000001     6.53816885e+02   # ~d_R
   2000002     6.49481720e+02   # ~u_R
   2000003     6.53816885e+02   # ~s_R
   2000004     6.49481720e+02   # ~c_R
   2000005     2.54917141e+03   # ~b_2
   2000006     2.55091311e+03   # ~t_2
   2000011     2.50357995e+03   # ~e_R
   2000013     2.50357995e+03   # ~mu_R
   2000015     2.52260094e+03   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.04703262e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.99807934e-01   # N_{1,1}
  1  2    -2.75418514e-04   # N_{1,2}
  1  3     1.87905460e-02   # N_{1,3}
  1  4    -5.56187327e-03   # N_{1,4}
  2  1     9.68897911e-03   # N_{2,1}
  2  2     8.38566042e-01   # N_{2,2}
  2  3    -3.90977502e-01   # N_{2,3}
  2  4     3.79275241e-01   # N_{2,4}
  3  1    -9.34917400e-03   # N_{3,1}
  3  2     9.85687591e-03   # N_{3,2}
  3  3     7.06913079e-01   # N_{3,3}
  3  4     7.07169947e-01   # N_{3,4}
  4  1    -1.42411916e-02   # N_{4,1}
  4  2     5.44710711e-01   # N_{4,2}
  4  3     5.89115784e-01   # N_{4,3}
  4  4    -5.96682514e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     7.47898161e-01   # U_{1,1}
  1  2    -6.63813483e-01   # U_{1,2}
  2  1     6.63813483e-01   # U_{2,1}
  2  2     7.47898161e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     7.60538295e-01   # V_{1,1}
  1  2    -6.49293079e-01   # V_{1,2}
  2  1     6.49293079e-01   # V_{2,1}
  2  2     7.60538295e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.44444345e-01   # F_{11}
  1  2     9.38806739e-01   # F_{12}
  2  1     9.38806739e-01   # F_{21}
  2  2    -3.44444345e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     4.03733277e-01   # F_{11}
  1  2     9.14876735e-01   # F_{12}
  2  1     9.14876735e-01   # F_{21}
  2  2    -4.03733277e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     4.04153789e-01   # F_{11}
  1  2     9.14691049e-01   # F_{12}
  2  1     9.14691049e-01   # F_{21}
  2  2    -4.04153789e-01   # F_{22}
Block gauge Q= 2.50362383e+03  # SM gauge couplings
     1     3.64676454e-01   # g'(Q)MSSM DRbar
     2     6.37373479e-01   # g(Q)MSSM DRbar
     3     1.04644767e+00   # g3(Q)MSSM DRbar
Block yu Q= 2.50362383e+03  
  3  3     8.29014545e-01   # Yt(Q)MSSM DRbar
Block yd Q= 2.50362383e+03  
  3  3     1.29271096e-01   # Yb(Q)MSSM DRbar
Block ye Q= 2.50362383e+03  
  3  3     9.96980026e-02   # Ytau(Q)MSSM DRbar
Block hmix Q= 2.50362383e+03 # Higgs mixing parameters
     1     2.50000000e+03    # mu(Q)MSSM DRbar
     2     9.54895580e+00    # tan beta(Q)MSSM DRbar
     3     2.43794148e+02    # higgs vev(Q)MSSM DRbar
     4     6.16511775e+06    # mA^2(Q)MSSM DRbar
Block msoft Q= 2.50362383e+03  # MSSM DRbar SUSY breaking parameters
     1     5.00000000e+02      # M_1(Q)
     2     2.50000000e+03      # M_2(Q)
     3     6.00000000e+02      # M_3(Q)
    21    -1.69052581e+05      # mH1^2(Q)
    22    -6.07254317e+06      # mH2^2(Q)
    31     2.50000000e+03      # meL(Q)
    32     2.50000000e+03      # mmuL(Q)
    33     2.50000000e+03      # mtauL(Q)
    34     2.50000000e+03      # meR(Q)
    35     2.50000000e+03      # mmuR(Q)
    36     2.50000000e+03      # mtauR(Q)
    41     5.99999998e+02      # mqL1(Q)
    42     5.99999998e+02      # mqL2(Q)
    43     2.50000000e+03      # mqL3(Q)
    44     5.99999998e+02      # muR(Q)
    45     5.99999998e+02      # mcR(Q)
    46     2.50000000e+03      # mtR(Q)
    47     5.99999998e+02      # mdR(Q)
    48     5.99999998e+02      # msR(Q)
    49     2.50000000e+03      # mbR(Q)
Block au Q= 2.50362383e+03  
  1  1     2.33895515e-06      # Au(Q)MSSM DRbar
  2  2     2.33896508e-06      # Ac(Q)MSSM DRbar
  3  3     3.33666351e-06      # At(Q)MSSM DRbar
Block ad Q= 2.50362383e+03  
  1  1     1.45035873e-06      # Ad(Q)MSSM DRbar
  2  2     1.45036558e-06      # As(Q)MSSM DRbar
  3  3     1.71465765e-06      # Ab(Q)MSSM DRbar
Block ae Q= 2.50362383e+03  
  1  1     0.00000000e+00      # Ae(Q)MSSM DRbar
  2  2     2.68655335e-08      # Amu(Q)MSSM DRbar
  3  3     2.67648189e-08      # Atau(Q)MSSM DRbar
