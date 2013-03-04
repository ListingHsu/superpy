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
     1    8.10000000e+04   # lambda
     2    9.00000000e+04   # M_mess
     5    1.00000000e+00   # N5
     6    1.00000000e+00   # cgrav
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=2.57814034e-04
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.04067500e+01   # MW
        25     1.11534983e+02   # h0
        35     4.18287856e+02   # H0
        36     4.17918801e+02   # A0
        37     4.25933809e+02   # H+
   1000021     7.86358157e+02   # ~g
   1000022     1.29700704e+02   # ~neutralino(1)
   1000023     2.36109626e+02   # ~neutralino(2)
   1000024     2.35503520e+02   # ~chargino(1)
   1000025    -3.36754631e+02   # ~neutralino(3)
   1000035     3.70183328e+02   # ~neutralino(4)
   1000037     3.69676460e+02   # ~chargino(2)
   1000039     1.72773000e-09   # ~gravitino
   1000001     9.35942421e+02   # ~d_L
   1000002     9.32743769e+02   # ~u_L
   1000003     9.35941141e+02   # ~s_L
   1000004     9.32742485e+02   # ~c_L
   1000005     8.86755454e+02   # ~b_1
   1000006     8.30835172e+02   # ~t_1
   1000011     2.87066791e+02   # ~e_L
   1000012     2.75582294e+02   # ~nue_L
   1000013     2.87102428e+02   # ~mu_L
   1000014     2.75581026e+02   # ~numu_L
   1000015     1.37825841e+02   # ~stau_1
   1000016     2.75019863e+02   # ~nu_tau_L
   2000001     8.94990016e+02   # ~d_R
   2000002     8.97036045e+02   # ~u_R
   2000003     8.94988236e+02   # ~s_R
   2000004     8.97035137e+02   # ~c_R
   2000005     9.02931206e+02   # ~b_2
   2000006     9.16951986e+02   # ~t_2
   2000011     1.44101245e+02   # ~e_R
   2000013     1.44096333e+02   # ~mu_R
   2000015     2.88643899e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -7.74389290e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.80369228e-01   # N_{1,1}
  1  2    -5.18308183e-02   # N_{1,2}
  1  3     1.73495319e-01   # N_{1,3}
  1  4    -7.80327951e-02   # N_{1,4}
  2  1     1.38981453e-01   # N_{2,1}
  2  2     8.58389345e-01   # N_{2,2}
  2  3    -3.96537647e-01   # N_{2,3}
  2  4     2.94295399e-01   # N_{2,4}
  3  1    -6.18481844e-02   # N_{3,1}
  3  2     8.75470831e-02   # N_{3,2}
  3  3     6.95287447e-01   # N_{3,3}
  3  4     7.10693799e-01   # N_{3,4}
  4  1    -1.25439763e-01   # N_{4,1}
  4  2     5.02808916e-01   # N_{4,2}
  4  3     5.73787970e-01   # N_{4,3}
  4  4    -6.34204561e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     8.14997458e-01   # U_{1,1}
  1  2    -5.79464531e-01   # U_{1,2}
  2  1     5.79464531e-01   # U_{2,1}
  2  2     8.14997458e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.01842730e-01   # V_{1,1}
  1  2    -4.32064452e-01   # V_{1,2}
  2  1     4.32064452e-01   # V_{2,1}
  2  2     9.01842730e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.00728435e-01   # F_{11}
  1  2     9.53709814e-01   # F_{12}
  2  1     9.53709814e-01   # F_{21}
  2  2    -3.00728435e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     5.08983754e-01   # F_{11}
  1  2     8.60776125e-01   # F_{12}
  2  1     8.60776125e-01   # F_{21}
  2  2    -5.08983754e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.36986049e-01   # F_{11}
  1  2     9.90572977e-01   # F_{12}
  2  1     9.90572977e-01   # F_{21}
  2  2    -1.36986049e-01   # F_{22}
Block gauge Q= 8.53510695e+02  # SM gauge couplings
     1     3.62738111e-01   # g'(Q)MSSM DRbar
     2     6.45480228e-01   # g(Q)MSSM DRbar
     3     1.07056385e+00   # g3(Q)MSSM DRbar
Block yu Q= 8.53510695e+02  
  3  3     8.69837633e-01   # Yt(Q)MSSM DRbar
Block yd Q= 8.53510695e+02  
  3  3     2.05749366e-01   # Yb(Q)MSSM DRbar
Block ye Q= 8.53510695e+02  
  3  3     1.51537365e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 8.53510695e+02 # Higgs mixing parameters
     1     3.27672142e+02    # mu(Q)MSSM DRbar
     2     1.45252196e+01    # tan beta(Q)MSSM DRbar
     3     2.43768747e+02    # higgs vev(Q)MSSM DRbar
     4     1.93921012e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 8.53510695e+02  # MSSM DRbar SUSY breaking parameters
     1     1.36353608e+02      # M_1(Q)
     2     2.58077433e+02      # M_2(Q)
     3     7.13548559e+02      # M_3(Q)
    21     6.86369740e+04      # mH1^2(Q)
    22    -9.55095765e+04      # mH2^2(Q)
    31     2.80612687e+02      # meL(Q)
    32     2.80611437e+02      # mmuL(Q)
    33     2.80230186e+02      # mtauL(Q)
    34     1.33295301e+02      # meR(Q)
    35     1.33289985e+02      # mmuR(Q)
    36     1.31659480e+02      # mtauR(Q)
    41     9.09175635e+02      # mqL1(Q)
    42     9.09174310e+02      # mqL2(Q)
    43     8.77409772e+02      # mqL3(Q)
    44     8.72730171e+02      # muR(Q)
    45     8.72729230e+02      # mcR(Q)
    46     8.07844142e+02      # mtR(Q)
    47     8.69279329e+02      # mdR(Q)
    48     8.69277480e+02      # msR(Q)
    49     8.65665836e+02      # mbR(Q)
Block au Q= 8.53510695e+02  
  1  1    -2.20500492e+02      # Au(Q)MSSM DRbar
  2  2    -2.20500176e+02      # Ac(Q)MSSM DRbar
  3  3    -2.07554270e+02      # At(Q)MSSM DRbar
Block ad Q= 8.53510695e+02  
  1  1    -2.34942896e+02      # Ad(Q)MSSM DRbar
  2  2    -2.34942455e+02      # As(Q)MSSM DRbar
  3  3    -2.30064349e+02      # Ab(Q)MSSM DRbar
Block ae Q= 8.53510695e+02  
  1  1    -2.19386874e+01      # Ae(Q)MSSM DRbar
  2  2    -2.19385249e+01      # Amu(Q)MSSM DRbar
  3  3    -2.18890085e+01      # Atau(Q)MSSM DRbar
