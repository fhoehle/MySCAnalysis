import os
dataDatasets = {
  'SingleMu__Run2011A-PromptReco-v6__AOD':{
    'localFile':'/store/user/fhohle/OfficialSamples/SingleMu__Run2011A-PromptReco-v6__AOD/24054E7E-17C0-E011-AA64-001D09F28D4A.root'
    ,'xSec':None
    ,'datasetName':'/SingleMu/Run2011A-PromptReco-v6/AOD'
    ,'label':'Data_Run2011A_PromptReco-v6'
    ,'color':0
    #,"addOptions":"runOnData=True"
    ,"crabConfig":{"CMSSW":{"lumis_per_job":5,"lumi_mask":os.getenv('CMSSW_BASE')+'/MySCAnalysis/runData/'+'singleMuRun2011A_all.txt',"total_number_of_lumis" : -1}}
    ,"runRange":"172620-175770"
  }
  ,'SingleMu__Run2011A-PromptReco-v4__AOD' : {
    'localFile':'/store/user/fhohle/OfficialSamples/SingleMu__Run2011A-PromptReco-v4__AOD/048D33D0-EE80-E011-94E2-0030487CD716.root'
    ,'xSec':None
    ,'datasetName':'/SingleMu/Run2011A-PromptReco-v4/AOD'
    ,'label':'Data_Run2011A_PromptReco-v4'
    ,"color":0
    ,"crabConfig":{"CMSSW":{"lumis_per_job":5,"lumi_mask":os.getenv('CMSSW_BASE')+'/MySCAnalysis/runData/'+'singleMuRun2011A_all.txt',"total_number_of_lumis" : -1}}
    ,"runRange":"165071-168437"
  }
  ,'SingleMu__Run2011A-May10ReReco-v1__AOD':{
     'localFile':'/store/user/fhohle/OfficialSamples/SingleMu__Run2011A-May10ReReco-v1__AOD/00454769-577B-E011-ACCD-001E0B49808A.root'
    ,'xSec':None
    ,'datasetName':'/SingleMu/Run2011A-May10ReReco-v1/AOD'
    ,'label':'Data_Run2011A_May10ReReco-v1'
    ,"color":0
    ,"crabConfig":{"CMSSW":{"lumis_per_job":5,"lumi_mask":os.getenv('CMSSW_BASE')+'/MySCAnalysis/runData/'+'singleMuRun2011A_all.txt',"total_number_of_lumis" : -1}}
    ,"runRange":"160329-163869"
 
  }
  ,'SingleMu__Run2011A-05Aug2011-v1__AOD':{
    'localFile':'/store/user/fhohle/OfficialSamples/SingleMu__Run2011A-05Aug2011-v1__AOD/000D68E1-8DC0-E011-AEFE-00248C55CC40.root'
    ,'xSec':None
    ,'datasetName':'/SingleMu/Run2011A-05Aug2011-v1/AOD'
    ,'label':'Data_Run2011A_05Aug2011-v1'
    ,"color":0
    ,"crabConfig":{"CMSSW":{"lumis_per_job":5,"lumi_mask":os.getenv('CMSSW_BASE')+'/MySCAnalysis/runData/'+'singleMuRun2011A_all.txt',"total_number_of_lumis" : -1}}
    ,"runRange":"170053-172619"

  }
  ,'SingleMu__Run2011B-PromptReco-v1__AOD':{
    'localFile':'/store/user/fhohle/OfficialSamples/SingleMu__Run2011B-PromptReco-v1__AOD/22EBE93E-B1DB-E011-9C16-BCAEC518FF8A.root'
    ,'xSec':None
    ,'datasetName':'/SingleMu/Run2011B-PromptReco-v1/AOD'
    ,'label':'Data_Run2011B_PromptReco-v1'
    ,"color":0
    ,"crabConfig":{"CMSSW":{"lumis_per_job":5,"lumi_mask":os.getenv('CMSSW_BASE')+'/MySCAnalysis/runData/'+'Cert_160404-180252_7TeV_PromptReco_Collisions11_JSON.txt',"total_number_of_lumis" : -1}}
    ,"runRange":"175832-180296"
  }
}
