# run cmssw analysis
import FWCore.ParameterSet.Config as cms
import sys,imp,subprocess,os,getopt,re
sys.path.append(os.getenv('CMSSW_BASE')+'/MyCMSSWAnalysisTools/Tools')
import tools as myTools
import testSamples
opts, args = getopt.getopt(sys.argv[1:], '',['addOptions=','help','runGrid','runParallel=','specificSamples=','dontExec'])
print sys.argv
cfgFileName=None
numProcesses=3
numJobs=2
runParallel=False
addOptions=''
runGrid = False
specificSamples = None
dontExec = False
for opt,arg in opts:
 if opt in ("--addOptions"):
   addOptions=arg
   myTools.removeOptFromArgv(opt,True)
 if opt in ("--runGrid"):
   runGrid = True
   myTools.removeOptFromArgv(opt)
 if opt in ("--dontExec"):
   dontExec = True; myTools.removeOptFromArgv(opt)
 if ("--runParallel") in opt:
   numProcesses =  int(arg) if arg != None  else numProcesses
   myTools.removeOptFromArgv(opt,arg != None)
   runParallel=True
 if ("--specificSamples") in opt:
   specificSamples = arg.split(",")
   myTools.removeOptFromArgv(opt,True)
 if opt in ("--help"):
   print 'python runAnalysis.py --specificSamples label1,label2 --runParallel 2 --runGrid --addOptions \"maxEvents=1 outputPath=/net/scratch_cms/institut_3b/hoehle/hoehle/tmp\"'
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
  options["outputPath"]= os.path.realpath(options["outputPath"])+"_"+timeStamp+os.path.sep 
  print options["outputPath"]
## preparing cfg with additional options
#make tmp copy
cfg = '../../DiLeptonicSelection/patRefSel_diLep_cfg.py'
cfg = myTools.createWorkDirCpCfg(options["outputPath"],cfg,timeStamp)
### json output
bookKeeping = myTools.bookKeeping()

### json output
bookKeeping = myTools.bookKeeping()
####
commandList = []
dontExecCrab = dontExec

for postfix,sampDict in testSamples.testFiles.iteritems()if specificSamples == None else [(p,s) for p,s in testSamples.testFiles.iteritems() if p in specificSamples ]:
  remainingOpts = myTools.removeAddOptions(options.keys(),addOptions+(" "+sampDict["addOptions"]) if sampDict.has_key("addOptions") else "")
  print "remainingOpts ",remainingOpts
  cfgSamp = myTools.compileCfg(cfg,remainingOpts,postfix ) 
  processSample =  myTools.processSample(cfgSamp)
  sample = myTools.sample(sampDict["localFile"],sampDict["label"],sampDict["xSec"],postfix,int(options["maxEvents"]))
  sample.__dict__["color"]=sampDict["color"]
  processSample.applyChanges(sample)
  print "processing ",postfix," ",sampDict["localFile"]
  sys.stdout.flush()
  if not runGrid:
    if not ( dontExec and not runParallel):
      commandList.append(processSample.runSample(not runParallel))
    bookKeeping.bookKeep(processSample)
  else:
    processSample.setOutputFilesGrid()
    processSample.createNewCfg()
    bookKeeping.bookKeep(processSample)
    sys.stdout.flush()
    sys.path.append(os.getenv('CMSSW_BASE')+os.path.sep+'MyCMSSWAnalysisTools')
    import CrabTools
    sample.setDataset()
    crabP = CrabTools.crabProcess(postfix,processSample.newCfgName,sample.dataset,options["outputPath"],timeStamp,addGridDir="test")
    crabP.setCrabDir(sample.postfix,timeStamp,options["outputPath"])
    crabP.createCrabCfg(sampDict.get("crabConfig"))
    crabCfgFilename = crabP.createCrabDir()
    crabP.writeCrabCfg()
    crabP.executeCrabCommand("-create",debug = True) 
    CrabTools.saveCrabProp(crabP,options["outputPath"]+"/"+postfix+"_"+timeStamp+"_CrabCfg.json")
    if not dontExecCrab:
      crabP.executeCrabCommand("-submit",debug = True)
      crabP.executeCrabCommand("-status")
processSample.end()
dontExecParallel = dontExec
if runParallel and len(commandList) > 0:
  print "running ",numProcesses," cmsRun in parallel"
  sys.path.append(os.getenv('CMSSW_BASE')+'/ParallelizationTools/BashParallel')
  import doWhatEverParallel
  if not dontExecParallel:
    doWhatEverParallel.execute(commandList,numProcesses)

##
bookKeeping.save(options["outputPath"]+'/',timeStamp)
   
