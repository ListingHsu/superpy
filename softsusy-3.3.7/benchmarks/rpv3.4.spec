# SOFTSUSY3.3.7 SLHA compliant output
# B.C. Allanach, Comput. Phys. Commun. 143 (2002) 305-331, hep-ph/0104145
# B.C. Allanach and M.A. Bernhardt, Comput. Phys. Commun. 181 (2010) 232,
# arXiv:0903.1805
# B.C. Allanach, M. Hanussek and C.H. Kom, arXiv:1109.3735
Block SPINFO          # Program information
     1    SOFTSUSY    # spectrum calculator
     2    3.3.7       # version number
Block MODSEL  # Select model
     1    1   # sugra
     4    1   # R-parity violating
Block SMINPUTS             # Standard Model inputs
     1    1.27934000e+02   # alpha_em^(-1)(MZ) SM MSbar
     2    1.16637000e-05   # G_Fermi
     3    1.17200000e-01   # alpha_s(MZ)MSbar
     4    9.11876000e+01   # MZ(pole)
     5    4.25000000e+00   # mb(mb)
     6    1.73300000e+02   # Mtop(pole)
     7    1.77700000e+00   # Mtau(pole)
    21    4.75000000e-03   # Mdown(2 GeV) MSbar
    22    2.40000000e-03   # Mup(2 GeV) MSbar
    23    1.04000000e-01   # Mstrange(2 GeV) MSbar
    24    1.27000000e+00   # Mcharm(Mcharm) MSbar
    11    5.10998902e-04   # Me(pole)
    13    1.05658357e-01   # Mmu(pole)
Block VCKMIN               # input CKM mixing matrix parameters
     1    2.27200000e-01   # lambda
     2    8.18000000e-01   # A
     3    2.21000000e-01   # rhobar
     4    3.40000000e-01   # etabar (no phases used in SOFTSUSY yet though)
Block MINPAR               # SUSY breaking input parameters
     3    1.00000000e+01   # tanb
     4    1.00000000e+00   # sign(mu)
     1    1.62500000e+02   # m0
     2    6.50000000e+02   # m12
     5    0.00000000e+00   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    1.35216441e+16   # MX scale
Block RVLAMUDDIN          # input LQD couplings at MSUSY
  1 2 3   1.00000000e-04   # lambda''_{123}
  1 3 2  -1.00000000e-04   # lambda''_{132}
# SOFTSUSY-specific non SLHA information:
# MIXING=1 Desired accuracy=1.00000000e-03 Achieved accuracy=8.66572076e-04
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     7.94218473e+01   # MW
        25     1.16257028e+02   # CP even neutral scalar
        35     4.56954406e+02   # CP even neutral scalar
        36     4.56954406e+02   # CP odd neutral scalar
        37     2.88637011e+02   # charged scalar
   1000021     1.46028725e+03   # ~g
   1000022     2.71683399e+02   # ~neutralino(1)
   1000023     5.11839123e+02   # ~neutralino(2)
   1000024     5.12082879e+02   # ~chargino(1)
   1000025    -8.05362815e+02   # ~neutralino(3)
   1000035     8.16783408e+02   # ~neutralino(4)
   1000037     8.16655455e+02   # ~chargino(2)
   1000011     2.95890811e+02   # charged scalar
   1000013     2.95913268e+02   # charged scalar
   1000015     4.64121147e+02   # charged scalar
   2000011     4.64999442e+02   # charged scalar
   2000013     4.65070454e+02   # charged scalar
   2000015     9.20569505e+02   # charged scalar
   1000012     4.58254700e+02   # CP even neutral scalar
   1000014     4.58259006e+02   # CP even neutral scalar
   1000016     9.16936469e+02   # CP even neutral scalar
   1000017     4.58254700e+02   # CP odd neutral scalar
   1000018     4.58259006e+02   # CP odd neutral scalar
   1000019     9.16936469e+02   # CP odd neutral scalar
   1000001     1.22768678e+03   # ~d_1
   1000003     1.27243320e+03   # ~d_2
   1000005     1.28255120e+03   # ~d_3
   2000001     1.28255538e+03   # ~d_4
   2000003     1.34037962e+03   # ~d_5
   2000005     1.34040446e+03   # ~d_6
   1000002     1.03267035e+03   # ~u_1
   1000004     1.25157471e+03   # ~u_2
   1000006     1.28751871e+03   # ~u_3
   2000002     1.28752428e+03   # ~u_4
   2000004     1.33827555e+03   # ~u_5
   2000006     1.33828174e+03   # ~u_6
        12     0.00000000e+00   # Mnu1 inverted hierarchy output
        14     0.00000000e+00   # Mnu2 inverted hierarchy output
        16     0.00000000e+00   # Mnu3 inverted hierarchy output
