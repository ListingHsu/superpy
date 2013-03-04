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
     1    1.08000000e+05   # lambda
     2    1.20000000e+05   # M_mess
     5    1.00000000e+00   # N5
     6    1.00000000e+00   # cgrav
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=3.58123900e-06
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.04016689e+01   # MW
        25     1.13658782e+02   # h0
        35     5.48383842e+02   # H0
        36     5.48099320e+02   # A0
        37     5.54236673e+02   # H+
   1000021     1.01901589e+03   # ~g
   1000022     1.75659243e+02   # ~neutralino(1)
   1000023     3.24194000e+02   # ~neutralino(2)
   1000024     3.23990258e+02   # ~chargino(1)
   1000025    -4.29634162e+02   # ~neutralino(3)
   1000035     4.61877494e+02   # ~neutralino(4)
   1000037     4.61199942e+02   # ~chargino(2)
   1000039     3.07152000e-09   # ~gravitino
   1000001     1.21782310e+03   # ~d_L
   1000002     1.21541050e+03   # ~u_L
   1000003     1.21782145e+03   # ~s_L
   1000004     1.21540884e+03   # ~c_L
   1000005     1.15451944e+03   # ~b_1
   1000006     1.07656982e+03   # ~t_1
   1000011     3.79290617e+02   # ~e_L
   1000012     3.70629094e+02   # ~nue_L
   1000013     3.79296881e+02   # ~mu_L
   1000014     3.70627424e+02   # ~numu_L
   1000015     1.83228509e+02   # ~stau_1
   1000016     3.69891333e+02   # ~nu_tau_L
   2000001     1.16292518e+03   # ~d_R
   2000002     1.16640560e+03   # ~u_R
   2000003     1.16292288e+03   # ~s_R
   2000004     1.16640442e+03   # ~c_R
   2000005     1.17314162e+03   # ~b_2
   2000006     1.18361202e+03   # ~t_2
   2000011     1.88973658e+02   # ~e_R
   2000013     1.88967030e+02   # ~mu_R
   2000015     3.80090010e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -7.39904906e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.88401656e-01   # N_{1,1}
  1  2    -3.18395822e-02   # N_{1,2}
  1  3     1.34384938e-01   # N_{1,3}
  1  4    -6.31592839e-02   # N_{1,4}
  2  1     9.82643413e-02   # N_{2,1}
  2  2     8.72095841e-01   # N_{2,2}
  2  3    -3.76890440e-01   # N_{2,3}
  2  4     2.96220459e-01   # N_{2,4}
  3  1    -4.77037247e-02   # N_{3,1}
  3  2     6.70112693e-02   # N_{3,2}
  3  3     7.00097320e-01   # N_{3,3}
  3  4     7.09293724e-01   # N_{3,4}
  4  1    -1.05501846e-01   # N_{4,1}
  4  2     4.83678173e-01   # N_{4,2}
  4  3     5.91403439e-01   # N_{4,3}
  4  4    -6.36527107e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     8.38998024e-01   # U_{1,1}
  1  2    -5.44134464e-01   # U_{1,2}
  2  1     5.44134464e-01   # U_{2,1}
  2  2     8.38998024e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.03011681e-01   # V_{1,1}
  1  2    -4.29615997e-01   # V_{1,2}
  2  1     4.29615997e-01   # V_{2,1}
  2  2     9.03011681e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     2.39617129e-01   # F_{11}
  1  2     9.70867463e-01   # F_{12}
  2  1     9.70867463e-01   # F_{21}
  2  2    -2.39617129e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     4.10545981e-01   # F_{11}
  1  2     9.11839897e-01   # F_{12}
  2  1     9.11839897e-01   # F_{21}
  2  2    -4.10545981e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.01444058e-01   # F_{11}
  1  2     9.94841245e-01   # F_{12}
  2  1     9.94841245e-01   # F_{21}
  2  2    -1.01444058e-01   # F_{22}
Block gauge Q= 1.10540105e+03  # SM gauge couplings
     1     3.63292085e-01   # g'(Q)MSSM DRbar
     2     6.44004319e-01   # g(Q)MSSM DRbar
     3     1.05665991e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.10540105e+03  
  3  3     8.60566047e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.10540105e+03  
  3  3     2.02957650e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.10540105e+03  
  3  3     1.51291010e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.10540105e+03 # Higgs mixing parameters
     1     4.21053596e+02    # mu(Q)MSSM DRbar
     2     1.44806570e+01    # tan beta(Q)MSSM DRbar
     3     2.43457739e+02    # higgs vev(Q)MSSM DRbar
     4     3.32823243e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.10540105e+03  # MSSM DRbar SUSY breaking parameters
     1     1.82413651e+02      # M_1(Q)
     2     3.42670668e+02      # M_2(Q)
     3     9.27062325e+02      # M_3(Q)
    21     1.22018517e+05      # mH1^2(Q)
    22    -1.53570356e+05      # mH2^2(Q)
    31     3.72686912e+02      # meL(Q)
    32     3.72685246e+02      # mmuL(Q)
    33     3.72175770e+02      # mtauL(Q)
    34     1.78535430e+02      # meR(Q)
    35     1.78528410e+02      # mmuR(Q)
    36     1.76368235e+02      # mtauR(Q)
    41     1.18471497e+03      # mqL1(Q)
    42     1.18471326e+03      # mqL2(Q)
    43     1.14373747e+03      # mqL3(Q)
    44     1.13541919e+03      # muR(Q)
    45     1.13541797e+03      # mcR(Q)
    46     1.05157648e+03      # mtR(Q)
    47     1.13066309e+03      # mdR(Q)
    48     1.13066071e+03      # msR(Q)
    49     1.12602294e+03      # mbR(Q)
Block au Q= 1.10540105e+03  
  1  1    -2.82995399e+02      # Au(Q)MSSM DRbar
  2  2    -2.82994998e+02      # Ac(Q)MSSM DRbar
  3  3    -2.66576437e+02      # At(Q)MSSM DRbar
Block ad Q= 1.10540105e+03  
  1  1    -3.01191329e+02      # Ad(Q)MSSM DRbar
  2  2    -3.01190769e+02      # As(Q)MSSM DRbar
  3  3    -2.95010632e+02      # Ab(Q)MSSM DRbar
Block ae Q= 1.10540105e+03  
  1  1    -2.93107656e+01      # Ae(Q)MSSM DRbar
  2  2    -2.93105490e+01      # Amu(Q)MSSM DRbar
  3  3    -2.92443113e+01      # Atau(Q)MSSM DRbar
