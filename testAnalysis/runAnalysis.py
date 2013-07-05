# run cmssw analysis
import FWCore.ParameterSet.Config as cms
import sys,imp,subprocess,os,getopt,re
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
options ={}
options["maxEvents"]=1000
for opt in addOptions.split():
  reOpt = re.match('([^=]*)=([^=]*)',opt)
  if options.has_key(reOpt.group(1)):
    options[reOpt.group(1)]=reOpt.group(2)
processSample =  myTools.processSample('../../DiLeptonicSelection/patRefSel_diLep_cfg.py')
for postfix,filename in [ (p,f) for p,f in testSamples.testFiles.iteritems()]: 
  sample = myTools.sample(filename,postfix,int(options["maxEvents"]))
  print "processing ",postfix," ",filename,"  "
  processSample.runSample(sample,True)
processSample.end()
#processSample =  myTools.processSample('../DiLeptonicSelection/patRefSel_diLep_cfg.py')
