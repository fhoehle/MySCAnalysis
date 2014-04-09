import ROOT
testFiles = {
  "ZZJetsTo2L2Q_TuneZ2_7TeV-madgraph-tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM":  {
    "localFile":"/store/user/fhohle//OfficialSamples/ZZJetsTo2L2Q_TuneZ2_7TeV-madgraph-tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM/FE49F29C-E703-E111-AE65-1CC1DE0510A8.root"
    #,"crabConfig":{"GRID":{"se_black_list":"T2_UK_London_IC"}}
    ,"label":"ZZJetsTo2L2Q"
    ,"xSec":0.776524 # https://twiki.cern.ch/twiki/bin/view/CMS/HiggsToTauTauWorkingSummer2013
    ,"color":ROOT.kCyan+1
    ,'datasetName':None
  }
  ,"ZZJetsTo2L2Nu_TuneZ2_7TeV-madgraph-tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM":{
    "localFile": "/store/user/fhohle//OfficialSamples/ZZJetsTo2L2Nu_TuneZ2_7TeV-madgraph-tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM/FAB8CFD9-66FF-E011-A567-001F29C49312.root"
    #,"crabConfig":{"GRID":{"se_black_list":"T2_UK_London_IC"}}
    ,"label":"ZZJetsTo2L2Nu"
    ,"xSec":0.250597
    ,"color":ROOT.kCyan+2
    ,'datasetName':None
  }
  ,"ZZTo2mu2tau_mll4_7TeV-powheg-pythia6__Fall11-PU_S6_START42_V14B-v1__AODSIM":  {
    "localFile":"/store/user/fhohle//OfficialSamples/ZZTo2mu2tau_mll4_7TeV-powheg-pythia6__Fall11-PU_S6_START42_V14B-v1__AODSIM/FCE3D0EC-4308-E211-AD4A-003048C6929A.root"
    ,"xSec":0.152 # https://twiki.cern.ch/twiki/bin/view/CMS/HZZSamples7TeV
    ,"label":"ZZTo2mu2tau"
    ,"color":ROOT.kCyan+3
    ,'datasetName':None
  }
,"ZZ_TuneZ2_7TeV_pythia6_tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM":  {
    "localFile":"/store/user/fhohle//OfficialSamples/ZZ_TuneZ2_7TeV_pythia6_tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM/FEECD332-92F3-E011-AC32-003048678B3C.root"
    ,"xSec":7.67
    ,"label":"ZZ"
    ,"color":ROOT.kCyan-1
    ,'datasetName':None
  }
  ,"WZJetsTo2L2Q_TuneZ2_7TeV-madgraph-tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM":  {
    "localFile":"/store/user/fhohle//OfficialSamples/WZJetsTo2L2Q_TuneZ2_7TeV-madgraph-tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM/FCFF1FD3-8AF3-E011-8E4F-0017A4771020.root"
    #,"crabConfig":{"GRID":{"se_black_list":"T2_TW_Taiwan"}}
    ,"xSec":18.2
    ,"label":"WZJetsTo2L2Q"    
    ,"color":ROOT.kCyan-4
    ,'datasetName':None
  }
  ,"WZ_TuneZ2_7TeV_pythia6_tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM":  {
    "localFile":"/store/user/fhohle//OfficialSamples/WZ_TuneZ2_7TeV_pythia6_tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM/FEA55495-9DF1-E011-9C3B-003048678F8A.root"
    ,"xSec":18.20
    ,"label":"WZ"
    ,"color":ROOT.kCyan
    ,'datasetName':None
  }
  ,"WW_TuneZ2_7TeV_pythia6_tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM":  {
    "localFile":"/store/user/fhohle//OfficialSamples/WW_TuneZ2_7TeV_pythia6_tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM/FE1BABC1-0C07-E111-8D3C-0018F3D09624.root"
    ,"xSec":47.04
    ,"label":"WW"
    ,"color":ROOT.kCyan-7
    ,'datasetName':None
  }
  ,"WWJetsTo2L2Nu_TuneZ2_7TeV-madgraph-tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM": {
    "localFile":"/store/user/fhohle//OfficialSamples/WWJetsTo2L2Nu_TuneZ2_7TeV-madgraph-tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM/FE41AF6E-9BF1-E011-AC7E-E0CB4E29C514.root"
    ,"xSec":4.526
    ,"label":"WWJetsTo2L2Nu"
    ,"color":ROOT.kCyan-3
    ,'datasetName':None
  }
  ,"WJetsToLNu_TuneZ2_7TeV-madgraph-tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM":  {
    "localFile":"/store/user/fhohle//OfficialSamples/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM/FECD1F53-09F3-E011-A327-001A92811720.root"
    ,"xSec":31314
    ,"label":"WJetsToLNu"
    ,"color":ROOT.kRed+1
    ,"crabConfig":{"CMSSW":{"events_per_job":20000}}
    ,'datasetName':None
  }
#  ,"T_TuneZ2_scaledown_tW-channel-DR_7TeV-powheg-tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM":  {
#    "localFile":"/store/user/fhohle//OfficialSamples/T_TuneZ2_scaledown_tW-channel-DR_7TeV-powheg-tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM/F4CA8516-5256-E111-9A2E-001EC9D7FA1C.root"
#    ,"xSec":7.87 # same like nominal
#    ,"label":"T-scaledown-tW-channel-DR"
#    ,"color":ROOT.kMagenta+1
#    #,"crabConfig":{"CMSSW":{"number_of_jobs":100}}
#    ,'datasetName':None
#  }
#  ,"T_TuneZ2_scaleup_tW-channel-DR_7TeV-powheg-tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM":  {
#    "localFile":"/store/user/fhohle//OfficialSamples/T_TuneZ2_scaleup_tW-channel-DR_7TeV-powheg-tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM/F87DDC98-3A56-E111-9596-001EC9D8D49F.root"
#    ,"xSec":7.87 # same like nominal
#    ,"label":"T-scaleup-tW-channel-DR"
#    ,"color":ROOT.kMagenta+2
#    #,"crabConfig":{"CMSSW":{"number_of_jobs":100}}
#    ,'datasetName':None
#  }
#  ,"T_TuneZ2_scaleup_tW-channel-DS_7TeV-powheg-tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM":  {
#    "localFile":"/store/user/fhohle//OfficialSamples/T_TuneZ2_scaleup_tW-channel-DS_7TeV-powheg-tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM/FAEA8086-B331-E111-AE45-90E6BA19A242.root"
#    ,"xSec":7.87 # same like nominal
#    ,"label":"T-scaleup-tW-channel-DS"
#    ,"color":ROOT.kMagenta+3
#    #,"crabConfig":{"CMSSW":{"number_of_jobs":100}}
#    ,'datasetName':None
#  }
#  ,"Tbar_TuneZ2_scaledown_tW-channel-DR_7TeV-powheg-tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM":  {
#    "localFile":"/store/user/fhohle//OfficialSamples/Tbar_TuneZ2_scaledown_tW-channel-DR_7TeV-powheg-tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM/FE8D1934-3D56-E111-9355-20CF3027A626.root"
#    ,"xSec":7.87 # same like nominal
#    ,"label":"Tbar-scaledown-tW-channel-DR"
#    ,"color":ROOT.kMagenta+4
#    #,"crabConfig":{"CMSSW":{"number_of_jobs":100}}
#    ,'datasetName':None
#  }
#  ,"Tbar_TuneZ2_scaleup_tW-channel-DR_7TeV-powheg-tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM":  {
#    "localFile":"/store/user/fhohle//OfficialSamples/Tbar_TuneZ2_scaleup_tW-channel-DR_7TeV-powheg-tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM/FC4D2E10-5256-E111-8E38-90E6BA0D09AD.root"
#    ,"xSec":7.87 # same like nominal
#    ,"label":"Tbar-scaleup-tW-channel-DR"
#    ,"color":ROOT.kMagenta
#    #,"crabConfig":{"CMSSW":{"number_of_jobs":100}}
#    ,'datasetName':None
#  }
  ,"Tbar_TuneZ2_tW-channel-DS_7TeV-powheg-tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM":  {
    "localFile":"/store/user/fhohle//OfficialSamples/Tbar_TuneZ2_tW-channel-DS_7TeV-powheg-tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM/FE1BA52C-15F4-E011-BA40-00261894385D.root"
    ,"xSec":7.87
    ,"label":"Tbar-tW-channel-DS"
    ,"color":ROOT.kMagenta-1
    #,"crabConfig":{"CMSSW":{"number_of_jobs":100}}
    ,'datasetName':None
  }
  ,"T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM":  {
    "localFile":"/store/user/fhohle//OfficialSamples/T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM/FCFA8B2F-DEF5-E011-B621-002618943868.root"
    ,"xSec":7.87
    ,"label":"T-tW-channel-DR"
    ,"color":ROOT.kMagenta-2
    #,"crabConfig":{"CMSSW":{"number_of_jobs":100}}
    ,'datasetName':None
  }
  ,"Tbar_TuneZ2_tW-channel-DR_7TeV-powheg-tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM":  {
    "localFile":"/store/user/fhohle//OfficialSamples/Tbar_TuneZ2_tW-channel-DR_7TeV-powheg-tauola__Fall11-PU_S6_START42_V14B-v2__AODSIM/F4159273-1A11-E111-8AFD-0018F3D09660.root"
    ,"xSec":7.87
    ,"label":"Tbar-tW-channel-DR"
    ,"color":ROOT.kMagenta-5
    #,"crabConfig":{"CMSSW":{"number_of_jobs":100}}
    ,'datasetName':None
  }
  ,"T_TuneZ2_tW-channel-DS_7TeV-powheg-tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM":  {
    "localFile":"/store/user/fhohle//OfficialSamples/T_TuneZ2_tW-channel-DS_7TeV-powheg-tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM/FEC1F9A5-5AF9-E011-B639-001A92811714.root"
    ,"xSec":7.87
    ,"label":"T-tW-channel-DS"
    ,"color":ROOT.kMagenta-3
    #,"crabConfig":{"CMSSW":{"number_of_jobs":100}}
    ,'datasetName':None
  }
#  ,"Tbar_TuneZ2_scaledown_tW-channel-DS_7TeV-powheg-tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM":  {
#    "localFile":"/store/user/fhohle//OfficialSamples/Tbar_TuneZ2_scaledown_tW-channel-DS_7TeV-powheg-tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM/F432634E-A02B-E111-9FC2-E0CB4EA0A917.root"
#    ,"xSec":7.87
#    ,"label":"Tbar-scaledown-tW-channel-DS"
#    ,"color":ROOT.kMagenta-4
#    ,'datasetName':None
#    #,"crabConfig":{"CMSSW":{"number_of_jobs":100}}
#  }
  ,"Tbar_TuneZ2_s-channel_7TeV-powheg-tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM":{
    "localFile":"/store/user/fhohle/OfficialSamples/Tbar_TuneZ2_s-channel_7TeV-powheg-tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM/F4D77C89-79F9-E011-82E8-001A92811746.root"
    ,"xSec":1.49
    ,"label":"Tbar-s-channel"
    ,"color":ROOT.kMagenta-4
    ,'datasetName':None
  }
  ,"T_TuneZ2_s-channel_7TeV-powheg-tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM":{
    "localFile":"/store/user/fhohle/OfficialSamples/T_TuneZ2_s-channel_7TeV-powheg-tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM/20512CDA-9DF8-E011-9C7C-485B39800B75.root"
    ,"xSec":2.72
    ,"label":"T-s-channel"
    ,"color":ROOT.kMagenta-4
    ,'datasetName':None
  }
  ,"T_TuneZ2_t-channel_7TeV-powheg-tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM":{
    "localFile":"/store/user/fhohle/OfficialSamples/T_TuneZ2_t-channel_7TeV-powheg-tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM/04BB1C32-34F9-E011-BFE0-0018F34D0D62.root"
    ,"xSec":42.6
    ,"label":"T-t-channel"
    ,"color":ROOT.kMagenta-4
    ,'datasetName':None
  }
  ,"Tbar_TuneZ2_t-channel_7TeV-powheg-tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM":{
    "localFile":"/store/user/fhohle/OfficialSamples/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM/065A5198-16F9-E011-8174-003048678BAC.root"
    ,"xSec":22.0
    ,"label":"Tbar-t-channel"
    ,"color":ROOT.kMagenta-4
    ,'datasetName':None
  }
  ,"DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM":{
    "localFile":"/store/user/fhohle/OfficialSamples/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM/00E828B9-1CF5-E011-AC89-00261834B524.root"
    ,"xSec":3048
    ,"label":"DYJetsToLL-M-50"
    ,"color":ROOT.kRed-4
    #,"crabConfig":{"CMSSW":{"number_of_jobs":2000}}
    ,'datasetName':None
  }
  ,"DYJetsToLL_M-10To50_TuneZ2_7TeV-madgraph__Fall11-PU_S6_START42_V14B-v1__AODSIM":{
  "localFile":"/store/user/fhohle/OfficialSamples/DYJetsToLL_M-10To50_TuneZ2_7TeV-madgraph__Fall11-PU_S6_START42_V14B-v1__AODSIM/020B21F7-AD3A-E111-8440-0018F3D0969C.root"
    ,"xSec":12782.63
    ,"label":"DYJetsToLL-M-10To50"
    ,"color":ROOT.kRed-4
    ,'datasetName':None
  }
  ,'QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6__Fall11-PU_S6_START42_V14B-v1__AODSIM':{
    "localFile":None
    ,'xSec':84679 #AN2011_186_v14
    ,'label':"QCD_Pt-20_MuEnrichedPt-15"
    ,"color":ROOT.kYellow
    ,'datasetName':'/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Fall11-PU_S6_START42_V14B-v1/AODSIM'
  }
  ,'QCD_Pt-20to30_EMEnriched_TuneZ2_7TeV-pythia6__Fall11-PU_S6_START42_V14B-v1__AODSIM':{
    'localFile':None
    ,'xSec':2.5E6 #AN2011_186_v14
    ,'datasetName':'/QCD_Pt-20to30_EMEnriched_TuneZ2_7TeV-pythia6/Fall11-PU_S6_START42_V14B-v1/AODSIM'
    ,'label':'QCD_Pt-20to30_EMEnriched'
    ,"color":ROOT.kYellow+1
  }
#  ,'QCD_Pt-30to80_EMEnriched_TuneZ2_7TeV-pythia__Fall11-PU_S6_START42_V14B-v1__AODSIM':{
#    'localFile':None
#    ,'xSec':3.63E6 #AN2011_186_v14
#    ,'datasetName':'/QCD_Pt-30to80_EMEnriched_TuneZ2_7TeV-pythia/Fall11-PU_S6_START42_V14B-v1/AODSIM'
#    ,'label':'QCD_Pt-30to80_EMEnriched'
#    ,"color":ROOT.kYellow+2
#  }
#  ,'QCD_Pt-80to170_EMEnriched_TuneZ2_7TeV-pythia6__Fall11-PU_S6_START42_V14B-v2__AODSIM':{
#    'localFile':None
#    ,'xSec':143E3 #AN2011_186_v14
#    ,'datasetName':'/QCD_Pt-80to170_EMEnriched_TuneZ2_7TeV-pythia6/Fall11-PU_S6_START42_V14B-v2/AODSIM'
#    ,'label':'QCD_Pt-80to170_EMEnriched'
#    ,"color":ROOT.kYellow+3
#  } 
  ,'QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6__Fall11-PU_S6_START42_V14B-v1__AODSIM':{
    'localFile':None
    ,'xSec':139E3 #AN2011_186_v14
    ,'datasetName':'/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/Fall11-PU_S6_START42_V14B-v1/AODSIM'
    ,'label':'QCD_Pt-20to30_BCtoE'
    ,"color":ROOT.kYellow+4
  }
#  ,'QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6__Fall11-PU_S6_START42_V14B-v1__AODSIM':{
#    'localFile':None
#    ,'xSec':144E3 #AN2011_186_v14
#    ,'datasetName':'/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/Fall11-PU_S6_START42_V14B-v1/AODSIM'
#    ,'label':'QCD_Pt-30to80_BCtoE'
#    ,"color":ROOT.kYellow+5
#  }
}
