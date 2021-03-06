* dse_G0G0.F
* generated 30-May-2012 12:10
* this file is part of FeynHiggs
* please do not edit directly

#include "externals.h"
#include "types.h"


	ComplexType function dse_G0G0(k2,bX)
	implicit none
	integer bX
	RealType k2

#include "FH.h"
#include "looptools.h"

	integer All3, All4, Cha3, Cha4, Gen3, Ind1, Ind2, Ind3, Ind4
	integer Neu3, Neu4, Sfe3, Sfe4

	ComplexType dup1, dup10, dup11, dup12, dup13, dup14, dup2
	ComplexType dup3, dup4, dup5, dup6, dup7, dup8, dup9, tmp1
	ComplexType tmp2

	dse_G0G0 = 0

	LOOP(Gen3, gM,3,1)

        dse_G0G0 = dse_G0G0 - 
     &    3/(4.D0*Pi)*(Alfa1L*
     &        (B1(k2,Mf2(tM,Gen3),Mf2(tM,Gen3)) + 
     &          k2*DB1(k2,Mf2(tM,Gen3),Mf2(tM,Gen3)))*Mf2(tM,Gen3))
     &       /(MW2*SW2)

	ENDLOOP(Gen3)

	LOOP(All4, 1,6,gM)
	LOOP(All3, 1,6,gM)

	tmp1 = DB0(k2,MASf2(All3,tM),MASf2(All4,tM))

	LOOP(Ind4, 1,3,1)
	LOOP(Ind3, 1,3,1)
	LOOP(Ind2, 1,3,1)
	LOOP(Ind1, 1,3,1)

        dse_G0G0 = dse_G0G0 - 
     &    3/(16.D0*Pi)*(Alfa1L*tmp1*
     &        ((TB*Kf(Ind3,Ind4,tM) - 
     &             MUEC*Delta(Ind3,Ind4)*Mf(tM,Ind3))*
     &           UASf(All4,3 + Ind4,tM)*UASfC(All3,Ind3,tM) + 
     &          (-(TB*KfC(Ind4,Ind3,tM)) + 
     &             MUE*Delta(Ind3,Ind4)*Mf(tM,Ind3))*
     &           UASf(All4,Ind4,tM)*UASfC(All3,3 + Ind3,tM))*
     &        ((TB*Kf(Ind1,Ind2,tM) - 
     &             MUEC*Delta(Ind1,Ind2)*Mf(tM,Ind1))*
     &           UASf(All3,3 + Ind2,tM)*UASfC(All4,Ind1,tM) + 
     &          (-(TB*KfC(Ind2,Ind1,tM)) + 
     &             MUE*Delta(Ind1,Ind2)*Mf(tM,Ind1))*
     &           UASf(All3,Ind2,tM)*UASfC(All4,3 + Ind1,tM)))/
     &      (MW2*SW2*TB2)

	ENDLOOP(Ind1)
	ENDLOOP(Ind2)
	ENDLOOP(Ind3)
	ENDLOOP(Ind4)

	ENDLOOP(All3)
	ENDLOOP(All4)

#ifdef DETAILED_DEBUG
	DHIGGS "dse_G0G0 =", dse_G0G0 ENDL
