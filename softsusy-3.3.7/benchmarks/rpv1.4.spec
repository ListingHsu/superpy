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
     0    1.35215755e+16   # MX scale
Block RVLAMLLEIN           # input LLE couplings at MSUSY
  1 2 1   1.00000000e-02   # lambda_{121}
  2 1 1  -1.00000000e-02   # lambda_{211}
# SOFTSUSY-specific non SLHA information:
# MIXING=1 Desired accuracy=1.00000000e-03 Achieved accuracy=1.73970469e-04
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     7.94219049e+01   # MW
        25     1.16257015e+02   # CP even neutral scalar
        35     4.56954339e+02   # CP even neutral scalar
        36     4.56954339e+02   # CP odd neutral scalar
        37     2.88637078e+02   # charged scalar
   1000021     1.46028662e+03   # ~g
   1000022     2.71683234e+02   # ~neutralino(1)
   1000023     5.11838754e+02   # ~neutralino(2)
   1000024     5.12082510e+02   # ~chargino(1)
   1000025    -8.05361755e+02   # ~neutralino(3)
   1000035     8.16782413e+02   # ~neutralino(4)
   1000037     8.16654455e+02   # ~chargino(2)
   1000011     2.95821562e+02   # charged scalar
   1000013     2.95890861e+02   # charged scalar
   1000015     4.64121089e+02   # charged scalar
   2000011     4.64970111e+02   # charged scalar
   2000013     4.65041147e+02   # charged scalar
   2000015     9.20568166e+02   # charged scalar
   1000012     4.58224945e+02   # CP even neutral scalar
   1000014     4.58229250e+02   # CP even neutral scalar
   1000016     9.16935122e+02   # CP even neutral scalar
   1000017     4.58224945e+02   # CP odd neutral scalar
   1000018     4.58229250e+02   # CP odd neutral scalar
   1000019     9.16935122e+02   # CP odd neutral scalar
   1000001     1.22768628e+03   # ~d_1
   1000003     1.27243262e+03   # ~d_2
   1000005     1.28255060e+03   # ~d_3
   2000001     1.28255471e+03   # ~d_4
   2000003     1.34037898e+03   # ~d_5
   2000005     1.34040381e+03   # ~d_6
   1000002     1.03266994e+03   # ~u_1
   1000004     1.25157427e+03   # ~u_2
   1000006     1.28751803e+03   # ~u_3
   2000002     1.28752366e+03   # ~u_4
   2000004     1.33827490e+03   # ~u_5
   2000006     1.33828108e+03   # ~u_6
        12     3.96058634e-41   # Mnu1 inverted hierarchy output
        14     4.02350030e-14   # Mnu2 inverted hierarchy output
        16     0.00000000e+00   # Mnu3 inverted hierarchy output
Block RVNMIX  # neutrino-neutralino mixing matrix 
  1 1    0.00000000e+00   # N_{11}
  1 2    1.00000000e+00   # N_{12}
  1 3    2.03515107e-14   # N_{13}
  1 4   -1.73423408e-23   # N_{14}
  1 5    1.57047527e-23   # N_{15}
  1 6   -1.08665265e-22   # N_{16}
  1 7    1.07302695e-22   # N_{17}
  2 1    0.00000000e+00   # N_{21}
  2 2   -2.03515107e-14   # N_{22}
  2 3    1.00000000e+00   # N_{23}
  2 4   -1.80685819e-11   # N_{24}
  2 5    4.16894590e-10   # N_{25}
  2 6   -2.98237789e-09   # N_{26}
  2 7    2.96133683e-09   # N_{27}
  3 1    1.00000000e+00   # N_{31}
  3 2    0.00000000e+00   # N_{32}
  3 3    0.00000000e+00   # N_{33}
  3 4    0.00000000e+00   # N_{34}
  3 5    0.00000000e+00   # N_{35}
  3 6    0.00000000e+00   # N_{36}
  3 7    0.00000000e+00   # N_{37}
  4 1    0.00000000e+00   # N_{41}
  4 2    1.26094837e-23   # N_{42}
  4 3   -2.52186224e-10   # N_{43}
  4 4    9.97447226e-01   # N_{44}
  4 5    2.45170822e-02   # N_{45}
  4 6   -2.56396486e-02   # N_{46}
  4 7    6.19721874e-02   # N_{47}
  5 1    0.00000000e+00   # N_{51}
  5 2    3.85946669e-24   # N_{52}
  5 3    2.89845969e-10   # N_{53}
  5 4   -1.07871928e-02   # N_{54}
  5 5    9.79343013e-01   # N_{55}
  5 6    3.70629464e-02   # N_{56}
  5 7   -1.98487374e-01   # N_{57}
  6 1    0.00000000e+00   # N_{61}
  6 2    6.84084681e-23   # N_{62}
  6 3    4.20602100e-09   # N_{63}
  6 4    6.48467038e-02   # N_{64}
  6 5   -1.65145853e-01   # N_{65}
  6 6    7.04928103e-01   # N_{66}
  6 7   -6.86730022e-01   # N_{67}
  7 1    0.00000000e+00   # N_{71}
  7 2   -1.03727561e-25   # N_{72}
  7 3    3.20666428e-13   # N_{73}
  7 4   -2.78849849e-02   # N_{74}
  7 5    1.14074638e-01   # N_{75}
  7 6    7.07845546e-01   # N_{76}
  7 7    6.96537212e-01   # N_{77}
