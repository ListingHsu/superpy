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
     1    1.05000000e+03   # m0
     2    3.75000000e+02   # m12
     5   -5.00000000e+02   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    2.21527037e+16   # MX scale
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=2.95410408e-04
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03927677e+01   # MW
        25     1.15874766e+02   # h0
        35     8.20787173e+02   # H0
        36     8.20912960e+02   # A0
        37     8.24992758e+02   # H+
   1000021     9.32886761e+02   # ~g
   1000022     1.55779542e+02   # ~neutralino(1)
   1000023     2.97728141e+02   # ~neutralino(2)
   1000024     2.97800905e+02   # ~chargino(1)
   1000025    -5.48130038e+02   # ~neutralino(3)
   1000035     5.58687518e+02   # ~neutralino(4)
   1000037     5.59699854e+02   # ~chargino(2)
   1000001     1.30091065e+03   # ~d_L
   1000002     1.29861781e+03   # ~u_L
   1000003     1.30086418e+03   # ~s_L
   1000004     1.29857125e+03   # ~c_L
   1000005     1.01223164e+03   # ~b_1
   1000006     8.34106663e+02   # ~t_1
   1000011     1.07654323e+03   # ~e_L
   1000012     1.07327740e+03   # ~nue_L
   1000013     1.07630257e+03   # ~mu_L
   1000014     1.07300653e+03   # ~numu_L
   1000015     8.66314888e+02   # ~stau_1
   1000016     9.85024324e+02   # ~nu_tau_L
   2000001     1.28362194e+03   # ~d_R
   2000002     1.28434712e+03   # ~u_R
   2000003     1.28353316e+03   # ~s_R
   2000004     1.28434109e+03   # ~c_R
   2000005     1.13034132e+03   # ~b_2
   2000006     1.04799879e+03   # ~t_2
   2000011     1.05896009e+03   # ~e_R
   2000013     1.05840882e+03   # ~mu_R
   2000015     9.92065193e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -2.60007175e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.95179533e-01   # N_{1,1}
  1  2    -1.63447973e-02   # N_{1,2}
  1  3     9.22868281e-02   # N_{1,3}
  1  4    -2.88736258e-02   # N_{1,4}
  2  1     3.77740750e-02   # N_{2,1}
  2  2     9.72625924e-01   # N_{2,2}
  2  3    -1.99995162e-01   # N_{2,3}
  2  4     1.12133252e-01   # N_{2,4}
  3  1    -4.34477224e-02   # N_{3,1}
  3  2     6.42699756e-02   # N_{3,2}
  3  3     7.01538269e-01   # N_{3,3}
  3  4     7.08396585e-01   # N_{3,4}
  4  1    -7.93921407e-02   # N_{4,1}
  4  2     2.22712886e-01   # N_{4,2}
  4  3     6.77738248e-01   # N_{4,3}
  4  4    -6.96251912e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.58894740e-01   # U_{1,1}
  1  2    -2.83762009e-01   # U_{1,2}
  2  1     2.83762009e-01   # U_{2,1}
  2  2     9.58894740e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.86960172e-01   # V_{1,1}
  1  2    -1.60964650e-01   # V_{1,2}
  2  1     1.60964650e-01   # V_{2,1}
  2  2     9.86960172e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.29869486e-01   # F_{11}
  1  2     9.44026547e-01   # F_{12}
  2  1     9.44026547e-01   # F_{21}
  2  2    -3.29869486e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.79574238e-01   # F_{11}
  1  2     2.01082851e-01   # F_{12}
  2  1    -2.01082851e-01   # F_{21}
  2  2     9.79574238e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.73670305e-01   # F_{11}
  1  2     9.84803851e-01   # F_{12}
  2  1     9.84803851e-01   # F_{21}
  2  2    -1.73670305e-01   # F_{22}
Block gauge Q= 9.12883651e+02  # SM gauge couplings
     1     3.61907561e-01   # g'(Q)MSSM DRbar
     2     6.42508641e-01   # g(Q)MSSM DRbar
     3     1.06238033e+00   # g3(Q)MSSM DRbar
Block yu Q= 9.12883651e+02  
  3  3     8.59694660e-01   # Yt(Q)MSSM DRbar
Block yd Q= 9.12883651e+02  
  3  3     5.18252397e-01   # Yb(Q)MSSM DRbar
Block ye Q= 9.12883651e+02  
  3  3     4.12541878e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 9.12883651e+02 # Higgs mixing parameters
     1     5.40229342e+02    # mu(Q)MSSM DRbar
     2     3.92445926e+01    # tan beta(Q)MSSM DRbar
     3     2.43808394e+02    # higgs vev(Q)MSSM DRbar
     4     8.12114976e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 9.12883651e+02  # MSSM DRbar SUSY breaking parameters
     1     1.57594178e+02      # M_1(Q)
     2     2.93241748e+02      # M_2(Q)
     3     8.41486149e+02      # M_3(Q)
    21     4.01148499e+05      # mH1^2(Q)
    22    -2.81381910e+05      # mH2^2(Q)
    31     1.07387017e+03      # meL(Q)
    32     1.07360015e+03      # mmuL(Q)
    33     9.87804184e+02      # mtauL(Q)
    34     1.05690280e+03      # meR(Q)
    35     1.05635127e+03      # mmuR(Q)
    36     8.71559314e+02      # mtauR(Q)
    41     1.27743191e+03      # mqL1(Q)
    42     1.27738466e+03      # mqL2(Q)
    43     9.97595167e+02      # mqL3(Q)
    44     1.26394027e+03      # muR(Q)
    45     1.26393414e+03      # mcR(Q)
    46     8.23578868e+02      # mtR(Q)
    47     1.26246407e+03      # mdR(Q)
    48     1.26237368e+03      # msR(Q)
    49     1.10698051e+03      # mbR(Q)
Block au Q= 9.12883651e+02  
  1  1    -1.19820824e+03      # Au(Q)MSSM DRbar
  2  2    -1.19817748e+03      # Ac(Q)MSSM DRbar
  3  3    -7.99680188e+02      # At(Q)MSSM DRbar
Block ad Q= 9.12883651e+02  
  1  1    -1.39277094e+03      # Ad(Q)MSSM DRbar
  2  2    -1.39269260e+03      # As(Q)MSSM DRbar
  3  3    -1.14449695e+03      # Ab(Q)MSSM DRbar
Block ae Q= 9.12883651e+02  
  1  1    -5.62915513e+02      # Ae(Q)MSSM DRbar
  2  2    -5.62620142e+02      # Amu(Q)MSSM DRbar
  3  3    -4.70902645e+02      # Atau(Q)MSSM DRbar
