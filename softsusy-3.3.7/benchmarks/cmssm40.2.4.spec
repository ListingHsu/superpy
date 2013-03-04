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
     3    4.00000000e+01   # tanb
     4    1.00000000e+00   # sign(mu)
     1    7.00000000e+02   # m0
     2    6.00000000e+02   # m12
     5   -5.00000000e+02   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    1.83492973e+16   # MX scale
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=5.66627752e-04
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.04510396e+01   # MW
        25     1.18042459e+02   # h0
        35     8.07404861e+02   # H0
        36     8.07397895e+02   # A0
        37     8.11714788e+02   # H+
   1000021     1.38443757e+03   # ~g
   1000022     2.51949243e+02   # ~neutralino(1)
   1000023     4.79898936e+02   # ~neutralino(2)
   1000024     4.80041540e+02   # ~chargino(1)
   1000025    -8.00383126e+02   # ~neutralino(3)
   1000035     8.08691290e+02   # ~neutralino(4)
   1000037     8.09296282e+02   # ~chargino(2)
   1000001     1.41603975e+03   # ~d_L
   1000002     1.41397465e+03   # ~u_L
   1000003     1.41599835e+03   # ~s_L
   1000004     1.41393318e+03   # ~c_L
   1000005     1.17745907e+03   # ~b_1
   1000006     1.00406642e+03   # ~t_1
   1000011     8.05692062e+02   # ~e_L
   1000012     8.01468094e+02   # ~nue_L
   1000013     8.05615490e+02   # ~mu_L
   1000014     8.01270236e+02   # ~numu_L
   1000015     5.63319118e+02   # ~stau_1
   1000016     7.33662356e+02   # ~nu_tau_L
   2000001     1.37095616e+03   # ~d_R
   2000002     1.37464419e+03   # ~u_R
   2000003     1.37087479e+03   # ~s_R
   2000004     1.37463888e+03   # ~c_R
   2000005     1.25386139e+03   # ~b_2
   2000006     1.23007696e+03   # ~t_2
   2000011     7.35512566e+02   # ~e_R
   2000013     7.35077346e+02   # ~mu_R
   2000015     7.48838755e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -2.59482893e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.97721983e-01   # N_{1,1}
  1  2    -7.90153358e-03   # N_{1,2}
  1  3     6.33750416e-02   # N_{1,3}
  1  4    -2.17259067e-02   # N_{1,4}
  2  1     1.94540704e-02   # N_{2,1}
  2  2     9.83847161e-01   # N_{2,2}
  2  3    -1.51729850e-01   # N_{2,3}
  2  4     9.29750261e-02   # N_{2,4}
  3  1    -2.90082094e-02   # N_{3,1}
  3  2     4.23521416e-02   # N_{3,2}
  3  3     7.04589800e-01   # N_{3,3}
  3  4     7.07755632e-01   # N_{3,4}
  4  1    -5.77140199e-02   # N_{4,1}
  4  2     1.73748743e-01   # N_{4,2}
  4  3     6.90300565e-01   # N_{4,3}
  4  4    -6.99975425e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.76680261e-01   # U_{1,1}
  1  2    -2.14699017e-01   # U_{1,2}
  2  1     2.14699017e-01   # U_{2,1}
  2  2     9.76680261e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.91112438e-01   # V_{1,1}
  1  2    -1.33026818e-01   # V_{1,2}
  2  1     1.33026818e-01   # V_{2,1}
  2  2     9.91112438e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.86664031e-01   # F_{11}
  1  2     9.22220650e-01   # F_{12}
  2  1     9.22220650e-01   # F_{21}
  2  2    -3.86664031e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.06316821e-01   # F_{11}
  1  2     4.22598887e-01   # F_{12}
  2  1    -4.22598887e-01   # F_{21}
  2  2     9.06316821e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     2.53583991e-01   # F_{11}
  1  2     9.67313372e-01   # F_{12}
  2  1     9.67313372e-01   # F_{21}
  2  2    -2.53583991e-01   # F_{22}
Block gauge Q= 1.07989985e+03  # SM gauge couplings
     1     3.62465854e-01   # g'(Q)MSSM DRbar
     2     6.41091635e-01   # g(Q)MSSM DRbar
     3     1.04982797e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.07989985e+03  
  3  3     8.49359779e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.07989985e+03  
  3  3     4.96037266e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.07989985e+03  
  3  3     4.23694205e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.07989985e+03 # Higgs mixing parameters
     1     7.95949752e+02    # mu(Q)MSSM DRbar
     2     3.91838368e+01    # tan beta(Q)MSSM DRbar
     3     2.43765931e+02    # higgs vev(Q)MSSM DRbar
     4     8.33186283e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.07989985e+03  # MSSM DRbar SUSY breaking parameters
     1     2.54866261e+02      # M_1(Q)
     2     4.70882260e+02      # M_2(Q)
     3     1.31978333e+03      # M_3(Q)
    21     3.00338320e+04      # mH1^2(Q)
    22    -6.19242598e+05      # mH2^2(Q)
    31     8.01537461e+02      # meL(Q)
    32     8.01339555e+02      # mmuL(Q)
    33     7.36140665e+02      # mtauL(Q)
    34     7.32531915e+02      # meR(Q)
    35     7.32095386e+02      # mmuR(Q)
    36     5.77369506e+02      # mtauR(Q)
    41     1.37567066e+03      # mqL1(Q)
    42     1.37562784e+03      # mqL2(Q)
    43     1.15994671e+03      # mqL3(Q)
    44     1.33677122e+03      # muR(Q)
    45     1.33676575e+03      # mcR(Q)
    46     9.99599617e+02      # mtR(Q)
    47     1.33211518e+03      # mdR(Q)
    48     1.33203122e+03      # msR(Q)
    49     1.20514996e+03      # mbR(Q)
Block au Q= 1.07989985e+03  
  1  1    -1.68089670e+03      # Au(Q)MSSM DRbar
  2  2    -1.68085682e+03      # Ac(Q)MSSM DRbar
  3  3    -1.17381531e+03      # At(Q)MSSM DRbar
Block ad Q= 1.07989985e+03  
  1  1    -1.94208138e+03      # Ad(Q)MSSM DRbar
  2  2    -1.94197985e+03      # As(Q)MSSM DRbar
  3  3    -1.63432814e+03      # Ab(Q)MSSM DRbar
Block ae Q= 1.07989985e+03  
  1  1    -6.62711590e+02      # Ae(Q)MSSM DRbar
  2  2    -6.62385457e+02      # Amu(Q)MSSM DRbar
  3  3    -5.55066102e+02      # Atau(Q)MSSM DRbar
