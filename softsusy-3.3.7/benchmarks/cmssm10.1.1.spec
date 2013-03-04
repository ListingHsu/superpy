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
     1    1.25000000e+02   # m0
     2    5.00000000e+02   # m12
     5    0.00000000e+00   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    1.87396773e+16   # MX scale
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=7.01391589e-04
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03966431e+01   # MW
        25     1.14893669e+02   # h0
        35     7.18021206e+02   # H0
        36     7.17744029e+02   # A0
        37     7.22473672e+02   # H+
   1000021     1.14697666e+03   # ~g
   1000022     2.04229901e+02   # ~neutralino(1)
   1000023     3.85953136e+02   # ~neutralino(2)
   1000024     3.86142985e+02   # ~chargino(1)
   1000025    -6.35418474e+02   # ~neutralino(3)
   1000035     6.49082290e+02   # ~neutralino(4)
   1000037     6.48999128e+02   # ~chargino(2)
   1000001     1.05533075e+03   # ~d_L
   1000002     1.05250353e+03   # ~u_L
   1000003     1.05532818e+03   # ~s_L
   1000004     1.05250095e+03   # ~c_L
   1000005     9.65907902e+02   # ~b_1
   1000006     8.04556691e+02   # ~t_1
   1000011     3.61713811e+02   # ~e_L
   1000012     3.52829761e+02   # ~nue_L
   1000013     3.61797789e+02   # ~mu_L
   1000014     3.52826414e+02   # ~numu_L
   1000015     2.22718161e+02   # ~stau_1
   1000016     3.51659284e+02   # ~nu_tau_L
   2000001     1.01074966e+03   # ~d_R
   2000002     1.01406921e+03   # ~u_R
   2000003     1.01074696e+03   # ~s_R
   2000004     1.01406646e+03   # ~c_R
   2000005     1.00749814e+03   # ~b_2
   2000006     1.01149401e+03   # ~t_2
   2000011     2.29854756e+02   # ~e_R
   2000013     2.29844322e+02   # ~mu_R
   2000015     3.62852217e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.06795864e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.95805826e-01   # N_{1,1}
  1  2    -1.74963325e-02   # N_{1,2}
  1  3     8.29381154e-02   # N_{1,3}
  1  4    -3.44369490e-02   # N_{1,4}
  2  1     3.81464443e-02   # N_{2,1}
  2  2     9.70403543e-01   # N_{2,2}
  2  3    -1.98321575e-01   # N_{2,3}
  2  4     1.32402283e-01   # N_{2,4}
  3  1    -3.32414884e-02   # N_{3,1}
  3  2     4.84244377e-02   # N_{3,2}
  3  3     7.03438564e-01   # N_{3,3}
  3  4     7.08324970e-01   # N_{3,4}
  4  1    -7.62273463e-02   # N_{4,1}
  4  2     2.35936252e-01   # N_{4,2}
  4  3     6.77468824e-01   # N_{4,3}
  4  4    -6.92502324e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.59631049e-01   # U_{1,1}
  1  2    -2.81261887e-01   # U_{1,2}
  2  1     2.81261887e-01   # U_{2,1}
  2  2     9.59631049e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.82004580e-01   # V_{1,1}
  1  2    -1.88857102e-01   # V_{1,2}
  2  1     1.88857102e-01   # V_{2,1}
  2  2     9.82004580e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     4.26569122e-01   # F_{11}
  1  2     9.04454965e-01   # F_{12}
  2  1     9.04454965e-01   # F_{21}
  2  2    -4.26569122e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.75342868e-01   # F_{11}
  1  2     2.20695016e-01   # F_{12}
  2  1    -2.20695016e-01   # F_{21}
  2  2     9.75342868e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.41999885e-01   # F_{11}
  1  2     9.89866674e-01   # F_{12}
  2  1     9.89866674e-01   # F_{21}
  2  2    -1.41999885e-01   # F_{22}
Block gauge Q= 8.74650624e+02  # SM gauge couplings
     1     3.62418839e-01   # g'(Q)MSSM DRbar
     2     6.43002742e-01   # g(Q)MSSM DRbar
     3     1.06092721e+00   # g3(Q)MSSM DRbar
Block yu Q= 8.74650624e+02  
  3  3     8.61186162e-01   # Yt(Q)MSSM DRbar
Block yd Q= 8.74650624e+02  
  3  3     1.35323736e-01   # Yb(Q)MSSM DRbar
Block ye Q= 8.74650624e+02  
  3  3     1.00512853e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 8.74650624e+02 # Higgs mixing parameters
     1     6.29931032e+02    # mu(Q)MSSM DRbar
     2     9.67352198e+00    # tan beta(Q)MSSM DRbar
     3     2.44115789e+02    # higgs vev(Q)MSSM DRbar
     4     5.34459643e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 8.74650624e+02  # MSSM DRbar SUSY breaking parameters
     1     2.09311210e+02      # M_1(Q)
     2     3.88509052e+02      # M_2(Q)
     3     1.11339799e+03      # M_3(Q)
    21     1.09119264e+05      # mH1^2(Q)
    22    -3.84358939e+05      # mH2^2(Q)
    31     3.54224747e+02      # meL(Q)
    32     3.54221414e+02      # mmuL(Q)
    33     3.53216500e+02      # mtauL(Q)
    34     2.22002004e+02      # meR(Q)
    35     2.21991188e+02      # mmuR(Q)
    36     2.18709574e+02      # mtauR(Q)
    41     1.01835257e+03      # mqL1(Q)
    42     1.01834995e+03      # mqL2(Q)
    43     9.38585025e+02      # mqL3(Q)
    44     9.80337377e+02      # muR(Q)
    45     9.80334587e+02      # mcR(Q)
    46     8.07037836e+02      # mtR(Q)
    47     9.75738702e+02      # mdR(Q)
    48     9.75735961e+02      # msR(Q)
    49     9.70731132e+02      # mbR(Q)
Block au Q= 8.74650624e+02  
  1  1    -1.14073236e+03      # Au(Q)MSSM DRbar
  2  2    -1.14072724e+03      # Ac(Q)MSSM DRbar
  3  3    -8.80142942e+02      # At(Q)MSSM DRbar
Block ad Q= 8.74650624e+02  
  1  1    -1.39566876e+03      # Ad(Q)MSSM DRbar
  2  2    -1.39566401e+03      # As(Q)MSSM DRbar
  3  3    -1.30417545e+03      # Ab(Q)MSSM DRbar
Block ae Q= 8.74650624e+02  
  1  1    -2.99342376e+02      # Ae(Q)MSSM DRbar
  2  2    -2.99336999e+02      # Amu(Q)MSSM DRbar
  3  3    -2.97715789e+02      # Atau(Q)MSSM DRbar
