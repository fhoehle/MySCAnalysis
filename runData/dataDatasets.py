import os,sys
sys.path.append(os.getenv('CMSSW_BASE')+'/MyCMSSWAnalysisTools')
import Tools.datasetTools as datasetTools
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

#######################
diMu =  datasetTools.createDatasampleFile(os.getenv('CMSSW_BASE')+'/MySCAnalysis/runData/diMuonData.py')
diEl =  datasetTools.createDatasampleFile(os.getenv('CMSSW_BASE')+'/MySCAnalysis/runData/diElectronData.py')
MuE =   datasetTools.createDatasampleFile(os.getenv('CMSSW_BASE')+'/MySCAnalysis/runData/MuonElectronData.py')
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
diLepton =  datasetTools.createDatasampleFile(os.getenv('CMSSW_BASE')+'/MySCAnalysis/runData/diLeptonData.py')
diLepton.datasets =  diMu.datasets + diEl.datasets + MuE.datasets
diLepton.dataDatasets = {}
diLepton.dataDatasets.update(diMu.dataDatasets); diLepton.dataDatasets.update(diEl.dataDatasets); diLepton.dataDatasets.update(MuE.dataDatasets)
diLepton.createFile()
print "created ",diLepton.filename

