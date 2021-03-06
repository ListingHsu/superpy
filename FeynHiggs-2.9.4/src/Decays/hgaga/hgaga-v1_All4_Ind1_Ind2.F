#if 0
* hgaga-v1_All4_Ind1_Ind2.F
* form factors for {S[10, {hno}]} -> {V[1], V[1]}
* generated by FormCalc 7.5 on 27-Sep-2012 9:09
* this file is part of FeynHiggs
#endif

#include "hgaga-vars.h"

	subroutine hgaga_v1_All4_Ind1_Ind2
	implicit none

#include "hgaga-vars.h"

#include "inline.h"

        Cloop(1) = Cloop(1) + 
     &    1/(36.D0*Pi)*(Alfa0*EL0*hgagaSq*
     &        (SB*TB*(Pair1*lint17(All4) - 
     &             4*(Pair1*lint18(cc00,All4) + Abb2*Sub45(All4)))*
     &           Sub63(All4,Ind1,Ind2) + 
     &          4*CB*(Pair1*
     &              (-lint19(All4) + 4*lint20(cc00,All4)) + 
     &             4*Abb2*Sub64(All4))*Sub82(All4,Ind1,Ind2)))/
     &      (CW*MW*SB2*SW)

#ifdef DETAILED_DEBUG
	DCOUP "v1_All4_Ind1_Ind2: Cloop(1) =", Cloop(1) ENDL
#endif

	end
