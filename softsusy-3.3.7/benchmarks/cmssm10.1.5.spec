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
     1    1.75000000e+02   # m0
     2    7.00000000e+02   # m12
     5    0.00000000e+00   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    1.67765664e+16   # MX scale
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=9.05002699e-04
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03929544e+01   # MW
        25     1.17043269e+02   # h0
        35     9.77209929e+02   # H0
        36     9.77001283e+02   # A0
        37     9.80514453e+02   # H+
   1000021     1.56472849e+03   # ~g
   1000022     2.91378062e+02   # ~neutralino(1)
   1000023     5.51267201e+02   # ~neutralino(2)
   1000024     5.51519130e+02   # ~chargino(1)
   1000025    -8.53798165e+02   # ~neutralino(3)
   1000035     8.65247323e+02   # ~neutralino(4)
   1000037     8.65112710e+02   # ~chargino(2)
   1000001     1.43571881e+03   # ~d_L
   1000002     1.43369075e+03   # ~u_L
   1000003     1.43571535e+03   # ~s_L
   1000004     1.43368729e+03   # ~c_L
   1000005     1.31633984e+03   # ~b_1
   1000006     1.10970552e+03   # ~t_1
   1000011     5.01753262e+02   # ~e_L
   1000012     4.95321878e+02   # ~nue_L
   1000013     5.01814350e+02   # ~mu_L
   1000014     4.95317350e+02   # ~numu_L
   1000015     3.11189682e+02   # ~stau_1
   1000016     4.93734684e+02   # ~nu_tau_L
   2000001     1.37265553e+03   # ~d_R
   2000002     1.37816729e+03   # ~u_R
   2000003     1.37265193e+03   # ~s_R
   2000004     1.37816357e+03   # ~c_R
   2000005     1.36714277e+03   # ~b_2
   2000006     1.35153304e+03   # ~t_2
   2000011     3.18457493e+02   # ~e_R
   2000013     3.18443201e+02   # ~mu_R
   2000015     5.01750203e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.05491965e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.97675617e-01   # N_{1,1}
  1  2    -9.67123214e-03   # N_{1,2}
  1  3     6.18915162e-02   # N_{1,3}
  1  4    -2.68192321e-02   # N_{1,4}
  2  1     2.25767114e-02   # N_{2,1}
  2  2     9.80061509e-01   # N_{2,2}
  2  3    -1.61743177e-01   # N_{2,3}
  2  4     1.13176306e-01   # N_{2,4}
  3  1    -2.43762975e-02   # N_{3,1}
  3  2     3.51999949e-02   # N_{3,2}
  3  3     7.05138219e-01   # N_{3,3}
  3  4     7.07775988e-01   # N_{3,4}
  4  1    -5.94932933e-02   # N_{4,1}
  4  2     1.95312230e-01   # N_{4,2}
  4  3     6.87596304e-01   # N_{4,3}
  4  4    -6.96796242e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.73573915e-01   # U_{1,1}
  1  2    -2.28372136e-01   # U_{1,2}
  2  1     2.28372136e-01   # U_{2,1}
  2  2     9.73573915e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.87024634e-01   # V_{1,1}
  1  2    -1.60568903e-01   # V_{1,2}
  2  1     1.60568903e-01   # V_{2,1}
  2  2     9.87024634e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.48683693e-01   # F_{11}
  1  2     9.37240461e-01   # F_{12}
  2  1     9.37240461e-01   # F_{21}
  2  2    -3.48683693e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.84754274e-01   # F_{11}
  1  2     1.73951202e-01   # F_{12}
  2  1    -1.73951202e-01   # F_{21}
  2  2     9.84754274e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.00640982e-01   # F_{11}
  1  2     9.94922807e-01   # F_{12}
  2  1     9.94922807e-01   # F_{21}
  2  2    -1.00640982e-01   # F_{22}
Block gauge Q= 1.18926791e+03  # SM gauge couplings
     1     3.63062082e-01   # g'(Q)MSSM DRbar
     2     6.41313346e-01   # g(Q)MSSM DRbar
     3     1.04483104e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.18926791e+03  
  3  3     8.50685761e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.18926791e+03  
  3  3     1.33203911e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.18926791e+03  
  3  3     1.00299224e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.18926791e+03 # Higgs mixing parameters
     1     8.48276903e+02    # mu(Q)MSSM DRbar
     2     9.63740247e+00    # tan beta(Q)MSSM DRbar
     3     2.43759756e+02    # higgs vev(Q)MSSM DRbar
     4     9.88746286e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.18926791e+03  # MSSM DRbar SUSY breaking parameters
     1     2.97403512e+02      # M_1(Q)
     2     5.47598869e+02      # M_2(Q)
     3     1.52267391e+03      # M_3(Q)
    21     2.13362147e+05      # mH1^2(Q)
    22    -6.91394371e+05      # mH2^2(Q)
    31     4.92906737e+02      # meL(Q)
    32     4.92902193e+02      # mmuL(Q)
    33     4.91526867e+02      # mtauL(Q)
    34     3.10275959e+02      # meR(Q)
    35     3.10261275e+02      # mmuR(Q)
    36     3.05790272e+02      # mtauR(Q)
    41     1.38743382e+03      # mqL1(Q)
    42     1.38743030e+03      # mqL2(Q)
    43     1.27995629e+03      # mqL3(Q)
    44     1.33326014e+03      # muR(Q)
    45     1.33325637e+03      # mcR(Q)
    46     1.09932161e+03      # mtR(Q)
    47     1.32659873e+03      # mdR(Q)
    48     1.32659507e+03      # msR(Q)
    49     1.31993959e+03      # mbR(Q)
Block au Q= 1.18926791e+03  
  1  1    -1.54179197e+03      # Au(Q)MSSM DRbar
  2  2    -1.54178515e+03      # Ac(Q)MSSM DRbar
  3  3    -1.19569408e+03      # At(Q)MSSM DRbar
Block ad Q= 1.18926791e+03  
  1  1    -1.87907282e+03      # Ad(Q)MSSM DRbar
  2  2    -1.87906652e+03      # As(Q)MSSM DRbar
  3  3    -1.75761427e+03      # Ab(Q)MSSM DRbar
Block ae Q= 1.18926791e+03  
  1  1    -4.12749457e+02      # Ae(Q)MSSM DRbar
  2  2    -4.12742191e+02      # Amu(Q)MSSM DRbar
  3  3    -4.10543107e+02      # Atau(Q)MSSM DRbar
