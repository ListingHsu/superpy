# SOFTSUSY3.3.7 SLHA compliant output
# B.C. Allanach, Comput. Phys. Commun. 143 (2002) 305-331, hep-ph/0104145
Block SPINFO          # Program information
     1    SOFTSUSY    # spectrum calculator
     2    3.3.7       # version number
Block MODSEL  # Select model
     1    3   # amsb
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
     1    3.00000000e+02   # m0
     2    4.00000000e+04   # m3/2
Block EXTPAR               # scale of SUSY breaking BCs
     0    2.65916680e+16   # MX scale
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=1.74090065e-04
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.04071989e+01   # MW
        25     1.12477896e+02   # h0
        35     7.25688429e+02   # H0
        36     7.25463734e+02   # A0
        37     7.30117514e+02   # H+
   1000021    -8.88553836e+02   # ~g
   1000022     1.30633090e+02   # ~neutralino(1)
   1000023     3.63255673e+02   # ~neutralino(2)
   1000024     1.30836020e+02   # ~chargino(1)
   1000025    -7.02200116e+02   # ~neutralino(3)
   1000035     7.10013923e+02   # ~neutralino(4)
   1000037     7.08767667e+02   # ~chargino(2)
   1000039     4.00000000e+04   # ~gravitino
   1000001     8.80770178e+02   # ~d_L
   1000002     8.77358736e+02   # ~u_L
   1000003     8.80764922e+02   # ~s_L
   1000004     8.77353453e+02   # ~c_L
   1000005     7.66252098e+02   # ~b_1
   1000006     6.31822552e+02   # ~t_1
   1000011     2.59766298e+02   # ~e_L
   1000012     2.47225199e+02   # ~nue_L
   1000013     2.59757058e+02   # ~mu_L
   1000014     2.47213327e+02   # ~numu_L
   1000015     2.25930652e+02   # ~stau_1
   1000016     2.43589069e+02   # ~nu_tau_L
   2000001     8.89128289e+02   # ~d_R
   2000002     8.82345708e+02   # ~u_R
   2000003     8.89122619e+02   # ~s_R
   2000004     8.82340903e+02   # ~c_R
   2000005     8.77491155e+02   # ~b_2
   2000006     8.12729213e+02   # ~t_2
   2000011     2.52012786e+02   # ~e_R
   2000013     2.51989378e+02   # ~mu_R
   2000015     2.73076552e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.07945483e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1    -8.12444339e-03   # N_{1,1}
  1  2     9.92465319e-01   # N_{1,2}
  1  3    -1.17819973e-01   # N_{1,3}
  1  4     3.26349209e-02   # N_{1,4}
  2  1     9.94607095e-01   # N_{2,1}
  2  2     2.02378231e-02   # N_{2,2}
  2  3     8.75407913e-02   # N_{2,3}
  2  4    -5.18050872e-02   # N_{2,4}
  3  1    -2.62793918e-02   # N_{3,1}
  3  2     6.00290113e-02   # N_{3,2}
  3  3     7.03490337e-01   # N_{3,3}
  3  4     7.07677368e-01   # N_{3,4}
  4  1    -1.00000568e-01   # N_{4,1}
  4  2     1.04878687e-01   # N_{4,2}
  4  3     6.95382204e-01   # N_{4,3}
  4  4    -7.03877786e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.86562371e-01   # U_{1,1}
  1  2    -1.63385089e-01   # U_{1,2}
  2  1     1.63385089e-01   # U_{2,1}
  2  2     9.86562371e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.98948688e-01   # V_{1,1}
  1  2    -4.58423152e-02   # V_{1,2}
  2  1     4.58423152e-02   # V_{2,1}
  2  2     9.98948688e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1    -4.53197736e-01   # F_{11}
  1  2     8.91410014e-01   # F_{12}
  2  1     8.91410014e-01   # F_{21}
  2  2     4.53197736e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.97263545e-01   # F_{11}
  1  2     7.39284888e-02   # F_{12}
  2  1    -7.39284888e-02   # F_{21}
  2  2     9.97263545e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     6.14359492e-01   # F_{11}
  1  2     7.89026244e-01   # F_{12}
  2  1     7.89026244e-01   # F_{21}
  2  2    -6.14359492e-01   # F_{22}
Block gauge Q= 6.89361809e+02  # SM gauge couplings
     1     3.61739203e-01   # g'(Q)MSSM DRbar
     2     6.46165360e-01   # g(Q)MSSM DRbar
     3     1.07367156e+00   # g3(Q)MSSM DRbar
Block yu Q= 6.89361809e+02  
  3  3     8.70664377e-01   # Yt(Q)MSSM DRbar
Block yd Q= 6.89361809e+02  
  3  3     1.50879660e-01   # Yb(Q)MSSM DRbar
Block ye Q= 6.89361809e+02  
  3  3     9.94838167e-02   # Ytau(Q)MSSM DRbar
Block hmix Q= 6.89361809e+02 # Higgs mixing parameters
     1     7.00134886e+02    # mu(Q)MSSM DRbar
     2     9.70362717e+00    # tan beta(Q)MSSM DRbar
     3     2.44686666e+02    # higgs vev(Q)MSSM DRbar
     4     5.26213603e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 6.89361809e+02  # MSSM DRbar SUSY breaking parameters
     1     3.71686203e+02      # M_1(Q)
     2     1.28393695e+02      # M_2(Q)
     3    -8.44097919e+02      # M_3(Q)
    21     3.01045086e+04      # mH1^2(Q)
    22    -4.82317002e+05      # mH2^2(Q)
    31     2.54918074e+02      # meL(Q)
    32     2.54906540e+02      # mmuL(Q)
    33     2.51528854e+02      # mtauL(Q)
    34     2.44777849e+02      # meR(Q)
    35     2.44753816e+02      # mmuR(Q)
    36     2.37659050e+02      # mtauR(Q)
    41     8.52463607e+02      # mqL1(Q)
    42     8.52458171e+02      # mqL2(Q)
    43     7.40260515e+02      # mqL3(Q)
    44     8.57467935e+02      # muR(Q)
    45     8.57462972e+02      # mcR(Q)
    46     6.28458425e+02      # mtR(Q)
    47     8.63409509e+02      # mdR(Q)
    48     8.63403639e+02      # msR(Q)
    49     8.51107031e+02      # mbR(Q)
Block au Q= 6.89361809e+02  
  1  1     1.32585764e+03      # Au(Q)MSSM DRbar
  2  2     1.32584652e+03      # Ac(Q)MSSM DRbar
  3  3     7.52924342e+02      # At(Q)MSSM DRbar
Block ad Q= 6.89361809e+02  
  1  1     1.87476035e+03      # Ad(Q)MSSM DRbar
  2  2     1.87475002e+03      # As(Q)MSSM DRbar
  3  3     1.66980964e+03      # Ab(Q)MSSM DRbar
Block ae Q= 6.89361809e+02  
  1  1     3.92911225e+02      # Ae(Q)MSSM DRbar
  2  2     3.92885698e+02      # Amu(Q)MSSM DRbar
  3  3     3.85376866e+02      # Atau(Q)MSSM DRbar
