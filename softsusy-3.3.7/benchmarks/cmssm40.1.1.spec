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
     1    3.30000000e+02   # m0
     2    5.00000000e+02   # m12
     5   -5.00000000e+02   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    1.87271808e+16   # MX scale
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=7.08779054e-04
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03906341e+01   # MW
        25     1.16993966e+02   # h0
        35     6.09523595e+02   # H0
        36     6.09537952e+02   # A0
        37     6.15182469e+02   # H+
   1000021     1.15306188e+03   # ~g
   1000022     2.07041721e+02   # ~neutralino(1)
   1000023     3.94704158e+02   # ~neutralino(2)
   1000024     3.94831154e+02   # ~chargino(1)
   1000025    -7.02935235e+02   # ~neutralino(3)
   1000035     7.10981997e+02   # ~neutralino(4)
   1000037     7.11768930e+02   # ~chargino(2)
   1000001     1.09878756e+03   # ~d_L
   1000002     1.09603215e+03   # ~u_L
   1000003     1.09875426e+03   # ~s_L
   1000004     1.09599876e+03   # ~c_L
   1000005     9.12024918e+02   # ~b_1
   1000006     7.76574752e+02   # ~t_1
   1000011     4.72677497e+02   # ~e_L
   1000012     4.65718450e+02   # ~nue_L
   1000013     4.72714266e+02   # ~mu_L
   1000014     4.65581263e+02   # ~numu_L
   1000015     2.08881978e+02   # ~stau_1
   1000016     4.19074961e+02   # ~nu_tau_L
   2000001     1.05637805e+03   # ~d_R
   2000002     1.05951743e+03   # ~u_R
   2000003     1.05631190e+03   # ~s_R
   2000004     1.05951327e+03   # ~c_R
   2000005     9.81460960e+02   # ~b_2
   2000006     9.89134976e+02   # ~t_2
   2000011     3.81824871e+02   # ~e_R
   2000013     3.81485113e+02   # ~mu_R
   2000015     4.49665017e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -2.61316225e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.97115749e-01   # N_{1,1}
  1  2    -1.02798600e-02   # N_{1,2}
  1  3     7.15316392e-02   # N_{1,3}
  1  4    -2.31890322e-02   # N_{1,4}
  2  1     2.39145939e-02   # N_{2,1}
  2  2     9.82071696e-01   # N_{2,2}
  2  3    -1.61891860e-01   # N_{2,3}
  2  4     9.35644296e-02   # N_{2,4}
  3  1    -3.35091365e-02   # N_{3,1}
  3  2     4.93692849e-02   # N_{3,2}
  3  3     7.03707661e-01   # N_{3,3}
  3  4     7.07979759e-01   # N_{3,4}
  4  1    -6.37605843e-02   # N_{4,1}
  4  2     1.81637504e-01   # N_{4,2}
  4  3     6.88091402e-01   # N_{4,3}
  4  4    -6.99623204e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.73442654e-01   # U_{1,1}
  1  2    -2.28930994e-01   # U_{1,2}
  2  1     2.28930994e-01   # U_{2,1}
  2  2     9.73442654e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.91002745e-01   # V_{1,1}
  1  2    -1.33841544e-01   # V_{1,2}
  2  1     1.33841544e-01   # V_{2,1}
  2  2     9.91002745e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     4.73121235e-01   # F_{11}
  1  2     8.80997331e-01   # F_{12}
  2  1     8.80997331e-01   # F_{21}
  2  2    -4.73121235e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     8.12094196e-01   # F_{11}
  1  2     5.83526364e-01   # F_{12}
  2  1    -5.83526364e-01   # F_{21}
  2  2     8.12094196e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     3.55493090e-01   # F_{11}
  1  2     9.34678909e-01   # F_{12}
  2  1     9.34678909e-01   # F_{21}
  2  2    -3.55493090e-01   # F_{22}
Block gauge Q= 8.50961456e+02  # SM gauge couplings
     1     3.62132841e-01   # g'(Q)MSSM DRbar
     2     6.42336602e-01   # g(Q)MSSM DRbar
     3     1.06123659e+00   # g3(Q)MSSM DRbar
Block yu Q= 8.50961456e+02  
  3  3     8.56328285e-01   # Yt(Q)MSSM DRbar
Block yd Q= 8.50961456e+02  
  3  3     4.91164660e-01   # Yb(Q)MSSM DRbar
Block ye Q= 8.50961456e+02  
  3  3     4.27326949e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 8.50961456e+02 # Higgs mixing parameters
     1     6.99524878e+02    # mu(Q)MSSM DRbar
     2     3.92347864e+01    # tan beta(Q)MSSM DRbar
     3     2.44017889e+02    # higgs vev(Q)MSSM DRbar
     4     4.69173140e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 8.50961456e+02  # MSSM DRbar SUSY breaking parameters
     1     2.10483052e+02      # M_1(Q)
     2     3.90867466e+02      # M_2(Q)
     3     1.11771418e+03      # M_3(Q)
    21    -1.16855180e+05      # mH1^2(Q)
    22    -4.83190527e+05      # mH2^2(Q)
    31     4.67134690e+02      # meL(Q)
    32     4.66997420e+02      # mmuL(Q)
    33     4.23259347e+02      # mtauL(Q)
    34     3.77269158e+02      # meR(Q)
    35     3.76925357e+02      # mmuR(Q)
    36     2.51009557e+02      # mtauR(Q)
    41     1.06388347e+03      # mqL1(Q)
    42     1.06384947e+03      # mqL2(Q)
    43     9.10616873e+02      # mqL3(Q)
    44     1.02772029e+03      # muR(Q)
    45     1.02771606e+03      # mcR(Q)
    46     7.90834228e+02      # mtR(Q)
    47     1.02339865e+03      # mdR(Q)
    48     1.02333134e+03      # msR(Q)
    49     9.28906345e+02      # mbR(Q)
Block au Q= 8.50961456e+02  
  1  1    -1.48305116e+03      # Au(Q)MSSM DRbar
  2  2    -1.48301470e+03      # Ac(Q)MSSM DRbar
  3  3    -1.02166789e+03      # At(Q)MSSM DRbar
Block ad Q= 8.50961456e+02  
  1  1    -1.72567827e+03      # Ad(Q)MSSM DRbar
  2  2    -1.72558541e+03      # As(Q)MSSM DRbar
  3  3    -1.44971254e+03      # Ab(Q)MSSM DRbar
Block ae Q= 8.50961456e+02  
  1  1    -6.25844707e+02      # Ae(Q)MSSM DRbar
  2  2    -6.25530639e+02      # Amu(Q)MSSM DRbar
  3  3    -5.20738990e+02      # Atau(Q)MSSM DRbar