Block RVUMIX  # lepton-chargino mixing matrix U
  1 1    1.00000000e+00   # U_{11}
  1 2    1.39626840e-32   # U_{12}
  1 3    0.00000000e+00   # U_{13}
  1 4    5.37390314e-25   # U_{14}
  1 5   -2.41812276e-23   # U_{15}
  2 1   -1.39626845e-32   # U_{21}
  2 2   -1.00000000e+00   # U_{22}
  2 3    0.00000000e+00   # U_{23}
  2 4    2.56517949e-11   # U_{24}
  2 5   -1.15426660e-09   # U_{25}
  3 1    0.00000000e+00   # U_{31}
  3 2    0.00000000e+00   # U_{32}
  3 3    1.00000000e+00   # U_{33}
  3 4    0.00000000e+00   # U_{34}
  3 5    0.00000000e+00   # U_{35}
  4 1   -6.23868590e-24   # U_{41}
  4 2    2.97797410e-10   # U_{42}
  4 3    0.00000000e+00   # U_{43}
  4 4    9.71654961e-01   # U_{44}
  4 5   -2.36403545e-01   # U_{45}
  5 1    2.33687688e-23   # U_{51}
  5 2   -1.11548470e-09   # U_{52}
  5 3    0.00000000e+00   # U_{53}
  5 4    2.36403545e-01   # U_{54}
  5 5    9.71654961e-01   # U_{55}
Block RVVMIX  # lepton-chargino mixing matrix V
  1 1    1.00000000e+00   # V_{11}
  1 2    1.93801138e-16   # V_{12}
  1 3    0.00000000e+00   # V_{13}
  1 4    0.00000000e+00   # V_{14}
  1 5    0.00000000e+00   # V_{15}
  2 1    2.50450702e-16   # V_{21}
  2 2   -1.00000000e+00   # V_{22}
  2 3    0.00000000e+00   # V_{23}
  2 4    3.93968409e-14   # V_{24}
  2 5   -1.53185539e-13   # V_{25}
  3 1    0.00000000e+00   # V_{31}
  3 2    0.00000000e+00   # V_{32}
  3 3    1.00000000e+00   # V_{33}
  3 4    0.00000000e+00   # V_{34}
  3 5    0.00000000e+00   # V_{35}
  4 1   -1.58984159e-29   # V_{41}
  4 2    6.34792228e-14   # V_{42}
  4 3    0.00000000e+00   # V_{43}
  4 4    9.87028251e-01   # V_{44}
  4 5   -1.60546667e-01   # V_{45}
  5 1    3.62836506e-29   # V_{51}
  5 2   -1.44873424e-13   # V_{52}
  5 3    0.00000000e+00   # V_{53}
  5 4    1.60546667e-01   # V_{54}
  5 5    9.87028251e-01   # V_{55}
