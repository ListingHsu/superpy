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
     1    7.50000000e+02   # m0
     2    6.50000000e+02   # m12
     5   -5.00000000e+02   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    1.79841596e+16   # MX scale
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=6.74164766e-05
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03886558e+01   # MW
        25     1.18446748e+02   # h0
        35     8.65263452e+02   # H0
        36     8.65257178e+02   # A0
        37     8.69282384e+02   # H+
   1000021     1.49024548e+03   # ~g
   1000022     2.73950407e+02   # ~neutralino(1)
   1000023     5.21375732e+02   # ~neutralino(2)
   1000024     5.21525151e+02   # ~chargino(1)
   1000025    -8.51061080e+02   # ~neutralino(3)
   1000035     8.59249419e+02   # ~neutralino(4)
   1000037     8.59795616e+02   # ~chargino(2)
   1000001     1.52211944e+03   # ~d_L
   1000002     1.52020945e+03   # ~u_L
   1000003     1.52207588e+03   # ~s_L
   1000004     1.52016583e+03   # ~c_L
   1000005     1.27052214e+03   # ~b_1
   1000006     1.08717122e+03   # ~t_1
   1000011     8.65165591e+02   # ~e_L
   1000012     8.61213812e+02   # ~nue_L
   1000013     8.65104580e+02   # ~mu_L
   1000014     8.61006467e+02   # ~numu_L
   1000015     6.09231564e+02   # ~stau_1
   1000016     7.89892948e+02   # ~nu_tau_L
   2000001     1.47304545e+03   # ~d_R
   2000002     1.47720317e+03   # ~u_R
   2000003     1.47295979e+03   # ~s_R
   2000004     1.47719757e+03   # ~c_R
   2000005     1.34752779e+03   # ~b_2
   2000006     1.31986730e+03   # ~t_2
   2000011     7.88645460e+02   # ~e_R
   2000013     7.88188383e+02   # ~mu_R
   2000015     8.03946731e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -2.59197957e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.97966675e-01   # N_{1,1}
  1  2    -7.00760103e-03   # N_{1,2}
  1  3     5.98014239e-02   # N_{1,3}
  1  4    -2.09092876e-02   # N_{1,4}
  2  1     1.75996552e-02   # N_{2,1}
  2  2     9.84843416e-01   # N_{2,2}
  2  3    -1.46322303e-01   # N_{2,3}
  2  4     9.14520694e-02   # N_{2,4}
  3  1    -2.71357533e-02   # N_{3,1}
  3  2     3.95012156e-02   # N_{3,2}
  3  3     7.04907070e-01   # N_{3,3}
  3  4     7.07678831e-01   # N_{3,4}
  4  1    -5.49219273e-02   # N_{4,1}
  4  2     1.68742386e-01   # N_{4,2}
  4  3     6.91461927e-01   # N_{4,3}
  4  4    -7.00278511e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.78329791e-01   # U_{1,1}
  1  2    -2.07052697e-01   # U_{1,2}
  2  1     2.07052697e-01   # U_{2,1}
  2  2     9.78329791e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.91405969e-01   # V_{1,1}
  1  2    -1.30821273e-01   # V_{1,2}
  2  1     1.30821273e-01   # V_{2,1}
  2  2     9.91405969e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.67725719e-01   # F_{11}
  1  2     9.29934296e-01   # F_{12}
  2  1     9.29934296e-01   # F_{21}
  2  2    -3.67725719e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.11530876e-01   # F_{11}
  1  2     4.11231640e-01   # F_{12}
  2  1    -4.11231640e-01   # F_{21}
  2  2     9.11530876e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     2.37496686e-01   # F_{11}
  1  2     9.71388349e-01   # F_{12}
  2  1     9.71388349e-01   # F_{21}
  2  2    -2.37496686e-01   # F_{22}
Block gauge Q= 1.16442975e+03  # SM gauge couplings
     1     3.62625128e-01   # g'(Q)MSSM DRbar
     2     6.40749696e-01   # g(Q)MSSM DRbar
     3     1.04601386e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.16442975e+03  
  3  3     8.46875145e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.16442975e+03  
  3  3     4.95572814e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.16442975e+03  
  3  3     4.23703372e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.16442975e+03 # Higgs mixing parameters
     1     8.46594647e+02    # mu(Q)MSSM DRbar
     2     3.91663648e+01    # tan beta(Q)MSSM DRbar
     3     2.43680724e+02    # higgs vev(Q)MSSM DRbar
     4     9.57085455e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.16442975e+03  # MSSM DRbar SUSY breaking parameters
     1     2.77018757e+02      # M_1(Q)
     2     5.10792908e+02      # M_2(Q)
     3     1.42163427e+03      # M_3(Q)
    21     4.46715318e+04      # mH1^2(Q)
    22    -6.99014166e+05      # mH2^2(Q)
    31     8.60786144e+02      # meL(Q)
    32     8.60578627e+02      # mmuL(Q)
    33     7.91994004e+02      # mtauL(Q)
    34     7.85602243e+02      # meR(Q)
    35     7.85143878e+02      # mmuR(Q)
    36     6.22390993e+02      # mtauR(Q)
    41     1.47887335e+03      # mqL1(Q)
    42     1.47882831e+03      # mqL2(Q)
    43     1.25025026e+03      # mqL3(Q)
    44     1.43647390e+03      # muR(Q)
    45     1.43646812e+03      # mcR(Q)
    46     1.07896195e+03      # mtR(Q)
    47     1.43137580e+03      # mdR(Q)
    48     1.43128747e+03      # msR(Q)
    49     1.29697115e+03      # mbR(Q)
Block au Q= 1.16442975e+03  
  1  1    -1.78111471e+03      # Au(Q)MSSM DRbar
  2  2    -1.78107305e+03      # Ac(Q)MSSM DRbar
  3  3    -1.25135893e+03      # At(Q)MSSM DRbar
Block ad Q= 1.16442975e+03  
  1  1    -2.05354077e+03      # Ad(Q)MSSM DRbar
  2  2    -2.05343470e+03      # As(Q)MSSM DRbar
  3  3    -1.73150746e+03      # Ab(Q)MSSM DRbar
Block ae Q= 1.16442975e+03  
  1  1    -6.82747121e+02      # Ae(Q)MSSM DRbar
  2  2    -6.82414659e+02      # Amu(Q)MSSM DRbar
  3  3    -5.72893590e+02      # Atau(Q)MSSM DRbar
