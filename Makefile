#########################################################################
#                                                                       #
#     M a k e f i l e

#    Project: SuperPy.
#    Author: Andrew Fowlie, University of Sheffield.
#    Version: 1.0.
#    Date: 03/13.

#                                                                       #
#########################################################################


# SuperPy - compile the codes. You might need to tweak individual makefiles
# for your own system. You will need LAPACK, gcc compilers and python and python-dev.

default: all

all: multinest softsusy multinest_bridge python micromegas superiso feynhiggs

multinest:
	make -C MultiNest_v* libnest3.so

softsusy:
	cd ./softsusy-*; ./configure F77=gfortran # Neccesary on my Ubuntu install.
	make -C softsusy-*

feynhiggs:
	cd ./FeynHiggs-*; ./configure
	make -C FeynHiggs-*
	cd ./FeynHiggs-*; make install
	cd ./FeynHiggs-*; gfortran -o SuperPyFH -Ibuild example/SuperPy.F -Lbuild -lFH

micromegas:
	make -C micromegas_*
	make -C micromegas_*/MSSM main=main.c

superiso:
	make -C superiso_v*
	make -C superiso_v* slha.c

# Requires LAPACK.
# You might need to alter MULTINEST_CALL=__nested_MOD_nestrun.
# Check what the relevant routine is called: nm ./MultiNest_v*/libnest3.so | grep run
multinest_bridge:
	export MULTINEST=$PWD/MultiNest_v*
	make -C ./PyMultiNest-master/multinest_bridge MULTINEST_CALL=__nested_MOD_nestrun
	export LD_LIBRARY_PATH=$PWD/MultiNest_v*:$PWD/PyMultiNest-master/multinest_bridge:$LD_LIBRARY_PATH

# Build the Python libraries. You might need to sudo these commands.
# Also, if you have your own machine, rather than a networked machine,
# you might want to install things globally, rather than locally, by
# removing the --user argument.

python:
	cd ./pyslha-*; python setup.py install --user
	cd ./PyMultiNest-master; python setup.py install --user

clean:
	make -C MultiNest_v* clean
	make -C softsusy-* clean
	make -C FeynHiggs-* clean
	make -C micromegas_* clean
	make -C superiso_v* clean
	make -C ./PyMultiNest-master/multinest_bridge clean
	rm *~ *.pyc