Block gauge Q= 1.10909256e+03  # SM gauge couplings
     1     3.63275217e-01   # g'(Q)MSSM DRbar
     2     6.40666792e-01   # g(Q)MSSM DRbar
     3     1.05200435e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.10909256e+03   # diagonal Up Yukawa matrix
  1  1     7.37934007e-06    # YU_{11}(Q)MSSM DRbar
  2  2     3.38027720e-03    # YU_{22}(Q)MSSM DRbar
  3  3     8.62111806e-01    # YU_{33}(Q)MSSM DRbar
Block yd Q= 1.10909256e+03   # diagonal down Yukawa matrix
  1  1     1.41628938e-04    # YD_{11}(Q)MSSM DRbar
  2  2     3.10099428e-03    # YD_{22}(Q)MSSM DRbar
  3  3     1.35044816e-01    # YD_{33}(Q)MSSM DRbar
Block ye Q= 1.10909256e+03   # diagonal lepton Yukawa matrix
  1  1     2.81854331e-05    # YE_{11}(Q)MSSM DRbar
  2  2     5.82780041e-03    # YE_{22}(Q)MSSM DRbar
  3  3     1.01457986e-01    # YE_{33}(Q)MSSM DRbar
Block hmix Q= 1.10909256e+03 # Higgs mixing parameters
     1     8.00121755e+02    # mu(Q)MSSM DRbar
     2     9.63834599e+00    # tan beta(Q)MSSM DRbar
     3     2.40867253e+02    # higgs vev(Q)MSSM DRbar
     4     8.70744596e+05    # mA^2(Q)MSSM DRbar
Block RVLAMLLE Q= 1.10909256e+03 # non-zero R-Parity violating LLE couplings 
  1 2 1    1.48488662e-02   # lambda_{121}
  1 2 2   -6.17053767e-24   # lambda_{122}
  1 3 3   -3.56681636e-23   # lambda_{133}
  2 1 1   -1.48488662e-02   # lambda_{211}
  2 1 2    6.17053767e-24   # lambda_{212}
  2 3 3    3.63844534e-09   # lambda_{233}
  3 1 3    3.56681636e-23   # lambda_{313}
  3 2 3   -3.63844534e-09   # lambda_{323}
Block RVLAMLQD Q= 1.10909256e+03 # non-zero R-Parity violating LQD couplings 
  1 1 1   -4.97905677e-26   # lambda'_{111}
  1 1 2    3.20726280e-30   # lambda'_{112}
  1 1 3   -3.23295976e-27   # lambda'_{113}
  1 2 1    1.46485549e-31   # lambda'_{121}
  1 2 2   -1.09017497e-24   # lambda'_{122}
  1 2 3    2.38014303e-26   # lambda'_{123}
  1 3 1   -3.43419596e-30   # lambda'_{131}
  1 3 2    5.53563690e-28   # lambda'_{132}
  1 3 3   -4.74770001e-23   # lambda'_{133}
  2 1 1    5.45515981e-12   # lambda'_{211}
  2 1 2   -2.64875287e-16   # lambda'_{212}
  2 1 3    3.07677563e-13   # lambda'_{213}
  2 2 1   -1.20976697e-17   # lambda'_{221}
  2 2 2    1.19441239e-10   # lambda'_{222}
  2 2 3   -2.26515548e-12   # lambda'_{223}
  2 3 1    2.84277865e-16   # lambda'_{231}
  2 3 2   -4.58231511e-14   # lambda'_{232}
  2 3 3    5.92791593e-09   # lambda'_{233}
Block RVLAMUDD Q= 1.10909256e+03 # non-zero R-Parity violating UDD couplings 
Block RVTLLE Q= 1.10909256e+03 # non-zero R-Parity violating LLE soft terms 
  1 2 1   -6.51487852e+00   # T_{121}
  1 2 2   -5.09482938e-21   # T_{122}
  1 3 3   -2.18510888e-19   # T_{133}
  2 1 1    6.51487852e+00   # T_{211}
  2 1 2    5.09482938e-21   # T_{212}
  2 3 3   -4.22918266e-06   # T_{233}
  3 1 3    2.18510888e-19   # T_{313}
  3 2 3    4.22918266e-06   # T_{323}
