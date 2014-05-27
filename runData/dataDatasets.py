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
    if not hasattr(self,'dataDatasets'):
      self.createDataDatasets()
    with open(self.filename,'w') as outputFile:
      outputFile.write('import os\n'+'dataDatasets = {\n')
      for j,(k,i) in enumerate(self.dataDatasets.iteritems()):
        outputFile.write(("," if j != 0 else "") +"'"+k+"':"+i)
      outputFile.write('}')
  def createDataDatasets(self):
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
        '\t,"datasetJSON":"'+d['json']+'"\n'
        '\t,"crabConfig":{\n'
          '\t\t"CMSSW":{"lumis_per_job":5\n'
            '\t\t\t,"lumi_mask": os.getenv("CMSSW_BASE") + '+'"/'+d['goldenJson'].lstrip('/')+'"\n'
            '\t\t\t,"total_number_of_lumis" : -1}\n'
          '\t\t}\n'
        '\t,"color":0\n'
        '\t,"runRange":"'+str(dsRuns[0])+"-"+str(dsRuns[-1])+'"\n'
      '\t}\n');
#######################
diMu =  createDatasampleFile(os.getenv('CMSSW_BASE')+'/MySCAnalysis/runData/diMuonData.py')
diEl =  createDatasampleFile(os.getenv('CMSSW_BASE')+'/MySCAnalysis/runData/diElectronData.py')
MuE =   createDatasampleFile(os.getenv('CMSSW_BASE')+'/MySCAnalysis/runData/MuonElectronData.py')
##############
for ds in dsDoubleMu:
  diMu.addDataset(ds)
diMu.createFile()
for ds in dsDoubleE:
  diEl.addDataset(ds)
diEl.createFile()
for ds in dsEMu:
  ""
  MuE.addDataset(ds)
MuE.createFile()
#######################
print "created ",diMu.filename
print "created ",diEl.filename
print "created ",MuE.filename
#########################
diLepton =  createDatasampleFile(os.getenv('CMSSW_BASE')+'/MySCAnalysis/runData/diLeptonData.py')
diLepton.datasets =  diMu.datasets + diEl.datasets + MuE.datasets
diLepton.dataDatasets = {}
diLepton.dataDatasets.update(diMu.dataDatasets); diLepton.dataDatasets.update(diEl.dataDatasets); diLepton.dataDatasets.update(MuE.dataDatasets)
diLepton.createFile()
print "created ",diLepton.filename

