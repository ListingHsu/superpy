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
     1    4.00000000e+02   # m0
     2    6.00000000e+02   # m12
     5    0.00000000e+00   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    1.83963727e+16   # MX scale
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=9.67415822e-04
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03921123e+01   # MW
        25     1.16164799e+02   # h0
        35     9.23391223e+02   # H0
        36     9.23093376e+02   # A0
        37     9.26925345e+02   # H+
   1000021     1.36694290e+03   # ~g
   1000022     2.48750906e+02   # ~neutralino(1)
   1000023     4.70782305e+02   # ~neutralino(2)
   1000024     4.71011984e+02   # ~chargino(1)
   1000025    -7.45459031e+02   # ~neutralino(3)
   1000035     7.57997300e+02   # ~neutralino(4)
   1000037     7.57868047e+02   # ~chargino(2)
   1000001     1.29915312e+03   # ~d_L
   1000002     1.29689992e+03   # ~u_L
   1000003     1.29914976e+03   # ~s_L
   1000004     1.29689655e+03   # ~c_L
   1000005     1.18100364e+03   # ~b_1
   1000006     9.85373606e+02   # ~t_1
   1000011     5.67737489e+02   # ~e_L
   1000012     5.62007554e+02   # ~nue_L
   1000013     5.67918624e+02   # ~mu_L
   1000014     5.62001206e+02   # ~numu_L
   1000015     4.53535688e+02   # ~stau_1
   1000016     5.59939537e+02   # ~nu_tau_L
   2000001     1.24828086e+03   # ~d_R
   2000002     1.25249781e+03   # ~u_R
   2000003     1.24827740e+03   # ~s_R
   2000004     1.25249420e+03   # ~c_R
   2000005     1.24263716e+03   # ~b_2
   2000006     1.21673310e+03   # ~t_2
   2000011     4.60313018e+02   # ~e_R
   2000013     4.60297308e+02   # ~mu_R
   2000015     5.67105548e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.05593559e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.96944618e-01   # N_{1,1}
  1  2    -1.26813736e-02   # N_{1,2}
  1  3     7.09027197e-02   # N_{1,3}
  1  4    -3.02227623e-02   # N_{1,4}
  2  1     2.88347912e-02   # N_{2,1}
  2  2     9.75812438e-01   # N_{2,2}
  2  3    -1.78593513e-01   # N_{2,3}
  2  4     1.22731404e-01   # N_{2,4}
  3  1    -2.81228963e-02   # N_{3,1}
  3  2     4.07223645e-02   # N_{3,2}
  3  3     7.04494268e-01   # N_{3,3}
  3  4     7.07982075e-01   # N_{3,4}
  4  1    -6.69259723e-02   # N_{4,1}
  4  2     2.14408389e-01   # N_{4,2}
  4  3     6.83202011e-01   # N_{4,3}
  4  4    -6.94827294e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.67409286e-01   # U_{1,1}
  1  2    -2.53217838e-01   # U_{1,2}
  2  1     2.53217838e-01   # U_{2,1}
  2  2     9.67409286e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.84552629e-01   # V_{1,1}
  1  2    -1.75088894e-01   # V_{1,2}
  2  1     1.75088894e-01   # V_{2,1}
  2  2     9.84552629e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.57621899e-01   # F_{11}
  1  2     9.33866467e-01   # F_{12}
  2  1     9.33866467e-01   # F_{21}
  2  2    -3.57621899e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.90228090e-01   # F_{11}
  1  2     1.39457268e-01   # F_{12}
  2  1    -1.39457268e-01   # F_{21}
  2  2     9.90228090e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.17315261e-01   # F_{11}
  1  2     9.93094723e-01   # F_{12}
  2  1     9.93094723e-01   # F_{21}
  2  2    -1.17315261e-01   # F_{22}
Block gauge Q= 1.06246987e+03  # SM gauge couplings
     1     3.62644101e-01   # g'(Q)MSSM DRbar
     2     6.41806378e-01   # g(Q)MSSM DRbar
     3     1.05103136e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.06246987e+03  
  3  3     8.55072876e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.06246987e+03  
  3  3     1.34186097e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.06246987e+03  
  3  3     1.00283858e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.06246987e+03 # Higgs mixing parameters
     1     7.39711399e+02    # mu(Q)MSSM DRbar
     2     9.65002365e+00    # tan beta(Q)MSSM DRbar
     3     2.43859510e+02    # higgs vev(Q)MSSM DRbar
     4     8.80133563e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.06246987e+03  # MSSM DRbar SUSY breaking parameters
     1     2.53258813e+02      # M_1(Q)
     2     4.68032327e+02      # M_2(Q)
     3     1.31811091e+03      # M_3(Q)
    21     2.88440421e+05      # mH1^2(Q)
    22    -5.24417232e+05      # mH2^2(Q)
    31     5.61693762e+02      # meL(Q)
    32     5.61687390e+02      # mmuL(Q)
    33     5.59763540e+02      # mtauL(Q)
    34     4.55808347e+02      # meR(Q)
    35     4.55792485e+02      # mmuR(Q)
    36     4.50985506e+02      # mtauR(Q)
    41     1.25617366e+03      # mqL1(Q)
    42     1.25617023e+03      # mqL2(Q)
    43     1.14774717e+03      # mqL3(Q)
    44     1.21255131e+03      # muR(Q)
    45     1.21254763e+03      # mcR(Q)
    46     9.76438710e+02      # mtR(Q)
    47     1.20724768e+03      # mdR(Q)
    48     1.20724415e+03      # msR(Q)
    49     1.20075700e+03      # mbR(Q)
Block au Q= 1.06246987e+03  
  1  1    -1.34113115e+03      # Au(Q)MSSM DRbar
  2  2    -1.34112518e+03      # Ac(Q)MSSM DRbar
  3  3    -1.03746183e+03      # At(Q)MSSM DRbar
Block ad Q= 1.06246987e+03  
  1  1    -1.63753505e+03      # Ad(Q)MSSM DRbar
  2  2    -1.63752953e+03      # As(Q)MSSM DRbar
  3  3    -1.53093540e+03      # Ab(Q)MSSM DRbar
Block ae Q= 1.06246987e+03  
  1  1    -3.56191858e+02      # Ae(Q)MSSM DRbar
  2  2    -3.56185529e+02      # Amu(Q)MSSM DRbar
  3  3    -3.54276639e+02      # Atau(Q)MSSM DRbar