Block RVTLQD Q= 1.10909256e+03 # non-zero R-Parity violating LQD soft terms 
  1 1 1   -2.01442561e-22   # T'_{111}
  1 1 2    5.33337791e-25   # T'_{112}
  1 1 3   -9.06034783e-22   # T'_{113}
  1 2 1    2.30273037e-26   # T'_{121}
  1 2 2   -4.41447040e-21   # T'_{122}
  1 2 3    6.63208920e-21   # T'_{123}
  1 3 1    7.38606402e-25   # T'_{131}
  1 3 2   -1.19338871e-22   # T'_{132}
  1 3 3   -2.64446235e-19   # T'_{133}
  2 1 1   -1.59009249e-08   # T'_{211}
  2 1 2    5.48654710e-13   # T'_{212}
  2 1 3    3.88353939e-09   # T'_{213}
  2 2 1    2.55565535e-14   # T'_{221}
  2 2 2   -3.48151053e-07   # T'_{222}
  2 2 3   -2.88128926e-08   # T'_{223}
  2 3 1    3.54869075e-12   # T'_{231}
  2 3 2   -5.76485529e-10   # T'_{232}
  2 3 3   -1.39468451e-05   # T'_{233}
Block RVTUDD Q= 1.10909256e+03 # non-zero R-Parity violating UDD soft terms 
Block RVKAPPA Q= 1.10909256e+03 # R-Parity violating kappa 
     1   -2.61999268e-19   # kappa_{1}
     2   -6.30626522e-06   # kappa_{2}
     3    0.00000000e+00   # kappa_{3}
Block RVD Q= 1.10909256e+03 # R-Parity violating D 
     1   -1.86641737e-15   # D_{1}
     2    8.34704721e-04   # D_{2}
     3    0.00000000e+00   # D_{3}
Block RVSNVEV Q= 1.10909256e+03 # sneutrino VEVs D 
     1    0.00000000e+00   # SneutrinoVev_{1}
     2    0.00000000e+00   # SneutrinoVev_{2}
     3    0.00000000e+00   # SneutrinoVev_{3}
Block RVM2LH1 Q= 1.10909256e+03 # M2LH1 
     1    3.53080371e-16   # M2LH1_{1}
     2    3.76354195e-02   # M2LH1_{2}
     3    0.00000000e+00   # M2LH1_{3}
Block UPMNS Q= 9.11876000e+01 # neutrino mixing matrix (inverted  hierarchy)
  1  1     1.00000000e+00   # UPMNS_{11} matrix element
  1  2     2.03517847e-14   # UPMNS_{12} matrix element
  1  3     0.00000000e+00   # UPMNS_{13} matrix element
  2  1    -2.03517847e-14   # UPMNS_{21} matrix element
  2  2     1.00000000e+00   # UPMNS_{22} matrix element
  2  3     0.00000000e+00   # UPMNS_{23} matrix element
  3  1     0.00000000e+00   # UPMNS_{31} matrix element
  3  2     0.00000000e+00   # UPMNS_{32} matrix element
  3  3     1.00000000e+00   # UPMNS_{33} matrix element
Block msq2 Q= 1.10909256e+03 # super CKM squark mass^2 matrix - DRbar
  1  1     1.67637664e+06    # (m^_Q^2)_{11}
  1  2     5.81215288e+01    # (m^_Q^2)_{12}
  1  3    -1.37569066e+03    # (m^_Q^2)_{13}
  2  1     5.81215288e+01    # (m^_Q^2)_{21}
  2  2     1.67595546e+06    # (m^_Q^2)_{22}
  2  3     1.01281144e+04    # (m^_Q^2)_{23}
  3  1    -1.37569066e+03    # (m^_Q^2)_{31}
  3  2     1.01281144e+04    # (m^_Q^2)_{32}
  3  3     1.42450645e+06    # (m^_Q^2)_{33}
Block msl2 Q= 1.10909256e+03 # super MNS slepton mass^2 matrix - DRbar
  1  1     2.08419166e+05    # (m^_L^2)_{11}
  1  2     3.39778673e-24    # (m^_L^2)_{12}
  1  3     0.00000000e+00    # (m^_L^2)_{13}
  2  1     3.39778673e-24    # (m^_L^2)_{21}
  2  2     2.08415254e+05    # (m^_L^2)_{22}
  2  3     0.00000000e+00    # (m^_L^2)_{23}
  3  1     0.00000000e+00    # (m^_L^2)_{31}
  3  2     0.00000000e+00    # (m^_L^2)_{32}
  3  3     2.07262290e+05    # (m^_L^2)_{33}
