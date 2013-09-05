# run cmssw analysis
#!/usr/bin/env python
import FWCore.ParameterSet.Config as cms
import os
import sys
sys.path.append(os.getenv('CMSSW_BASE')+'/MyCMSSWAnalysisTools/Tools')
import  cmsswAnalysisTools
import testSamp
cfg = '../../DiLeptonicSelection/patRefSel_diLep_cfg.py'
myAnalysis = cmsswAnalysisTools.cmsswAnalysis(testSamp.testFiles,cfg)
myAnalysis.readOpts()
myAnalysis.startAnalysis()
