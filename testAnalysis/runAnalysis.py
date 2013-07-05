# run cmssw analysis
import FWCore.ParameterSet.Config as cms
import sys,imp,subprocess,os,getopt
sys.path.append(os.getenv('CMSSW_BASE')+'/MyCMSSWAnalysisTools/Tools')
import tools as myTools
import testSamples
opts, args = getopt.getopt(sys.argv[1:], '',['addOptions='])
print sys.argv
cfgFileName=None
numProcesses=2
numJobs=2
addOptions=''
for opt,arg in opts:
 if opt in ("--addOptions"):
   addOptions=arg
   sys.argv.remove(arg); sys.argv.remove("--addOptions")
processSample =  myTools.processSample('../../DiLeptonicSelection/patRefSel_diLep_cfg.py')
for postfix,filename in [ (p,f) for p,f in testSamples.testFiles.iteritems()]: 
  sample = myTools.sample(filename,postfix,1000)
  print "processing ",postfix," ",filename,"  "
  processSample.runSample(sample,True)
processSample.end()
#processSample =  myTools.processSample('../DiLeptonicSelection/patRefSel_diLep_cfg.py')