Block msd2 Q= 1.10909256e+03 # super CKM squark mass^2 matrix - DRbar
  1  1     1.53519858e+06    # (m^_d^2)_{11}
  1  2    -4.16393075e-06    # (m^_d^2)_{12}
  1  3     4.31300610e-03    # (m^_d^2)_{13}
  2  1    -4.16393075e-06    # (m^_d^2)_{21}
  2  2     1.53518997e+06    # (m^_d^2)_{22}
  2  3    -6.95244560e-01    # (m^_d^2)_{23}
  3  1     4.31300610e-03    # (m^_d^2)_{31}
  3  2    -6.95244560e-01    # (m^_d^2)_{32}
  3  3     1.51958022e+06    # (m^_d^2)_{33}
Block msu2 Q= 1.10909256e+03 # super CKM squark mass^2 matrix - DRbar
  1  1     1.55039906e+06    # (m^_u^2)_{11}
  1  2    -2.26600696e-08    # (m^_u^2)_{12}
  1  3    -2.07546568e-05    # (m^_u^2)_{13}
  2  1    -2.26600696e-08    # (m^_u^2)_{21}
  2  2     1.55039018e+06    # (m^_u^2)_{22}
  2  3    -1.00995817e-01    # (m^_u^2)_{23}
  3  1    -2.07546568e-05    # (m^_u^2)_{31}
  3  2    -1.00995817e-01    # (m^_u^2)_{32}
  3  3     1.04950583e+06    # (m^_u^2)_{33}
Block mse2 Q= 1.10909256e+03 # super MNS slepton mass^2 matrix - DRbar
  1  1     8.28404481e+04    # (m^_e^2)_{11}
  1  2     1.36127101e-14    # (m^_e^2)_{12}
  1  3     0.00000000e+00    # (m^_e^2)_{13}
  2  1     1.36127101e-14    # (m^_e^2)_{21}
  2  2     8.28868228e+04    # (m^_e^2)_{22}
  2  3     0.00000000e+00    # (m^_e^2)_{23}
  3  1     0.00000000e+00    # (m^_e^2)_{31}
  3  2     0.00000000e+00    # (m^_e^2)_{32}
  3  3     8.04802025e+04    # (m^_e^2)_{33}
Block tu Q= 1.10909256e+03   # super CKM trilinear matrix - DRbar
  1  1    -1.05807483e-02    # (T^_u)_{11}
  1  2    -2.40511671e-08    # (T^_u)_{12}
  1  3    -1.08003080e-07    # (T^_u)_{13}
  2  1    -1.10172131e-05    # (T^_u)_{21}
  2  2    -4.84680024e+00    # (T^_u)_{22}
  2  3    -5.25153595e-04    # (T^_u)_{23}
  3  1    -1.49493801e-02    # (T^_u)_{31}
  3  2    -1.58656556e-01    # (T^_u)_{32}
  3  3    -9.52715331e+02    # (T^_u)_{33}
Block td Q= 1.10909256e+03   # super CKM trilinear matrix - DRbar
  1  1    -2.48587348e-01    # (T^_d)_{11}
  1  2    -3.72730657e-06    # (T^_d)_{12}
  1  3     8.87132800e-05    # (T^_d)_{13}
  2  1    -8.16098073e-05    # (T^_d)_{21}
  2  2    -5.44229323e+00    # (T^_d)_{22}
  2  3    -1.43002800e-02    # (T^_d)_{23}
  3  1     8.44141541e-02    # (T^_d)_{31}
  3  2    -6.21475403e-01    # (T^_d)_{32}
  3  3    -2.21479020e+02    # (T^_d)_{33}