Block RVNMIX  # neutrino-neutralino mixing matrix 
  1 1    0.00000000e+00   # N_{11}
  1 2    0.00000000e+00   # N_{12}
  1 3    0.00000000e+00   # N_{13}
  1 4    0.00000000e+00   # N_{14}
  1 5    0.00000000e+00   # N_{15}
  1 6    0.00000000e+00   # N_{16}
  1 7    0.00000000e+00   # N_{17}
  2 1    0.00000000e+00   # N_{21}
  2 2    0.00000000e+00   # N_{22}
  2 3    0.00000000e+00   # N_{23}
  2 4    0.00000000e+00   # N_{24}
  2 5    0.00000000e+00   # N_{25}
  2 6    0.00000000e+00   # N_{26}
  2 7    0.00000000e+00   # N_{27}
  3 1    0.00000000e+00   # N_{31}
  3 2    0.00000000e+00   # N_{32}
  3 3    0.00000000e+00   # N_{33}
  3 4    0.00000000e+00   # N_{34}
  3 5    0.00000000e+00   # N_{35}
  3 6    0.00000000e+00   # N_{36}
  3 7    0.00000000e+00   # N_{37}
  4 1    0.00000000e+00   # N_{41}
  4 2    0.00000000e+00   # N_{42}
  4 3    0.00000000e+00   # N_{43}
  4 4    0.00000000e+00   # N_{44}
  4 5    0.00000000e+00   # N_{45}
  4 6    0.00000000e+00   # N_{46}
  4 7    0.00000000e+00   # N_{47}
  5 1    0.00000000e+00   # N_{51}
  5 2    0.00000000e+00   # N_{52}
  5 3    0.00000000e+00   # N_{53}
  5 4    0.00000000e+00   # N_{54}
  5 5    0.00000000e+00   # N_{55}
  5 6    0.00000000e+00   # N_{56}
  5 7    0.00000000e+00   # N_{57}
  6 1    0.00000000e+00   # N_{61}
  6 2    0.00000000e+00   # N_{62}
  6 3    0.00000000e+00   # N_{63}
  6 4    0.00000000e+00   # N_{64}
  6 5    0.00000000e+00   # N_{65}
  6 6    0.00000000e+00   # N_{66}
  6 7    0.00000000e+00   # N_{67}
  7 1    0.00000000e+00   # N_{71}
  7 2    0.00000000e+00   # N_{72}
  7 3    0.00000000e+00   # N_{73}
  7 4    0.00000000e+00   # N_{74}
  7 5    0.00000000e+00   # N_{75}
  7 6    0.00000000e+00   # N_{76}
  7 7    0.00000000e+00   # N_{77}
Block RVUMIX  # lepton-chargino mixing matrix U
  1 1    1.00000000e+00   # U_{11}
  1 2    0.00000000e+00   # U_{12}
  1 3    0.00000000e+00   # U_{13}
  1 4    0.00000000e+00   # U_{14}
  1 5    0.00000000e+00   # U_{15}
  2 1    0.00000000e+00   # U_{21}
  2 2    1.00000000e+00   # U_{22}
  2 3    0.00000000e+00   # U_{23}
  2 4    0.00000000e+00   # U_{24}
  2 5    0.00000000e+00   # U_{25}
  3 1    0.00000000e+00   # U_{31}
  3 2    0.00000000e+00   # U_{32}
  3 3    1.00000000e+00   # U_{33}
  3 4    0.00000000e+00   # U_{34}
  3 5    0.00000000e+00   # U_{35}
  4 1    0.00000000e+00   # U_{41}
  4 2    0.00000000e+00   # U_{42}
  4 3    0.00000000e+00   # U_{43}
  4 4    9.71654886e-01   # U_{44}
  4 5   -2.36403853e-01   # U_{45}
  5 1    0.00000000e+00   # U_{51}
  5 2    0.00000000e+00   # U_{52}
  5 3    0.00000000e+00   # U_{53}
  5 4    2.36403853e-01   # U_{54}
  5 5    9.71654886e-01   # U_{55}
