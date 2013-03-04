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
     1    1.00000000e+03   # m0
     2    3.50000000e+02   # m12
     5   -5.00000000e+02   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    2.27415331e+16   # MX scale
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=3.01116357e-04
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.04003513e+01   # MW
        25     1.15486342e+02   # h0
        35     7.79880285e+02   # H0
        36     7.80018782e+02   # A0
        37     7.84288946e+02   # H+
   1000021     8.76435377e+02   # ~g
   1000022     1.44930793e+02   # ~neutralino(1)
   1000023     2.76965444e+02   # ~neutralino(2)
   1000024     2.77026137e+02   # ~chargino(1)
   1000025    -5.23672885e+02   # ~neutralino(3)
   1000035     5.34236718e+02   # ~neutralino(4)
   1000037     5.35348825e+02   # ~chargino(2)
   1000001     1.23230275e+03   # ~d_L
   1000002     1.22987027e+03   # ~u_L
   1000003     1.23225805e+03   # ~s_L
   1000004     1.22982548e+03   # ~c_L
   1000005     9.54931429e+02   # ~b_1
   1000006     7.84129970e+02   # ~t_1
   1000011     1.02429123e+03   # ~e_L
   1000012     1.02087157e+03   # ~nue_L
   1000013     1.02405781e+03   # ~mu_L
   1000014     1.02061111e+03   # ~numu_L
   1000015     8.23236610e+02   # ~stau_1
   1000016     9.36232798e+02   # ~nu_tau_L
   2000001     1.21639788e+03   # ~d_R
   2000002     1.21694211e+03   # ~u_R
   2000003     1.21631250e+03   # ~s_R
   2000004     1.21693632e+03   # ~c_R
   2000005     1.06986254e+03   # ~b_2
   2000006     9.92634938e+02   # ~t_2
   2000011     1.00826961e+03   # ~e_R
   2000013     1.00774005e+03   # ~mu_R
   2000015     9.43641878e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -2.60338829e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.94738141e-01   # N_{1,1}
  1  2    -1.79114619e-02   # N_{1,2}
  1  3     9.64650197e-02   # N_{1,3}
  1  4    -2.94908649e-02   # N_{1,4}
  2  1     4.06692508e-02   # N_{2,1}
  2  2     9.71533191e-01   # N_{2,2}
  2  3    -2.04729542e-01   # N_{2,3}
  2  4     1.12049475e-01   # N_{2,4}
  3  1    -4.57445050e-02   # N_{3,1}
  3  2     6.79046883e-02   # N_{3,2}
  3  3     7.00926581e-01   # N_{3,3}
  3  4     7.08518399e-01   # N_{3,4}
  4  1    -8.21552427e-02   # N_{4,1}
  4  2     2.26255146e-01   # N_{4,2}
  4  3     6.76374336e-01   # N_{4,3}
  4  4    -6.96115567e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.56842652e-01   # U_{1,1}
  1  2    -2.90606501e-01   # U_{1,2}
  2  1     2.90606501e-01   # U_{2,1}
  2  2     9.56842652e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.86961056e-01   # V_{1,1}
  1  2    -1.60959233e-01   # V_{1,2}
  2  1     1.60959233e-01   # V_{2,1}
  2  2     9.86961056e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.42565591e-01   # F_{11}
  1  2     9.39493915e-01   # F_{12}
  2  1     9.39493915e-01   # F_{21}
  2  2    -3.42565591e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.77810096e-01   # F_{11}
  1  2     2.09493237e-01   # F_{12}
  2  1    -2.09493237e-01   # F_{21}
  2  2     9.77810096e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.82469772e-01   # F_{11}
  1  2     9.83211464e-01   # F_{12}
  2  1     9.83211464e-01   # F_{21}
  2  2    -1.82469772e-01   # F_{22}
Block gauge Q= 8.61229809e+02  # SM gauge couplings
     1     3.61772322e-01   # g'(Q)MSSM DRbar
     2     6.42830530e-01   # g(Q)MSSM DRbar
     3     1.06554360e+00   # g3(Q)MSSM DRbar
Block yu Q= 8.61229809e+02  
  3  3     8.61785732e-01   # Yt(Q)MSSM DRbar
Block yd Q= 8.61229809e+02  
  3  3     5.19076865e-01   # Yb(Q)MSSM DRbar
Block ye Q= 8.61229809e+02  
  3  3     4.12410071e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 8.61229809e+02 # Higgs mixing parameters
     1     5.15701740e+02    # mu(Q)MSSM DRbar
     2     3.92588747e+01    # tan beta(Q)MSSM DRbar
     3     2.43885161e+02    # higgs vev(Q)MSSM DRbar
     4     7.33522924e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 8.61229809e+02  # MSSM DRbar SUSY breaking parameters
     1     1.46727902e+02      # M_1(Q)
     2     2.73428343e+02      # M_2(Q)
     3     7.89146391e+02      # M_3(Q)
    21     3.60120652e+05      # mH1^2(Q)
    22    -2.57361050e+05      # mH2^2(Q)
    31     1.02169253e+03      # meL(Q)
    32     1.02143295e+03      # mmuL(Q)
    33     9.39132926e+02      # mtauL(Q)
    34     1.00623663e+03      # meR(Q)
    35     1.00570679e+03      # mmuR(Q)
    36     8.28502268e+02      # mtauR(Q)
    41     1.21013465e+03      # mqL1(Q)
    42     1.21008922e+03      # mqL2(Q)
    43     9.41659122e+02      # mqL3(Q)
    44     1.19784538e+03      # muR(Q)
    45     1.19783949e+03      # mcR(Q)
    46     7.75208460e+02      # mtR(Q)
    47     1.19651191e+03      # mdR(Q)
    48     1.19642504e+03      # msR(Q)
    49     1.04740142e+03      # mbR(Q)
Block au Q= 8.61229809e+02  
  1  1    -1.14579983e+03      # Au(Q)MSSM DRbar
  2  2    -1.14577001e+03      # Ac(Q)MSSM DRbar
  3  3    -7.59312493e+02      # At(Q)MSSM DRbar
Block ad Q= 8.61229809e+02  
  1  1    -1.33445195e+03      # Ad(Q)MSSM DRbar
  2  2    -1.33437601e+03      # As(Q)MSSM DRbar
  3  3    -1.09384924e+03      # Ab(Q)MSSM DRbar
Block ae Q= 8.61229809e+02  
  1  1    -5.52961064e+02      # Ae(Q)MSSM DRbar
  2  2    -5.52668772e+02      # Amu(Q)MSSM DRbar
  3  3    -4.62034059e+02      # Atau(Q)MSSM DRbar
