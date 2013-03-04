/*#######################################################################
#                                                                       #
    W r a p p e r s                           

    Python wrapper for SoftSUSY.
    Project: SuperPy.
    Author: Andrew Fowlie, University of Sheffield.
    Version: 1.0
    Date: 03/13
#                                                                       #
#######################################################################*/

#include <Python.h> // Include Python headers.
#include <mycomplex.h>
#include <def.h>
#include <linalg.h>
#include <lowe.h>
#include <rge.h>
#include <softsusy.h>
#include <softpars.h>
#include <susy.h>
#include <utils.h>
#include <numerics.h>
#include <rpvsoft.h>
#include <twoloophiggs.h>
 
static PyObject* cmssm(PyObject* self, PyObject* args)
{
  // CMSSM parameters.
  double m12, a0, mGutGuess = 2.0e16, tanb, m0;
  int sgnMu = 1;
  bool uni = true; // MGUT defined by g1(MGUT)=g2(MGUT).
  // Most important Standard Model inputs: you may change these and recompile.
  double alphasMZ = 0.1184, mtop = 173.5, mbmb = 4.18; // PDG Dec/12.
  
  // If there are 4 double argumnents ("dddd"), pass them to inputs. Else return.
  if (!PyArg_ParseTuple(args, "dddd", &m0, &m12, &a0, &tanb))
        return NULL;

  // Sets up exception handling.
  signal(SIGFPE, FPE_ExceptionHandler); 

  // Sets format of output: 6 decimal places.
  outputCharacteristics(6);

  QedQcd oneset;      // See "lowe.h" for default definitions parameters.
  oneset.setAlpha(ALPHAS, alphasMZ);
  oneset.setPoleMt(mtop);
  oneset.setMass(mBottom, mbmb);
  oneset.toMz();      // Runs SM fermion masses to MZ.

  // Preparation for calculation: set up object and input parameters.
  MssmSoftsusy r; 
  DoubleVector pars(3); 
  pars(1) = m0; pars(2) = m12; pars(3) = a0;

  // Calculate the spectrum
  r.lowOrg(sugraBcs, mGutGuess, pars, sgnMu, tanb, oneset, uni);
  
  // Output in SLHA to a string, via an ostringstream.
  ostringstream stream;
  r.lesHouchesAccordOutput(stream, "sugra", pars, sgnMu, tanb, 0,  
			      1, mGutGuess, false);
  string slha = stream.str(); 	 
  
  // Check physicality of point.
  string problem="None";
  if (r.displayProblem().test()){    
    stream << r.displayProblem();
    problem = stream.str(); 
  }
  
  // Note the LSP.
  int posj = 0, posi = 0; double mass = 0;
  int temp = r.lsp(mass, posi, posj); // Find LSP indices.
  string lsp = recogLsp(temp, posj); // Convert LSP indices into its name.
  
  // Return spectrum, physicality, problem and LSP to Python as three strings ("sss").
  return Py_BuildValue("sss", slha.c_str(), problem.c_str(), lsp.c_str());
  
  Py_RETURN_NONE;
}
 
// Define available methods, and initial method. Do not alter. 
 
static PyMethodDef softsusyMethods[] =
{
     {"cmssm", cmssm, METH_VARARGS, "Calculate SOFTSUSY CMSSM spectrum."},
     {NULL, NULL, 0, NULL}
};
 
PyMODINIT_FUNC
 
initsoftsusy(void)
{
     (void) Py_InitModule("softsusy", softsusyMethods);
}