Block te Q= 1.10909256e+03   # super CKM trilinear matrix - DRbar
  1  1    -1.07283338e-02    # (T^_e)_{11}
  1  2    -7.47043407e-20    # (T^_e)_{12}
  1  3     0.00000000e+00    # (T^_e)_{13}
  2  1    -3.59617196e-22    # (T^_e)_{21}
  2  2    -2.21851588e+00    # (T^_e)_{22}
  2  3     0.00000000e+00    # (T^_e)_{23}
  3  1     0.00000000e+00    # (T^_e)_{31}
  3  2     0.00000000e+00    # (T^_e)_{32}
  3  3    -3.84147479e+01    # (T^_e)_{33}
Block VCKM Q= 1.10909256e+03 # DRbar CKM mixing matrix
  1  1     9.73840760e-01    # CKM_{11} matrix element
  1  2     2.27197319e-01    # CKM_{12} matrix element
  1  3     3.94378177e-03    # CKM_{13} matrix element
  2  1    -2.27161574e-01    # CKM_{21} matrix element
  2  2     9.72963576e-01    # CKM_{22} matrix element
  2  3     4.17072928e-02    # CKM_{23} matrix element
  3  1     5.63862908e-03    # CKM_{31} matrix element
  3  2    -4.15121374e-02    # CKM_{32} matrix element
  3  3     9.99122089e-01    # CKM_{33} matrix element
Block msoft Q= 1.10909256e+03 # MSSM DRbar SUSY breaking parameters
     1     2.77453239e+02     # M_1(Q)
     2     5.09254970e+02     # M_2(Q)
     3     1.42038618e+03     # M_3(Q)
    21     1.82209263e+05     # mH1^2(Q)
    22    -6.15599820e+05     # mH2^2(Q)
Block USQMIX  # super CKM squark mass^2 matrix
  1  1     1.92494851e-05   # (USQMIX)_{11}
  1  2     2.03833321e-04   # (USQMIX)_{12}
  1  3     3.63166495e-01   # (USQMIX)_{13}
  1  4     1.05672600e-10   # (USQMIX)_{14}
  1  5     5.13217290e-07   # (USQMIX)_{15}
  1  6     9.31724238e-01   # (USQMIX)_{16}
  2  1     1.28308062e-04   # (USQMIX)_{21}
  2  2     1.35795596e-03   # (USQMIX)_{22}
  2  3     9.31723289e-01   # (USQMIX)_{23}
  2  4     2.76975776e-09   # (USQMIX)_{24}
  2  5     1.34302103e-05   # (USQMIX)_{25}
  2  6    -3.63166425e-01   # (USQMIX)_{26}
  3  1     1.19914230e-07   # (USQMIX)_{31}
  3  2     6.51758777e-03   # (USQMIX)_{32}
  3  3    -2.14281846e-05   # (USQMIX)_{33}
  3  4     1.90545853e-08   # (USQMIX)_{34}
  3  5     9.99978760e-01   # (USQMIX)_{35}
  3  6     6.37558645e-06   # (USQMIX)_{36}
  4  1     1.42277576e-05   # (USQMIX)_{41}
  4  2     1.37617122e-10   # (USQMIX)_{42}
  4  3    -4.41933274e-09   # (USQMIX)_{43}
  4  4     1.00000000e+00   # (USQMIX)_{44}
  4  5    -1.90576962e-08   # (USQMIX)_{45}
  4  6     1.31518067e-09   # (USQMIX)_{46}
  5  1     1.35681661e-01   # (USQMIX)_{51}
  5  2     9.90730483e-01   # (USQMIX)_{52}
  5  3    -1.34393978e-03   # (USQMIX)_{53}
  5  4    -1.93071153e-06   # (USQMIX)_{54}
  5  5    -6.45735704e-03   # (USQMIX)_{55}
  5  6     3.04297682e-04   # (USQMIX)_{56}
  6  1     9.90752477e-01   # (USQMIX)_{61}
  6  2    -1.35678830e-01   # (USQMIX)_{62}
  6  3     5.63305241e-05   # (USQMIX)_{63}
  6  4    -1.40961503e-05   # (USQMIX)_{64}
  6  5     8.84199945e-04   # (USQMIX)_{65}
  6  6    -1.27434930e-05   # (USQMIX)_{66}
