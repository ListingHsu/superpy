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
     1    1.05000000e+03   # m0
     2    5.00000000e+02   # m12
     5    0.00000000e+00   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    2.04491798e+16   # MX scale
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=5.46991372e-04
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.04569637e+01   # MW
        25     1.15544124e+02   # h0
        35     1.24698235e+03   # H0
        36     1.24692985e+03   # A0
        37     1.24969660e+03   # H+
   1000021     1.19893753e+03   # ~g
   1000022     2.07766642e+02   # ~neutralino(1)
   1000023     3.93592666e+02   # ~neutralino(2)
   1000024     3.93762617e+02   # ~chargino(1)
   1000025    -6.31640163e+02   # ~neutralino(3)
   1000035     6.46526850e+02   # ~neutralino(4)
   1000037     6.46323448e+02   # ~chargino(2)
   1000001     1.46188308e+03   # ~d_L
   1000002     1.45992144e+03   # ~u_L
   1000003     1.46187802e+03   # ~s_L
   1000004     1.45991636e+03   # ~c_L
   1000005     1.26992741e+03   # ~b_1
   1000006     1.01661480e+03   # ~t_1
   1000011     1.09843179e+03   # ~e_L
   1000012     1.09529305e+03   # ~nue_L
   1000013     1.09847162e+03   # ~mu_L
   1000014     1.09527817e+03   # ~numu_L
   1000015     1.05579438e+03   # ~stau_1
   1000016     1.09071662e+03   # ~nu_tau_L
   2000001     1.43351286e+03   # ~d_R
   2000002     1.43549469e+03   # ~u_R
   2000003     1.43350794e+03   # ~s_R
   2000004     1.43548922e+03   # ~c_R
   2000005     1.42385307e+03   # ~b_2
   2000006     1.29126858e+03   # ~t_2
   2000011     1.06599503e+03   # ~e_R
   2000013     1.06596432e+03   # ~mu_R
   2000015     1.09459066e+03   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.04674232e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.95661608e-01   # N_{1,1}
  1  2    -1.74473371e-02   # N_{1,2}
  1  3     8.42260737e-02   # N_{1,3}
  1  4    -3.54897387e-02   # N_{1,4}
  2  1     3.93145880e-02   # N_{2,1}
  2  2     9.67856477e-01   # N_{2,2}
  2  3    -2.05374444e-01   # N_{2,3}
  2  4     1.39748133e-01   # N_{2,4}
  3  1    -3.34167628e-02   # N_{3,1}
  3  2     4.83673180e-02   # N_{3,2}
  3  3     7.03488067e-01   # N_{3,3}
  3  4     7.08271461e-01   # N_{3,4}
  4  1    -7.74315552e-02   # N_{4,1}
  4  2     2.46191049e-01   # N_{4,2}
  4  3     6.75153202e-01   # N_{4,3}
  4  4    -6.91058952e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.56253939e-01   # U_{1,1}
  1  2    -2.92537869e-01   # U_{1,2}
  2  1     2.92537869e-01   # U_{2,1}
  2  2     9.56253939e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.79715605e-01   # V_{1,1}
  1  2    -2.00392949e-01   # V_{1,2}
  2  1     2.00392949e-01   # V_{2,1}
  2  2     9.79715605e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     2.33457271e-01   # F_{11}
  1  2     9.72367062e-01   # F_{12}
  2  1     9.72367062e-01   # F_{21}
  2  2    -2.33457271e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.99109423e-01   # F_{11}
  1  2     4.21943240e-02   # F_{12}
  2  1    -4.21943240e-02   # F_{21}
  2  2     9.99109423e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.38291745e-01   # F_{11}
  1  2     9.90391535e-01   # F_{12}
  2  1     9.90391535e-01   # F_{21}
  2  2    -1.38291745e-01   # F_{22}
Block gauge Q= 1.11563617e+03  # SM gauge couplings
     1     3.62453406e-01   # g'(Q)MSSM DRbar
     2     6.41700130e-01   # g(Q)MSSM DRbar
     3     1.05155919e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.11563617e+03  
  3  3     8.57559526e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.11563617e+03  
  3  3     1.35254700e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.11563617e+03  
  3  3     9.95269908e-02   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.11563617e+03 # Higgs mixing parameters
     1     6.24019996e+02    # mu(Q)MSSM DRbar
     2     9.64101292e+00    # tan beta(Q)MSSM DRbar
     3     2.43628797e+02    # higgs vev(Q)MSSM DRbar
     4     1.58722298e+06    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.11563617e+03  # MSSM DRbar SUSY breaking parameters
     1     2.10804893e+02      # M_1(Q)
     2     3.89863994e+02      # M_2(Q)
     3     1.10019844e+03      # M_3(Q)
    21     1.14794148e+06      # mH1^2(Q)
    22    -3.53916941e+05      # mH2^2(Q)
    31     1.09540841e+03      # meL(Q)
    32     1.09539356e+03      # mmuL(Q)
    33     1.09097194e+03      # mtauL(Q)
    34     1.06371486e+03      # meR(Q)
    35     1.06368413e+03      # mmuR(Q)
    36     1.05451078e+03      # mtauR(Q)
    41     1.42919156e+03      # mqL1(Q)
    42     1.42918635e+03      # mqL2(Q)
    43     1.24144492e+03      # mqL3(Q)
    44     1.40568460e+03      # muR(Q)
    45     1.40567897e+03      # mcR(Q)
    46     9.92260484e+02      # mtR(Q)
    47     1.40293040e+03      # mdR(Q)
    48     1.40292534e+03      # msR(Q)
    49     1.39320824e+03      # mbR(Q)
Block au Q= 1.11563617e+03  
  1  1    -1.11892463e+03      # Au(Q)MSSM DRbar
  2  2    -1.11891965e+03      # Ac(Q)MSSM DRbar
  3  3    -8.63675247e+02      # At(Q)MSSM DRbar
Block ad Q= 1.11563617e+03  
  1  1    -1.36814943e+03      # Ad(Q)MSSM DRbar
  2  2    -1.36814483e+03      # As(Q)MSSM DRbar
  3  3    -1.27849290e+03      # Ab(Q)MSSM DRbar
Block ae Q= 1.11563617e+03  
  1  1    -2.97133508e+02      # Ae(Q)MSSM DRbar
  2  2    -2.97128221e+02      # Amu(Q)MSSM DRbar
  3  3    -2.95556784e+02      # Atau(Q)MSSM DRbar
