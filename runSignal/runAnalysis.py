#!/usr/bin/env python
# run cmssw analysis
import FWCore.ParameterSet.Config as cms
import os
import sys
sys.path.append(os.getenv('CMSSW_BASE')+'/MyCMSSWAnalysisTools/Tools')
import  cmsswAnalysisTools
import signalSamples
cfg = os.getenv('CMSSW_BASE')+'/DiLeptonicSelection/patRefSel_diLep_cfg.py'
myAnalysis = cmsswAnalysisTools.cmsswAnalysis(signalSamples.testFiles,cfg)
myAnalysis.readOpts()
myAnalysis.startAnalysis()
