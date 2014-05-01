#!/usr/bin/env python
import FWCore.ParameterSet.Config as cms
import os
import sys
sys.path.append(os.getenv('CMSSW_BASE')+'/MyCMSSWAnalysisTools/Tools')
import  cmsswAnalysisTools
import dataSamples
import dataDatasets
cfg = os.getenv('CMSSW_BASE')+'/DiLeptonicSelection/patRefSel_diLep_cfg.py'
#myAnalysis = cmsswAnalysisTools.cmsswAnalysis(dataSamples.dataDatasets,cfg)
myAnalysis = cmsswAnalysisTools.cmsswAnalysis(dataDatasets.dataDatasets,cfg)
sys.argv.append('--runOnData')
myAnalysis.readOpts()
myAnalysis.startAnalysis()
