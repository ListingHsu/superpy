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
     1    1.17000000e+05   # lambda
     2    1.30000000e+05   # M_mess
     5    1.00000000e+00   # N5
     6    1.00000000e+00   # cgrav
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=8.02397623e-05
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.04002847e+01   # MW
        25     1.14217811e+02   # h0
        35     5.90782724e+02   # H0
        36     5.90516271e+02   # A0
        37     5.96220258e+02   # H+
   1000021     1.09537602e+03   # ~g
   1000022     1.90923883e+02   # ~neutralino(1)
   1000023     3.53351686e+02   # ~neutralino(2)
   1000024     3.53225628e+02   # ~chargino(1)
   1000025    -4.59626397e+02   # ~neutralino(3)
   1000035     4.91681006e+02   # ~neutralino(4)
   1000037     4.90973650e+02   # ~chargino(2)
   1000039     3.60477000e-09   # ~gravitino
   1000001     1.31059787e+03   # ~d_L
   1000002     1.30836923e+03   # ~u_L
   1000003     1.31059609e+03   # ~s_L
   1000004     1.30836745e+03   # ~c_L
   1000005     1.24245336e+03   # ~b_1
   1000006     1.15737202e+03   # ~t_1
   1000011     4.10062315e+02   # ~e_L
   1000012     4.02048174e+02   # ~nue_L
   1000013     4.10058855e+02   # ~mu_L
   1000014     4.02046370e+02   # ~numu_L
   1000015     1.98438859e+02   # ~stau_1
   1000016     4.01252793e+02   # ~nu_tau_L
   2000001     1.25097400e+03   # ~d_R
   2000002     1.25491733e+03   # ~u_R
   2000003     1.25097153e+03   # ~s_R
   2000004     1.25491606e+03   # ~c_R
   2000005     1.26216184e+03   # ~b_2
   2000006     1.27184068e+03   # ~t_2
   2000011     2.04125745e+02   # ~e_R
   2000013     2.04118555e+02   # ~mu_R
   2000015     4.10664235e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -7.33553971e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.89891588e-01   # N_{1,1}
  1  2    -2.78710150e-02   # N_{1,2}
  1  3     1.25575264e-01   # N_{1,3}
  1  4    -5.97386295e-02   # N_{1,4}
  2  1     8.98174734e-02   # N_{2,1}
  2  2     8.74541143e-01   # N_{2,2}
  2  3    -3.72528404e-01   # N_{2,3}
  2  4     2.97209015e-01   # N_{2,4}
  3  1    -4.43922074e-02   # N_{3,1}
  3  2     6.22260711e-02   # N_{3,2}
  3  3     7.01039940e-01   # N_{3,3}
  3  4     7.09013576e-01   # N_{3,4}
  4  1    -1.00383254e-01   # N_{4,1}
  4  2     4.80134264e-01   # N_{4,2}
  4  3     5.94976003e-01   # N_{4,3}
  4  4    -6.36708605e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     8.43728423e-01   # U_{1,1}
  1  2    -5.36770293e-01   # U_{1,2}
  2  1     5.36770293e-01   # U_{2,1}
  2  2     8.43728423e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.02757904e-01   # V_{1,1}
  1  2    -4.30149005e-01   # V_{1,2}
  2  1     4.30149005e-01   # V_{2,1}
  2  2     9.02757904e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     2.24838851e-01   # F_{11}
  1  2     9.74395962e-01   # F_{12}
  2  1     9.74395962e-01   # F_{21}
  2  2    -2.24838851e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     3.80226130e-01   # F_{11}
  1  2     9.24893556e-01   # F_{12}
  2  1     9.24893556e-01   # F_{21}
  2  2    -3.80226130e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     9.30975940e-02   # F_{11}
  1  2     9.95656988e-01   # F_{12}
  2  1     9.95656988e-01   # F_{21}
  2  2    -9.30975940e-02   # F_{22}
Block gauge Q= 1.18855465e+03  # SM gauge couplings
     1     3.63446817e-01   # g'(Q)MSSM DRbar
     2     6.43604130e-01   # g(Q)MSSM DRbar
     3     1.05287012e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.18855465e+03  
  3  3     8.58049990e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.18855465e+03  
  3  3     2.02201859e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.18855465e+03  
  3  3     1.51218470e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.18855465e+03 # Higgs mixing parameters
     1     4.51058170e+02    # mu(Q)MSSM DRbar
     2     1.44684312e+01    # tan beta(Q)MSSM DRbar
     3     2.43371542e+02    # higgs vev(Q)MSSM DRbar
     4     3.86169407e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.18855465e+03  # MSSM DRbar SUSY breaking parameters
     1     1.97798699e+02      # M_1(Q)
     2     3.70806027e+02      # M_2(Q)
     3     9.97189126e+02      # M_3(Q)
    21     1.43192444e+05      # mH1^2(Q)
    22    -1.75189204e+05      # mH2^2(Q)
    31     4.03313517e+02      # meL(Q)
    32     4.03311714e+02      # mmuL(Q)
    33     4.02759536e+02      # mtauL(Q)
    34     1.93654730e+02      # meR(Q)
    35     1.93647145e+02      # mmuR(Q)
    36     1.91311437e+02      # mtauR(Q)
    41     1.27538814e+03      # mqL1(Q)
    42     1.27538630e+03      # mqL2(Q)
    43     1.23139923e+03      # mqL3(Q)
    44     1.22177408e+03      # muR(Q)
    45     1.22177276e+03      # mcR(Q)
    46     1.13172742e+03      # mtR(Q)
    47     1.21657452e+03      # mdR(Q)
    48     1.21657196e+03      # msR(Q)
    49     1.21159947e+03      # mbR(Q)
Block au Q= 1.18855465e+03  
  1  1    -3.03358429e+02      # Au(Q)MSSM DRbar
  2  2    -3.03357999e+02      # Ac(Q)MSSM DRbar
  3  3    -2.85816660e+02      # At(Q)MSSM DRbar
Block ad Q= 1.18855465e+03  
  1  1    -3.22762892e+02      # Ad(Q)MSSM DRbar
  2  2    -3.22762295e+02      # As(Q)MSSM DRbar
  3  3    -3.16161434e+02      # Ab(Q)MSSM DRbar
Block ae Q= 1.18855465e+03  
  1  1    -3.17677449e+01      # Ae(Q)MSSM DRbar
  2  2    -3.17675103e+01      # Amu(Q)MSSM DRbar
  3  3    -3.16957066e+01      # Atau(Q)MSSM DRbar
