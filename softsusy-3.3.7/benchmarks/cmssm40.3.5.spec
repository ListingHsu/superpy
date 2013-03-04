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
     1    1.20000000e+03   # m0
     2    4.50000000e+02   # m12
     5   -5.00000000e+02   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    2.09045829e+16   # MX scale
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=1.34548320e-04
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03915331e+01   # MW
        25     1.16887400e+02   # h0
        35     9.42538786e+02   # H0
        36     9.42645583e+02   # A0
        37     9.46221400e+02   # H+
   1000021     1.10074173e+03   # ~g
   1000022     1.88519288e+02   # ~neutralino(1)
   1000023     3.60117177e+02   # ~neutralino(2)
   1000024     3.60218038e+02   # ~chargino(1)
   1000025    -6.19912823e+02   # ~neutralino(3)
   1000035     6.30449680e+02   # ~neutralino(4)
   1000037     6.31229956e+02   # ~chargino(2)
   1000001     1.50616544e+03   # ~d_L
   1000002     1.50421238e+03   # ~u_L
   1000003     1.50611364e+03   # ~s_L
   1000004     1.50416052e+03   # ~c_L
   1000005     1.18335995e+03   # ~b_1
   1000006     9.83201144e+02   # ~t_1
   1000011     1.23339892e+03   # ~e_L
   1000012     1.23051471e+03   # ~nue_L
   1000013     1.23313712e+03   # ~mu_L
   1000014     1.23021237e+03   # ~numu_L
   1000015     9.95427608e+02   # ~stau_1
   1000016     1.13138240e+03   # ~nu_tau_L
   2000001     1.48465998e+03   # ~d_R
   2000002     1.48591140e+03   # ~u_R
   2000003     1.48456096e+03   # ~s_R
   2000004     1.48590464e+03   # ~c_R
   2000005     1.31117539e+03   # ~b_2
   2000006     1.21424754e+03   # ~t_2
   2000011     1.21108629e+03   # ~e_R
   2000013     1.21046948e+03   # ~mu_R
   2000015     1.13749496e+03   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -2.59230187e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.96171410e-01   # N_{1,1}
  1  2    -1.28146099e-02   # N_{1,2}
  1  3     8.20714383e-02   # N_{1,3}
  1  4    -2.72504396e-02   # N_{1,4}
  2  1     3.11399310e-02   # N_{2,1}
  2  2     9.75147648e-01   # N_{2,2}
  2  3    -1.88419018e-01   # N_{2,3}
  2  4     1.12319378e-01   # N_{2,4}
  3  1    -3.78253689e-02   # N_{3,1}
  3  2     5.54600558e-02   # N_{3,2}
  3  3     7.02896753e-01   # N_{3,3}
  3  4     7.08116924e-01   # N_{3,4}
  4  1    -7.24021259e-02   # N_{4,1}
  4  2     2.14119201e-01   # N_{4,2}
  4  3     6.80954262e-01   # N_{4,3}
  4  4    -6.96571743e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.63654406e-01   # U_{1,1}
  1  2    -2.67151991e-01   # U_{1,2}
  2  1     2.67151991e-01   # U_{2,1}
  2  2     9.63654406e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.86953448e-01   # V_{1,1}
  1  2    -1.61005875e-01   # V_{1,2}
  2  1     1.61005875e-01   # V_{2,1}
  2  2     9.86953448e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     2.95809780e-01   # F_{11}
  1  2     9.55246866e-01   # F_{12}
  2  1     9.55246866e-01   # F_{21}
  2  2    -2.95809780e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.83809747e-01   # F_{11}
  1  2     1.79216018e-01   # F_{12}
  2  1    -1.79216018e-01   # F_{21}
  2  2     9.83809747e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.51027227e-01   # F_{11}
  1  2     9.88529603e-01   # F_{12}
  2  1     9.88529603e-01   # F_{21}
  2  2    -1.51027227e-01   # F_{22}
Block gauge Q= 1.06740301e+03  # SM gauge couplings
     1     3.62257932e-01   # g'(Q)MSSM DRbar
     2     6.41715950e-01   # g(Q)MSSM DRbar
     3     1.05405672e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.06740301e+03  
  3  3     8.54177638e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.06740301e+03  
  3  3     5.16115920e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.06740301e+03  
  3  3     4.12816901e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.06740301e+03 # Higgs mixing parameters
     1     6.12049715e+02    # mu(Q)MSSM DRbar
     2     3.92072181e+01    # tan beta(Q)MSSM DRbar
     3     2.43613901e+02    # higgs vev(Q)MSSM DRbar
     4     1.06997550e+06    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.06740301e+03  # MSSM DRbar SUSY breaking parameters
     1     1.90402715e+02      # M_1(Q)
     2     3.52810293e+02      # M_2(Q)
     3     9.97151477e+02      # M_3(Q)
    21     5.37864302e+05      # mH1^2(Q)
    22    -3.57879823e+05      # mH2^2(Q)
    31     1.23047083e+03      # meL(Q)
    32     1.23016928e+03      # mmuL(Q)
    33     1.13384984e+03      # mtauL(Q)
    34     1.20893263e+03      # meR(Q)
    35     1.20831563e+03      # mmuR(Q)
    36     1.00067927e+03      # mtauR(Q)
    41     1.47876011e+03      # mqL1(Q)
    42     1.47870740e+03      # mqL2(Q)
    43     1.16478858e+03      # mqL3(Q)
    44     1.46163646e+03      # muR(Q)
    45     1.46162958e+03      # mcR(Q)
    46     9.68013101e+02      # mtR(Q)
    47     1.45972556e+03      # mdR(Q)
    48     1.45962464e+03      # msR(Q)
    49     1.28505730e+03      # mbR(Q)
Block au Q= 1.06740301e+03  
  1  1    -1.35324357e+03      # Au(Q)MSSM DRbar
  2  2    -1.35321002e+03      # Ac(Q)MSSM DRbar
  3  3    -9.19227615e+02      # At(Q)MSSM DRbar
Block ad Q= 1.06740301e+03  
  1  1    -1.56514838e+03      # Ad(Q)MSSM DRbar
  2  2    -1.56506298e+03      # As(Q)MSSM DRbar
  3  3    -1.29424458e+03      # Ab(Q)MSSM DRbar
Block ae Q= 1.06740301e+03  
  1  1    -5.92741842e+02      # Ae(Q)MSSM DRbar
  2  2    -5.92437207e+02      # Amu(Q)MSSM DRbar
  3  3    -4.97519393e+02      # Atau(Q)MSSM DRbar
