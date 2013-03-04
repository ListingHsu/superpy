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
     1    3.50000000e+04   # lambda
     2    7.00000000e+04   # M_mess
     5    3.00000000e+00   # N5
     6    1.00000000e+00   # cgrav
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=1.64904481e-04
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.04741069e+01   # MW
        25     1.10108956e+02   # h0
        35     3.39343579e+02   # H0
        36     3.38941001e+02   # A0
        37     3.48641000e+02   # H+
   1000021     8.39053170e+02   # ~g
   1000022     1.40801871e+02   # ~neutralino(1)
   1000023     2.32119374e+02   # ~neutralino(2)
   1000024     2.28779331e+02   # ~chargino(1)
   1000025    -2.81453223e+02   # ~neutralino(3)
   1000035     3.48492773e+02   # ~neutralino(4)
   1000037     3.47543897e+02   # ~chargino(2)
   1000039     5.80650000e-10   # ~gravitino
   1000001     7.99279972e+02   # ~d_L
   1000002     7.95440670e+02   # ~u_L
   1000003     7.99278964e+02   # ~s_L
   1000004     7.95439656e+02   # ~c_L
   1000005     7.59913575e+02   # ~b_1
   1000006     7.14433078e+02   # ~t_1
   1000011     2.31242055e+02   # ~e_L
   1000012     2.16864754e+02   # ~nue_L
   1000013     2.31291283e+02   # ~mu_L
   1000014     2.16863786e+02   # ~numu_L
   1000015     1.09012759e+02   # ~stau_1
   1000016     2.16426247e+02   # ~nu_tau_L
   2000001     7.68369227e+02   # ~d_R
   2000002     7.69254462e+02   # ~u_R
   2000003     7.68367817e+02   # ~s_R
   2000004     7.69253747e+02   # ~c_R
   2000005     7.74761078e+02   # ~b_2
   2000006     7.93595065e+02   # ~t_2
   2000011     1.16280043e+02   # ~e_R
   2000013     1.16276373e+02   # ~mu_R
   2000015     2.33602676e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -8.19975516e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.55294752e-01   # N_{1,1}
  1  2    -8.09431400e-02   # N_{1,2}
  1  3     2.47851834e-01   # N_{1,3}
  1  4    -1.39390148e-01   # N_{1,4}
  2  1    -2.62543914e-01   # N_{2,1}
  2  2    -6.53431874e-01   # N_{2,2}
  2  3     5.37898434e-01   # N_{2,3}
  2  4    -4.63425026e-01   # N_{2,4}
  3  1    -6.79271371e-02   # N_{3,1}
  3  2     9.21926883e-02   # N_{3,2}
  3  3     6.92497356e-01   # N_{3,3}
  3  4     7.12273701e-01   # N_{3,4}
  4  1    -1.17764739e-01   # N_{4,1}
  4  2     7.46977578e-01   # N_{4,2}
  4  3     4.11924940e-01   # N_{4,3}
  4  4    -5.08403194e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1    -5.82253631e-01   # U_{1,1}
  1  2     8.13007201e-01   # U_{1,2}
  2  1    -8.13007201e-01   # U_{2,1}
  2  2    -5.82253631e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1    -7.18462977e-01   # V_{1,1}
  1  2     6.95565202e-01   # V_{1,2}
  2  1    -6.95565202e-01   # V_{2,1}
  2  2    -7.18462977e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.95251350e-01   # F_{11}
  1  2     9.18573008e-01   # F_{12}
  2  1     9.18573008e-01   # F_{21}
  2  2    -3.95251350e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     5.95892737e-01   # F_{11}
  1  2     8.03064036e-01   # F_{12}
  2  1     8.03064036e-01   # F_{21}
  2  2    -5.95892737e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.73877731e-01   # F_{11}
  1  2     9.84767249e-01   # F_{12}
  2  1     9.84767249e-01   # F_{21}
  2  2    -1.73877731e-01   # F_{22}
Block gauge Q= 7.29472177e+02  # SM gauge couplings
     1     3.62414364e-01   # g'(Q)MSSM DRbar
     2     6.45717885e-01   # g(Q)MSSM DRbar
     3     1.07446076e+00   # g3(Q)MSSM DRbar
Block yu Q= 7.29472177e+02  
  3  3     8.72938319e-01   # Yt(Q)MSSM DRbar
Block yd Q= 7.29472177e+02  
  3  3     2.07500378e-01   # Yb(Q)MSSM DRbar
Block ye Q= 7.29472177e+02  
  3  3     1.52181609e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 7.29472177e+02 # Higgs mixing parameters
     1     2.72003479e+02    # mu(Q)MSSM DRbar
     2     1.45563673e+01    # tan beta(Q)MSSM DRbar
     3     2.44078797e+02    # higgs vev(Q)MSSM DRbar
     4     1.31662936e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 7.29472177e+02  # MSSM DRbar SUSY breaking parameters
     1     1.51189197e+02      # M_1(Q)
     2     2.86888551e+02      # M_2(Q)
     3     7.98376804e+02      # M_3(Q)
    21     4.26355430e+04      # mH1^2(Q)
    22    -6.75616369e+04      # mH2^2(Q)
    31     2.22451023e+02      # meL(Q)
    32     2.22450081e+02      # mmuL(Q)
    33     2.22161320e+02      # mtauL(Q)
    34     1.03666342e+02      # meR(Q)
    35     1.03662233e+02      # mmuR(Q)
    36     1.02395723e+02      # mtauR(Q)
    41     7.67254685e+02      # mqL1(Q)
    42     7.67253645e+02      # mqL2(Q)
    43     7.42565666e+02      # mqL3(Q)
    44     7.40597070e+02      # muR(Q)
    45     7.40596338e+02      # mcR(Q)
    46     6.90531677e+02      # mtR(Q)
    47     7.38232379e+02      # mdR(Q)
    48     7.38230931e+02      # msR(Q)
    49     7.35399782e+02      # mbR(Q)
Block au Q= 7.29472177e+02  
  1  1    -2.43798881e+02      # Au(Q)MSSM DRbar
  2  2    -2.43798534e+02      # Ac(Q)MSSM DRbar
  3  3    -2.29650963e+02      # At(Q)MSSM DRbar
Block ad Q= 7.29472177e+02  
  1  1    -2.59645794e+02      # Ad(Q)MSSM DRbar
  2  2    -2.59645308e+02      # As(Q)MSSM DRbar
  3  3    -2.54307714e+02      # Ab(Q)MSSM DRbar
Block ae Q= 7.29472177e+02  
  1  1    -2.38566442e+01      # Ae(Q)MSSM DRbar
  2  2    -2.38564700e+01      # Amu(Q)MSSM DRbar
  3  3    -2.38031130e+01      # Atau(Q)MSSM DRbar