Block RVVMIX  # lepton-chargino mixing matrix V
  1 1    1.00000000e+00   # V_{11}
  1 2    0.00000000e+00   # V_{12}
  1 3    0.00000000e+00   # V_{13}
  1 4    0.00000000e+00   # V_{14}
  1 5    0.00000000e+00   # V_{15}
  2 1    0.00000000e+00   # V_{21}
  2 2    1.00000000e+00   # V_{22}
  2 3    0.00000000e+00   # V_{23}
  2 4    0.00000000e+00   # V_{24}
  2 5    0.00000000e+00   # V_{25}
  3 1    0.00000000e+00   # V_{31}
  3 2    0.00000000e+00   # V_{32}
  3 3    1.00000000e+00   # V_{33}
  3 4    0.00000000e+00   # V_{34}
  3 5    0.00000000e+00   # V_{35}
  4 1    0.00000000e+00   # V_{41}
  4 2    0.00000000e+00   # V_{42}
  4 3    0.00000000e+00   # V_{43}
  4 4    9.87028196e-01   # V_{44}
  4 5   -1.60547002e-01   # V_{45}
  5 1    0.00000000e+00   # V_{51}
  5 2    0.00000000e+00   # V_{52}
  5 3    0.00000000e+00   # V_{53}
  5 4    1.60547002e-01   # V_{54}
  5 5    9.87028196e-01   # V_{55}
Block gauge Q= 1.10909324e+03  # SM gauge couplings
     1     3.63275191e-01   # g'(Q)MSSM DRbar
     2     6.40666745e-01   # g(Q)MSSM DRbar
     3     1.05200449e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.10909324e+03   # diagonal Up Yukawa matrix
  1  1     7.37934562e-06    # YU_{11}(Q)MSSM DRbar
  2  2     3.38027973e-03    # YU_{22}(Q)MSSM DRbar
  3  3     8.62112453e-01    # YU_{33}(Q)MSSM DRbar
Block yd Q= 1.10909324e+03   # diagonal down Yukawa matrix
  1  1     1.41629035e-04    # YD_{11}(Q)MSSM DRbar
  2  2     3.10099643e-03    # YD_{22}(Q)MSSM DRbar
  3  3     1.35044903e-01    # YD_{33}(Q)MSSM DRbar
Block ye Q= 1.10909324e+03   # diagonal lepton Yukawa matrix
  1  1     2.81850513e-05    # YE_{11}(Q)MSSM DRbar
  2  2     5.82778386e-03    # YE_{22}(Q)MSSM DRbar
  3  3     1.01458057e-01    # YE_{33}(Q)MSSM DRbar
Block hmix Q= 1.10909324e+03 # Higgs mixing parameters
     1     8.00122830e+02    # mu(Q)MSSM DRbar
     2     9.63834539e+00    # tan beta(Q)MSSM DRbar
     3     2.40867060e+02    # higgs vev(Q)MSSM DRbar
     4     8.70746303e+05    # mA^2(Q)MSSM DRbar
Block RVLAMLLE Q= 1.10909324e+03 # non-zero R-Parity violating LLE couplings 
Block RVLAMLQD Q= 1.10909324e+03 # non-zero R-Parity violating LQD couplings 
Block RVLAMUDD Q= 1.10909324e+03 # non-zero R-Parity violating UDD couplings 
  1 1 2    2.48223294e-13   # lambda''_{112}
  1 1 3    2.18040184e-16   # lambda''_{113}
  1 2 1   -2.48223294e-13   # lambda''_{121}
  1 2 3    3.53777358e-04   # lambda''_{123}
  1 3 1   -2.18040184e-16   # lambda''_{131}
  1 3 2   -3.53777358e-04   # lambda''_{132}
  2 1 2    5.60183594e-18   # lambda''_{212}
  2 1 3    4.92068447e-21   # lambda''_{213}
  2 2 1   -5.60183594e-18   # lambda''_{221}
  2 2 3    7.98616168e-09   # lambda''_{223}
  2 3 1   -4.92068447e-21   # lambda''_{231}
  2 3 2   -7.98616168e-09   # lambda''_{232}
  3 1 2   -1.30687752e-16   # lambda''_{312}
  3 1 3   -1.14796637e-19   # lambda''_{313}
  3 2 1    1.30687752e-16   # lambda''_{321}
  3 2 3   -1.86315755e-07   # lambda''_{323}
  3 3 1    1.14796637e-19   # lambda''_{331}
  3 3 2    1.86315755e-07   # lambda''_{332}
