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

dsDoubleMu_16Jan2012 = [
  '/DoubleMu/Run2011A-16Jan2012-v1/AOD'
  ,'/DoubleMu/Run2011B-16Jan2012-v1/AOD'
]

#######################
diMu =  datasetTools.createDatasampleFile(os.getenv('CMSSW_BASE')+'/MySCAnalysis/runData/diMuonData.py')
diEl =  datasetTools.createDatasampleFile(os.getenv('CMSSW_BASE')+'/MySCAnalysis/runData/diElectronData.py')
MuE =   datasetTools.createDatasampleFile(os.getenv('CMSSW_BASE')+'/MySCAnalysis/runData/MuonElectronData.py')
diMu_16Jan2012 = datasetTools.createDatasampleFile(os.getenv('CMSSW_BASE')+'/MySCAnalysis/runData/diMuonData_16Jan2012.py')
##############
for ds in dsDoubleMu:
 diMu.addDataset(ds)
for ds in dsDoubleE:
  diEl.addDataset(ds)
for ds in dsEMu:
  MuE.addDataset(ds)
for ds in dsDoubleMu_16Jan2012:
  diMu_16Jan2012.addDataset(ds)
#########################
diLepton =  datasetTools.createDatasampleFile(os.getenv('CMSSW_BASE')+'/MySCAnalysis/runData/diLeptonData.py')
diLepton.datasets =  diMu.datasets + diEl.datasets + MuE.datasets
diLepton.dataDatasets = {}
###########################
if __name__ == '__main__':
  diMu.createFile()
  diEl.createFile()
  MuE.createFile()
  print "created ",diMu.filename
  print "created ",diEl.filename
  print "created ",MuE.filename
  diLepton.dataDatasets.update(diMu.dataDatasets); diLepton.dataDatasets.update(diEl.dataDatasets); diLepton.dataDatasets.update(MuE.dataDatasets)
  diLepton.createFile()
  print "created ",diLepton.filename
  
