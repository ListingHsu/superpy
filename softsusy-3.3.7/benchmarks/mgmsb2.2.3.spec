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
     1    1.40000000e+05   # lambda
     2    1.00000000e+14   # M_mess
     5    1.00000000e+00   # N5
     6    1.00000000e+00   # cgrav
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=7.51416744e-05
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03968904e+01   # MW
        25     1.14913279e+02   # h0
        35     9.33704172e+02   # H0
        36     9.33657626e+02   # A0
        37     9.37316255e+02   # H+
   1000021     1.05931172e+03   # ~g
   1000022     1.86563414e+02   # ~neutralino(1)
   1000023     3.59541692e+02   # ~neutralino(2)
   1000024     3.59726296e+02   # ~chargino(1)
   1000025    -7.38363230e+02   # ~neutralino(3)
   1000035     7.45899641e+02   # ~neutralino(4)
   1000037     7.46532255e+02   # ~chargino(2)
   1000039     3.31800000e+00   # ~gravitino
   1000001     1.29686420e+03   # ~d_L
   1000002     1.29460117e+03   # ~u_L
   1000003     1.29685905e+03   # ~s_L
   1000004     1.29459601e+03   # ~c_L
   1000005     1.14617288e+03   # ~b_1
   1000006     9.11771607e+02   # ~t_1
   1000011     6.23578039e+02   # ~e_L
   1000012     6.18221613e+02   # ~nue_L
   1000013     6.23674695e+02   # ~mu_L
   1000014     6.18208287e+02   # ~numu_L
   1000015     4.08618615e+02   # ~stau_1
   1000016     6.13864915e+02   # ~nu_tau_L
   2000001     1.16705607e+03   # ~d_R
   2000002     1.19043637e+03   # ~u_R
   2000003     1.16704841e+03   # ~s_R
   2000004     1.19043260e+03   # ~c_R
   2000005     1.17538660e+03   # ~b_2
   2000006     1.18857029e+03   # ~t_2
   2000011     4.23406821e+02   # ~e_R
   2000013     4.23367601e+02   # ~mu_R
   2000015     6.20705834e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -7.02943121e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.97453149e-01   # N_{1,1}
  1  2    -1.14294293e-02   # N_{1,2}
  1  3     6.70617640e-02   # N_{1,3}
  1  4    -2.14313615e-02   # N_{1,4}
  2  1     2.23973624e-02   # N_{2,1}
  2  2     9.86905721e-01   # N_{2,2}
  2  3    -1.40856457e-01   # N_{2,3}
  2  4     7.53320308e-02   # N_{2,4}
  3  1    -3.15841406e-02   # N_{3,1}
  3  2     4.71660180e-02   # N_{3,2}
  3  3     7.04035716e-01   # N_{3,3}
  3  4     7.07892307e-01   # N_{3,4}
  4  1    -5.99000461e-02   # N_{4,1}
  4  2     1.53824033e-01   # N_{4,2}
  4  3     6.92817356e-01   # N_{4,3}
  4  4    -7.01964574e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.79987457e-01   # U_{1,1}
  1  2    -1.99059247e-01   # U_{1,2}
  2  1     1.99059247e-01   # U_{2,1}
  2  2     9.79987457e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.94225936e-01   # V_{1,1}
  1  2    -1.07306978e-01   # V_{1,2}
  2  1     1.07306978e-01   # V_{2,1}
  2  2     9.94225936e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     2.11823439e-01   # F_{11}
  1  2     9.77307951e-01   # F_{12}
  2  1     9.77307951e-01   # F_{21}
  2  2    -2.11823439e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     4.61965594e-01   # F_{11}
  1  2     8.86897846e-01   # F_{12}
  2  1     8.86897846e-01   # F_{21}
  2  2    -4.61965594e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     9.01230746e-02   # F_{11}
  1  2     9.95930636e-01   # F_{12}
  2  1     9.95930636e-01   # F_{21}
  2  2    -9.01230746e-02   # F_{22}
Block gauge Q= 1.01069793e+03  # SM gauge couplings
     1     3.62544611e-01   # g'(Q)MSSM DRbar
     2     6.42385612e-01   # g(Q)MSSM DRbar
     3     1.05773395e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.01069793e+03  
  3  3     8.58251941e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.01069793e+03  
  3  3     1.98178072e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.01069793e+03  
  3  3     1.50810926e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.01069793e+03 # Higgs mixing parameters
     1     7.32110820e+02    # mu(Q)MSSM DRbar
     2     1.45008287e+01    # tan beta(Q)MSSM DRbar
     3     2.43963727e+02    # higgs vev(Q)MSSM DRbar
     4     9.10311276e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.01069793e+03  # MSSM DRbar SUSY breaking parameters
     1     1.89765302e+02      # M_1(Q)
     2     3.52258996e+02      # M_2(Q)
     3     9.72646534e+02      # M_3(Q)
    21     3.28157784e+05      # mH1^2(Q)
    22    -5.19248967e+05      # mH2^2(Q)
    31     6.20016364e+02      # meL(Q)
    32     6.20003072e+02      # mmuL(Q)
    33     6.15951681e+02      # mtauL(Q)
    34     4.18502632e+02      # meR(Q)
    35     4.18462978e+02      # mmuR(Q)
    36     4.06234327e+02      # mtauR(Q)
    41     1.26679568e+03      # mqL1(Q)
    42     1.26679038e+03      # mqL2(Q)
    43     1.14336520e+03      # mqL3(Q)
    44     1.16090474e+03      # muR(Q)
    45     1.16090084e+03      # mcR(Q)
    46     8.80885147e+02      # mtR(Q)
    47     1.13542193e+03      # mdR(Q)
    48     1.13541399e+03      # msR(Q)
    49     1.12090383e+03      # mbR(Q)
Block au Q= 1.01069793e+03  
  1  1    -9.06033493e+02      # Au(Q)MSSM DRbar
  2  2    -9.06028917e+02      # Ac(Q)MSSM DRbar
  3  3    -7.20223415e+02      # At(Q)MSSM DRbar
Block ad Q= 1.01069793e+03  
  1  1    -1.08312824e+03      # Ad(Q)MSSM DRbar
  2  2    -1.08312191e+03      # As(Q)MSSM DRbar
  3  3    -1.01316560e+03      # Ab(Q)MSSM DRbar
Block ae Q= 1.01069793e+03  
  1  1    -2.00108570e+02      # Ae(Q)MSSM DRbar
  2  2    -2.00101677e+02      # Amu(Q)MSSM DRbar
  3  3    -1.98006541e+02      # Atau(Q)MSSM DRbar
