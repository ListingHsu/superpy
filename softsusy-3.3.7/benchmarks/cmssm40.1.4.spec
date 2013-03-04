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
     1    3.75000000e+02   # m0
     2    6.50000000e+02   # m12
     5   -5.00000000e+02   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    1.71599181e+16   # MX scale
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=5.78813493e-04
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03882626e+01   # MW
        25     1.18308485e+02   # h0
        35     7.58126074e+02   # H0
        36     7.58051251e+02   # A0
        37     7.62596675e+02   # H+
   1000021     1.46728585e+03   # ~g
   1000022     2.72319019e+02   # ~neutralino(1)
   1000023     5.18123718e+02   # ~neutralino(2)
   1000024     5.18275097e+02   # ~chargino(1)
   1000025    -8.60821916e+02   # ~neutralino(3)
   1000035     8.68437341e+02   # ~neutralino(4)
   1000037     8.69006036e+02   # ~chargino(2)
   1000001     1.38374868e+03   # ~d_L
   1000002     1.38159619e+03   # ~u_L
   1000003     1.38371059e+03   # ~s_L
   1000004     1.38155802e+03   # ~c_L
   1000005     1.16856833e+03   # ~b_1
   1000006     1.01167900e+03   # ~t_1
   1000011     5.75690076e+02   # ~e_L
   1000012     5.69952534e+02   # ~nue_L
   1000013     5.75715745e+02   # ~mu_L
   1000014     5.69810064e+02   # ~numu_L
   1000015     2.72422426e+02   # ~stau_1
   1000016     5.20571370e+02   # ~nu_tau_L
   2000001     1.32751019e+03   # ~d_R
   2000002     1.33229210e+03   # ~u_R
   2000003     1.32743440e+03   # ~s_R
   2000004     1.33228728e+03   # ~c_R
   2000005     1.23514730e+03   # ~b_2
   2000006     1.23565460e+03   # ~t_2
   2000011     4.48955787e+02   # ~e_R
   2000013     4.48588242e+02   # ~mu_R
   2000015     5.45949133e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -2.60025523e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.98034152e-01   # N_{1,1}
  1  2    -6.88741695e-03   # N_{1,2}
  1  3     5.88854644e-02   # N_{1,3}
  1  4    -2.03198525e-02   # N_{1,4}
  2  1     1.69709309e-02   # N_{2,1}
  2  2     9.85825199e-01   # N_{2,2}
  2  3    -1.42129908e-01   # N_{2,3}
  2  4     8.75200159e-02   # N_{2,4}
  3  1    -2.69123064e-02   # N_{3,1}
  3  2     3.92679533e-02   # N_{3,2}
  3  3     7.04925296e-01   # N_{3,3}
  3  4     7.07682191e-01   # N_{3,4}
  4  1    -5.39957970e-02   # N_{4,1}
  4  2     1.62970144e-01   # N_{4,2}
  4  3     6.92395782e-01   # N_{4,3}
  4  4    -7.00794740e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.79629219e-01   # U_{1,1}
  1  2    -2.00814821e-01   # U_{1,2}
  2  1     2.00814821e-01   # U_{2,1}
  2  2     9.79629219e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.92159416e-01   # V_{1,1}
  1  2    -1.24978771e-01   # V_{1,2}
  2  1     1.24978771e-01   # V_{2,1}
  2  2     9.92159416e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     4.17869510e-01   # F_{11}
  1  2     9.08507057e-01   # F_{12}
  2  1     9.08507057e-01   # F_{21}
  2  2    -4.17869510e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     8.07995129e-01   # F_{11}
  1  2     5.89189165e-01   # F_{12}
  2  1    -5.89189165e-01   # F_{21}
  2  2     8.07995129e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     3.02801662e-01   # F_{11}
  1  2     9.53053594e-01   # F_{12}
  2  1     9.53053594e-01   # F_{21}
  2  2    -3.02801662e-01   # F_{22}
Block gauge Q= 1.08706621e+03  # SM gauge couplings
     1     3.62685137e-01   # g'(Q)MSSM DRbar
     2     6.41136258e-01   # g(Q)MSSM DRbar
     3     1.04857384e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.08706621e+03  
  3  3     8.48085303e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.08706621e+03  
  3  3     4.89901284e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.08706621e+03  
  3  3     4.27859623e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.08706621e+03 # Higgs mixing parameters
     1     8.57825064e+02    # mu(Q)MSSM DRbar
     2     3.91757267e+01    # tan beta(Q)MSSM DRbar
     3     2.43737772e+02    # higgs vev(Q)MSSM DRbar
     4     7.28526857e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.08706621e+03  # MSSM DRbar SUSY breaking parameters
     1     2.76572775e+02      # M_1(Q)
     2     5.10366691e+02      # M_2(Q)
     3     1.42573850e+03      # M_3(Q)
    21    -1.63098316e+05      # mH1^2(Q)
    22    -7.21546188e+05      # mH2^2(Q)
    31     5.68932469e+02      # meL(Q)
    32     5.68789241e+02      # mmuL(Q)
    33     5.22705095e+02      # mtauL(Q)
    34     4.43880951e+02      # meR(Q)
    35     4.43509163e+02      # mmuR(Q)
    36     3.07294040e+02      # mtauR(Q)
    41     1.34026967e+03      # mqL1(Q)
    42     1.34023083e+03      # mqL2(Q)
    43     1.16072649e+03      # mqL3(Q)
    44     1.29201312e+03      # muR(Q)
    45     1.29200823e+03      # mcR(Q)
    46     1.01385162e+03      # mtR(Q)
    47     1.28615455e+03      # mdR(Q)
    48     1.28607753e+03      # msR(Q)
    49     1.17581288e+03      # mbR(Q)
Block au Q= 1.08706621e+03  
  1  1    -1.78771980e+03      # Au(Q)MSSM DRbar
  2  2    -1.78767788e+03      # Ac(Q)MSSM DRbar
  3  3    -1.25732142e+03      # At(Q)MSSM DRbar
Block ad Q= 1.08706621e+03  
  1  1    -2.06512022e+03      # Ad(Q)MSSM DRbar
  2  2    -2.06501347e+03      # As(Q)MSSM DRbar
  3  3    -1.74605965e+03      # Ab(Q)MSSM DRbar
Block ae Q= 1.08706621e+03  
  1  1    -6.86336502e+02      # Ae(Q)MSSM DRbar
  2  2    -6.86003412e+02      # Amu(Q)MSSM DRbar
  3  3    -5.74197417e+02      # Atau(Q)MSSM DRbar
