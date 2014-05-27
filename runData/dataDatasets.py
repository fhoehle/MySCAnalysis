import os,sys,json
sys.path.append(os.getenv('CMSSW_BASE')+'/MyCMSSWAnalysisTools')
import MyDASTools.dasTools as dasTools
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
class createDatasampleFile(object):
  def __init__(self,filename):
    self.filename = filename
    self.datasets = []
  def addDataset(self,dataset,goldenJson="MySCAnalysis/runData/jsonFiles/Cert_160404-180252_7TeV_PromptReco_Collisions11_JSON.txt"):
    dsLabel = myTools.getLabelFromDatasetName(dataset)
    timeStamp = coreTools.getTimeStamp()
    dsJsonFilename =  os.getenv('CMSSW_BASE')+'/MySCAnalysis/runData/jsonFiles/'+dsLabel+'_'+timeStamp+'_JSON.txt'
    
    self.datasets.append(  {
      'label':dsLabel, 'json':dsJsonFilename , 'dataset':dataset,"goldenJson":goldenJson   }
    )
  def createFile(self):
    self.dataDatasets = {}
    for d in self.datasets:
      dsLumiList = None
      if not os.path.isfile(d['json']):
        oldSsArgv = sys.argv; sys.argv=[] # sys argv fix
        dasC = dasTools.myDasClient();dasC.limit=0
        dsLumiList = dasC.getJsonOfDataset(d["dataset"])
        dsLumiList.writeJSON(d['json'])
        sys.argv = oldSsArgv
      else:
        dsLumiList = LumiList(compactList=json.load(open(d['json'])))
      dsRuns = dsLumiList.compactList.keys()
      self.dataDatasets[d['label']] = ('{ \n '
        '\t"xSec":None\n'
        '\t,"localFile":None\n'
        '\t,"datasetName":"'+d["dataset"]+'"\n'
        '\t,"label":"Data_'+d['label']+'"\n'
        '\t,"crabConfig":{\n'
          '\t\t"CMSSW":{"lumis_per_job":5\n'
            '\t\t\t,"lumi_mask": os.getenv("CMSSW_BASE") + '+'"/'+d['goldenJson'].lstrip('/')+'"\n'
            '\t\t\t,"total_number_of_lumis" : -1}\n'
          '\t\t}\n'
        '\t,"color":0\n'
        '\t,"runRange":"'+str(dsRuns[0])+"-"+str(dsRuns[-1])+'"\n'
      '\t}\n')
      with open(self.filename,'w') as outputFile:
        outputFile.write('import os\n'+'dataDatasets = {\n')
        for k,i in self.dataDatasets.iteritems():
          outputFile.write("'"+k+"':"+i)
        outputFile.write('}')
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
#dataDatasets = {
#  'SingleMu__Run2011A-PromptReco-v6__AOD':{
#    'localFile':'/store/user/fhohle/OfficialSamples/SingleMu__Run2011A-PromptReco-v6__AOD/24054E7E-17C0-E011-AA64-001D09F28D4A.root'
#    ,'xSec':None
#    ,'datasetName':'/SingleMu/Run2011A-PromptReco-v6/AOD'
#    ,'label':'Data_Run2011A_PromptReco-v6'
#    ,'color':0
#    #,"addOptions":"runOnData=True"
#    ,"crabConfig":{"CMSSW":{"lumis_per_job":5,"lumi_mask":os.getenv('CMSSW_BASE')+'/MySCAnalysis/runData/'+'singleMuRun2011A_all.txt',"total_number_of_lumis" : -1}}
#    ,"runRange":"172620-175770"
#  }
#  ,'SingleMu__Run2011A-PromptReco-v4__AOD' : {
#    'localFile':'/store/user/fhohle/OfficialSamples/SingleMu__Run2011A-PromptReco-v4__AOD/048D33D0-EE80-E011-94E2-0030487CD716.root'
#    ,'xSec':None
#    ,'datasetName':'/SingleMu/Run2011A-PromptReco-v4/AOD'
#    ,'label':'Data_Run2011A_PromptReco-v4'
#    ,"color":0
#    ,"crabConfig":{"CMSSW":{"lumis_per_job":5,"lumi_mask":os.getenv('CMSSW_BASE')+'/MySCAnalysis/runData/'+'singleMuRun2011A_all.txt',"total_number_of_lumis" : -1}}
#    ,"runRange":"165071-168437"
#  }
#  ,'SingleMu__Run2011A-May10ReReco-v1__AOD':{
#     'localFile':'/store/user/fhohle/OfficialSamples/SingleMu__Run2011A-May10ReReco-v1__AOD/00454769-577B-E011-ACCD-001E0B49808A.root'
#    ,'xSec':None
#    ,'datasetName':'/SingleMu/Run2011A-May10ReReco-v1/AOD'
#    ,'label':'Data_Run2011A_May10ReReco-v1'
#    ,"color":0
#    ,"crabConfig":{"CMSSW":{"lumis_per_job":5,"lumi_mask":os.getenv('CMSSW_BASE')+'/MySCAnalysis/runData/'+'singleMuRun2011A_all.txt',"total_number_of_lumis" : -1}}
#    ,"runRange":"160329-163869"
# 
#  }
#  ,'SingleMu__Run2011A-05Aug2011-v1__AOD':{
#    'localFile':'/store/user/fhohle/OfficialSamples/SingleMu__Run2011A-05Aug2011-v1__AOD/000D68E1-8DC0-E011-AEFE-00248C55CC40.root'
#    ,'xSec':None
#    ,'datasetName':'/SingleMu/Run2011A-05Aug2011-v1/AOD'
#    ,'label':'Data_Run2011A_05Aug2011-v1'
#    ,"color":0
#    ,"crabConfig":{"CMSSW":{"lumis_per_job":5,"lumi_mask":os.getenv('CMSSW_BASE')+'/MySCAnalysis/runData/'+'singleMuRun2011A_all.txt',"total_number_of_lumis" : -1}}
#    ,"runRange":"170053-172619"
#
#  }
#  ,'SingleMu__Run2011B-PromptReco-v1__AOD':{
#    'localFile':'/store/user/fhohle/OfficialSamples/SingleMu__Run2011B-PromptReco-v1__AOD/22EBE93E-B1DB-E011-9C16-BCAEC518FF8A.root'
#    ,'xSec':None
#    ,'datasetName':'/SingleMu/Run2011B-PromptReco-v1/AOD'
#    ,'label':'Data_Run2011B_PromptReco-v1'
#    ,"color":0
#    ,"crabConfig":{"CMSSW":{"lumis_per_job":5,"lumi_mask":os.getenv('CMSSW_BASE')+'/MySCAnalysis/runData/'+'Cert_160404-180252_7TeV_PromptReco_Collisions11_JSON.txt',"total_number_of_lumis" : -1}}
#    ,"runRange":"175832-180296"
#  }
#}
