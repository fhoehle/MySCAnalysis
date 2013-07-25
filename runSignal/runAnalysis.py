# run cmssw analysis
import FWCore.ParameterSet.Config as cms
import sys,imp,subprocess,os,getopt,re
sys.path.append(os.getenv('CMSSW_BASE')+'/MyCMSSWAnalysisTools/Tools')
import tools as myTools
import signalSamples
opts, args = getopt.getopt(sys.argv[1:], '',['addOptions=','noTimeStamp','help'])
print sys.argv
cfgFileName=None
numProcesses=2
numJobs=2
addOptions=''
noTimeStamp = False
for opt,arg in opts:
 if opt in ("--addOptions"):
   addOptions=arg
   sys.argv.remove(arg); sys.argv.remove("--addOptions")
 if opt in ("--noTimeStamp"):
   noTimeStamp = True
   sys.argv.remove("--noTimeStamp")
 if opt in ("--help"):
   print 'python runAnalysis.py --addOptions \"maxEvents=1 outputPath=/net/scratch_cms/institut_3b/hoehle/hoehle/tmp\"'
   sys.exit(0)
options ={}
options["maxEvents"]=1000
options["outputPath"]=os.getenv("PWD")
for opt in addOptions.split():
  reOpt = re.match('([^=]*)=([^=]*)',opt)
  if options.has_key(reOpt.group(1)):
    options[reOpt.group(1)]=reOpt.group(2)
if options["outputPath"] != os.getenv("PWD"):
  if not noTimeStamp:
    import datetime,time  
    options["outputPath"]= os.path.realpath(options["outputPath"])+"_"+datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d_%H-%M-%S')+os.path.sep 
    print options["outputPath"]
processSample =  myTools.processSample('../../DiLeptonicSelection/patRefSel_diLep_cfg.py')
for postfix,filename in [ (p,f) for p,f in signalSamples.testFiles.iteritems()]: 
  sample = myTools.sample(filename,postfix,int(options["maxEvents"]))
  print "processing ",postfix," ",filename,"  ",options["outputPath"]
  processSample.runSample(sample,True,options["outputPath"])
processSample.end()
#processSample =  myTools.processSample('../DiLeptonicSelection/patRefSel_diLep_cfg.py')
