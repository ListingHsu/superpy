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
     2    7.00000000e+02   # m12
     5    0.00000000e+00   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    1.71152472e+16   # MX scale
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=1.85241292e-04
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03931119e+01   # MW
        25     1.17071102e+02   # h0
        35     1.00595593e+03   # H0
        36     1.00574848e+03   # A0
        37     1.00918476e+03   # H+
   1000021     1.56851465e+03   # ~g
   1000022     2.91962508e+02   # ~neutralino(1)
   1000023     5.52361579e+02   # ~neutralino(2)
   1000024     5.52613419e+02   # ~chargino(1)
   1000025    -8.53577891e+02   # ~neutralino(3)
   1000035     8.65067283e+02   # ~neutralino(4)
   1000037     8.64929942e+02   # ~chargino(2)
   1000001     1.45584080e+03   # ~d_L
   1000002     1.45384487e+03   # ~u_L
   1000003     1.45583721e+03   # ~s_L
   1000004     1.45384128e+03   # ~c_L
   1000005     1.33124114e+03   # ~b_1
   1000006     1.12000395e+03   # ~t_1
   1000011     5.57312837e+02   # ~e_L
   1000012     5.51506101e+02   # ~nue_L
   1000013     5.57427565e+02   # ~mu_L
   1000014     5.51500568e+02   # ~numu_L
   1000015     3.93493472e+02   # ~stau_1
   1000016     5.49631792e+02   # ~nu_tau_L
   2000001     1.39391542e+03   # ~d_R
   2000002     1.39934651e+03   # ~u_R
   2000003     1.39391170e+03   # ~s_R
   2000004     1.39934265e+03   # ~c_R
   2000005     1.38794338e+03   # ~b_2
   2000006     1.36510138e+03   # ~t_2
   2000011     4.00523965e+02   # ~e_R
   2000013     4.00508498e+02   # ~mu_R
   2000015     5.56860667e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.05391169e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.97666854e-01   # N_{1,1}
  1  2    -9.68415090e-03   # N_{1,2}
  1  3     6.19937842e-02   # N_{1,3}
  1  4    -2.69042124e-02   # N_{1,4}
  2  1     2.26515671e-02   # N_{2,1}
  2  2     9.79943175e-01   # N_{2,2}
  2  3    -1.62154528e-01   # N_{2,3}
  2  4     1.13596607e-01   # N_{2,4}
  3  1    -2.43881405e-02   # N_{3,1}
  3  2     3.51990795e-02   # N_{3,2}
  3  3     7.05139028e-01   # N_{3,3}
  3  4     7.07774819e-01   # N_{3,4}
  4  1    -5.96068269e-02   # N_{4,1}
  4  2     1.95904609e-01   # N_{4,2}
  4  3     6.87489368e-01   # N_{4,3}
  4  4    -6.96725757e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.73347795e-01   # U_{1,1}
  1  2    -2.29333970e-01   # U_{1,2}
  2  1     2.29333970e-01   # U_{2,1}
  2  2     9.73347795e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.86867019e-01   # V_{1,1}
  1  2    -1.61534784e-01   # V_{1,2}
  2  1     1.61534784e-01   # V_{2,1}
  2  2     9.86867019e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.39667470e-01   # F_{11}
  1  2     9.40545592e-01   # F_{12}
  2  1     9.40545592e-01   # F_{21}
  2  2    -3.39667470e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.88135978e-01   # F_{11}
  1  2     1.53581542e-01   # F_{12}
  2  1    -1.53581542e-01   # F_{21}
  2  2     9.88135978e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.00314516e-01   # F_{11}
  1  2     9.94955777e-01   # F_{12}
  2  1     9.94955777e-01   # F_{21}
  2  2    -1.00314516e-01   # F_{22}
Block gauge Q= 1.20066580e+03  # SM gauge couplings
     1     3.63001687e-01   # g'(Q)MSSM DRbar
     2     6.41211670e-01   # g(Q)MSSM DRbar
     3     1.04447278e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.20066580e+03  
  3  3     8.50555266e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.20066580e+03  
  3  3     1.33209164e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.20066580e+03  
  3  3     1.00278014e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.20066580e+03 # Higgs mixing parameters
     1     8.47926941e+02    # mu(Q)MSSM DRbar
     2     9.63615582e+00    # tan beta(Q)MSSM DRbar
     3     2.43743149e+02    # higgs vev(Q)MSSM DRbar
     4     1.04646432e+06    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.20066580e+03  # MSSM DRbar SUSY breaking parameters
     1     2.97414585e+02      # M_1(Q)
     2     5.47621053e+02      # M_2(Q)
     3     1.52241155e+03      # M_3(Q)
    21     2.70176782e+05      # mH1^2(Q)
    22    -6.89511701e+05      # mH2^2(Q)
    31     5.49280247e+02      # meL(Q)
    32     5.49274679e+02      # mmuL(Q)
    33     5.47589018e+02      # mtauL(Q)
    34     3.94207646e+02      # meR(Q)
    35     3.94191920e+02      # mmuR(Q)
    36     3.89408350e+02      # mtauR(Q)
    41     1.40738371e+03      # mqL1(Q)
    42     1.40738005e+03      # mqL2(Q)
    43     1.29431146e+03      # mqL3(Q)
    44     1.35417939e+03      # muR(Q)
    45     1.35417547e+03      # mcR(Q)
    46     1.10797445e+03      # mtR(Q)
    47     1.34764610e+03      # mdR(Q)
    48     1.34764231e+03      # msR(Q)
    49     1.34073995e+03      # mbR(Q)
Block au Q= 1.20066580e+03  
  1  1    -1.54129767e+03      # Au(Q)MSSM DRbar
  2  2    -1.54129085e+03      # Ac(Q)MSSM DRbar
  3  3    -1.19522579e+03      # At(Q)MSSM DRbar
Block ad Q= 1.20066580e+03  
  1  1    -1.87853358e+03      # Ad(Q)MSSM DRbar
  2  2    -1.87852728e+03      # As(Q)MSSM DRbar
  3  3    -1.75708108e+03      # Ab(Q)MSSM DRbar
Block ae Q= 1.20066580e+03  
  1  1    -4.12754859e+02      # Ae(Q)MSSM DRbar
  2  2    -4.12747592e+02      # Amu(Q)MSSM DRbar
  3  3    -4.10548712e+02      # Atau(Q)MSSM DRbar
