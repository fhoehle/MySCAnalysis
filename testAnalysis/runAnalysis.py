#!/usr/bin/env python
# run cmssw analysis
import FWCore.ParameterSet.Config as cms
import os,sys
sys.path.append(os.getenv('CMSSW_BASE')+'/MyCMSSWAnalysisTools/Tools')
import  cmsswAnalysisTools
import testSamples
cfg = '../../DiLeptonicSelection/patRefSel_diLep_cfg.py'
myAnalysis = cmsswAnalysisTools.cmsswAnalysis(testSamples.testFiles,cfg)
myAnalysis.readOpts()
myAnalysis.startAnalysis()
