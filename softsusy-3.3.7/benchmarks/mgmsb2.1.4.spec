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
     1    9.90000000e+04   # lambda
     2    1.10000000e+05   # M_mess
     5    1.00000000e+00   # N5
     6    1.00000000e+00   # cgrav
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=1.26338848e-04
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.04660704e+01   # MW
        25     1.13033851e+02   # h0
        35     5.05546027e+02   # H0
        36     5.05239616e+02   # A0
        37     5.11887544e+02   # H+
   1000021     9.42100558e+02   # ~g
   1000022     1.60379806e+02   # ~neutralino(1)
   1000023     2.94922263e+02   # ~neutralino(2)
   1000024     2.94619632e+02   # ~chargino(1)
   1000025    -3.99210585e+02   # ~neutralino(3)
   1000035     4.31722721e+02   # ~neutralino(4)
   1000037     4.31085229e+02   # ~chargino(2)
   1000039     2.58093000e-09   # ~gravitino
   1000001     1.12448471e+03   # ~d_L
   1000002     1.12185677e+03   # ~u_L
   1000003     1.12448318e+03   # ~s_L
   1000004     1.12185523e+03   # ~c_L
   1000005     1.06596598e+03   # ~b_1
   1000006     9.95204041e+02   # ~t_1
   1000011     3.48496060e+02   # ~e_L
   1000012     3.39068271e+02   # ~nue_L
   1000013     3.48512125e+02   # ~mu_L
   1000014     3.39066736e+02   # ~numu_L
   1000015     1.68054983e+02   # ~stau_1
   1000016     3.38388455e+02   # ~nu_tau_L
   2000001     1.07428850e+03   # ~d_R
   2000002     1.07730051e+03   # ~u_R
   2000003     1.07428637e+03   # ~s_R
   2000004     1.07729942e+03   # ~c_R
   2000005     1.08362605e+03   # ~b_2
   2000006     1.09504348e+03   # ~t_2
   2000011     1.73908950e+02   # ~e_R
   2000013     1.73902890e+02   # ~mu_R
   2000015     3.49519557e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -7.48159497e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.86477932e-01   # N_{1,1}
  1  2    -3.68445671e-02   # N_{1,2}
  1  3     1.44874491e-01   # N_{1,3}
  1  4    -6.71948597e-02   # N_{1,4}
  2  1     1.08698571e-01   # N_{2,1}
  2  2     8.68833221e-01   # N_{2,2}
  2  3    -3.82188900e-01   # N_{2,3}
  2  4     2.95372815e-01   # N_{2,4}
  3  1    -5.15899584e-02   # N_{3,1}
  3  2     7.26385039e-02   # N_{3,2}
  3  3     6.98903012e-01   # N_{3,3}
  3  4     7.09645478e-01   # N_{3,4}
  4  1    -1.11285158e-01   # N_{4,1}
  4  2     4.88359458e-01   # N_{4,2}
  4  3     5.86922147e-01   # N_{4,3}
  4  4    -6.36115592e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     8.32981608e-01   # U_{1,1}
  1  2    -5.53300679e-01   # U_{1,2}
  2  1     5.53300679e-01   # U_{2,1}
  2  2     8.32981608e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.03017206e-01   # V_{1,1}
  1  2    -4.29604382e-01   # V_{1,2}
  2  1     4.29604382e-01   # V_{2,1}
  2  2     9.03017206e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     2.57061908e-01   # F_{11}
  1  2     9.66394938e-01   # F_{12}
  2  1     9.66394938e-01   # F_{21}
  2  2    -2.57061908e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     4.42788753e-01   # F_{11}
  1  2     8.96625965e-01   # F_{12}
  2  1     8.96625965e-01   # F_{21}
  2  2    -4.42788753e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.11289657e-01   # F_{11}
  1  2     9.93788012e-01   # F_{12}
  2  1     9.93788012e-01   # F_{21}
  2  2    -1.11289657e-01   # F_{22}
Block gauge Q= 1.02185139e+03  # SM gauge couplings
     1     3.63129267e-01   # g'(Q)MSSM DRbar
     2     6.44415471e-01   # g(Q)MSSM DRbar
     3     1.06081884e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.02185139e+03  
  3  3     8.63330546e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.02185139e+03  
  3  3     2.03789071e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.02185139e+03  
  3  3     1.51367751e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.02185139e+03 # Higgs mixing parameters
     1     3.90555237e+02    # mu(Q)MSSM DRbar
     2     1.44940405e+01    # tan beta(Q)MSSM DRbar
     3     2.43552437e+02    # higgs vev(Q)MSSM DRbar
     4     2.82954999e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.02185139e+03  # MSSM DRbar SUSY breaking parameters
     1     1.67048198e+02      # M_1(Q)
     2     3.14478026e+02      # M_2(Q)
     3     8.56450436e+02      # M_3(Q)
    21     1.02513717e+05      # mH1^2(Q)
    22    -1.33072317e+05      # mH2^2(Q)
    31     3.42000030e+02      # meL(Q)
    32     3.41998503e+02      # mmuL(Q)
    33     3.41531777e+02      # mtauL(Q)
    34     1.63439855e+02      # meR(Q)
    35     1.63433402e+02      # mmuR(Q)
    36     1.61449607e+02      # mtauR(Q)
    41     1.09348705e+03      # mqL1(Q)
    42     1.09348546e+03      # mqL2(Q)
    43     1.05554867e+03      # mqL3(Q)
    44     1.04850303e+03      # muR(Q)
    45     1.04850190e+03      # mcR(Q)
    46     9.70918975e+02      # mtR(Q)
    47     1.04418618e+03      # mdR(Q)
    48     1.04418397e+03      # msR(Q)
    49     1.03988439e+03      # mbR(Q)
Block au Q= 1.02185139e+03  
  1  1    -2.62412579e+02      # Au(Q)MSSM DRbar
  2  2    -2.62412206e+02      # Ac(Q)MSSM DRbar
  3  3    -2.47132676e+02      # At(Q)MSSM DRbar
Block ad Q= 1.02185139e+03  
  1  1    -2.79380102e+02      # Ad(Q)MSSM DRbar
  2  2    -2.79379581e+02      # As(Q)MSSM DRbar
  3  3    -2.73626362e+02      # Ab(Q)MSSM DRbar
Block ae Q= 1.02185139e+03  
  1  1    -2.68496671e+01      # Ae(Q)MSSM DRbar
  2  2    -2.68494685e+01      # Amu(Q)MSSM DRbar
  3  3    -2.67888095e+01      # Atau(Q)MSSM DRbar
