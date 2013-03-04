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
     1    3.00000000e+02   # m0
     2    4.50000000e+02   # m12
     5    0.00000000e+00   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    2.01245380e+16   # MX scale
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=2.10533698e-04
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.04592188e+01   # MW
        25     1.14248319e+02   # h0
        35     7.06804086e+02   # H0
        36     7.06480893e+02   # A0
        37     7.11370829e+02   # H+
   1000021     1.04853030e+03   # ~g
   1000022     1.83384609e+02   # ~neutralino(1)
   1000023     3.46122769e+02   # ~neutralino(2)
   1000024     3.46275878e+02   # ~chargino(1)
   1000025    -5.79643845e+02   # ~neutralino(3)
   1000035     5.94178417e+02   # ~neutralino(4)
   1000037     5.94118233e+02   # ~chargino(2)
   1000001     9.96853875e+02   # ~d_L
   1000002     9.93859021e+02   # ~u_L
   1000003     9.96851280e+02   # ~s_L
   1000004     9.93856416e+02   # ~c_L
   1000005     9.05192118e+02   # ~b_1
   1000006     7.47238319e+02   # ~t_1
   1000011     4.27878399e+02   # ~e_L
   1000012     4.20324665e+02   # ~nue_L
   1000013     4.27971246e+02   # ~mu_L
   1000014     4.20319795e+02   # ~numu_L
   1000015     3.40316368e+02   # ~stau_1
   1000016     4.18751084e+02   # ~nu_tau_L
   2000001     9.58877892e+02   # ~d_R
   2000002     9.61502508e+02   # ~u_R
   2000003     9.58875203e+02   # ~s_R
   2000004     9.61499729e+02   # ~c_R
   2000005     9.55124462e+02   # ~b_2
   2000006     9.49940105e+02   # ~t_2
   2000011     3.46577310e+02   # ~e_R
   2000013     3.46565335e+02   # ~mu_R
   2000015     4.28293475e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.06819893e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.94898630e-01   # N_{1,1}
  1  2    -2.10692272e-02   # N_{1,2}
  1  3     9.12629278e-02   # N_{1,3}
  1  4    -3.74684100e-02   # N_{1,4}
  2  1     4.51505035e-02   # N_{2,1}
  2  2     9.66235850e-01   # N_{2,2}
  2  3    -2.11856483e-01   # N_{2,3}
  2  4     1.39522564e-01   # N_{2,4}
  3  1    -3.66388388e-02   # N_{3,1}
  3  2     5.34624670e-02   # N_{3,2}
  3  3     7.02663444e-01   # N_{3,3}
  3  4     7.08564355e-01   # N_{3,4}
  4  1    -8.24363002e-02   # N_{4,1}
  4  2     2.51169535e-01   # N_{4,2}
  4  3     6.73091371e-01   # N_{4,3}
  4  4    -6.90699738e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.53407467e-01   # U_{1,1}
  1  2    -3.01685602e-01   # U_{1,2}
  2  1     3.01685602e-01   # U_{2,1}
  2  2     9.53407467e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.79780133e-01   # V_{1,1}
  1  2    -2.00077214e-01   # V_{1,2}
  2  1     2.00077214e-01   # V_{2,1}
  2  2     9.79780133e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     4.24991593e-01   # F_{11}
  1  2     9.05197297e-01   # F_{12}
  2  1     9.05197297e-01   # F_{21}
  2  2    -4.24991593e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.84105699e-01   # F_{11}
  1  2     1.77583710e-01   # F_{12}
  2  1    -1.77583710e-01   # F_{21}
  2  2     9.84105699e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.57084236e-01   # F_{11}
  1  2     9.87585208e-01   # F_{12}
  2  1     9.87585208e-01   # F_{21}
  2  2    -1.57084236e-01   # F_{22}
Block gauge Q= 8.16311403e+02  # SM gauge couplings
     1     3.62099242e-01   # g'(Q)MSSM DRbar
     2     6.43227184e-01   # g(Q)MSSM DRbar
     3     1.06501881e+00   # g3(Q)MSSM DRbar
Block yu Q= 8.16311403e+02  
  3  3     8.64181779e-01   # Yt(Q)MSSM DRbar
Block yd Q= 8.16311403e+02  
  3  3     1.36028635e-01   # Yb(Q)MSSM DRbar
Block ye Q= 8.16311403e+02  
  3  3     1.00472996e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 8.16311403e+02 # Higgs mixing parameters
     1     5.73796961e+02    # mu(Q)MSSM DRbar
     2     9.68146122e+00    # tan beta(Q)MSSM DRbar
     3     2.44182205e+02    # higgs vev(Q)MSSM DRbar
     4     5.16302295e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 8.16311403e+02  # MSSM DRbar SUSY breaking parameters
     1     1.87564049e+02      # M_1(Q)
     2     3.48997716e+02      # M_2(Q)
     3     1.00878848e+03      # M_3(Q)
    21     1.62324616e+05      # mH1^2(Q)
    22    -3.18371003e+05      # mH2^2(Q)
    31     4.22476323e+02      # meL(Q)
    32     4.22471461e+02      # mmuL(Q)
    33     4.21007967e+02      # mtauL(Q)
    34     3.42012839e+02      # meR(Q)
    35     3.42000707e+02      # mmuR(Q)
    36     3.38334785e+02      # mtauR(Q)
    41     9.62553180e+02      # mqL1(Q)
    42     9.62550521e+02      # mqL2(Q)
    43     8.78999074e+02      # mqL3(Q)
    44     9.30284768e+02      # muR(Q)
    45     9.30281936e+02      # mcR(Q)
    46     7.48591807e+02      # mtR(Q)
    47     9.26415133e+02      # mdR(Q)
    48     9.26412388e+02      # msR(Q)
    49     9.21352833e+02      # mbR(Q)
Block au Q= 8.16311403e+02  
  1  1    -1.03669588e+03      # Au(Q)MSSM DRbar
  2  2    -1.03669121e+03      # Ac(Q)MSSM DRbar
  3  3    -7.98455902e+02      # At(Q)MSSM DRbar
Block ad Q= 8.16311403e+02  
  1  1    -1.27000603e+03      # Ad(Q)MSSM DRbar
  2  2    -1.27000169e+03      # As(Q)MSSM DRbar
  3  3    -1.18634073e+03      # Ab(Q)MSSM DRbar
Block ae Q= 8.16311403e+02  
  1  1    -2.70582965e+02      # Ae(Q)MSSM DRbar
  2  2    -2.70578075e+02      # Amu(Q)MSSM DRbar
  3  3    -2.69107492e+02      # Atau(Q)MSSM DRbar