Block RVTLLE Q= 1.10909324e+03 # non-zero R-Parity violating LLE soft terms 
Block RVTLQD Q= 1.10909324e+03 # non-zero R-Parity violating LQD soft terms 
Block RVTUDD Q= 1.10909324e+03 # non-zero R-Parity violating UDD soft terms 
  1 1 2   -2.70571587e-10   # T''_{112}
  1 1 3   -1.54603274e-12   # T''_{113}
  1 2 1    2.70571587e-10   # T''_{121}
  1 2 3   -8.42124875e-01   # T''_{123}
  1 3 1    1.54603274e-12   # T''_{131}
  1 3 2    8.42124875e-01   # T''_{132}
  2 1 2   -5.37140584e-14   # T''_{212}
  2 1 3   -7.67107666e-17   # T''_{213}
  2 2 1    5.37140584e-14   # T''_{221}
  2 2 3   -8.68283269e-05   # T''_{223}
  2 3 1    7.67107666e-17   # T''_{231}
  2 3 2    8.68283269e-05   # T''_{232}
  3 1 2    3.98199271e-13   # T''_{312}
  3 1 3    1.03869838e-15   # T''_{313}
  3 2 1   -3.98199271e-13   # T''_{321}
  3 2 3    8.06850210e-04   # T''_{323}
  3 3 1   -1.03869838e-15   # T''_{331}
  3 3 2   -8.06850210e-04   # T''_{332}
Block RVKAPPA Q= 1.10909324e+03 # R-Parity violating kappa 
     1    0.00000000e+00   # kappa_{1}
     2    0.00000000e+00   # kappa_{2}
     3    0.00000000e+00   # kappa_{3}
Block RVD Q= 1.10909324e+03 # R-Parity violating D 
     1    0.00000000e+00   # D_{1}
     2    0.00000000e+00   # D_{2}
     3    0.00000000e+00   # D_{3}
Block RVSNVEV Q= 1.10909324e+03 # sneutrino VEVs D 
     1    0.00000000e+00   # SneutrinoVev_{1}
     2    0.00000000e+00   # SneutrinoVev_{2}
     3    0.00000000e+00   # SneutrinoVev_{3}
Block RVM2LH1 Q= 1.10909324e+03 # M2LH1 
     1    0.00000000e+00   # M2LH1_{1}
     2    0.00000000e+00   # M2LH1_{2}
     3    0.00000000e+00   # M2LH1_{3}
Block UPMNS Q= 9.11876000e+01 # neutrino mixing matrix (inverted  hierarchy)
  1  1     0.00000000e+00   # UPMNS_{11} matrix element
  1  2     0.00000000e+00   # UPMNS_{12} matrix element
  1  3     0.00000000e+00   # UPMNS_{13} matrix element
  2  1     0.00000000e+00   # UPMNS_{21} matrix element
  2  2     0.00000000e+00   # UPMNS_{22} matrix element
  2  3     0.00000000e+00   # UPMNS_{23} matrix element
  3  1     0.00000000e+00   # UPMNS_{31} matrix element
  3  2     0.00000000e+00   # UPMNS_{32} matrix element
  3  3     0.00000000e+00   # UPMNS_{33} matrix element
Block msq2 Q= 1.10909324e+03 # super CKM squark mass^2 matrix - DRbar
  1  1     1.67637822e+06    # (m^_Q^2)_{11}
  1  2     5.81216351e+01    # (m^_Q^2)_{12}
  1  3    -1.37569320e+03    # (m^_Q^2)_{13}
  2  1     5.81216351e+01    # (m^_Q^2)_{21}
  2  2     1.67595705e+06    # (m^_Q^2)_{22}
  2  3     1.01281331e+04    # (m^_Q^2)_{23}
  3  1    -1.37569320e+03    # (m^_Q^2)_{31}
  3  2     1.01281331e+04    # (m^_Q^2)_{32}
  3  3     1.42450756e+06    # (m^_Q^2)_{33}
