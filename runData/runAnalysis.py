#!/usr/bin/env python
import FWCore.ParameterSet.Config as cms
import os
import sys
sys.path.append(os.getenv('CMSSW_BASE')+'/MyCMSSWAnalysisTools/Tools')
import  cmsswAnalysisTools
import diLeptonData
cfg = os.getenv('CMSSW_BASE')+'/DiLeptonicSelection/patRefSel_diLep_cfg.py'
myAnalysis = cmsswAnalysisTools.cmsswAnalysis(diLeptonData.dataDatasets,cfg)
sys.argv.append('--runOnData')
myAnalysis.readOpts()
myAnalysis.startAnalysis()
