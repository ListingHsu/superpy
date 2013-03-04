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
     1    1.60000000e+05   # lambda
     2    1.00000000e+14   # M_mess
     5    1.00000000e+00   # N5
     6    1.00000000e+00   # cgrav
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=4.25284056e-04
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.04574996e+01   # MW
        25     1.15799485e+02   # h0
        35     1.05792780e+03   # H0
        36     1.05788401e+03   # A0
        37     1.06113310e+03   # H+
   1000021     1.19552348e+03   # ~g
   1000022     2.13904422e+02   # ~neutralino(1)
   1000023     4.12101509e+02   # ~neutralino(2)
   1000024     4.12294931e+02   # ~chargino(1)
   1000025    -8.31824067e+02   # ~neutralino(3)
   1000035     8.38671665e+02   # ~neutralino(4)
   1000037     8.39238836e+02   # ~chargino(2)
   1000039     3.79200000e+00   # ~gravitino
   1000001     1.46944936e+03   # ~d_L
   1000002     1.46747387e+03   # ~u_L
   1000003     1.46944354e+03   # ~s_L
   1000004     1.46746804e+03   # ~c_L
   1000005     1.29911146e+03   # ~b_1
   1000006     1.03327510e+03   # ~t_1
   1000011     7.09632516e+02   # ~e_L
   1000012     7.04899821e+02   # ~nue_L
   1000013     7.09722100e+02   # ~mu_L
   1000014     7.04884751e+02   # ~numu_L
   1000015     4.66321294e+02   # ~stau_1
   1000016     6.99969874e+02   # ~nu_tau_L
   2000001     1.32104494e+03   # ~d_R
   2000002     1.34815816e+03   # ~u_R
   2000003     1.32103630e+03   # ~s_R
   2000004     1.34815389e+03   # ~c_R
   2000005     1.33062632e+03   # ~b_2
   2000006     1.34213222e+03   # ~t_2
   2000011     4.82487226e+02   # ~e_R
   2000013     4.82442856e+02   # ~mu_R
   2000015     7.05987543e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -7.00914644e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.98006927e-01   # N_{1,1}
  1  2    -8.99361786e-03   # N_{1,2}
  1  3     5.94228073e-02   # N_{1,3}
  1  4    -1.92410511e-02   # N_{1,4}
  2  1     1.77845558e-02   # N_{2,1}
  2  2     9.89399281e-01   # N_{2,2}
  2  3    -1.26703095e-01   # N_{2,3}
  2  4     6.86956881e-02   # N_{2,4}
  3  1    -2.79398915e-02   # N_{3,1}
  3  2     4.16091824e-02   # N_{3,2}
  3  3     7.04708860e-01   # N_{3,3}
  3  4     7.07724142e-01   # N_{3,4}
  4  1    -5.37144792e-02   # N_{4,1}
  4  2     1.38841107e-01   # N_{4,2}
  4  3     6.95557818e-01   # N_{4,3}
  4  4    -7.02877815e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.83876739e-01   # U_{1,1}
  1  2    -1.78847875e-01   # U_{1,2}
  2  1     1.78847875e-01   # U_{2,1}
  2  2     9.83876739e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.95214037e-01   # V_{1,1}
  1  2    -9.77190871e-02   # V_{1,2}
  2  1     9.77190871e-02   # V_{2,1}
  2  2     9.95214037e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     1.87120726e-01   # F_{11}
  1  2     9.82336925e-01   # F_{12}
  2  1     9.82336925e-01   # F_{21}
  2  2    -1.87120726e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     4.14020486e-01   # F_{11}
  1  2     9.10267563e-01   # F_{12}
  2  1     9.10267563e-01   # F_{21}
  2  2    -4.14020486e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     7.87956838e-02   # F_{11}
  1  2     9.96890787e-01   # F_{12}
  2  1     9.96890787e-01   # F_{21}
  2  2    -7.87956838e-02   # F_{22}
Block gauge Q= 1.14416330e+03  # SM gauge couplings
     1     3.62811903e-01   # g'(Q)MSSM DRbar
     2     6.41699586e-01   # g(Q)MSSM DRbar
     3     1.05131143e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.14416330e+03  
  3  3     8.54042323e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.14416330e+03  
  3  3     1.96985689e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.14416330e+03  
  3  3     1.50683754e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.14416330e+03 # Higgs mixing parameters
     1     8.25465449e+02    # mu(Q)MSSM DRbar
     2     1.44798145e+01    # tan beta(Q)MSSM DRbar
     3     2.43814816e+02    # higgs vev(Q)MSSM DRbar
     4     1.16817980e+06    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.14416330e+03  # MSSM DRbar SUSY breaking parameters
     1     2.17285830e+02      # M_1(Q)
     2     4.01987869e+02      # M_2(Q)
     3     1.09852224e+03      # M_3(Q)
    21     4.26550633e+05      # mH1^2(Q)
    22    -6.58293579e+05      # mH2^2(Q)
    31     7.05928729e+02      # meL(Q)
    32     7.05913677e+02      # mmuL(Q)
    33     7.01319903e+02      # mtauL(Q)
    34     4.77495131e+02      # meR(Q)
    35     4.77450326e+02      # mmuR(Q)
    36     4.63615608e+02      # mtauR(Q)
    41     1.43612172e+03      # mqL1(Q)
    42     1.43611575e+03      # mqL2(Q)
    43     1.29669861e+03      # mqL3(Q)
    44     1.31513292e+03      # muR(Q)
    45     1.31512851e+03      # mcR(Q)
    46     9.98594146e+02      # mtR(Q)
    47     1.28584193e+03      # mdR(Q)
    48     1.28583297e+03      # msR(Q)
    49     1.26949346e+03      # mbR(Q)
Block au Q= 1.14416330e+03  
  1  1    -1.01772965e+03      # Au(Q)MSSM DRbar
  2  2    -1.01772454e+03      # Ac(Q)MSSM DRbar
  3  3    -8.10573306e+02      # At(Q)MSSM DRbar
Block ad Q= 1.14416330e+03  
  1  1    -1.21487486e+03      # Ad(Q)MSSM DRbar
  2  2    -1.21486781e+03      # As(Q)MSSM DRbar
  3  3    -1.13689906e+03      # Ab(Q)MSSM DRbar
Block ae Q= 1.14416330e+03  
  1  1    -2.26811870e+02      # Ae(Q)MSSM DRbar
  2  2    -2.26804119e+02      # Amu(Q)MSSM DRbar
  3  3    -2.24444902e+02      # Atau(Q)MSSM DRbar
