# run cmssw analysis
def removeAddOptions(toRemove,options):
  for key in toRemove:
   options = re.sub(key+'=[^\ ]*','',options)
  return options
import FWCore.ParameterSet.Config as cms
import sys,imp,subprocess,os,getopt,re,signal,json
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
import datetime,time
timeStamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d_%H-%M-%S')
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
import shutil
cfg = '../../DiLeptonicSelection/patRefSel_diLep_cfg.py'
tmpCfg = options["outputPath"]+ os.path.splitext(os.path.basename(cfg))[0]+"_"+timeStamp + os.path.splitext(os.path.basename(cfg))[1]
os.makedirs(os.path.dirname(tmpCfg))
shutil.copyfile(cfg,tmpCfg)
remainingOptions = removeAddOptions(options.keys(),addOptions)
if remainingOptions != '' and not remainingOptions.isspace():
  tmpCfgDumpPython = os.path.splitext(tmpCfg)[0]+"_addedDumpLine"+os.path.splitext(tmpCfg)[1]
  tmpCfgAddLine = open(tmpCfg,"a");tmpCfgAddLine.write('myTmpFile = open ("'+tmpCfgDumpPython+'","w"); myTmpFile.write(process.dumpPython()); myTmpFile.close()');tmpCfgAddLine.close()
  import subprocess
  buildFile = subprocess.Popen(["python "+tmpCfg+" "+removeAddOptions(options.keys(),addOptions)],shell=True,stdout=subprocess.PIPE,env=os.environ)
  buildFile.wait()
  errorcode = buildFile.returncode
  if errorcode != 0:
    sys.exit("failed building config with "+str(errorcode))
    cfg = tmpCfgDumpPython
  else:
    print "python cfg creation done"
else:
  cfg = tmpCfg
### json output
bookKeeping = myTools.bookKeeping()
### start processing sample
processSample = myTools.processSample(cfg)
for postfix,filename in [ (p,f) for p,f in signalSamples.testFiles.iteritems()]: 
  sample = myTools.sample(filename,postfix,int(options["maxEvents"]))
  processSample.applyChanges(sample,True,options["outputPath"])
  bookKeeping.numInputEvts(processSample.tmpCfgFileLoaded,postfix)
  print "processing ",postfix," ",filename,"  ",options["outputPath"]
  processSample.runSample(sample,True,options["outputPath"])
processSample.end()
## save bookKeeping
bookKeeping.save(options["outputPath"],timeStamp)
#processSample =  myTools.processSample('../DiLeptonicSelection/patRefSel_diLep_cfg.py')