Block msl2 Q= 1.10909324e+03 # super MNS slepton mass^2 matrix - DRbar
  1  1     2.08446378e+05    # (m^_L^2)_{11}
  1  2     0.00000000e+00    # (m^_L^2)_{12}
  1  3     0.00000000e+00    # (m^_L^2)_{13}
  2  1     0.00000000e+00    # (m^_L^2)_{21}
  2  2     2.08442466e+05    # (m^_L^2)_{22}
  2  3     0.00000000e+00    # (m^_L^2)_{23}
  3  1     0.00000000e+00    # (m^_L^2)_{31}
  3  2     0.00000000e+00    # (m^_L^2)_{32}
  3  3     2.07262324e+05    # (m^_L^2)_{33}
Block msd2 Q= 1.10909324e+03 # super CKM squark mass^2 matrix - DRbar
  1  1     1.53520015e+06    # (m^_d^2)_{11}
  1  2    -4.20463837e-06    # (m^_d^2)_{12}
  1  3     4.31304761e-03    # (m^_d^2)_{13}
  2  1    -4.20463837e-06    # (m^_d^2)_{21}
  2  2     1.53519138e+06    # (m^_d^2)_{22}
  2  3    -6.95247685e-01    # (m^_d^2)_{23}
  3  1     4.31304761e-03    # (m^_d^2)_{31}
  3  2    -6.95247685e-01    # (m^_d^2)_{32}
  3  3     1.51958160e+06    # (m^_d^2)_{33}
Block msu2 Q= 1.10909324e+03 # super CKM squark mass^2 matrix - DRbar
  1  1     1.55040048e+06    # (m^_u^2)_{11}
  1  2     3.40085404e-02    # (m^_u^2)_{12}
  1  3    -7.50652200e-04    # (m^_u^2)_{13}
  2  1     3.40085404e-02    # (m^_u^2)_{21}
  2  2     1.55039173e+06    # (m^_u^2)_{22}
  2  3    -1.00826491e-01    # (m^_u^2)_{23}
  3  1    -7.50652200e-04    # (m^_u^2)_{31}
  3  2    -1.00826491e-01    # (m^_u^2)_{32}
  3  3     1.04950644e+06    # (m^_u^2)_{33}
Block mse2 Q= 1.10909324e+03 # super MNS slepton mass^2 matrix - DRbar
  1  1     8.28948123e+04    # (m^_e^2)_{11}
  1  2     0.00000000e+00    # (m^_e^2)_{12}
  1  3     0.00000000e+00    # (m^_e^2)_{13}
  2  1     0.00000000e+00    # (m^_e^2)_{21}
  2  2     8.28868354e+04    # (m^_e^2)_{22}
  2  3     0.00000000e+00    # (m^_e^2)_{23}
  3  1     0.00000000e+00    # (m^_e^2)_{31}
  3  2     0.00000000e+00    # (m^_e^2)_{32}
  3  3     8.04802102e+04    # (m^_e^2)_{33}
Block tu Q= 1.10909324e+03   # super CKM trilinear matrix - DRbar
  1  1    -1.05807590e-02    # (T^_u)_{11}
  1  2    -5.84988377e-08    # (T^_u)_{12}
  1  3     9.23920029e-08    # (T^_u)_{13}
  2  1    -1.10173460e-05    # (T^_u)_{21}
  2  2    -4.84680525e+00    # (T^_u)_{22}
  2  3    -5.25203275e-04    # (T^_u)_{23}
  3  1    -1.49494687e-02    # (T^_u)_{31}
  3  2    -1.58657495e-01    # (T^_u)_{32}
  3  3    -9.52715800e+02    # (T^_u)_{33}
Block td Q= 1.10909324e+03   # super CKM trilinear matrix - DRbar
  1  1    -2.48587682e-01    # (T^_d)_{11}
  1  2    -3.72731699e-06    # (T^_d)_{12}
  1  3     8.87135311e-05    # (T^_d)_{13}
  2  1    -8.16100365e-05    # (T^_d)_{21}
  2  2    -5.44230041e+00    # (T^_d)_{22}
  2  3    -1.43003207e-02    # (T^_d)_{23}
  3  1     8.44143891e-02    # (T^_d)_{31}
  3  2    -6.21477133e-01    # (T^_d)_{32}
  3  3    -2.21479278e+02    # (T^_d)_{33}
