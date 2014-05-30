import os,sys,json
sys.path.append(os.getenv('CMSSW_BASE')+'/MyCMSSWAnalysisTools')
import MyDASTools.dasTools as dasTools
import Tools.datasetTools as datasetTools
import Tools.tools as myTools
import Tools.coreTools as coreTools
from FWCore.PythonUtilities.LumiList   import LumiList
dsDoubleMu = [
 '/DoubleMu/Run2011B-PromptReco-v1/AOD',
 '/DoubleMu/Run2011A-PromptReco-v6/AOD',
 '/DoubleMu/Run2011A-PromptReco-v4/AOD',
 '/DoubleMu/Run2011A-May10ReReco-v1/AOD',
 '/DoubleMu/Run2011A-05Aug2011-v1/AOD'
]

dsDoubleE =[
 '/DoubleElectron/Run2011A-05Aug2011-v1/AOD',
 '/DoubleElectron/Run2011A-May10ReReco-v1/AOD',
 '/DoubleElectron/Run2011A-PromptReco-v4/AOD',
 '/DoubleElectron/Run2011A-PromptReco-v6/AOD',
 '/DoubleElectron/Run2011B-PromptReco-v1/AOD'
]

dsEMu =[
 '/MuEG/Run2011A-PromptReco-v4/AOD',
 '/MuEG/Run2011A-PromptReco-v6/AOD',
 '/MuEG/Run2011A-05Aug2011-v1/AOD',
 '/MuEG/Run2011A-May10ReReco-v1/AOD',
 '/MuEG/Run2011B-PromptReco-v1/AOD'
]
#dsMET =[
#'/METBTag/Run2011A-May10ReReco-v1/AOD',
##'/MET/Run2011B-PromptReco-v1/AOD',
#'/MET/Run2011A-PromptReco-v6/AOD',
#'/MET/Run2011A-PromptReco-v4/AOD',
#'/MET/Run2011A-05Aug2011-v1/AOD'
#]
dataDatasets = {}
for ds in dsDoubleMu+dsDoubleE+dsEMu:#+dsMET:
  ""
  dsLabel = myTools.getLabelFromDatasetName(ds)
  dsJSON = os.getenv('CMSSW_BASE')+'/MySCAnalysis/runData/'+dsLabel+'_JSON.txt'
  print dsJSON.lstrip(os.getenv('CMSSW_BASE'))
  dsLumiList = None
  if not os.path.isfile(dsJSON):
    oldSsArgv = sys.argv
    sys.argv=[]
    dasC = dasTools.myDasClient()
    dsLumiList = dasC.getJsonOfDataset(ds)
    dsLumiList.writeJSON(dsJSON)
    sys.argv = oldSsArgv
  else:
    dsLumiList = LumiList(compactList=json.load(open(dsJSON)))
  dsRuns = dsLumiList.compactList.keys()
  dataDatasets[myTools.getStringFromDatasetName(ds)] = {
    'xSec':None
    ,'localFile':None
    ,'datasetName':ds
    ,'label':'Data_'+myTools.getLabelFromDatasetName(ds)
    ,"crabConfig":{
      "CMSSW":{"lumis_per_job":5
        ,"lumi_mask": os.getenv('CMSSW_BASE')+'/'+os.path.relpath(dsJSON,os.getenv('CMSSW_BASE'))
        ,"total_number_of_lumis" : -1}}
    ,'color':0
    ,"runRange":str(dsRuns[0])+"-"+dsRuns[-1]
  }

