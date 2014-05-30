import sys,os
sys.path.append(os.getenv('CMSSW_BASE')+'/MyCMSSWAnalysisTools')
import Tools
import Tools.lumiTools as lumiTools
import Tools.tools as tools
import Tools.coreTools as coreTools
import Tools.jsonTools as jsonTools
import Tools.runRangesManagment as runRangesManagment
import imp
testFile = os.getenv('CMSSW_BASE')+'/MySCAnalysis/runData/diLeptonData.py'
test = imp.load_source('module.name', testFile)
dataDatasets = test.dataDatasets
cfg = os.getenv('CMSSW_BASE')+'/DiLeptonicSelection/patRefSel_diLep_cfg.py'
mappingLabelDatastream = {'DoubleMu':'diMuon','DoubleElectron':'diElectron','MuEG':'electronMuon'}
analysisTriggers = tools.processSample(cfg).getTriggersUsedForAnalysis()
#####################
#expecting
# dataDatasets = {'label':{'datasetJSON':'jsonFileOfDataset'}}
#
#######################
import re
primDataS = re.compile('/([^\/][^\/]*)/.*')
dataStreams = set([primDataS.match(d['datasetName']).group(1) for d in  dataDatasets.values()])
jobs={}
for dataStream in list(dataStreams):
  print "testing ",dataStream
  triggers = analysisTriggers[mappingLabelDatastream[dataStream]]["data"]
  
  triggerRunRanges = runRangesManagment.runRangeManager(triggers.values())
  triggerRunRanges.calcTriggerRunRanges()
  dsRr = {}
  dataSJobs=[]
  for k,l in [(k,i['datasetJSON']) for k,i in dataDatasets.iteritems() if dataStream in k]:
    lL = lumiTools.LumiList(l)
    dsRuns = lL.getRuns()
    for rR in triggerRunRanges.ranges:
      shortlL = jsonTools.shortenJson(lL,rR[0],rR[1])
      if len(shortlL)>0:
        shortlLRuns=shortlL.getRuns()
        dataSJobs.append({"trigger":" and ".join([trig for trig,rR in triggers.iteritems() if int(shortlLRuns[0]) >= rR[0] and int(shortlLRuns[0]) <= rR[1]]),"dataset":k,'datasetJSON':l,'triggerRunRange':rR,"shortLumiList":shortlL,"jobRunRange":[int(shortlLRuns[0]),int(shortlLRuns[-1])]})
  jobs[dataStream]=sorted(dataSJobs,key= lambda x: int(x['jobRunRange'][0]))
#################
for ds,js in jobs.iteritems():
  print "dataStream ",ds
  intLumi = 0
  for j in js:
    print  "  trigger ",j["trigger"]
    print  "  dataset ",j["dataset"]  
    print  "  jobRunRange ",j["jobRunRange"]
    intLumiTmp = lumiTools.calcLumi(j["shortLumiList"])
    intLumi += intLumiTmp
    print  "  intLumi ",intLumiTmp/1000/1000
    print "  ------"
  print "intLumi of dataStream ",ds," ",intLumi/1000/1000
  print "#######"
  
################