Block te Q= 1.10909324e+03   # super CKM trilinear matrix - DRbar
  1  1    -1.07301210e-02    # (T^_e)_{11}
  1  2     0.00000000e+00    # (T^_e)_{12}
  1  3     0.00000000e+00    # (T^_e)_{13}
  2  1     0.00000000e+00    # (T^_e)_{21}
  2  2    -2.21861230e+00    # (T^_e)_{22}
  2  3     0.00000000e+00    # (T^_e)_{23}
  3  1     0.00000000e+00    # (T^_e)_{31}
  3  2     0.00000000e+00    # (T^_e)_{32}
  3  3    -3.84147855e+01    # (T^_e)_{33}
Block VCKM Q= 1.10909324e+03 # DRbar CKM mixing matrix
  1  1     9.73840760e-01    # CKM_{11} matrix element
  1  2     2.27197319e-01    # CKM_{12} matrix element
  1  3     3.94378170e-03    # CKM_{13} matrix element
  2  1    -2.27161574e-01    # CKM_{21} matrix element
  2  2     9.72963576e-01    # CKM_{22} matrix element
  2  3     4.17072920e-02    # CKM_{23} matrix element
  3  1     5.63862897e-03    # CKM_{31} matrix element
  3  2    -4.15121366e-02    # CKM_{32} matrix element
  3  3     9.99122089e-01    # CKM_{33} matrix element
Block msoft Q= 1.10909324e+03 # MSSM DRbar SUSY breaking parameters
     1     2.77453118e+02     # M_1(Q)
     2     5.09254927e+02     # M_2(Q)
     3     1.42038677e+03     # M_3(Q)
    21     1.82209240e+05     # mH1^2(Q)
    22    -6.15601405e+05     # mH2^2(Q)
Block USQMIX  # super CKM squark mass^2 matrix
  1  1     1.92495020e-05   # (USQMIX)_{11}
  1  2     2.03833500e-04   # (USQMIX)_{12}
  1  3     3.63166175e-01   # (USQMIX)_{13}
  1  4     1.23488921e-09   # (USQMIX)_{14}
  1  5     5.12955147e-07   # (USQMIX)_{15}
  1  6     9.31724362e-01   # (USQMIX)_{16}
  2  1     1.28308016e-04   # (USQMIX)_{21}
  2  2     1.35795547e-03   # (USQMIX)_{22}
  2  3     9.31723414e-01   # (USQMIX)_{23}
  2  4    -4.85683487e-10   # (USQMIX)_{24}
  2  5     1.34308768e-05   # (USQMIX)_{25}
  2  6    -3.63166105e-01   # (USQMIX)_{26}
  3  1     8.62087452e-08   # (USQMIX)_{31}
  3  2     6.51757106e-03   # (USQMIX)_{32}
  3  3    -2.14286478e-05   # (USQMIX)_{33}
  3  4    -2.36923075e-03   # (USQMIX)_{34}
  3  5     9.99975953e-01   # (USQMIX)_{35}
  3  6     6.37604793e-06   # (USQMIX)_{36}
  4  1     1.42279905e-05   # (USQMIX)_{41}
  4  2     1.54436482e-05   # (USQMIX)_{42}
  4  3    -5.25685095e-08   # (USQMIX)_{43}
  4  4     9.99997193e-01   # (USQMIX)_{44}
  4  5     2.36918041e-03   # (USQMIX)_{45}
  4  6     1.41878021e-08   # (USQMIX)_{46}
  5  1     1.35681592e-01   # (USQMIX)_{51}
  5  2     9.90730493e-01   # (USQMIX)_{52}
  5  3    -1.34393949e-03   # (USQMIX)_{53}
  5  4    -1.93240224e-06   # (USQMIX)_{54}
  5  5    -6.45735868e-03   # (USQMIX)_{55}
  5  6     3.04296873e-04   # (USQMIX)_{56}
  6  1     9.90752486e-01   # (USQMIX)_{61}
  6  2    -1.35678761e-01   # (USQMIX)_{62}
  6  3     5.63304185e-05   # (USQMIX)_{63}
  6  4    -1.40959070e-05   # (USQMIX)_{64}
  6  5     8.84199707e-04   # (USQMIX)_{65}
  6  6    -1.27434377e-05   # (USQMIX)_{66}