Block DSQMIX  # super CKM squark mass^2 matrix
  1  1     4.67842384e-03   # (DSQMIX)_{11}
  1  2    -3.44438991e-02   # (DSQMIX)_{12}
  1  3     9.83131665e-01   # (DSQMIX)_{13}
  1  4     7.83734767e-07   # (DSQMIX)_{14}
  1  5    -1.26345246e-04   # (DSQMIX)_{15}
  1  6     1.79565706e-01   # (DSQMIX)_{16}
  2  1    -1.40059893e-03   # (DSQMIX)_{21}
  2  2     1.03122440e-02   # (DSQMIX)_{22}
  2  3    -1.79308438e-01   # (DSQMIX)_{23}
  2  4    -1.42953351e-06   # (DSQMIX)_{24}
  2  5     2.30530043e-04   # (DSQMIX)_{25}
  2  6     9.83737834e-01   # (DSQMIX)_{26}
  3  1     1.31566384e-06   # (DSQMIX)_{31}
  3  2     3.39075399e-03   # (DSQMIX)_{32}
  3  3     2.87037823e-04   # (DSQMIX)_{33}
  3  4     3.39862835e-06   # (DSQMIX)_{34}
  3  5     9.99994187e-01   # (DSQMIX)_{35}
  3  6    -2.17562877e-04   # (DSQMIX)_{36}
  4  1     1.55307129e-04   # (DSQMIX)_{41}
  4  2     4.85345405e-08   # (DSQMIX)_{42}
  4  3    -1.78152283e-06   # (DSQMIX)_{43}
  4  4     9.99999988e-01   # (DSQMIX)_{44}
  4  5    -3.39821192e-06   # (DSQMIX)_{45}
  4  6     1.34984877e-06   # (DSQMIX)_{46}
  5  1    -1.35198468e-01   # (DSQMIX)_{51}
  5  2     9.90148229e-01   # (DSQMIX)_{52}
  5  3     3.60628568e-02   # (DSQMIX)_{53}
  5  4     2.10074266e-05   # (DSQMIX)_{54}
  5  5    -3.36841203e-03   # (DSQMIX)_{55}
  5  6    -3.99787190e-03   # (DSQMIX)_{56}
  6  1     9.90806490e-01   # (DSQMIX)_{61}
  6  2     1.35285858e-01   # (DSQMIX)_{62}
  6  3     2.52290160e-05   # (DSQMIX)_{63}
  6  4    -1.53887394e-04   # (DSQMIX)_{64}
  6  5    -4.60034631e-04   # (DSQMIX)_{65}
  6  6    -2.79409518e-06   # (DSQMIX)_{66}
Block RVLMIX  # charged higgs-slepton mixing matrix 
  1 1    0.00000000e+00   # C_{11}
  1 2    0.00000000e+00   # C_{12}
  1 3    0.00000000e+00   # C_{13}
  1 4    0.00000000e+00   # C_{14}
  1 5    1.11571931e-01   # C_{15}
  1 6    0.00000000e+00   # C_{16}
  1 7    0.00000000e+00   # C_{17}
  1 8    9.93756361e-01   # C_{18}
  2 1    0.00000000e+00   # C_{21}
  2 2    0.00000000e+00   # C_{22}
  2 3    3.18983965e-05   # C_{23}
  2 4   -2.19428333e-18   # C_{24}
  2 5    0.00000000e+00   # C_{25}
  2 6    9.99999999e-01   # C_{26}
  2 7   -8.22292286e-17   # C_{27}
  2 8    0.00000000e+00   # C_{28}
  3 1    0.00000000e+00   # C_{31}
  3 2    0.00000000e+00   # C_{32}
  3 3    8.80797885e-21   # C_{33}
  3 4    6.59776160e-03   # C_{34}
  3 5    0.00000000e+00   # C_{35}
  3 6    8.22419160e-17   # C_{36}
  3 7    9.99978235e-01   # C_{37}
  3 8    0.00000000e+00   # C_{38}
  4 1    0.00000000e+00   # C_{41}
  4 2    0.00000000e+00   # C_{42}
  4 3    9.99999999e-01   # C_{43}
  4 4    2.72125071e-19   # C_{44}
  4 5    0.00000000e+00   # C_{45}
  4 6   -3.18983965e-05   # C_{46}
  4 7   -7.98018363e-21   # C_{47}
  4 8    0.00000000e+00   # C_{48}
  5 1    0.00000000e+00   # C_{51}
  5 2    0.00000000e+00   # C_{52}
  5 3   -2.72119112e-19   # C_{53}
  5 4    9.99978235e-01   # C_{54}
  5 5    0.00000000e+00   # C_{55}
  5 6    1.65171540e-18   # C_{56}
  5 7   -6.59776160e-03   # C_{57}
  5 8    0.00000000e+00   # C_{58}
  6 1    0.00000000e+00   # C_{61}
  6 2    0.00000000e+00   # C_{62}
  6 3    0.00000000e+00   # C_{63}
  6 4    0.00000000e+00   # C_{64}
  6 5    9.93756361e-01   # C_{65}
  6 6    0.00000000e+00   # C_{66}
  6 7    0.00000000e+00   # C_{67}
  6 8   -1.11571931e-01   # C_{68}
  7 1    9.94660799e-01   # C_{71}
  7 2    1.03198325e-01   # C_{72}
  7 3    0.00000000e+00   # C_{73}
  7 4    0.00000000e+00   # C_{74}
  7 5    0.00000000e+00   # C_{75}
  7 6    0.00000000e+00   # C_{76}
  7 7    0.00000000e+00   # C_{77}
  7 8    0.00000000e+00   # C_{78}
