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
     1    8.50000000e+02   # m0
     2    4.00000000e+02   # m12
     5    0.00000000e+00   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    2.21120041e+16   # MX scale
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=2.23836995e-04
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03976178e+01   # MW
        25     1.14022097e+02   # h0
        35     1.01399552e+03   # H0
        36     1.01394720e+03   # A0
        37     1.01720893e+03   # H+
   1000021     9.76358720e+02   # ~g
   1000022     1.63864561e+02   # ~neutralino(1)
   1000023     3.09431765e+02   # ~neutralino(2)
   1000024     3.09517650e+02   # ~chargino(1)
   1000025    -5.24849847e+02   # ~neutralino(3)
   1000035     5.41079884e+02   # ~neutralino(4)
   1000037     5.40967640e+02   # ~chargino(2)
   1000001     1.18772854e+03   # ~d_L
   1000002     1.18527037e+03   # ~u_L
   1000003     1.18772440e+03   # ~s_L
   1000004     1.18526622e+03   # ~c_L
   1000005     1.03079137e+03   # ~b_1
   1000006     8.22265438e+02   # ~t_1
   1000011     8.88821171e+02   # ~e_L
   1000012     8.85002739e+02   # ~nue_L
   1000013     8.88847473e+02   # ~mu_L
   1000014     8.84990550e+02   # ~numu_L
   1000015     8.54334900e+02   # ~stau_1
   1000016     8.81264470e+02   # ~nu_tau_L
   2000001     1.16508611e+03   # ~d_R
   2000002     1.16633155e+03   # ~u_R
   2000003     1.16508208e+03   # ~s_R
   2000004     1.16632709e+03   # ~c_R
   2000005     1.15726314e+03   # ~b_2
   2000006     1.05751744e+03   # ~t_2
   2000011     8.63017148e+02   # ~e_R
   2000013     8.62992039e+02   # ~mu_R
   2000015     8.86038987e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.05047306e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.93659135e-01   # N_{1,1}
  1  2    -2.54605256e-02   # N_{1,2}
  1  3     1.01462335e-01   # N_{1,3}
  1  4    -4.12150366e-02   # N_{1,4}
  2  1     5.41991880e-02   # N_{2,1}
  2  2     9.60331998e-01   # N_{2,2}
  2  3    -2.29099170e-01   # N_{2,3}
  2  4     1.49460604e-01   # N_{2,4}
  3  1    -4.07308828e-02   # N_{3,1}
  3  2     5.93883449e-02   # N_{3,2}
  3  3     7.01719327e-01   # N_{3,3}
  3  4     7.08804632e-01   # N_{3,4}
  4  1    -8.96937353e-02   # N_{4,1}
  4  2     2.71269681e-01   # N_{4,2}
  4  3     6.66939991e-01   # N_{4,3}
  4  4    -6.88156118e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.44806595e-01   # U_{1,1}
  1  2    -3.27628597e-01   # U_{1,2}
  2  1     3.27628597e-01   # U_{2,1}
  2  2     9.44806595e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.76539224e-01   # V_{1,1}
  1  2    -2.15339601e-01   # V_{1,2}
  2  1     2.15339601e-01   # V_{2,1}
  2  2     9.76539224e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     2.79638333e-01   # F_{11}
  1  2     9.60105412e-01   # F_{12}
  2  1     9.60105412e-01   # F_{21}
  2  2    -2.79638333e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.98599537e-01   # F_{11}
  1  2     5.29052403e-02   # F_{12}
  2  1    -5.29052403e-02   # F_{21}
  2  2     9.98599537e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.74458257e-01   # F_{11}
  1  2     9.84664571e-01   # F_{12}
  2  1     9.84664571e-01   # F_{21}
  2  2    -1.74458257e-01   # F_{22}
Block gauge Q= 9.06827995e+02  # SM gauge couplings
     1     3.62006510e-01   # g'(Q)MSSM DRbar
     2     6.42823043e-01   # g(Q)MSSM DRbar
     3     1.06242239e+00   # g3(Q)MSSM DRbar
Block yu Q= 9.06827995e+02  
  3  3     8.64664790e-01   # Yt(Q)MSSM DRbar
Block yd Q= 9.06827995e+02  
  3  3     1.36734180e-01   # Yb(Q)MSSM DRbar
Block ye Q= 9.06827995e+02  
  3  3     9.96770637e-02   # Ytau(Q)MSSM DRbar
Block hmix Q= 9.06827995e+02 # Higgs mixing parameters
     1     5.17374229e+02    # mu(Q)MSSM DRbar
     2     9.66569940e+00    # tan beta(Q)MSSM DRbar
     3     2.43891254e+02    # higgs vev(Q)MSSM DRbar
     4     1.04982020e+06    # mA^2(Q)MSSM DRbar
Block msoft Q= 9.06827995e+02  # MSSM DRbar SUSY breaking parameters
     1     1.66999419e+02      # M_1(Q)
     2     3.10475327e+02      # M_2(Q)
     3     8.94171850e+02      # M_3(Q)
    21     7.50481811e+05      # mH1^2(Q)
    22    -2.46326284e+05      # mH2^2(Q)
    31     8.86101185e+02      # meL(Q)
    32     8.86089034e+02      # mmuL(Q)
    33     8.82478979e+02      # mtauL(Q)
    34     8.60818560e+02      # meR(Q)
    35     8.60793422e+02      # mmuR(Q)
    36     8.53306690e+02      # mtauR(Q)
    41     1.16032503e+03      # mqL1(Q)
    42     1.16032077e+03      # mqL2(Q)
    43     1.00685826e+03      # mqL3(Q)
    44     1.14176967e+03      # muR(Q)
    45     1.14176508e+03      # mcR(Q)
    46     8.03810595e+02      # mtR(Q)
    47     1.13962036e+03      # mdR(Q)
    48     1.13961621e+03      # msR(Q)
    49     1.13161885e+03      # mbR(Q)
Block au Q= 9.06827995e+02  
  1  1    -9.16500877e+02      # Au(Q)MSSM DRbar
  2  2    -9.16496766e+02      # Ac(Q)MSSM DRbar
  3  3    -7.04979973e+02      # At(Q)MSSM DRbar
Block ad Q= 9.06827995e+02  
  1  1    -1.12355697e+03      # Ad(Q)MSSM DRbar
  2  2    -1.12355316e+03      # As(Q)MSSM DRbar
  3  3    -1.04923410e+03      # Ab(Q)MSSM DRbar
Block ae Q= 9.06827995e+02  
  1  1    -2.40111373e+02      # Ae(Q)MSSM DRbar
  2  2    -2.40107043e+02      # Amu(Q)MSSM DRbar
  3  3    -2.38822989e+02      # Atau(Q)MSSM DRbar
