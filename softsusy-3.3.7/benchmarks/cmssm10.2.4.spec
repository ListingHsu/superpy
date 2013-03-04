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
     1    2.75000000e+02   # m0
     2    6.50000000e+02   # m12
     5    0.00000000e+00   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    1.75136477e+16   # MX scale
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=4.30830768e-04
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03931820e+01   # MW
        25     1.16617214e+02   # h0
        35     9.38843449e+02   # H0
        36     9.38616369e+02   # A0
        37     9.42286962e+02   # H+
   1000021     1.46435213e+03   # ~g
   1000022     2.70020270e+02   # ~neutralino(1)
   1000023     5.10928483e+02   # ~neutralino(2)
   1000024     5.11171772e+02   # ~chargino(1)
   1000025    -7.99943066e+02   # ~neutralino(3)
   1000035     8.11877179e+02   # ~neutralino(4)
   1000037     8.11746275e+02   # ~chargino(2)
   1000001     1.35933376e+03   # ~d_L
   1000002     1.35718321e+03   # ~u_L
   1000003     1.35933041e+03   # ~s_L
   1000004     1.35717985e+03   # ~c_L
   1000005     1.24273364e+03   # ~b_1
   1000006     1.04344058e+03   # ~t_1
   1000011     5.16378139e+02   # ~e_L
   1000012     5.10126166e+02   # ~nue_L
   1000013     5.16494036e+02   # ~mu_L
   1000014     5.10121030e+02   # ~numu_L
   1000015     3.62828503e+02   # ~stau_1
   1000016     5.08385112e+02   # ~nu_tau_L
   2000001     1.30194141e+03   # ~d_R
   2000002     1.30684428e+03   # ~u_R
   2000003     1.30193792e+03   # ~s_R
   2000004     1.30684067e+03   # ~c_R
   2000005     1.29652808e+03   # ~b_2
   2000006     1.27877937e+03   # ~t_2
   2000011     3.69700651e+02   # ~e_R
   2000013     3.69686260e+02   # ~mu_R
   2000015     5.16190855e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.05586716e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.97351544e-01   # N_{1,1}
  1  2    -1.10227076e-02   # N_{1,2}
  1  3     6.60477715e-02   # N_{1,3}
  1  4    -2.83917081e-02   # N_{1,4}
  2  1     2.53827005e-02   # N_{2,1}
  2  2     9.78162776e-01   # N_{2,2}
  2  3    -1.69512789e-01   # N_{2,3}
  2  4     1.17553033e-01   # N_{2,4}
  3  1    -2.61091649e-02   # N_{3,1}
  3  2     3.77562290e-02   # N_{3,2}
  3  3     7.04850476e-01   # N_{3,3}
  3  4     7.07869045e-01   # N_{3,4}
  4  1    -6.29597276e-02   # N_{4,1}
  4  2     2.04084663e-01   # N_{4,2}
  4  3     6.85630303e-01   # N_{4,3}
  4  4    -6.95914226e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.70802457e-01   # U_{1,1}
  1  2    -2.39880367e-01   # U_{1,2}
  2  1     2.39880367e-01   # U_{2,1}
  2  2     9.70802457e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.85909083e-01   # V_{1,1}
  1  2    -1.67282037e-01   # V_{1,2}
  2  1     1.67282037e-01   # V_{2,1}
  2  2     9.85909083e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.57318275e-01   # F_{11}
  1  2     9.33982682e-01   # F_{12}
  2  1     9.33982682e-01   # F_{21}
  2  2    -3.57318275e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.86584943e-01   # F_{11}
  1  2     1.63248739e-01   # F_{12}
  2  1    -1.63248739e-01   # F_{21}
  2  2     9.86584943e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.08356332e-01   # F_{11}
  1  2     9.94112119e-01   # F_{12}
  2  1     9.94112119e-01   # F_{21}
  2  2    -1.08356332e-01   # F_{22}
Block gauge Q= 1.12132484e+03  # SM gauge couplings
     1     3.62861377e-01   # g'(Q)MSSM DRbar
     2     6.41581673e-01   # g(Q)MSSM DRbar
     3     1.04797232e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.12132484e+03  
  3  3     8.52832257e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.12132484e+03  
  3  3     1.33667676e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.12132484e+03  
  3  3     1.00328813e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.12132484e+03 # Higgs mixing parameters
     1     7.94376616e+02    # mu(Q)MSSM DRbar
     2     9.64406416e+00    # tan beta(Q)MSSM DRbar
     3     2.43819233e+02    # higgs vev(Q)MSSM DRbar
     4     9.11713383e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.12132484e+03  # MSSM DRbar SUSY breaking parameters
     1     2.75273798e+02      # M_1(Q)
     2     5.07759223e+02      # M_2(Q)
     3     1.42090214e+03      # M_3(Q)
    21     2.31172563e+05      # mH1^2(Q)
    22    -6.06105473e+05      # mH2^2(Q)
    31     5.08677974e+02      # meL(Q)
    32     5.08672812e+02      # mmuL(Q)
    33     5.07111028e+02      # mtauL(Q)
    34     3.63436333e+02      # meR(Q)
    35     3.63421684e+02      # mmuR(Q)
    36     3.58969029e+02      # mtauR(Q)
    41     1.31370592e+03      # mqL1(Q)
    42     1.31370250e+03      # mqL2(Q)
    43     1.20807730e+03      # mqL3(Q)
    44     1.26444663e+03      # muR(Q)
    45     1.26444297e+03      # mcR(Q)
    46     1.03454276e+03      # mtR(Q)
    47     1.25841899e+03      # mdR(Q)
    48     1.25841545e+03      # msR(Q)
    49     1.25194516e+03      # mbR(Q)
Block au Q= 1.12132484e+03  
  1  1    -1.44230249e+03      # Au(Q)MSSM DRbar
  2  2    -1.44229609e+03      # Ac(Q)MSSM DRbar
  3  3    -1.11720434e+03      # At(Q)MSSM DRbar
Block ad Q= 1.12132484e+03  
  1  1    -1.75937169e+03      # Ad(Q)MSSM DRbar
  2  2    -1.75936577e+03      # As(Q)MSSM DRbar
  3  3    -1.64526822e+03      # Ab(Q)MSSM DRbar
Block ae Q= 1.12132484e+03  
  1  1    -3.84565923e+02      # Ae(Q)MSSM DRbar
  2  2    -3.84559122e+02      # Amu(Q)MSSM DRbar
  3  3    -3.82502828e+02      # Atau(Q)MSSM DRbar
