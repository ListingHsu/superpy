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
     1    3.45000000e+02   # m0
     2    5.50000000e+02   # m12
     5   -5.00000000e+02   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    1.81416585e+16   # MX scale
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=3.01616167e-04
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03881985e+01   # MW
        25     1.17476592e+02   # h0
        35     6.59533158e+02   # H0
        36     6.59605169e+02   # A0
        37     6.64825025e+02   # H+
   1000021     1.25848101e+03   # ~g
   1000022     2.28687561e+02   # ~neutralino(1)
   1000023     4.35797830e+02   # ~neutralino(2)
   1000024     4.35934807e+02   # ~chargino(1)
   1000025    -7.56135191e+02   # ~neutralino(3)
   1000035     7.64032047e+02   # ~neutralino(4)
   1000037     7.64730921e+02   # ~chargino(2)
   1000001     1.19435024e+03   # ~d_L
   1000002     1.19182929e+03   # ~u_L
   1000003     1.19431535e+03   # ~s_L
   1000004     1.19179431e+03   # ~c_L
   1000005     9.98180119e+02   # ~b_1
   1000006     8.55853704e+02   # ~t_1
   1000011     5.06809126e+02   # ~e_L
   1000012     5.00312294e+02   # ~nue_L
   1000013     5.06851349e+02   # ~mu_L
   1000014     5.00173651e+02   # ~numu_L
   1000015     2.30313645e+02   # ~stau_1
   1000016     4.52845683e+02   # ~nu_tau_L
   2000001     1.14735927e+03   # ~d_R
   2000002     1.15105244e+03   # ~u_R
   2000003     1.14728993e+03   # ~s_R
   2000004     1.15104806e+03   # ~c_R
   2000005     1.06656793e+03   # ~b_2
   2000006     1.07150614e+03   # ~t_2
   2000011     4.04035775e+02   # ~e_R
   2000013     4.03687062e+02   # ~mu_R
   2000015     4.81540386e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -2.60819806e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.97491180e-01   # N_{1,1}
  1  2    -8.88995028e-03   # N_{1,2}
  1  3     6.66584108e-02   # N_{1,3}
  1  4    -2.21126935e-02   # N_{1,4}
  2  1     2.11097007e-02   # N_{2,1}
  2  2     9.83546258e-01   # N_{2,2}
  2  3    -1.54405731e-01   # N_{2,3}
  2  4     9.13783890e-02   # N_{2,4}
  3  1    -3.09625147e-02   # N_{3,1}
  3  2     4.54526942e-02   # N_{3,2}
  3  3     7.04210519e-01   # N_{3,3}
  3  4     7.07857980e-01   # N_{3,4}
  4  1    -6.00587161e-02   # N_{4,1}
  4  2     1.74618958e-01   # N_{4,2}
  4  3     6.89784801e-01   # N_{4,3}
  4  4    -7.00070067e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.75891168e-01   # U_{1,1}
  1  2    -2.18257711e-01   # U_{1,2}
  2  1     2.18257711e-01   # U_{2,1}
  2  2     9.75891168e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.91432311e-01   # V_{1,1}
  1  2    -1.30621489e-01   # V_{1,2}
  2  1     1.30621489e-01   # V_{2,1}
  2  2     9.91432311e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     4.53847214e-01   # F_{11}
  1  2     8.91079517e-01   # F_{12}
  2  1     8.91079517e-01   # F_{21}
  2  2    -4.53847214e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     8.11026918e-01   # F_{11}
  1  2     5.85008836e-01   # F_{12}
  2  1    -5.85008836e-01   # F_{21}
  2  2     8.11026918e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     3.36729954e-01   # F_{11}
  1  2     9.41601263e-01   # F_{12}
  2  1     9.41601263e-01   # F_{21}
  2  2    -3.36729954e-01   # F_{22}
Block gauge Q= 9.30283146e+02  # SM gauge couplings
     1     3.62334756e-01   # g'(Q)MSSM DRbar
     2     6.41903514e-01   # g(Q)MSSM DRbar
     3     1.05658599e+00   # g3(Q)MSSM DRbar
Block yu Q= 9.30283146e+02  
  3  3     8.53328765e-01   # Yt(Q)MSSM DRbar
Block yd Q= 9.30283146e+02  
  3  3     4.90781528e-01   # Yb(Q)MSSM DRbar
Block ye Q= 9.30283146e+02  
  3  3     4.27556682e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 9.30283146e+02 # Higgs mixing parameters
     1     7.52914122e+02    # mu(Q)MSSM DRbar
     2     3.92129057e+01    # tan beta(Q)MSSM DRbar
     3     2.43906889e+02    # higgs vev(Q)MSSM DRbar
     4     5.49773796e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 9.30283146e+02  # MSSM DRbar SUSY breaking parameters
     1     2.32390732e+02      # M_1(Q)
     2     4.30622366e+02      # M_2(Q)
     3     1.22104173e+03      # M_3(Q)
    21    -1.31850028e+05      # mH1^2(Q)
    22    -5.58192810e+05      # mH2^2(Q)
    31     5.00884132e+02      # meL(Q)
    32     5.00745142e+02      # mmuL(Q)
    33     4.56307250e+02      # mtauL(Q)
    34     3.99325513e+02      # meR(Q)
    35     3.98972712e+02      # mmuR(Q)
    36     2.69776324e+02      # mtauR(Q)
    41     1.15655967e+03      # mqL1(Q)
    42     1.15652406e+03      # mqL2(Q)
    43     9.94551414e+02      # mqL3(Q)
    44     1.11637489e+03      # muR(Q)
    45     1.11637044e+03      # mcR(Q)
    46     8.65778663e+02      # mtR(Q)
    47     1.11154479e+03      # mdR(Q)
    48     1.11147427e+03      # msR(Q)
    49     1.01177161e+03      # mbR(Q)
Block au Q= 9.30283146e+02  
  1  1    -1.58565468e+03      # Au(Q)MSSM DRbar
  2  2    -1.58561637e+03      # Ac(Q)MSSM DRbar
  3  3    -1.10090128e+03      # At(Q)MSSM DRbar
Block ad Q= 9.30283146e+02  
  1  1    -1.84004391e+03      # Ad(Q)MSSM DRbar
  2  2    -1.83994635e+03      # As(Q)MSSM DRbar
  3  3    -1.54946264e+03      # Ab(Q)MSSM DRbar
Block ae Q= 9.30283146e+02  
  1  1    -6.46011184e+02      # Ae(Q)MSSM DRbar
  2  2    -6.45690735e+02      # Amu(Q)MSSM DRbar
  3  3    -5.38524176e+02      # Atau(Q)MSSM DRbar
