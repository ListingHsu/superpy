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
     1    2.50000000e+02   # m0
     2    6.00000000e+02   # m12
     5    0.00000000e+00   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    1.79615537e+16   # MX scale
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=6.80601001e-04
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03937261e+01   # MW
        25     1.16114670e+02   # h0
        35     8.71243798e+02   # H0
        36     8.70999802e+02   # A0
        37     8.74972869e+02   # H+
   1000021     1.35967004e+03   # ~g
   1000022     2.48137468e+02   # ~neutralino(1)
   1000023     4.69489593e+02   # ~neutralino(2)
   1000024     4.69720953e+02   # ~chargino(1)
   1000025    -7.45765680e+02   # ~neutralino(3)
   1000035     7.58203595e+02   # ~neutralino(4)
   1000037     7.58082635e+02   # ~chargino(2)
   1000001     1.26232047e+03   # ~d_L
   1000002     1.25999031e+03   # ~u_L
   1000003     1.26231735e+03   # ~s_L
   1000004     1.25998719e+03   # ~c_L
   1000005     1.15376682e+03   # ~b_1
   1000006     9.66353754e+02   # ~t_1
   1000011     4.75449790e+02   # ~e_L
   1000012     4.68673876e+02   # ~nue_L
   1000013     4.75566875e+02   # ~mu_L
   1000014     4.68669139e+02   # ~numu_L
   1000015     3.32175559e+02   # ~stau_1
   1000016     4.67066916e+02   # ~nu_tau_L
   2000001     1.20943672e+03   # ~d_R
   2000002     1.21380692e+03   # ~u_R
   2000003     1.20943348e+03   # ~s_R
   2000004     1.21380357e+03   # ~c_R
   2000005     1.20460236e+03   # ~b_2
   2000006     1.19226492e+03   # ~t_2
   2000011     3.38923982e+02   # ~e_R
   2000013     3.38910676e+02   # ~mu_R
   2000015     4.75551858e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.05842864e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.96958068e-01   # N_{1,1}
  1  2    -1.26834007e-02   # N_{1,2}
  1  3     7.07624621e-02   # N_{1,3}
  1  4    -3.01067560e-02   # N_{1,4}
  2  1     2.87254027e-02   # N_{2,1}
  2  2     9.76043332e-01   # N_{2,2}
  2  3    -1.77864489e-01   # N_{2,3}
  2  4     1.21977411e-01   # N_{2,4}
  3  1    -2.81052718e-02   # N_{3,1}
  3  2     4.07287024e-02   # N_{3,2}
  3  3     7.04490898e-01   # N_{3,3}
  3  4     7.07985763e-01   # N_{3,4}
  4  1    -6.67799101e-02   # N_{4,1}
  4  2     2.13353505e-01   # N_{4,2}
  4  3     6.83410178e-01   # N_{4,3}
  4  4    -6.94961333e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.67754445e-01   # U_{1,1}
  1  2    -2.51895483e-01   # U_{1,2}
  2  1     2.51895483e-01   # U_{2,1}
  2  2     9.67754445e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.84790902e-01   # V_{1,1}
  1  2    -1.73743717e-01   # V_{1,2}
  2  1     1.73743717e-01   # V_{2,1}
  2  2     9.84790902e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.76443637e-01   # F_{11}
  1  2     9.26439522e-01   # F_{12}
  2  1     9.26439522e-01   # F_{21}
  2  2    -3.76443637e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.84681850e-01   # F_{11}
  1  2     1.74360700e-01   # F_{12}
  2  1    -1.74360700e-01   # F_{21}
  2  2     9.84681850e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.17700686e-01   # F_{11}
  1  2     9.93049117e-01   # F_{12}
  2  1     9.93049117e-01   # F_{21}
  2  2    -1.17700686e-01   # F_{22}
Block gauge Q= 1.04161607e+03  # SM gauge couplings
     1     3.62710212e-01   # g'(Q)MSSM DRbar
     2     6.41985276e-01   # g(Q)MSSM DRbar
     3     1.05179174e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.04161607e+03  
  3  3     8.55318382e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.04161607e+03  
  3  3     1.34168676e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.04161607e+03  
  3  3     1.00383031e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.04161607e+03 # Higgs mixing parameters
     1     7.40250122e+02    # mu(Q)MSSM DRbar
     2     9.65267393e+00    # tan beta(Q)MSSM DRbar
     3     2.43903350e+02    # higgs vev(Q)MSSM DRbar
     4     7.85385604e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.04161607e+03  # MSSM DRbar SUSY breaking parameters
     1     2.53205810e+02      # M_1(Q)
     2     4.67951439e+02      # M_2(Q)
     3     1.31890933e+03      # M_3(Q)
    21     1.95209670e+05      # mH1^2(Q)
    22    -5.27304898e+05      # mH2^2(Q)
    31     4.68056374e+02      # meL(Q)
    32     4.68051619e+02      # mmuL(Q)
    33     4.66614208e+02      # mtauL(Q)
    34     3.32676461e+02      # meR(Q)
    35     3.32662895e+02      # mmuR(Q)
    36     3.28542660e+02      # mtauR(Q)
    41     1.21953599e+03      # mqL1(Q)
    42     1.21953281e+03      # mqL2(Q)
    43     1.12140489e+03      # mqL3(Q)
    44     1.17421162e+03      # muR(Q)
    45     1.17420822e+03      # mcR(Q)
    46     9.60720860e+02      # mtR(Q)
    47     1.16868657e+03      # mdR(Q)
    48     1.16868327e+03      # msR(Q)
    49     1.16264938e+03      # mbR(Q)
Block au Q= 1.04161607e+03  
  1  1    -1.34255331e+03      # Au(Q)MSSM DRbar
  2  2    -1.34254733e+03      # Ac(Q)MSSM DRbar
  3  3    -1.03867598e+03      # At(Q)MSSM DRbar
Block ad Q= 1.04161607e+03  
  1  1    -1.63919998e+03      # Ad(Q)MSSM DRbar
  2  2    -1.63919445e+03      # As(Q)MSSM DRbar
  3  3    -1.53253284e+03      # Ab(Q)MSSM DRbar
Block ae Q= 1.04161607e+03  
  1  1    -3.56275253e+02      # Ae(Q)MSSM DRbar
  2  2    -3.56268922e+02      # Amu(Q)MSSM DRbar
  3  3    -3.54356329e+02      # Atau(Q)MSSM DRbar