#endif

	if( mssmpart .eq. 1 ) return

	LOOP(Gen3, gM,3,1)

        dse_G0G0 = dse_G0G0 - 
     &    3/(4.D0*Pi)*(Alfa1L*
     &        (B1(k2,Mf2(bX,Gen3),Mf2(bX,Gen3)) + 
     &          k2*DB1(k2,Mf2(bX,Gen3),Mf2(bX,Gen3)))*Mf2(bX,Gen3))
     &       /(MW2*SW2)

	ENDLOOP(Gen3)

	LOOP(All4, 1,6,gM)
	LOOP(All3, 1,6,gM)

	tmp2 = DB0(k2,MASf2(All3,bX),MASf2(All4,bX))

	LOOP(Ind4, 1,3,1)
	LOOP(Ind3, 1,3,1)
	LOOP(Ind2, 1,3,1)
	LOOP(Ind1, 1,3,1)

        dse_G0G0 = dse_G0G0 + 
     &    3/(16.D0*Pi)*(Alfa1L*tmp2*
     &        ((Kf(Ind3,Ind4,bX) - 
     &             MUEC*TB*Delta(Ind3,Ind4)*Mf(bX,Ind3))*
     &           UASf(All4,3 + Ind4,bX)*UASfC(All3,Ind3,bX) + 
     &          (-KfC(Ind4,Ind3,bX) + 
     &             MUE*TB*Delta(Ind3,Ind4)*Mf(bX,Ind3))*
     &           UASf(All4,Ind4,bX)*UASfC(All3,3 + Ind3,bX))*
     &        ((-Kf(Ind1,Ind2,bX) + 
     &             MUEC*TB*Delta(Ind1,Ind2)*Mf(bX,Ind1))*
     &           UASf(All3,3 + Ind2,bX)*UASfC(All4,Ind1,bX) + 
     &          (KfC(Ind2,Ind1,bX) - 
     &             MUE*TB*Delta(Ind1,Ind2)*Mf(bX,Ind1))*
     &           UASf(All3,Ind2,bX)*UASfC(All4,3 + Ind1,bX)))/
     &      (MW2*SW2)

	ENDLOOP(Ind1)
	ENDLOOP(Ind2)
	ENDLOOP(Ind3)
	ENDLOOP(Ind4)

	ENDLOOP(All3)
	ENDLOOP(All4)

#ifdef DETAILED_DEBUG
	DHIGGS "dse_G0G0 =", dse_G0G0 ENDL
#endif

	if( mssmpart .eq. 2 ) return

	LOOP(Gen3, 1,3,1)

        dse_G0G0 = dse_G0G0 - 
     &    1/(4.D0*Pi)*(Alfa1L*
     &        (B1(k2,Mf2(2,Gen3),Mf2(2,Gen3)) + 
     &          k2*DB1(k2,Mf2(2,Gen3),Mf2(2,Gen3)))*Mf2(2,Gen3))/
     &      (MW2*SW2)

	ENDLOOP(Gen3)

	LOOP(Sfe4, 1,2,1)
	LOOP(Sfe3, 1,2,1)
	LOOP(Gen3, 1,3,1)

	dup1 = -KfC(Gen3,Gen3,2) + MUE*TB*Mf(2,Gen3)

	dup2 = Kf(Gen3,Gen3,2) - MUEC*TB*Mf(2,Gen3)

        dse_G0G0 = dse_G0G0 - 
     &    1/(16.D0*Pi)*(Alfa1L*
     &        DB0(k2,MSf2(Sfe3,2,Gen3),MSf2(Sfe4,2,Gen3))*
     &        (dup2*USf(Sfe4,2,2,Gen3)*USfC(Sfe3,1,2,Gen3) + 
     &          dup1*USf(Sfe4,1,2,Gen3)*USfC(Sfe3,2,2,Gen3))*
     &        (dup2*USf(Sfe3,2,2,Gen3)*USfC(Sfe4,1,2,Gen3) + 
     &          dup1*USf(Sfe3,1,2,Gen3)*USfC(Sfe4,2,2,Gen3)))/
     &      (MW2*SW2)

	ENDLOOP(Gen3)
	ENDLOOP(Sfe3)
	ENDLOOP(Sfe4)

#ifdef DETAILED_DEBUG
	DHIGGS "dse_G0G0 =", dse_G0G0 ENDL
