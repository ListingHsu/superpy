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
     1    9.50000000e+02   # m0
     2    4.50000000e+02   # m12
     5    0.00000000e+00   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    2.12712318e+16   # MX scale
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=2.87401644e-04
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03964308e+01   # MW
        25     1.14839753e+02   # h0
        35     1.13080420e+03   # H0
        36     1.13075577e+03   # A0
        37     1.13370467e+03   # H+
   1000021     1.08804636e+03   # ~g
   1000022     1.85789916e+02   # ~neutralino(1)
   1000023     3.51521605e+02   # ~neutralino(2)
   1000024     3.51657298e+02   # ~chargino(1)
   1000025    -5.78813904e+02   # ~neutralino(3)
   1000035     5.94309639e+02   # ~neutralino(4)
   1000037     5.94144108e+02   # ~chargino(2)
   1000001     1.32507477e+03   # ~d_L
   1000002     1.32289093e+03   # ~u_L
   1000003     1.32507016e+03   # ~s_L
   1000004     1.32288632e+03   # ~c_L
   1000005     1.15058792e+03   # ~b_1
   1000006     9.19662010e+02   # ~t_1
   1000011     9.93624000e+02   # ~e_L
   1000012     9.90181295e+02   # ~nue_L
   1000013     9.93656831e+02   # ~mu_L
   1000014     9.90167756e+02   # ~numu_L
   1000015     9.55064446e+02   # ~stau_1
   1000016     9.86023171e+02   # ~nu_tau_L
   2000001     1.29958173e+03   # ~d_R
   2000002     1.30120232e+03   # ~u_R
   2000003     1.29957725e+03   # ~s_R
   2000004     1.30119735e+03   # ~c_R
   2000005     1.29083214e+03   # ~b_2
   2000006     1.17423501e+03   # ~t_2
   2000011     9.64495477e+02   # ~e_R
   2000013     9.64467560e+02   # ~mu_R
   2000015     9.90299404e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.04820280e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.94824741e-01   # N_{1,1}
  1  2    -2.08404082e-02   # N_{1,2}
  1  3     9.18780278e-02   # N_{1,3}
  1  4    -3.80504948e-02   # N_{1,4}
  2  1     4.56863915e-02   # N_{2,1}
  2  2     9.64566240e-01   # N_{2,2}
  2  3    -2.16159408e-01   # N_{2,3}
  2  4     1.44221469e-01   # N_{2,4}
  3  1    -3.66870604e-02   # N_{3,1}
  3  2     5.32876619e-02   # N_{3,2}
  3  3     7.02740834e-01   # N_{3,3}
  3  4     7.08498274e-01   # N_{3,4}
  4  1    -8.30093248e-02   # N_{4,1}
  4  2     2.57561780e-01   # N_{4,2}
  4  3     6.71557040e-01   # N_{4,3}
  4  4    -6.89769906e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.51259713e-01   # U_{1,1}
  1  2    -3.08390918e-01   # U_{1,2}
  2  1     3.08390918e-01   # U_{2,1}
  2  2     9.51259713e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.78297112e-01   # V_{1,1}
  1  2    -2.07207050e-01   # V_{1,2}
  2  1     2.07207050e-01   # V_{2,1}
  2  2     9.78297112e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     2.54748935e-01   # F_{11}
  1  2     9.67007229e-01   # F_{12}
  2  1     9.67007229e-01   # F_{21}
  2  2    -2.54748935e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.98895794e-01   # F_{11}
  1  2     4.69807617e-02   # F_{12}
  2  1    -4.69807617e-02   # F_{21}
  2  2     9.98895794e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.54511323e-01   # F_{11}
  1  2     9.87991018e-01   # F_{12}
  2  1     9.87991018e-01   # F_{21}
  2  2    -1.54511323e-01   # F_{22}
Block gauge Q= 1.01134676e+03  # SM gauge couplings
     1     3.62238817e-01   # g'(Q)MSSM DRbar
     2     6.42244249e-01   # g(Q)MSSM DRbar
     3     1.05665740e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.01134676e+03  
  3  3     8.60888050e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.01134676e+03  
  3  3     1.35948356e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.01134676e+03  
  3  3     9.95982291e-02   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.01134676e+03 # Higgs mixing parameters
     1     5.71310655e+02    # mu(Q)MSSM DRbar
     2     9.65262224e+00    # tan beta(Q)MSSM DRbar
     3     2.43752357e+02    # higgs vev(Q)MSSM DRbar
     4     1.30542034e+06    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.01134676e+03  # MSSM DRbar SUSY breaking parameters
     1     1.88858161e+02      # M_1(Q)
     2     3.50124774e+02      # M_2(Q)
     3     9.97548543e+02      # M_3(Q)
    21     9.38689461e+05      # mH1^2(Q)
    22    -2.98329384e+05      # mH2^2(Q)
    31     9.90764888e+02      # meL(Q)
    32     9.90751385e+02      # mmuL(Q)
    33     9.86734678e+02      # mtauL(Q)
    34     9.62267120e+02      # meR(Q)
    35     9.62239177e+02      # mmuR(Q)
    36     9.53907238e+02      # mtauR(Q)
    41     1.29502217e+03      # mqL1(Q)
    42     1.29501744e+03      # mqL2(Q)
    43     1.12437381e+03      # mqL3(Q)
    44     1.27399168e+03      # muR(Q)
    45     1.27398658e+03      # mcR(Q)
    46     8.98209209e+02      # mtR(Q)
    47     1.27154087e+03      # mdR(Q)
    48     1.27153626e+03      # msR(Q)
    49     1.26267525e+03      # mbR(Q)
Block au Q= 1.01134676e+03  
  1  1    -1.01828682e+03      # Au(Q)MSSM DRbar
  2  2    -1.01828227e+03      # Ac(Q)MSSM DRbar
  3  3    -7.84716314e+02      # At(Q)MSSM DRbar
Block ad Q= 1.01134676e+03  
  1  1    -1.24661964e+03      # Ad(Q)MSSM DRbar
  2  2    -1.24661543e+03      # As(Q)MSSM DRbar
  3  3    -1.16456429e+03      # Ab(Q)MSSM DRbar
Block ae Q= 1.01134676e+03  
  1  1    -2.68702469e+02      # Ae(Q)MSSM DRbar
  2  2    -2.68697657e+02      # Amu(Q)MSSM DRbar
  3  3    -2.67269109e+02      # Atau(Q)MSSM DRbar
