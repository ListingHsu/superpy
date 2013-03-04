# SOFTSUSY3.3.7 SLHA compliant output
# B.C. Allanach, Comput. Phys. Commun. 143 (2002) 305-331, hep-ph/0104145
Block SPINFO          # Program information
     1    SOFTSUSY    # spectrum calculator
     2    3.3.7       # version number
Block MODSEL  # Select model
     1    3   # amsb
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
     1    4.50000000e+02   # m0
     2    6.00000000e+04   # m3/2
Block EXTPAR               # scale of SUSY breaking BCs
     0    2.28734986e+16   # MX scale
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=8.04797052e-04
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.04537154e+01   # MW
        25     1.15407674e+02   # h0
        35     1.06451458e+03   # H0
        36     1.06435183e+03   # A0
        37     1.06767061e+03   # H+
   1000021    -1.28226926e+03   # ~g
   1000022     1.97394373e+02   # ~neutralino(1)
   1000023     5.49108427e+02   # ~neutralino(2)
   1000024     1.97579701e+02   # ~chargino(1)
   1000025    -1.02067809e+03   # ~neutralino(3)
   1000035     1.02659802e+03   # ~neutralino(4)
   1000037     1.02552419e+03   # ~chargino(2)
   1000039     6.00000000e+04   # ~gravitino
   1000001     1.27601474e+03   # ~d_L
   1000002     1.27372298e+03   # ~u_L
   1000003     1.27600701e+03   # ~s_L
   1000004     1.27371523e+03   # ~c_L
   1000005     1.10806503e+03   # ~b_1
   1000006     9.26031220e+02   # ~t_1
   1000011     3.87377839e+02   # ~e_L
   1000012     3.79018954e+02   # ~nue_L
   1000013     3.87368256e+02   # ~mu_L
   1000014     3.79001758e+02   # ~numu_L
   1000015     3.48476083e+02   # ~stau_1
   1000016     3.73715592e+02   # ~nu_tau_L
   2000001     1.28948830e+03   # ~d_R
   2000002     1.27993010e+03   # ~u_R
   2000003     1.28948002e+03   # ~s_R
   2000004     1.27992300e+03   # ~c_R
   2000005     1.27226226e+03   # ~b_2
   2000006     1.14254049e+03   # ~t_2
   2000011     3.74872873e+02   # ~e_R
   2000013     3.74837970e+02   # ~mu_R
   2000015     3.96427948e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.05614294e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1    -3.76942165e-03   # N_{1,1}
  1  2     9.96454444e-01   # N_{1,2}
  1  3    -8.08611084e-02   # N_{1,3}
  1  4     2.29306460e-02   # N_{1,4}
  2  1     9.97183274e-01   # N_{2,1}
  2  2     9.81495020e-03   # N_{2,2}
  2  3     6.34878362e-02   # N_{2,3}
  2  4    -3.87101919e-02   # N_{2,4}
  3  1    -1.78552199e-02   # N_{3,1}
  3  2     4.08988660e-02   # N_{3,2}
  3  3     7.05428416e-01   # N_{3,3}
  3  4     7.07374882e-01   # N_{3,4}
  4  1    -7.27495714e-02   # N_{4,1}
  4  2     7.28662572e-02   # N_{4,2}
  4  3     7.01285623e-01   # N_{4,3}
  4  4    -7.05405191e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.93632011e-01   # U_{1,1}
  1  2    -1.12673985e-01   # U_{1,2}
  2  1     1.12673985e-01   # U_{2,1}
  2  2     9.93632011e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.99478194e-01   # V_{1,1}
  1  2    -3.23007572e-02   # V_{1,2}
  2  1     3.23007572e-02   # V_{2,1}
  2  2     9.99478194e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1    -3.61114801e-01   # F_{11}
  1  2     9.32521367e-01   # F_{12}
  2  1     9.32521367e-01   # F_{21}
  2  2     3.61114801e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.98793215e-01   # F_{11}
  1  2     4.91132823e-02   # F_{12}
  2  1    -4.91132823e-02   # F_{21}
  2  2     9.98793215e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     5.57638927e-01   # F_{11}
  1  2     8.30083627e-01   # F_{12}
  2  1     8.30083627e-01   # F_{21}
  2  2    -5.57638927e-01   # F_{22}
Block gauge Q= 9.91554848e+02  # SM gauge couplings
     1     3.62523578e-01   # g'(Q)MSSM DRbar
     2     6.44050008e-01   # g(Q)MSSM DRbar
     3     1.05399637e+00   # g3(Q)MSSM DRbar
Block yu Q= 9.91554848e+02  
  3  3     8.57781036e-01   # Yt(Q)MSSM DRbar
Block yd Q= 9.91554848e+02  
  3  3     1.47582782e-01   # Yb(Q)MSSM DRbar
Block ye Q= 9.91554848e+02  
  3  3     9.92460387e-02   # Ytau(Q)MSSM DRbar
Block hmix Q= 9.91554848e+02 # Higgs mixing parameters
     1     1.02018037e+03    # mu(Q)MSSM DRbar
     2     9.65972384e+00    # tan beta(Q)MSSM DRbar
     3     2.44242748e+02    # higgs vev(Q)MSSM DRbar
     4     1.13326354e+06    # mA^2(Q)MSSM DRbar
Block msoft Q= 9.91554848e+02  # MSSM DRbar SUSY breaking parameters
     1     5.59620229e+02      # M_1(Q)
     2     1.90401849e+02      # M_2(Q)
     3    -1.22154541e+03      # M_3(Q)
    21     7.36676884e+04      # mH1^2(Q)
    22    -1.01735895e+06      # mH2^2(Q)
    31     3.83173889e+02      # meL(Q)
    32     3.83156875e+02      # mmuL(Q)
    33     3.78150742e+02      # mtauL(Q)
    34     3.67221544e+02      # meR(Q)
    35     3.67186021e+02      # mmuR(Q)
    36     3.56651108e+02      # mtauR(Q)
    41     1.23783962e+03      # mqL1(Q)
    42     1.23783164e+03      # mqL2(Q)
    43     1.07286184e+03      # mqL3(Q)
    44     1.24507738e+03      # muR(Q)
    45     1.24507006e+03      # mcR(Q)
    46     9.07657599e+02      # mtR(Q)
    47     1.25424875e+03      # mdR(Q)
    48     1.25424019e+03      # msR(Q)
    49     1.23650630e+03      # mbR(Q)
Block au Q= 9.91554848e+02  
  1  1     1.92807614e+03      # Au(Q)MSSM DRbar
  2  2     1.92805986e+03      # Ac(Q)MSSM DRbar
  3  3     1.09355328e+03      # At(Q)MSSM DRbar
Block ad Q= 9.91554848e+02  
  1  1     2.72562071e+03      # Ad(Q)MSSM DRbar
  2  2     2.72560566e+03      # As(Q)MSSM DRbar
  3  3     2.42738475e+03      # Ab(Q)MSSM DRbar
Block ae Q= 9.91554848e+02  
  1  1     5.88141421e+02      # Ae(Q)MSSM DRbar
  2  2     5.88103490e+02      # Amu(Q)MSSM DRbar
  3  3     5.76893187e+02      # Atau(Q)MSSM DRbar
