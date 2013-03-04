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
     1     8.00000000e+02  # M_1(MX)
     2     2.50000000e+03  # M_2(MX)
     3     9.60000000e+02  # M_3(MX)
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
     41    9.60000000e+02  # mqL1(MX)
     42    9.60000000e+02  # mqL2(MX)
     43    2.50000000e+03  # mqL3(MX)
     44    9.60000000e+02  # muR(MX)
     45    9.60000000e+02  # mcR(MX)
     46    2.50000000e+03  # mtR(MX)
     47    9.60000000e+02  # mdR(MX)
     48    9.60000000e+02  # msR(MX)
     49    2.50000000e+03  # mbR(MX)
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=6.04158329e-04
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.04147266e+01   # MW
        25     1.16912957e+02   # h0
        35     2.50010092e+03   # H0
        36     2.49999379e+03   # A0
        37     2.50165432e+03   # H+
   1000021     1.08706583e+03   # ~g
   1000022     7.89595232e+02   # ~neutralino(1)
   1000023     2.43112746e+03   # ~neutralino(2)
   1000024     2.43222963e+03   # ~chargino(1)
   1000025    -2.50010289e+03   # ~neutralino(3)
   1000035     2.55116351e+03   # ~neutralino(4)
   1000037     2.55002869e+03   # ~chargino(2)
   1000001     1.05760357e+03   # ~d_L
   1000002     1.05491058e+03   # ~u_L
   1000003     1.05760357e+03   # ~s_L
   1000004     1.05491058e+03   # ~c_L
   1000005     2.52499490e+03   # ~b_1
   1000006     2.52776642e+03   # ~t_1
   1000011     2.51895182e+03   # ~e_L
   1000012     2.51742938e+03   # ~nue_L
   1000013     2.51895184e+03   # ~mu_L
   1000014     2.51742938e+03   # ~numu_L
   1000015     2.49953498e+03   # ~stau_1
   1000016     2.51720767e+03   # ~nu_tau_L
   2000001     1.02747154e+03   # ~d_R
   2000002     1.02547016e+03   # ~u_R
   2000003     1.02747154e+03   # ~s_R
   2000004     1.02547016e+03   # ~c_R
   2000005     2.55379985e+03   # ~b_2
   2000006     2.55635417e+03   # ~t_2
   2000011     2.50390654e+03   # ~e_R
   2000013     2.50390654e+03   # ~mu_R
   2000015     2.52269404e+03   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.04724085e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.99758529e-01   # N_{1,1}
  1  2    -4.62390689e-04   # N_{1,2}
  1  3     2.03432954e-02   # N_{1,3}
  1  4    -8.29581553e-03   # N_{1,4}
  2  1     1.26192281e-02   # N_{2,1}
  2  2     7.98775468e-01   # N_{2,2}
  2  3    -4.30848918e-01   # N_{2,3}
  2  4     4.19723381e-01   # N_{2,4}
  3  1    -8.51206693e-03   # N_{3,1}
  3  2     9.84977801e-03   # N_{3,2}
  3  3     7.06922309e-01   # N_{3,3}
  3  4     7.07171390e-01   # N_{3,4}
  4  1    -1.58487800e-02   # N_{4,1}
  4  2     6.01548435e-01   # N_{4,2}
  4  3     5.60549916e-01   # N_{4,3}
  4  4    -5.68921865e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     7.56858570e-01   # U_{1,1}
  1  2    -6.53578691e-01   # U_{1,2}
  2  1     6.53578691e-01   # U_{2,1}
  2  2     7.56858570e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     7.69286660e-01   # V_{1,1}
  1  2    -6.38903776e-01   # V_{1,2}
  2  1     6.38903776e-01   # V_{2,1}
  2  2     7.69286660e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.75454966e-01   # F_{11}
  1  2     9.26840638e-01   # F_{12}
  2  1     9.26840638e-01   # F_{21}
  2  2    -3.75454966e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     4.03315539e-01   # F_{11}
  1  2     9.15060969e-01   # F_{12}
  2  1     9.15060969e-01   # F_{21}
  2  2    -4.03315539e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     4.08091975e-01   # F_{11}
  1  2     9.12940820e-01   # F_{12}
  2  1     9.12940820e-01   # F_{21}
  2  2    -4.08091975e-01   # F_{22}
Block gauge Q= 2.50365397e+03  # SM gauge couplings
     1     3.64478595e-01   # g'(Q)MSSM DRbar
     2     6.36823140e-01   # g(Q)MSSM DRbar
     3     1.03567293e+00   # g3(Q)MSSM DRbar
Block yu Q= 2.50365397e+03  
  3  3     8.32204058e-01   # Yt(Q)MSSM DRbar
Block yd Q= 2.50365397e+03  
  3  3     1.27838735e-01   # Yb(Q)MSSM DRbar
Block ye Q= 2.50365397e+03  
  3  3     9.96610638e-02   # Ytau(Q)MSSM DRbar
Block hmix Q= 2.50365397e+03 # Higgs mixing parameters
     1     2.50000000e+03    # mu(Q)MSSM DRbar
     2     9.54706813e+00    # tan beta(Q)MSSM DRbar
     3     2.43747712e+02    # higgs vev(Q)MSSM DRbar
     4     6.16291484e+06    # mA^2(Q)MSSM DRbar
Block msoft Q= 2.50365397e+03  # MSSM DRbar SUSY breaking parameters
     1     8.00000000e+02      # M_1(Q)
     2     2.50000000e+03      # M_2(Q)
     3     9.60000000e+02      # M_3(Q)
    21    -1.69413689e+05      # mH1^2(Q)
    22    -6.07088939e+06      # mH2^2(Q)
    31     2.50000000e+03      # meL(Q)
    32     2.50000000e+03      # mmuL(Q)
    33     2.50000000e+03      # mtauL(Q)
    34     2.50000000e+03      # meR(Q)
    35     2.50000000e+03      # mmuR(Q)
    36     2.50000000e+03      # mtauR(Q)
    41     9.59999997e+02      # mqL1(Q)
    42     9.59999997e+02      # mqL2(Q)
    43     2.50000000e+03      # mqL3(Q)
    44     9.59999997e+02      # muR(Q)
    45     9.59999997e+02      # mcR(Q)
    46     2.50000000e+03      # mtR(Q)
    47     9.59999997e+02      # mdR(Q)
    48     9.59999997e+02      # msR(Q)
    49     2.50000000e+03      # mbR(Q)
Block au Q= 2.50365397e+03  
  1  1     3.16506052e-06      # Au(Q)MSSM DRbar
  2  2     3.16508426e-06      # Ac(Q)MSSM DRbar
  3  3     4.85578902e-06      # At(Q)MSSM DRbar
Block ad Q= 2.50365397e+03  
  1  1     1.56871342e-06      # Ad(Q)MSSM DRbar
  2  2     1.56873562e-06      # As(Q)MSSM DRbar
  3  3     2.07778947e-06      # Ab(Q)MSSM DRbar
Block ae Q= 2.50365397e+03  
  1  1     0.00000000e+00      # Ae(Q)MSSM DRbar
  2  2     4.87498981e-08      # Amu(Q)MSSM DRbar
  3  3     4.87168206e-08      # Atau(Q)MSSM DRbar
