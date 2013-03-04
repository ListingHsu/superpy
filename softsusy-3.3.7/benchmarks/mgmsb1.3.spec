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
     1    4.50000000e+04   # lambda
     2    9.00000000e+04   # M_mess
     5    3.00000000e+00   # N5
     6    1.00000000e+00   # cgrav
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=4.13232334e-04
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.04022015e+01   # MW
        25     1.12046737e+02   # h0
        35     4.31793931e+02   # H0
        36     4.31483307e+02   # A0
        37     4.39149289e+02   # H+
   1000021     1.05245702e+03   # ~g
   1000022     1.84859165e+02   # ~neutralino(1)
   1000023     3.04849359e+02   # ~neutralino(2)
   1000024     3.02246387e+02   # ~chargino(1)
   1000025    -3.48795655e+02   # ~neutralino(3)
   1000035     4.24314344e+02   # ~neutralino(4)
   1000037     4.23376676e+02   # ~chargino(2)
   1000039     9.59850000e-10   # ~gravitino
   1000001     1.00382627e+03   # ~d_L
   1000002     1.00081420e+03   # ~u_L
   1000003     1.00382501e+03   # ~s_L
   1000004     1.00081293e+03   # ~c_L
   1000005     9.55636439e+02   # ~b_1
   1000006     8.95299317e+02   # ~t_1
   1000011     2.94116094e+02   # ~e_L
   1000012     2.82913239e+02   # ~nue_L
   1000013     2.94145318e+02   # ~mu_L
   1000014     2.82912016e+02   # ~numu_L
   1000015     1.39385711e+02   # ~stau_1
   1000016     2.82352866e+02   # ~nu_tau_L
   2000001     9.64096638e+02   # ~d_R
   2000002     9.65952781e+02   # ~u_R
   2000003     9.64094875e+02   # ~s_R
   2000004     9.65951882e+02   # ~c_R
   2000005     9.71221610e+02   # ~b_2
   2000006     9.86097278e+02   # ~t_2
   2000011     1.45768624e+02   # ~e_R
   2000013     1.45763798e+02   # ~mu_R
   2000015     2.95689108e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -7.69044501e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.71223563e-01   # N_{1,1}
  1  2    -5.39631966e-02   # N_{1,2}
  1  3     2.00094429e-01   # N_{1,3}
  1  4    -1.17366876e-01   # N_{1,4}
  2  1    -2.12034557e-01   # N_{2,1}
  2  2    -6.13822973e-01   # N_{2,2}
  2  3     5.65301291e-01   # N_{2,3}
  2  4    -5.08622802e-01   # N_{2,4}
  3  1    -5.38969118e-02   # N_{3,1}
  3  2     7.26931801e-02   # N_{3,2}
  3  3     6.97921237e-01   # N_{3,3}
  3  4     7.10434213e-01   # N_{3,4}
  4  1    -9.41342661e-02   # N_{4,1}
  4  2     7.84235317e-01   # N_{4,2}
  4  3     3.91538781e-01   # N_{4,3}
  4  4    -4.72028696e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1    -5.51719357e-01   # U_{1,1}
  1  2     8.34029826e-01   # U_{1,2}
  2  1    -8.34029826e-01   # U_{2,1}
  2  2    -5.51719357e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1    -6.64408941e-01   # V_{1,1}
  1  2     7.47369225e-01   # V_{1,2}
  2  1    -7.47369225e-01   # V_{2,1}
  2  2    -6.64408941e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.32999090e-01   # F_{11}
  1  2     9.42927148e-01   # F_{12}
  2  1     9.42927148e-01   # F_{21}
  2  2    -3.32999090e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     5.35502436e-01   # F_{11}
  1  2     8.44533682e-01   # F_{12}
  2  1     8.44533682e-01   # F_{21}
  2  2    -5.35502436e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.35338778e-01   # F_{11}
  1  2     9.90799382e-01   # F_{12}
  2  1     9.90799382e-01   # F_{21}
  2  2    -1.35338778e-01   # F_{22}
Block gauge Q= 9.11118527e+02  # SM gauge couplings
     1     3.62885654e-01   # g'(Q)MSSM DRbar
     2     6.44415086e-01   # g(Q)MSSM DRbar
     3     1.06221075e+00   # g3(Q)MSSM DRbar
Block yu Q= 9.11118527e+02  
  3  3     8.64761313e-01   # Yt(Q)MSSM DRbar
Block yd Q= 9.11118527e+02  
  3  3     2.05044997e-01   # Yb(Q)MSSM DRbar
Block ye Q= 9.11118527e+02  
  3  3     1.51968244e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 9.11118527e+02 # Higgs mixing parameters
     1     3.39955149e+02    # mu(Q)MSSM DRbar
     2     1.45173674e+01    # tan beta(Q)MSSM DRbar
     3     2.43803968e+02    # higgs vev(Q)MSSM DRbar
     4     2.12497445e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 9.11118527e+02  # MSSM DRbar SUSY breaking parameters
     1     1.94940794e+02      # M_1(Q)
     2     3.67497822e+02      # M_2(Q)
     3     1.00341289e+03      # M_3(Q)
    21     7.05610923e+04      # mH1^2(Q)
    22    -1.02349582e+05      # mH2^2(Q)
    31     2.85058000e+02      # meL(Q)
    32     2.85056788e+02      # mmuL(Q)
    33     2.84684392e+02      # mtauL(Q)
    34     1.33835486e+02      # meR(Q)
    35     1.33830242e+02      # mmuR(Q)
    36     1.32209368e+02      # mtauR(Q)
    41     9.65416666e+02      # mqL1(Q)
    42     9.65415366e+02      # mqL2(Q)
    43     9.34577830e+02      # mqL3(Q)
    44     9.30612552e+02      # muR(Q)
    45     9.30611632e+02      # mcR(Q)
    46     8.67983454e+02      # mtR(Q)
    47     9.27470524e+02      # mdR(Q)
    48     9.27468715e+02      # msR(Q)
    49     9.23946452e+02      # mbR(Q)
Block au Q= 9.11118527e+02  
  1  1    -3.03324718e+02      # Au(Q)MSSM DRbar
  2  2    -3.03324289e+02      # Ac(Q)MSSM DRbar
  3  3    -2.85892608e+02      # At(Q)MSSM DRbar
Block ad Q= 9.11118527e+02  
  1  1    -3.22735407e+02      # Ad(Q)MSSM DRbar
  2  2    -3.22734808e+02      # As(Q)MSSM DRbar
  3  3    -3.16164088e+02      # Ab(Q)MSSM DRbar
Block ae Q= 9.11118527e+02  
  1  1    -3.07531848e+01      # Ae(Q)MSSM DRbar
  2  2    -3.07529605e+01      # Amu(Q)MSSM DRbar
  3  3    -3.06840491e+01      # Atau(Q)MSSM DRbar
