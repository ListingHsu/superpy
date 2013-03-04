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
     1    7.50000000e+02   # m0
     2    3.50000000e+02   # m12
     5    0.00000000e+00   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    2.31243123e+16   # MX scale
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=3.17862541e-04
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03988642e+01   # MW
        25     1.13057828e+02   # h0
        35     8.96428928e+02   # H0
        36     8.96376078e+02   # A0
        37     9.00039674e+02   # H+
   1000021     8.63753959e+02   # ~g
   1000022     1.41996913e+02   # ~neutralino(1)
   1000023     2.67295527e+02   # ~neutralino(2)
   1000024     2.67305606e+02   # ~chargino(1)
   1000025    -4.69576617e+02   # ~neutralino(3)
   1000035     4.86708317e+02   # ~neutralino(4)
   1000037     4.86673496e+02   # ~chargino(2)
   1000001     1.04976889e+03   # ~d_L
   1000002     1.04696181e+03   # ~u_L
   1000003     1.04976522e+03   # ~s_L
   1000004     1.04695813e+03   # ~c_L
   1000005     9.10476379e+02   # ~b_1
   1000006     7.24391764e+02   # ~t_1
   1000011     7.84035276e+02   # ~e_L
   1000012     7.79738936e+02   # ~nue_L
   1000013     7.84055564e+02   # ~mu_L
   1000014     7.79728103e+02   # ~numu_L
   1000015     7.53606689e+02   # ~stau_1
   1000016     7.76422347e+02   # ~nu_tau_L
   2000001     1.02993736e+03   # ~d_R
   2000002     1.03078761e+03   # ~u_R
   2000003     1.02993378e+03   # ~s_R
   2000004     1.03078366e+03   # ~c_R
   2000005     1.02306229e+03   # ~b_2
   2000006     9.40655498e+02   # ~t_2
   2000011     7.61569027e+02   # ~e_R
   2000013     7.61546746e+02   # ~mu_R
   2000015     7.81830356e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.05405485e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.91945666e-01   # N_{1,1}
  1  2    -3.20294226e-02   # N_{1,2}
  1  3     1.13884452e-01   # N_{1,3}
  1  4    -4.52575210e-02   # N_{1,4}
  2  1     6.60379865e-02   # N_{2,1}
  2  2     9.54710865e-01   # N_{2,2}
  2  3    -2.44852425e-01   # N_{2,3}
  2  4     1.55606681e-01   # N_{2,4}
  3  1    -4.58690204e-02   # N_{3,1}
  3  2     6.71709957e-02   # N_{3,2}
  3  3     7.00264407e-01   # N_{3,3}
  3  4     7.09234693e-01   # N_{3,4}
  4  1    -9.78714096e-02   # N_{4,1}
  4  2     2.88078701e-01   # N_{4,2}
  4  3     6.60838393e-01   # N_{4,3}
  4  4    -6.86093629e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.36212625e-01   # U_{1,1}
  1  2    -3.51434093e-01   # U_{1,2}
  2  1     3.51434093e-01   # U_{2,1}
  2  2     9.36212625e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.74325167e-01   # V_{1,1}
  1  2    -2.25145439e-01   # V_{1,2}
  2  1     2.25145439e-01   # V_{2,1}
  2  2     9.74325167e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.08917351e-01   # F_{11}
  1  2     9.51088886e-01   # F_{12}
  2  1     9.51088886e-01   # F_{21}
  2  2    -3.08917351e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.98173133e-01   # F_{11}
  1  2     6.04185159e-02   # F_{12}
  2  1    -6.04185159e-02   # F_{21}
  2  2     9.98173133e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.99376561e-01   # F_{11}
  1  2     9.79922949e-01   # F_{12}
  2  1     9.79922949e-01   # F_{21}
  2  2    -1.99376561e-01   # F_{22}
Block gauge Q= 8.02092702e+02  # SM gauge couplings
     1     3.61745436e-01   # g'(Q)MSSM DRbar
     2     6.43485505e-01   # g(Q)MSSM DRbar
     3     1.06904038e+00   # g3(Q)MSSM DRbar
Block yu Q= 8.02092702e+02  
  3  3     8.69012414e-01   # Yt(Q)MSSM DRbar
Block yd Q= 8.02092702e+02  
  3  3     1.37637458e-01   # Yb(Q)MSSM DRbar
Block ye Q= 8.02092702e+02  
  3  3     9.97644407e-02   # Ytau(Q)MSSM DRbar
Block hmix Q= 8.02092702e+02 # Higgs mixing parameters
     1     4.61999519e+02    # mu(Q)MSSM DRbar
     2     9.68063855e+00    # tan beta(Q)MSSM DRbar
     3     2.44050580e+02    # higgs vev(Q)MSSM DRbar
     4     8.20643005e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 8.02092702e+02  # MSSM DRbar SUSY breaking parameters
     1     1.45252123e+02      # M_1(Q)
     2     2.70915844e+02      # M_2(Q)
     3     7.89952598e+02      # M_3(Q)
    21     5.83323543e+05      # mH1^2(Q)
    22    -1.98099008e+05      # mH2^2(Q)
    31     7.81417775e+02      # meL(Q)
    32     7.81406985e+02      # mmuL(Q)
    33     7.78205691e+02      # mtauL(Q)
    34     7.59369338e+02      # meR(Q)
    35     7.59347023e+02      # mmuR(Q)
    36     7.52710075e+02      # mtauR(Q)
    41     1.02501666e+03      # mqL1(Q)
    42     1.02501288e+03      # mqL2(Q)
    43     8.88830269e+02      # mqL3(Q)
    44     1.00893288e+03      # muR(Q)
    45     1.00892883e+03      # mcR(Q)
    46     7.09011904e+02      # mtR(Q)
    47     1.00708288e+03      # mdR(Q)
    48     1.00707919e+03      # msR(Q)
    49     9.99954311e+02      # mbR(Q)
Block au Q= 8.02092702e+02  
  1  1    -8.13410887e+02      # Au(Q)MSSM DRbar
  2  2    -8.13407218e+02      # Ac(Q)MSSM DRbar
  3  3    -6.24369783e+02      # At(Q)MSSM DRbar
Block ad Q= 8.02092702e+02  
  1  1    -9.98743484e+02      # Ad(Q)MSSM DRbar
  2  2    -9.98740079e+02      # As(Q)MSSM DRbar
  3  3    -9.32305423e+02      # Ab(Q)MSSM DRbar
Block ae Q= 8.02092702e+02  
  1  1    -2.11358431e+02      # Ae(Q)MSSM DRbar
  2  2    -2.11354589e+02      # Amu(Q)MSSM DRbar
  3  3    -2.10216811e+02      # Atau(Q)MSSM DRbar