Block DSQMIX  # super CKM squark mass^2 matrix
  1  1     4.67842424e-03   # (DSQMIX)_{11}
  1  2    -3.44439020e-02   # (DSQMIX)_{12}
  1  3     9.83131709e-01   # (DSQMIX)_{13}
  1  4     7.83732843e-07   # (DSQMIX)_{14}
  1  5    -1.26345084e-04   # (DSQMIX)_{15}
  1  6     1.79565464e-01   # (DSQMIX)_{16}
  2  1    -1.40059763e-03   # (DSQMIX)_{21}
  2  2     1.03122344e-02   # (DSQMIX)_{22}
  2  3    -1.79308196e-01   # (DSQMIX)_{23}
  2  4    -1.42952281e-06   # (DSQMIX)_{24}
  2  5     2.30529577e-04   # (DSQMIX)_{25}
  2  6     9.83737879e-01   # (DSQMIX)_{26}
  3  1     1.31565493e-06   # (DSQMIX)_{31}
  3  2     3.39075364e-03   # (DSQMIX)_{32}
  3  3     2.87037519e-04   # (DSQMIX)_{33}
  3  4     3.35271566e-06   # (DSQMIX)_{34}
  3  5     9.99994187e-01   # (DSQMIX)_{35}
  3  6    -2.17562483e-04   # (DSQMIX)_{36}
  4  1     1.55307273e-04   # (DSQMIX)_{41}
  4  2     4.86900356e-08   # (DSQMIX)_{42}
  4  3    -1.78150624e-06   # (DSQMIX)_{43}
  4  4     9.99999988e-01   # (DSQMIX)_{44}
  4  5    -3.35229950e-06   # (DSQMIX)_{45}
  4  6     1.34982890e-06   # (DSQMIX)_{46}
  5  1    -1.35198459e-01   # (DSQMIX)_{51}
  5  2     9.90148230e-01   # (DSQMIX)_{52}
  5  3     3.60628570e-02   # (DSQMIX)_{53}
  5  4     2.10074447e-05   # (DSQMIX)_{54}
  5  5    -3.36841167e-03   # (DSQMIX)_{55}
  5  6    -3.99787074e-03   # (DSQMIX)_{56}
  6  1     9.90806491e-01   # (DSQMIX)_{61}
  6  2     1.35285849e-01   # (DSQMIX)_{62}
  6  3     2.52286886e-05   # (DSQMIX)_{63}
  6  4    -1.53887537e-04   # (DSQMIX)_{64}
  6  5    -4.60034551e-04   # (DSQMIX)_{65}
  6  6    -2.79405807e-06   # (DSQMIX)_{66}
Block RVLMIX  # charged higgs-slepton mixing matrix 
  1 1    0.00000000e+00   # C_{11}
  1 2    0.00000000e+00   # C_{12}
  1 3    0.00000000e+00   # C_{13}
  1 4    0.00000000e+00   # C_{14}
  1 5    1.11572038e-01   # C_{15}
  1 6    0.00000000e+00   # C_{16}
  1 7    0.00000000e+00   # C_{17}
  1 8    9.93756349e-01   # C_{18}
  2 1    0.00000000e+00   # C_{21}
  2 2    0.00000000e+00   # C_{22}
  2 3    0.00000000e+00   # C_{23}
  2 4    6.59633249e-03   # C_{24}
  2 5    0.00000000e+00   # C_{25}
  2 6    0.00000000e+00   # C_{26}
  2 7    9.99978244e-01   # C_{27}
  2 8    0.00000000e+00   # C_{28}
  3 1    0.00000000e+00   # C_{31}
  3 2    0.00000000e+00   # C_{32}
  3 3    3.19051428e-05   # C_{33}
  3 4    0.00000000e+00   # C_{34}
  3 5    0.00000000e+00   # C_{35}
  3 6    9.99999999e-01   # C_{36}
  3 7    0.00000000e+00   # C_{37}
  3 8    0.00000000e+00   # C_{38}
  4 1    0.00000000e+00   # C_{41}
  4 2    0.00000000e+00   # C_{42}
  4 3    9.99999999e-01   # C_{43}
  4 4    0.00000000e+00   # C_{44}
  4 5    0.00000000e+00   # C_{45}
  4 6   -3.19051428e-05   # C_{46}
  4 7    0.00000000e+00   # C_{47}
  4 8    0.00000000e+00   # C_{48}
  5 1    0.00000000e+00   # C_{51}
  5 2    0.00000000e+00   # C_{52}
  5 3    0.00000000e+00   # C_{53}
  5 4    9.99978244e-01   # C_{54}
  5 5    0.00000000e+00   # C_{55}
  5 6    0.00000000e+00   # C_{56}
  5 7   -6.59633249e-03   # C_{57}
  5 8    0.00000000e+00   # C_{58}
  6 1    0.00000000e+00   # C_{61}
  6 2    0.00000000e+00   # C_{62}
  6 3    0.00000000e+00   # C_{63}
  6 4    0.00000000e+00   # C_{64}
  6 5    9.93756349e-01   # C_{65}
  6 6    0.00000000e+00   # C_{66}
  6 7    0.00000000e+00   # C_{67}
  6 8   -1.11572038e-01   # C_{68}
  7 1    9.94660807e-01   # C_{71}
  7 2    1.03198249e-01   # C_{72}
  7 3    0.00000000e+00   # C_{73}
  7 4    0.00000000e+00   # C_{74}
  7 5    0.00000000e+00   # C_{75}
  7 6    0.00000000e+00   # C_{76}
  7 7    0.00000000e+00   # C_{77}
  7 8    0.00000000e+00   # C_{78}
