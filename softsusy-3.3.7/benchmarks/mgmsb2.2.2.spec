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
     1    1.30000000e+05   # lambda
     2    1.00000000e+14   # M_mess
     5    1.00000000e+00   # N5
     6    1.00000000e+00   # cgrav
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=8.44529546e-04
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.04593466e+01   # MW
        25     1.14402182e+02   # h0
        35     8.71040339e+02   # H0
        36     8.70997282e+02   # A0
        37     8.74901177e+02   # H+
   1000021     9.90608582e+02   # ~g
   1000022     1.72908182e+02   # ~neutralino(1)
   1000023     3.33121523e+02   # ~neutralino(2)
   1000024     3.33298933e+02   # ~chargino(1)
   1000025    -6.91146402e+02   # ~neutralino(3)
   1000035     6.99089328e+02   # ~neutralino(4)
   1000037     6.99763606e+02   # ~chargino(2)
   1000039     3.08100000e+00   # ~gravitino
   1000001     1.21003332e+03   # ~d_L
   1000002     1.20759552e+03   # ~u_L
   1000003     1.21002851e+03   # ~s_L
   1000004     1.20759069e+03   # ~c_L
   1000005     1.06913900e+03   # ~b_1
   1000006     8.50698794e+02   # ~t_1
   1000011     5.80361583e+02   # ~e_L
   1000012     5.74622439e+02   # ~nue_L
   1000013     5.80461979e+02   # ~mu_L
   1000014     5.74609991e+02   # ~numu_L
   1000015     3.79767595e+02   # ~stau_1
   1000016     5.70554268e+02   # ~nu_tau_L
   2000001     1.08955129e+03   # ~d_R
   2000002     1.11106669e+03   # ~u_R
   2000003     1.08954413e+03   # ~s_R
   2000004     1.11106317e+03   # ~c_R
   2000005     1.09737059e+03   # ~b_2
   2000006     1.11161033e+03   # ~t_2
   2000011     3.93892489e+02   # ~e_R
   2000013     3.93855881e+02   # ~mu_R
   2000015     5.77902231e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -7.04403707e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.97076980e-01   # N_{1,1}
  1  2    -1.30644480e-02   # N_{1,2}
  1  3     7.17540451e-02   # N_{1,3}
  1  4    -2.27634345e-02   # N_{1,4}
  2  1     2.54606690e-02   # N_{2,1}
  2  2     9.85289903e-01   # N_{2,2}
  2  3    -1.49276528e-01   # N_{2,3}
  2  4     7.91964668e-02   # N_{2,4}
  3  1    -3.38066473e-02   # N_{3,1}
  3  2     5.05616454e-02   # N_{3,2}
  3  3     7.03584030e-01   # N_{3,3}
  3  4     7.08004339e-01   # N_{3,4}
  4  1    -6.36110184e-02   # N_{4,1}
  4  2     1.62716465e-01   # N_{4,2}
  4  3     6.91040801e-01   # N_{4,3}
  4  4    -7.01384062e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.77457753e-01   # U_{1,1}
  1  2    -2.11131098e-01   # U_{1,2}
  2  1     2.11131098e-01   # U_{2,1}
  2  2     9.77457753e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.93604112e-01   # V_{1,1}
  1  2    -1.12919747e-01   # V_{1,2}
  2  1     1.12919747e-01   # V_{2,1}
  2  2     9.93604112e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     2.26424348e-01   # F_{11}
  1  2     9.74028755e-01   # F_{12}
  2  1     9.74028755e-01   # F_{21}
  2  2    -2.26424348e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     4.87596241e-01   # F_{11}
  1  2     8.73069245e-01   # F_{12}
  2  1     8.73069245e-01   # F_{21}
  2  2    -4.87596241e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     9.71214872e-02   # F_{11}
  1  2     9.95272534e-01   # F_{12}
  2  1     9.95272534e-01   # F_{21}
  2  2    -9.71214872e-02   # F_{22}
Block gauge Q= 9.43695806e+02  # SM gauge couplings
     1     3.62405532e-01   # g'(Q)MSSM DRbar
     2     6.42721184e-01   # g(Q)MSSM DRbar
     3     1.06134228e+00   # g3(Q)MSSM DRbar
Block yu Q= 9.43695806e+02  
  3  3     8.60625345e-01   # Yt(Q)MSSM DRbar
Block yd Q= 9.43695806e+02  
  3  3     1.98848438e-01   # Yb(Q)MSSM DRbar
Block ye Q= 9.43695806e+02  
  3  3     1.50881434e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 9.43695806e+02 # Higgs mixing parameters
     1     6.84896906e+02    # mu(Q)MSSM DRbar
     2     1.45125956e+01    # tan beta(Q)MSSM DRbar
     3     2.44046644e+02    # higgs vev(Q)MSSM DRbar
     4     7.92426915e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 9.43695806e+02  # MSSM DRbar SUSY breaking parameters
     1     1.76033742e+02      # M_1(Q)
     2     3.27318376e+02      # M_2(Q)
     3     9.09165689e+02      # M_3(Q)
    21     2.83606131e+05      # mH1^2(Q)
    22    -4.55254070e+05      # mH2^2(Q)
    31     5.76847679e+02      # meL(Q)
    32     5.76835273e+02      # mmuL(Q)
    33     5.73056963e+02      # mtauL(Q)
    34     3.89002527e+02      # meR(Q)
    35     3.88965482e+02      # mmuR(Q)
    36     3.77549687e+02      # mtauR(Q)
    41     1.18160145e+03      # mqL1(Q)
    42     1.18159650e+03      # mqL2(Q)
    43     1.06624128e+03      # mqL3(Q)
    44     1.08331524e+03      # muR(Q)
    45     1.08331160e+03      # mcR(Q)
    46     8.21730814e+02      # mtR(Q)
    47     1.05972527e+03      # mdR(Q)
    48     1.05971783e+03      # msR(Q)
    49     1.04613358e+03      # mbR(Q)
Block au Q= 9.43695806e+02  
  1  1    -8.49408852e+02      # Au(Q)MSSM DRbar
  2  2    -8.49404547e+02      # Ac(Q)MSSM DRbar
  3  3    -6.74483364e+02      # At(Q)MSSM DRbar
Block ad Q= 9.43695806e+02  
  1  1    -1.01626732e+03      # Ad(Q)MSSM DRbar
  2  2    -1.01626135e+03      # As(Q)MSSM DRbar
  3  3    -9.50391602e+02      # Ab(Q)MSSM DRbar
Block ae Q= 9.43695806e+02  
  1  1    -1.86623199e+02      # Ae(Q)MSSM DRbar
  2  2    -1.86616742e+02      # Amu(Q)MSSM DRbar
  3  3    -1.84655656e+02      # Atau(Q)MSSM DRbar
