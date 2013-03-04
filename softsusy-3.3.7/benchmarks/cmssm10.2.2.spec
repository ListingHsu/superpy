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
     1    2.25000000e+02   # m0
     2    5.50000000e+02   # m12
     5    0.00000000e+00   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    1.83732861e+16   # MX scale
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=5.73917867e-04
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.04572004e+01   # MW
        25     1.15551282e+02   # h0
        35     8.03085286e+02   # H0
        36     8.02824027e+02   # A0
        37     8.07091037e+02   # H+
   1000021     1.25474458e+03   # ~g
   1000022     2.26313139e+02   # ~neutralino(1)
   1000023     4.28051843e+02   # ~neutralino(2)
   1000024     4.28266354e+02   # ~chargino(1)
   1000025    -6.90981198e+02   # ~neutralino(3)
   1000035     7.03995586e+02   # ~neutralino(4)
   1000037     7.03889129e+02   # ~chargino(2)
   1000001     1.16473733e+03   # ~d_L
   1000002     1.16219665e+03   # ~u_L
   1000003     1.16473445e+03   # ~s_L
   1000004     1.16219376e+03   # ~c_L
   1000005     1.06428201e+03   # ~b_1
   1000006     8.88692379e+02   # ~t_1
   1000011     4.34524279e+02   # ~e_L
   1000012     4.27123891e+02   # ~nue_L
   1000013     4.34642527e+02   # ~mu_L
   1000014     4.27119553e+02   # ~numu_L
   1000015     3.01539878e+02   # ~stau_1
   1000016     4.25652059e+02   # ~nu_tau_L
   2000001     1.11633762e+03   # ~d_R
   2000002     1.12016899e+03   # ~u_R
   2000003     1.11633461e+03   # ~s_R
   2000004     1.12016590e+03   # ~c_R
   2000005     1.11210719e+03   # ~b_2
   2000006     1.10554724e+03   # ~t_2
   2000011     3.08209798e+02   # ~e_R
   2000013     3.08197586e+02   # ~mu_R
   2000015     4.34947051e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.06183171e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.96456049e-01   # N_{1,1}
  1  2    -1.47818060e-02   # N_{1,2}
  1  3     7.63260051e-02   # N_{1,3}
  1  4    -3.21120201e-02   # N_{1,4}
  2  1     3.28894615e-02   # N_{2,1}
  2  2     9.73482059e-01   # N_{2,2}
  2  3    -1.87433003e-01   # N_{2,3}
  2  4     1.26963908e-01   # N_{2,4}
  3  1    -3.04507324e-02   # N_{3,1}
  3  2     4.42262717e-02   # N_{3,2}
  3  3     7.04034481e-01   # N_{3,3}
  3  4     7.08132925e-01   # N_{3,4}
  4  1    -7.11785001e-02   # N_{4,1}
  4  2     2.23960301e-01   # N_{4,2}
  4  3     6.80719222e-01   # N_{4,3}
  4  4    -6.93827605e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.64048482e-01   # U_{1,1}
  1  2    -2.65726408e-01   # U_{1,2}
  2  1     2.65726408e-01   # U_{2,1}
  2  2     9.64048482e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.83469135e-01   # V_{1,1}
  1  2    -1.81075842e-01   # V_{1,2}
  2  1     1.81075842e-01   # V_{2,1}
  2  2     9.83469135e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.97160518e-01   # F_{11}
  1  2     9.17749161e-01   # F_{12}
  2  1     9.17749161e-01   # F_{21}
  2  2    -3.97160518e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.82309769e-01   # F_{11}
  1  2     1.87263229e-01   # F_{12}
  2  1    -1.87263229e-01   # F_{21}
  2  2     9.82309769e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.28686406e-01   # F_{11}
  1  2     9.91685338e-01   # F_{12}
  2  1     9.91685338e-01   # F_{21}
  2  2    -1.28686406e-01   # F_{22}
Block gauge Q= 9.61500033e+02  # SM gauge couplings
     1     3.62551737e-01   # g'(Q)MSSM DRbar
     2     6.42398179e-01   # g(Q)MSSM DRbar
     3     1.05598968e+00   # g3(Q)MSSM DRbar
Block yu Q= 9.61500033e+02  
  3  3     8.58049715e-01   # Yt(Q)MSSM DRbar
Block yd Q= 9.61500033e+02  
  3  3     1.34719376e-01   # Yb(Q)MSSM DRbar
Block ye Q= 9.61500033e+02  
  3  3     1.00440801e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 9.61500033e+02 # Higgs mixing parameters
     1     6.85474363e+02    # mu(Q)MSSM DRbar
     2     9.66211804e+00    # tan beta(Q)MSSM DRbar
     3     2.43998136e+02    # higgs vev(Q)MSSM DRbar
     4     6.67564506e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 9.61500033e+02  # MSSM DRbar SUSY breaking parameters
     1     2.31213365e+02      # M_1(Q)
     2     4.28217754e+02      # M_2(Q)
     3     1.21637253e+03      # M_3(Q)
    21     1.62281707e+05      # mH1^2(Q)
    22    -4.53191397e+05      # mH2^2(Q)
    31     4.27405411e+02      # meL(Q)
    32     4.27401064e+02      # mmuL(Q)
    33     4.26088593e+02      # mtauL(Q)
    34     3.01933218e+02      # meR(Q)
    35     3.01920742e+02      # mmuR(Q)
    36     2.98134752e+02      # mtauR(Q)
    41     1.12481028e+03      # mqL1(Q)
    42     1.12480734e+03      # mqL2(Q)
    43     1.03423801e+03      # mqL3(Q)
    44     1.08341328e+03      # muR(Q)
    45     1.08341014e+03      # mcR(Q)
    46     8.86464304e+02      # mtR(Q)
    47     1.07838739e+03      # mdR(Q)
    48     1.07838433e+03      # msR(Q)
    49     1.07279185e+03      # mbR(Q)
Block au Q= 9.61500033e+02  
  1  1    -1.24193685e+03      # Au(Q)MSSM DRbar
  2  2    -1.24193130e+03      # Ac(Q)MSSM DRbar
  3  3    -9.59564580e+02      # At(Q)MSSM DRbar
Block ad Q= 9.61500033e+02  
  1  1    -1.51786715e+03      # Ad(Q)MSSM DRbar
  2  2    -1.51786201e+03      # As(Q)MSSM DRbar
  3  3    -1.41873670e+03      # Ab(Q)MSSM DRbar
Block ae Q= 9.61500033e+02  
  1  1    -3.27847217e+02      # Ae(Q)MSSM DRbar
  2  2    -3.27841361e+02      # Amu(Q)MSSM DRbar
  3  3    -3.26073845e+02      # Atau(Q)MSSM DRbar