Block RVHMIX  # CP-even neutral scalar mixing matrix 
  1 1    1.05018939e-01   # curlyN_{11}
  1 2    9.94470222e-01   # curlyN_{12}
  1 3   -9.49653250e-21   # curlyN_{13}
  1 4   -1.31574343e-08   # curlyN_{14}
  1 5    0.00000000e+00   # curlyN_{15}
  2 1    0.00000000e+00   # curlyN_{21}
  2 2    0.00000000e+00   # curlyN_{22}
  2 3    0.00000000e+00   # curlyN_{23}
  2 4    0.00000000e+00   # curlyN_{24}
  2 5    1.00000000e+00   # curlyN_{25}
  3 1   -4.71054615e-08   # curlyN_{31}
  3 2    1.82050699e-08   # curlyN_{32}
  3 3   -2.74016734e-19   # curlyN_{33}
  3 4    1.00000000e+00   # curlyN_{34}
  3 5    0.00000000e+00   # curlyN_{35}
  4 1    1.07690914e-21   # curlyN_{41}
  4 2    9.43561712e-21   # curlyN_{42}
  4 3    1.00000000e+00   # curlyN_{43}
  4 4    2.74016734e-19   # curlyN_{44}
  4 5    0.00000000e+00   # curlyN_{45}
  5 1    9.94470222e-01   # curlyN_{51}
  5 2   -1.05018939e-01   # curlyN_{52}
  5 3   -8.00489353e-23   # curlyN_{53}
  5 4    4.87568558e-08   # curlyN_{54}
  5 5    0.00000000e+00   # curlyN_{55}
Block RVAMIX  # CP-odd neutral scalar mixing matrix 
  1 1    0.00000000e+00   # curlyN~_{11}
  1 2    0.00000000e+00   # curlyN~_{12}
  1 3    0.00000000e+00   # curlyN~_{13}
  1 4    0.00000000e+00   # curlyN~_{14}
  1 5    1.00000000e+00   # curlyN~_{15}
  2 1   -4.71989640e-08   # curlyN~_{21}
  2 2   -1.78434841e-08   # curlyN~_{22}
  2 3   -2.74016558e-19   # curlyN~_{23}
  2 4    1.00000000e+00   # curlyN~_{24}
  2 5    0.00000000e+00   # curlyN~_{25}
  3 1    1.05627689e-21   # curlyN~_{31}
  3 2   -9.45463881e-21   # curlyN~_{32}
  3 3    1.00000000e+00   # curlyN~_{33}
  3 4    2.74016558e-19   # curlyN~_{34}
  3 5    0.00000000e+00   # curlyN~_{35}
  4 1    9.94660796e-01   # curlyN~_{41}
  4 2    1.03198358e-01   # curlyN~_{42}
  4 3   -7.49473813e-23   # curlyN~_{43}
  4 4    4.87883774e-08   # curlyN~_{44}
  4 5    0.00000000e+00   # curlyN~_{45}