Block RVHMIX  # CP-even neutral scalar mixing matrix 
  1 1    1.05018781e-01   # curlyN_{11}
  1 2    9.94470239e-01   # curlyN_{12}
  1 3    0.00000000e+00   # curlyN_{13}
  1 4    0.00000000e+00   # curlyN_{14}
  1 5    0.00000000e+00   # curlyN_{15}
  2 1    0.00000000e+00   # curlyN_{21}
  2 2    0.00000000e+00   # curlyN_{22}
  2 3    0.00000000e+00   # curlyN_{23}
  2 4    0.00000000e+00   # curlyN_{24}
  2 5    1.00000000e+00   # curlyN_{25}
  3 1    0.00000000e+00   # curlyN_{31}
  3 2    0.00000000e+00   # curlyN_{32}
  3 3    0.00000000e+00   # curlyN_{33}
  3 4    1.00000000e+00   # curlyN_{34}
  3 5    0.00000000e+00   # curlyN_{35}
  4 1    0.00000000e+00   # curlyN_{41}
  4 2    0.00000000e+00   # curlyN_{42}
  4 3    1.00000000e+00   # curlyN_{43}
  4 4    0.00000000e+00   # curlyN_{44}
  4 5    0.00000000e+00   # curlyN_{45}
  5 1    9.94470239e-01   # curlyN_{51}
  5 2   -1.05018781e-01   # curlyN_{52}
  5 3    0.00000000e+00   # curlyN_{53}
  5 4    0.00000000e+00   # curlyN_{54}
  5 5    0.00000000e+00   # curlyN_{55}
Block RVAMIX  # CP-odd neutral scalar mixing matrix 
  1 1    0.00000000e+00   # curlyN~_{11}
  1 2    0.00000000e+00   # curlyN~_{12}
  1 3    0.00000000e+00   # curlyN~_{13}
  1 4    0.00000000e+00   # curlyN~_{14}
  1 5    1.00000000e+00   # curlyN~_{15}
  2 1    0.00000000e+00   # curlyN~_{21}
  2 2    0.00000000e+00   # curlyN~_{22}
  2 3    0.00000000e+00   # curlyN~_{23}
  2 4    1.00000000e+00   # curlyN~_{24}
  2 5    0.00000000e+00   # curlyN~_{25}
  3 1    0.00000000e+00   # curlyN~_{31}
  3 2    0.00000000e+00   # curlyN~_{32}
  3 3    1.00000000e+00   # curlyN~_{33}
  3 4    0.00000000e+00   # curlyN~_{34}
  3 5    0.00000000e+00   # curlyN~_{35}
  4 1    9.94660811e-01   # curlyN~_{41}
  4 2    1.03198210e-01   # curlyN~_{42}
  4 3    0.00000000e+00   # curlyN~_{43}
  4 4    0.00000000e+00   # curlyN~_{44}
  4 5    0.00000000e+00   # curlyN~_{45}
