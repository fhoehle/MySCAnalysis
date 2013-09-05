import ROOT
ttbarFileList = []
testFiles = {
  "TT_TuneZ2_7TeV-mcatnlo__Fall11-PU_S6_START42_V14B-v1__AODSIM_test": {
    "localFile": ttbarFileList    ,"label":"TTbarSignal"
    ,"xSec":157
    ,"color":ROOT.kGreen+1
    ,"addOptions":"runOnTTbar=True eventsToProcess=1:96186:19229528"
  }
}
###
ttbarFileList.extend([
"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/98CBA318-412A-E111-ABB8-002618943948.root"
])