#endif

	if( mssmpart .eq. 3 ) return

        dse_G0G0 = dse_G0G0 + 
     &    1/(16.D0*Pi)*(Alfa1L*
     &        (MW2*S2B**2*(SAB**2*DB0(k2,MA02,Mh02) + 
     &             CAB**2*DB0(k2,MA02,MHH2)) + 
     &          (C2B**2*MW2*SAB**2 + CW2*(-(k2*SBA2) - Mh02*SBA2))*
     &           DB0(k2,Mh02,MZ2) - 
     &          (CBA2*CW2*(k2 + MHH2) - C2B**2*CAB**2*MW2)*
     &           DB0(k2,MHH2,MZ2) + 
     &          CW2*(-(SBA2*B0(k2,Mh02,MZ2)) - 
     &             CBA2*B0(k2,MHH2,MZ2) + 2*SBA2*B1(k2,Mh02,MZ2) - 
     &             2*CW2*(B0(k2,MW2,MW2) - 2*B1(k2,MW2,MW2) + 
     &                k2*DB0(k2,MW2,MW2)) + 
     &             2*k2*SBA2*DB1(k2,Mh02,MZ2) + 
     &             2*CBA2*
     &              (B1(k2,MHH2,MZ2) + k2*DB1(k2,MHH2,MZ2)) + 
     &             4*CW2*k2*DB1(k2,MW2,MW2))))/(CW2**2*SW2)

	LOOP(Cha4, 1,2,1)
	LOOP(Cha3, 1,2,1)

        dup3 = -(CB*UCha(Cha4,2)*VCha(Cha3,1)) + 
     &    SB*UCha(Cha4,1)*VCha(Cha3,2)

        dup4 = -(CB*UCha(Cha3,2)*VCha(Cha4,1)) + 
     &    SB*UCha(Cha3,1)*VCha(Cha4,2)

        dup5 = CB*UChaC(Cha4,2)*VChaC(Cha3,1) - 
     &    SB*UChaC(Cha4,1)*VChaC(Cha3,2)

        dup6 = CB*UChaC(Cha3,2)*VChaC(Cha4,1) - 
     &    SB*UChaC(Cha3,1)*VChaC(Cha4,2)

        dse_G0G0 = dse_G0G0 + 
     &    1/(4.D0*Pi)*(Alfa1L*
     &        ((dup3*dup5 + dup4*dup6)*
     &           (B1(k2,MCha2(Cha3),MCha2(Cha4)) + 
     &             k2*DB1(k2,MCha2(Cha3),MCha2(Cha4))) + 
     &          DB0(k2,MCha2(Cha3),MCha2(Cha4))*
     &           ((dup3*dup5 + dup4*dup6)*MCha2(Cha3) + 
     &             MCha(Cha3)*MCha(Cha4)*
     &              (dup5*dup6 + 
     &                (CB*UCha(Cha4,2)*VCha(Cha3,1) - 
     &                   SB*UCha(Cha4,1)*VCha(Cha3,2))*
     &                 (CB*UCha(Cha3,2)*VCha(Cha4,1) - 
     &                   SB*UCha(Cha3,1)*VCha(Cha4,2))))))/SW2

	ENDLOOP(Cha3)
	ENDLOOP(Cha4)

	LOOP(Neu4, 1,4,1)
	LOOP(Neu3, 1,4,1)

	dup7 = SW*ZNeu(Neu3,1) - CW*ZNeu(Neu3,2)

	dup8 = CB*ZNeu(Neu3,3) + SB*ZNeu(Neu3,4)

	dup9 = SW*ZNeu(Neu4,1) - CW*ZNeu(Neu4,2)

	dup10 = CB*ZNeu(Neu4,3) + SB*ZNeu(Neu4,4)

	dup11 = SW*ZNeuC(Neu3,1) - CW*ZNeuC(Neu3,2)

	dup12 = CB*ZNeuC(Neu3,3) + SB*ZNeuC(Neu3,4)

	dup13 = SW*ZNeuC(Neu4,1) - CW*ZNeuC(Neu4,2)

	dup14 = CB*ZNeuC(Neu4,3) + SB*ZNeuC(Neu4,4)

        dse_G0G0 = dse_G0G0 + 
     &    1/(16.D0*Pi)*(Alfa1L*
     &        (-2*(dup12*dup13 + dup11*dup14)*
     &           (dup10*dup7 + dup8*dup9)*
     &           (B1(k2,MNeu2(Neu3),MNeu2(Neu4)) + 
     &             k2*DB1(k2,MNeu2(Neu3),MNeu2(Neu4))) + 
     &          DB0(k2,MNeu2(Neu3),MNeu2(Neu4))*
     &           ((dup11**2*dup14**2 + 
     &                dup12*
     &                 (dup12*dup13**2 + 2*dup11*dup13*dup14) + 
     &                dup8**2*dup9**2 + 
     &                dup10*(dup10*dup7**2 + 2*dup7*dup8*dup9))*
     &              MNeu(Neu3)*MNeu(Neu4) - 
     &             2*(dup12*dup13 + dup11*dup14)*
     &              (dup10*dup7 + dup8*dup9)*MNeu2(Neu3))))/
     &      (CW2*SW2)

	ENDLOOP(Neu3)
	ENDLOOP(Neu4)

#ifdef DETAILED_DEBUG
	DHIGGS "dse_G0G0 =", dse_G0G0 ENDL
#endif

	end

