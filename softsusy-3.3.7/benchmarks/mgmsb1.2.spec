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
     1    4.00000000e+04   # lambda
     2    8.00000000e+04   # M_mess
     5    3.00000000e+00   # N5
     6    1.00000000e+00   # cgrav
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=1.81804165e-04
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.04695598e+01   # MW
        25     1.11156203e+02   # h0
        35     3.85974677e+02   # H0
        36     3.85671873e+02   # A0
        37     3.94229710e+02   # H+
   1000021     9.46336970e+02   # ~g
   1000022     1.62904934e+02   # ~neutralino(1)
   1000023     2.68727674e+02   # ~neutralino(2)
   1000024     2.65839386e+02   # ~chargino(1)
   1000025    -3.15489457e+02   # ~neutralino(3)
   1000035     3.86455372e+02   # ~neutralino(4)
   1000037     3.85497366e+02   # ~chargino(2)
   1000039     7.58400000e-10   # ~gravitino
   1000001     9.02040695e+02   # ~d_L
   1000002     8.98665089e+02   # ~u_L
   1000003     9.02039559e+02   # ~s_L
   1000004     8.98663948e+02   # ~c_L
   1000005     8.58302900e+02   # ~b_1
   1000006     8.05238952e+02   # ~t_1
   1000011     2.62628415e+02   # ~e_L
   1000012     2.50042185e+02   # ~nue_L
   1000013     2.62667769e+02   # ~mu_L
   1000014     2.50041090e+02   # ~numu_L
   1000015     1.24155427e+02   # ~stau_1
   1000016     2.49541941e+02   # ~nu_tau_L
   2000001     8.66763508e+02   # ~d_R
   2000002     8.68146353e+02   # ~u_R
   2000003     8.66761920e+02   # ~s_R
   2000004     8.68145546e+02   # ~c_R
   2000005     8.73453633e+02   # ~b_2
   2000006     8.90065646e+02   # ~t_2
   2000011     1.30911408e+02   # ~e_R
   2000013     1.30907156e+02   # ~mu_R
   2000015     2.64558783e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -7.89254738e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.64836808e-01   # N_{1,1}
  1  2    -6.51946657e-02   # N_{1,2}
  1  3     2.20714203e-01   # N_{1,3}
  1  4    -1.26983582e-01   # N_{1,4}
  2  1    -2.33281773e-01   # N_{2,1}
  2  2    -6.35492963e-01   # N_{2,2}
  2  3     5.51892041e-01   # N_{2,3}
  2  4    -4.86973803e-01   # N_{2,4}
  3  1    -6.00557457e-02   # N_{3,1}
  3  2     8.12389975e-02   # N_{3,2}
  3  3     6.95697876e-01   # N_{3,3}
  3  4     7.11194768e-01   # N_{3,4}
  4  1    -1.05180112e-01   # N_{4,1}
  4  2     7.65048087e-01   # N_{4,2}
  4  3     4.03366931e-01   # N_{4,3}
  4  4    -4.90849965e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1    -5.69243639e-01   # U_{1,1}
  1  2     8.22168887e-01   # U_{1,2}
  2  1    -8.22168887e-01   # U_{2,1}
  2  2    -5.69243639e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1    -6.92148889e-01   # V_{1,1}
  1  2     7.21754747e-01   # V_{1,2}
  2  1    -7.21754747e-01   # V_{2,1}
  2  2    -6.92148889e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.62157923e-01   # F_{11}
  1  2     9.32116752e-01   # F_{12}
  2  1     9.32116752e-01   # F_{21}
  2  2    -3.62157923e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     5.67257403e-01   # F_{11}
  1  2     8.23540551e-01   # F_{12}
  2  1     8.23540551e-01   # F_{21}
  2  2    -5.67257403e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.52522251e-01   # F_{11}
  1  2     9.88300037e-01   # F_{12}
  2  1     9.88300037e-01   # F_{21}
  2  2    -1.52522251e-01   # F_{22}
Block gauge Q= 8.20581196e+02  # SM gauge couplings
     1     3.62666891e-01   # g'(Q)MSSM DRbar
     2     6.45004397e-01   # g(Q)MSSM DRbar
     3     1.06791220e+00   # g3(Q)MSSM DRbar
Block yu Q= 8.20581196e+02  
  3  3     8.68560018e-01   # Yt(Q)MSSM DRbar
Block yd Q= 8.20581196e+02  
  3  3     2.06185696e-01   # Yb(Q)MSSM DRbar
Block ye Q= 8.20581196e+02  
  3  3     1.52070808e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 8.20581196e+02 # Higgs mixing parameters
     1     3.06436941e+02    # mu(Q)MSSM DRbar
     2     1.45355795e+01    # tan beta(Q)MSSM DRbar
     3     2.43933402e+02    # higgs vev(Q)MSSM DRbar
     4     1.70024025e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 8.20581196e+02  # MSSM DRbar SUSY breaking parameters
     1     1.73051727e+02      # M_1(Q)
     2     3.27209524e+02      # M_2(Q)
     3     9.01439207e+02      # M_3(Q)
    21     5.57181571e+04      # mH1^2(Q)
    22    -8.42716076e+04      # mH2^2(Q)
    31     2.53766053e+02      # meL(Q)
    32     2.53764976e+02      # mmuL(Q)
    33     2.53434395e+02      # mtauL(Q)
    34     1.18738813e+02      # meR(Q)
    35     1.18734136e+02      # mmuR(Q)
    36     1.17290218e+02      # mtauR(Q)
    41     8.66825401e+02      # mqL1(Q)
    42     8.66824230e+02      # mqL2(Q)
    43     8.39039585e+02      # mqL3(Q)
    44     8.36112518e+02      # muR(Q)
    45     8.36111691e+02      # mcR(Q)
    46     7.79723342e+02      # mtR(Q)
    47     8.33362036e+02      # mdR(Q)
    48     8.33360407e+02      # msR(Q)
    49     8.30180958e+02      # mbR(Q)
Block au Q= 8.20581196e+02  
  1  1    -2.73805107e+02      # Au(Q)MSSM DRbar
  2  2    -2.73804719e+02      # Ac(Q)MSSM DRbar
  3  3    -2.57997000e+02      # At(Q)MSSM DRbar
Block ad Q= 8.20581196e+02  
  1  1    -2.91456156e+02      # Ad(Q)MSSM DRbar
  2  2    -2.91455613e+02      # As(Q)MSSM DRbar
  3  3    -2.85494517e+02      # Ab(Q)MSSM DRbar
Block ae Q= 8.20581196e+02  
  1  1    -2.73029401e+01      # Ae(Q)MSSM DRbar
  2  2    -2.73027408e+01      # Amu(Q)MSSM DRbar
  3  3    -2.72416075e+01      # Atau(Q)MSSM DRbar
