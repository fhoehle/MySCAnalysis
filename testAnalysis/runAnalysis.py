# run cmssw analysis
import FWCore.ParameterSet.Config as cms
import sys,imp,subprocess,os,getopt,re
sys.path.append(os.getenv('CMSSW_BASE')+'/MyCMSSWAnalysisTools/Tools')
import tools as myTools
import testSamples
opts, args = getopt.getopt(sys.argv[1:], '',['addOptions=','noTimeStamp','help','runGrid'])
print sys.argv
cfgFileName=None
numProcesses=2
numJobs=2
addOptions=''
runGrid = False
noTimeStamp = False
for opt,arg in opts:
 if opt in ("--addOptions"):
   addOptions=arg
   sys.argv.remove(arg); sys.argv.remove("--addOptions")
 if opt in ("--noTimeStamp"):
   noTimeStamp = True
   sys.argv.remove("--noTimeStamp")
 if opt in ("--runGrid"):
   runGrid = True
   sys.argv.remove("--runGrid")
 if opt in ("--help"):
   print 'python runAnalysis.py --addOptions \"maxEvents=1 outputPath=/net/scratch_cms/institut_3b/hoehle/hoehle/tmp\"'
   sys.exit(0)
options ={}
options["maxEvents"]=1000
options["outputPath"]=os.getenv("PWD")
timeStamp = myTools.getTimeStamp()
for opt in addOptions.split():
  reOpt = re.match('([^=]*)=([^=]*)',opt)
  if options.has_key(reOpt.group(1)):
    options[reOpt.group(1)]=reOpt.group(2)
if options["outputPath"] != os.getenv("PWD"):
  if not noTimeStamp:
    options["outputPath"]= os.path.realpath(options["outputPath"])+"_"+timeStamp+os.path.sep 
    print options["outputPath"]
## preparing cfg with additional options
#make tmp copy
cfg = '../../DiLeptonicSelection/patRefSel_diLep_cfg.py'
cfg = myTools.createWorkDirCpCfg(options["outputPath"],cfg,timeStamp)
cfg = myTools.compileCfg(cfg,options,addOptions)
### json output
bookKeeping = myTools.bookKeeping()
processSample =  myTools.processSample(cfg)
### json output
bookKeeping = myTools.bookKeeping()
####
for postfix,sampDict in testSamples.testFiles.iteritems(): 
  sample = myTools.sample(sampDict["localFile"],sampDict["label"],sampDict["xSec"],postfix,int(options["maxEvents"]))
  processSample.applyChanges(sample)
  print "processing ",postfix," ",sampDict["localFile"]
  if not runGrid:
    processSample.runSample()
    bookKeeping.bookKeep(processSample)
  else:
    processSample.setOutputFilesGrid()
    processSample.createNewCfg(sample,True,options["outputPath"])
    bookKeeping.bookKeep(processSample)
    sys.path.append(os.getenv('CMSSW_BASE')+os.path.sep+'MyCMSSWAnalysisTools')
    import CrabTools
    sample.getSampleName()
    crabP = CrabTools.crabProcess(postfix,processSample.newCfgName,sample.dataset,options["outputPath"],timeStamp,addGridDir="test")
    crabP.createCrabCfg()
    if sampDict.has_key("crabConfig"):
      for k1 in sampDict["crabConfig"].keys():
        for k2 in sampDict["crabConfig"][k1].keys():
          crabP.crabCfg[k1][k2]=sampDict["crabConfig"][k1][k2]
    crabP.crabCfg["CMSSW"]["total_number_of_events"]=1000000
    crabP.crabCfg["CMSSW"]["number_of_jobs"]= 100
    crabCfgFilename = crabP.createCrabDir()
    crabP.writeCrabCfg()
    crabP.executeCrabCommand("-create",debug = True) 
    CrabTools.saveCrabProp(crabP,options["outputPath"]+"/"+postfix+"_"+timeStamp+"_CrabCfg.json")
    crabP.executeCrabCommand("-submit",debug = True)
    #crabP.executeCrabCommand("-status")
processSample.end()
##
bookKeeping.save(options["outputPath"]+'/',timeStamp)
