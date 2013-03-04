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
     1    3.50000000e+02   # m0
     2    5.25000000e+02   # m12
     5    0.00000000e+00   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    1.91141605e+16   # MX scale
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=4.94341340e-04
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.04571881e+01   # MW
        25     1.15297037e+02   # h0
        35     8.15772818e+02   # H0
        36     8.15462180e+02   # A0
        37     8.19750191e+02   # H+
   1000021     1.20846456e+03   # ~g
   1000022     2.16019189e+02   # ~neutralino(1)
   1000023     4.08493036e+02   # ~neutralino(2)
   1000024     4.08694721e+02   # ~chargino(1)
   1000025    -6.63271427e+02   # ~neutralino(3)
   1000035     6.76700470e+02   # ~neutralino(4)
   1000037     6.76595477e+02   # ~chargino(2)
   1000001     1.14866613e+03   # ~d_L
   1000002     1.14609352e+03   # ~u_L
   1000003     1.14866315e+03   # ~s_L
   1000004     1.14609053e+03   # ~c_L
   1000005     1.04370308e+03   # ~b_1
   1000006     8.66907236e+02   # ~t_1
   1000011     4.97800793e+02   # ~e_L
   1000012     4.91291094e+02   # ~nue_L
   1000013     4.97981585e+02   # ~mu_L
   1000014     4.91285484e+02   # ~numu_L
   1000015     3.96932216e+02   # ~stau_1
   1000016     4.89468556e+02   # ~nu_tau_L
   2000001     1.10428660e+03   # ~d_R
   2000002     1.10771873e+03   # ~u_R
   2000003     1.10428352e+03   # ~s_R
   2000004     1.10771554e+03   # ~c_R
   2000005     1.09955648e+03   # ~b_2
   2000006     1.08349623e+03   # ~t_2
   2000011     4.03404123e+02   # ~e_R
   2000013     4.03390271e+02   # ~mu_R
   2000015     4.97650163e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.06063534e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.96136154e-01   # N_{1,1}
  1  2    -1.60404794e-02   # N_{1,2}
  1  3     7.96377214e-02   # N_{1,3}
  1  4    -3.33661385e-02   # N_{1,4}
  2  1     3.54768621e-02   # N_{2,1}
  2  2     9.71771412e-01   # N_{2,2}
  2  3    -1.93399804e-01   # N_{2,3}
  2  4     1.30377265e-01   # N_{2,4}
  3  1    -3.17974362e-02   # N_{3,1}
  3  2     4.62049088e-02   # N_{3,2}
  3  3     7.03764044e-01   # N_{3,3}
  3  4     7.08216210e-01   # N_{3,4}
  4  1    -7.37772197e-02   # N_{4,1}
  4  2     2.30798901e-01   # N_{4,2}
  4  3     6.78948098e-01   # N_{4,3}
  4  4    -6.93049976e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.61540355e-01   # U_{1,1}
  1  2    -2.74663697e-01   # U_{1,2}
  2  1     2.74663697e-01   # U_{2,1}
  2  2     9.61540355e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.82480027e-01   # V_{1,1}
  1  2    -1.86367908e-01   # V_{1,2}
  2  1     1.86367908e-01   # V_{2,1}
  2  2     9.82480027e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.89108912e-01   # F_{11}
  1  2     9.21191758e-01   # F_{12}
  2  1     9.21191758e-01   # F_{21}
  2  2    -3.89108912e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.87742392e-01   # F_{11}
  1  2     1.56092816e-01   # F_{12}
  2  1    -1.56092816e-01   # F_{21}
  2  2     9.87742392e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.34535831e-01   # F_{11}
  1  2     9.90908730e-01   # F_{12}
  2  1     9.90908730e-01   # F_{21}
  2  2    -1.34535831e-01   # F_{22}
Block gauge Q= 9.39845658e+02  # SM gauge couplings
     1     3.62393450e-01   # g'(Q)MSSM DRbar
     2     6.42444869e-01   # g(Q)MSSM DRbar
     3     1.05746408e+00   # g3(Q)MSSM DRbar
Block yu Q= 9.39845658e+02  
  3  3     8.59243108e-01   # Yt(Q)MSSM DRbar
Block yd Q= 9.39845658e+02  
  3  3     1.35031401e-01   # Yb(Q)MSSM DRbar
Block ye Q= 9.39845658e+02  
  3  3     1.00371047e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 9.39845658e+02 # Higgs mixing parameters
     1     6.57545842e+02    # mu(Q)MSSM DRbar
     2     9.66452430e+00    # tan beta(Q)MSSM DRbar
     3     2.44010916e+02    # higgs vev(Q)MSSM DRbar
     4     6.87272318e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 9.39845658e+02  # MSSM DRbar SUSY breaking parameters
     1     2.20334848e+02      # M_1(Q)
     2     4.08455326e+02      # M_2(Q)
     3     1.16409354e+03      # M_3(Q)
    21     2.20889335e+05      # mH1^2(Q)
    22    -4.15907021e+05      # mH2^2(Q)
    31     4.92122540e+02      # meL(Q)
    32     4.92116920e+02      # mmuL(Q)
    33     4.90422564e+02      # mtauL(Q)
    34     3.98916134e+02      # meR(Q)
    35     3.98902130e+02      # mmuR(Q)
    36     3.94663730e+02      # mtauR(Q)
    41     1.11001636e+03      # mqL1(Q)
    42     1.11001332e+03      # mqL2(Q)
    43     1.01395581e+03      # mqL3(Q)
    44     1.07208819e+03      # muR(Q)
    45     1.07208493e+03      # mcR(Q)
    46     8.63041234e+02      # mtR(Q)
    47     1.06750563e+03      # mdR(Q)
    48     1.06750249e+03      # msR(Q)
    49     1.06172331e+03      # mbR(Q)
Block au Q= 9.39845658e+02  
  1  1    -1.18990784e+03      # Au(Q)MSSM DRbar
  2  2    -1.18990252e+03      # Ac(Q)MSSM DRbar
  3  3    -9.18640667e+02      # At(Q)MSSM DRbar
Block ad Q= 9.39845658e+02  
  1  1    -1.45509103e+03      # Ad(Q)MSSM DRbar
  2  2    -1.45508609e+03      # As(Q)MSSM DRbar
  3  3    -1.35984779e+03      # Ab(Q)MSSM DRbar
Block ae Q= 9.39845658e+02  
  1  1    -3.13489995e+02      # Ae(Q)MSSM DRbar
  2  2    -3.13484381e+02      # Amu(Q)MSSM DRbar
  3  3    -3.11793479e+02      # Atau(Q)MSSM DRbar
