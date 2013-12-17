import ROOT
ttbarFileList = [];ttbarNoCorrFileList = []
testFiles = {
  "TT_TuneZ2_7TeV-mcatnlo__Fall11-PU_S6_START42_V14B-v1__AODSIM_Signal": {
    "localFile": ttbarFileList    ,"label":"TTbarSignal"
    ,"datasetName":'/TT_TuneZ2_7TeV-mcatnlo/Fall11-PU_S6_START42_V14B-v1/AODSIM'
    ,"xSec":157
    ,"color":ROOT.kGreen+1
    ,"addOptions":"runOnTTbar=True"
    ,"crabConfig":{"CMSSW":{"number_of_jobs":1500},"GRID":{"se_white_list":"T2_DE_RWTH"}}
  },
  "TT_TuneZ2_7TeV-mcatnlo__Fall11-PU_S6_START42_V14B-v1__AODSIM_Bck": {
    "localFile": ttbarFileList  ,"label":"TTbarBackground"
    ,"datasetName":"/TT_TuneZ2_7TeV-mcatnlo/Fall11-PU_S6_START42_V14B-v1/AODSIM"
    ,"xSec":157
    ,"color":ROOT.kTeal + 3
    ,"addOptions":"runOnTTbar=True N1TTbarDiLepBck=True"
    ,"crabConfig":{"CMSSW":{"number_of_jobs":1500},"GRID":{"se_white_list":"T2_DE_RWTH"}}
  }
  ,"TT_noCorr_7TeV-mcatnlo_Fall11-PU_S6_START42_V14B-v1__AODSIM_Signal": {
    "localFile": ttbarNoCorrFileList    ,"label":"TTbarNoCorrSignal"
    ,"xSec":157
    ,'datasetName':'/TT_noCorr_7TeV-mcatnlo_Fall11-PU_S6_START42_V14B-v1/AODSIM'
    ,"color":ROOT.kGreen+1
    ,"addOptions":"runOnTTbar=True"
    ,"crabConfig":{"CMSSW":{"number_of_jobs":1500},"GRID":{"se_white_list":"T2_DE_RWTH"}}
  }
  ,"TT_noCorr_7TeV-mcatnlo_Fall11-PU_S6_START42_V14B-v1__AODSIM_Bck": {
    "localFile": ttbarNoCorrFileList    ,"label":"TTbarNoCorrSignal"
    ,'datasetName':'/TT_noCorr_7TeV-mcatnlo_Fall11-PU_S6_START42_V14B-v1/AODSIM'
    ,"xSec":157
    ,"color":ROOT.kTeal + 3
    ,"addOptions":"runOnTTbar=True N1TTbarDiLepBck=True"
    ,"crabConfig":{"CMSSW":{"number_of_jobs":1500},"GRID":{"se_white_list":"T2_DE_RWTH"}}
  }

}
###
ttbarFileList.extend([
"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/0051A2ED-482A-E111-9863-0026189438F7.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/006394AE-F729-E111-BB9C-001A9281173E.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/006BF955-422A-E111-8885-0026189438BD.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/00DEB8A5-4C2A-E111-B88B-003048679150.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/0211CBF1-222A-E111-A810-00248C0BE01E.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/0238B110-332A-E111-BEE2-002618FDA248.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/0242E521-0C2A-E111-8B1C-00248C0BE012.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/0245F41B-502A-E111-918D-002354EF3BD0.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/024C35A7-0E2A-E111-B9FF-001A92810AA0.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/0260FE94-392A-E111-A9B1-003048679182.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/026F08A1-0A2A-E111-8753-003048678E8A.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/027D9E4E-542A-E111-895F-0026189437FD.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/0285DC46-342A-E111-BCE0-00304867D838.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/0289E91E-502A-E111-ABA5-001A92971ADC.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/02B344A7-FC29-E111-AB7F-002618943975.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/02E0D47F-202A-E111-BE56-003048FFD7D4.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/02E6F52D-2D2A-E111-B9EB-002618943930.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/02F2ABA6-4C2A-E111-B238-002618FDA204.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/04021747-FD29-E111-BE68-002618943834.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/040E96B6-112A-E111-B699-00261894382D.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/0419D184-202A-E111-8C71-00304867BFF2.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/0461948D-392A-E111-ABB0-002618943906.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/04E62A95-392A-E111-9FE0-002618FDA259.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/04EC4182-202A-E111-BB20-00248C0BE005.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/06123840-EF29-E111-BC00-002618943982.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/06278A7F-202A-E111-9F56-002618943821.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/062B50B6-F729-E111-9008-001A92971B30.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/0658DC31-362A-E111-A18C-002354EF3BDE.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/06766CF1-222A-E111-8246-0018F3D09600.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/069857D5-3B2A-E111-B52C-002618943920.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/06F8124F-062A-E111-B420-002618943832.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/0808FD85-142A-E111-9E12-003048FFD720.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/082F3CB6-412A-E111-A878-002618943978.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/084F504D-302A-E111-A4A7-002618943982.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/0856BA50-572A-E111-942F-002618FDA263.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/0873EA8E-172A-E111-B67D-003048FFCBA8.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/08888F77-472A-E111-808C-001A92810AB2.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/08A84624-502A-E111-ACAB-001A92971B5E.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/08D97C1D-3B2A-E111-88D0-002618943863.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/08ECD7A6-2A2A-E111-91A4-0026189438F6.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/08F9F855-4D2A-E111-9C51-002618943963.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/08FCF15F-152A-E111-8A34-003048FFCB9E.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/0A15BBB9-182A-E111-A920-001A92971B84.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/0A1A163D-532A-E111-B6EE-003048D15D04.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/0A381DAB-472A-E111-938C-0030486790BE.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/0A675E8F-3E2A-E111-AB01-00261894393F.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/0A7CC2F8-1A2A-E111-97CB-001A92810AEE.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/0A9C9BF5-512A-E111-B1FF-003048678B00.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/0AA384E5-EA29-E111-9FBC-001A92810AD8.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/0ABBCDFE-012A-E111-8A96-003048FFCBA8.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/0AC9A2E2-FE29-E111-BD8D-003048FFD76E.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/0AD8F5D9-542A-E111-A0CC-0018F3D09630.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/0AF4762E-4A2A-E111-AA7C-003048678E92.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/0C11E7C1-362A-E111-BE24-002618943946.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/0C371C29-1F2A-E111-9F33-0026189438AA.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/0C4E4243-542A-E111-8FD6-002618943865.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/0C52FCB4-562A-E111-94DC-002618943958.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/0C612AB3-112A-E111-91E3-003048678F92.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/0CA3ECB3-0C2A-E111-B8E5-00261894396E.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/0CCB79D9-3B2A-E111-B85C-00261894392C.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/0CE41B3D-F529-E111-996C-003048678ED4.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/0E1F167C-102A-E111-B51E-00261894391B.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/0E37DCAF-0D2A-E111-8405-00304867BECC.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/0E4D4648-542A-E111-A9BE-001A92971B62.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/0E5D9DEF-222A-E111-AF72-00261894397E.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/0E6061B3-4C2A-E111-8FB8-001A928116FC.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/0E7860EF-532A-E111-9DC8-001A9281173C.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/0E7CF903-2A2A-E111-B349-002618943980.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/0E7EC806-382A-E111-ACDD-0026189438DC.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/0E92C3A2-052A-E111-B484-003048678C26.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/0EA877DF-532A-E111-8BE7-00261894384A.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/0EA8CB00-3E2A-E111-9AD9-001BFCDBD100.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/0EDEC363-4D2A-E111-A111-00261894397D.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/0EE73E43-EA29-E111-AC10-001A92971B7E.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/10079D9B-432A-E111-AFCD-001A92971B68.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/1024574B-122A-E111-8DED-001A92971AA8.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/1054F010-382A-E111-9563-003048678F62.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/1075DAB0-3C2A-E111-9BB6-001BFCDBD184.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/10761381-142A-E111-ADF4-00261894393E.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/10E7559A-472A-E111-900B-00304867900C.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/1208F85B-4D2A-E111-8F10-002618FDA204.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/12096BEB-532A-E111-8D16-0026189438A5.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/122FE333-4F2A-E111-98A3-003048FFCB74.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/12399B24-562A-E111-B617-003048FFD756.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/127E2717-382A-E111-B2C0-001A92811730.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/1295077C-FA29-E111-ACFF-003048678DD6.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/1295434B-532A-E111-AA72-00261894386F.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/12D68262-572A-E111-84AE-0018F3D096A0.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/14089EF7-E629-E111-B4A7-002618943907.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/1416D71D-562A-E111-9384-001A92811726.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/141EC655-222A-E111-9809-002618943961.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/14221976-192A-E111-AF0B-0018F3D096BC.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/14300796-3E2A-E111-8E1F-0030486792B8.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/14585C00-432A-E111-9CE6-00261894389F.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/146B97E2-442A-E111-8C2A-0018F3D09620.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/149D9DB7-412A-E111-A297-003048678F62.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/14B2D382-F929-E111-98B3-00261894389D.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/14B5060E-512A-E111-8BA0-00248C55CC97.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/14F8FA4E-3D2A-E111-BDCC-001A9281170E.root"
,"/store/mc/Fall11/TT_TuneZ2_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/16059C6D-4B2A-E111-86C2-003048FFCB8C.root"
])
ttbarNoCorrFileList.extend([
"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/FED2AF8E-6CC3-E111-B412-003048FFCC1E.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/FECAD413-48C3-E111-B43F-0026189438E7.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/FE9B6BD1-B4C2-E111-A031-0018F3D0969A.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/FE778563-09C3-E111-8E9B-003048FF9AA6.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/FE2550D2-6CC3-E111-891A-00261894385D.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/FCF9C3B0-57C3-E111-BD84-003048678E6E.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/FCE9D6BA-A6C1-E111-AACA-003048678ADA.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/FCB7FD3F-A5C1-E111-A214-00261894392D.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/FCB6A14E-84C2-E111-AC30-0025905822B6.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/FCB1DDA7-A8C2-E111-BE72-0018F3D0967E.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/FC9AF659-08C3-E111-A296-003048FFD720.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/FC8FA9A2-53C3-E111-90C8-0026189438A0.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/FC889A84-A7C1-E111-B2A4-002618943957.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/FC840379-D0C1-E111-AF6D-003048FFD7BE.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/FC4AADA2-53C3-E111-AAEF-002618FDA259.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/FC43818E-A0C2-E111-B86D-0018F3D0966C.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/FC166827-8AC2-E111-A075-0018F3D096BC.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/FAF8EFD4-69C3-E111-BE0F-002618FDA265.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/FAF2387A-8CC2-E111-9E37-003048FFCB84.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/FADA3E9E-A6C3-E111-B593-0026189438CF.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/FAD341D2-62C3-E111-929A-0026189438DE.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/FAAA28E3-61C3-E111-AE8B-003048678ED2.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/FAA0C509-90C2-E111-A9BF-001A92811734.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/FA385201-83C2-E111-A61A-003048FFCB84.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/FA3401D0-A5C1-E111-8EB6-002618943876.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/FA075ED0-89C1-E111-8D6C-00261894380D.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/F8D7E03A-97C1-E111-88C0-002618943959.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/F8D712B4-B3C2-E111-BC3F-001A92971B20.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/F8CB88D2-07C3-E111-8995-001A92811718.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/F89E5057-5CC2-E111-8C7E-003048FFD728.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/F87E60B4-A4C3-E111-9566-002618943940.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/F8764998-08C3-E111-B549-002618943896.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/F6DAB833-6FC2-E111-BE67-002618943879.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/F608D651-82C3-E111-93C0-00261894398C.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/F4FEF749-ADC1-E111-B9A3-003048678C9A.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/F4FC9FB3-B5C2-E111-974A-001BFCDBD1B6.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/F4DFD84F-7AC3-E111-AEDC-00304867BED8.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/F4BD0103-70C3-E111-89B4-001A928116EA.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/F494FCD4-7CC2-E111-98E6-003048FFCB8C.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/F2C57494-88C3-E111-B31D-003048FFCC0A.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/F2A9C54B-74C3-E111-9276-002618943970.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/F29EB862-07C3-E111-BFDB-00261894392F.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/F0E731C6-7FC2-E111-B5D0-0018F3D0962A.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/F0E42B4B-76C3-E111-94ED-00304867906C.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/F0E20A47-85C2-E111-B822-0025905822B6.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/F0884C00-E0C1-E111-850E-003048FFCB6A.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/F02B518B-85C1-E111-9034-003048679166.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/F0246E2F-84C2-E111-AE73-001BFCDBD190.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/EEFB7DE9-5CC3-E111-9BEF-003048678BAA.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/EEEE9393-9FC3-E111-80B6-0018F3D09700.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/EEB0D491-08C3-E111-B9DD-0018F3D0960A.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/EE5FCC82-07C3-E111-8B71-003048678EE2.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/EE5EC846-4DC3-E111-B3C1-0026189437ED.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/EE45AEAC-98C2-E111-9727-003048FFD720.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/EE4073D2-9FC1-E111-99CB-0026189438FD.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/ECEF46E6-9BC2-E111-8ADA-001BFCDBD11E.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/ECA501B3-95C2-E111-95D9-003048FFD7A2.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/EC32BA4C-51C3-E111-8733-002618943937.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/EC24C3FE-AAC1-E111-BD34-00261894393F.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/EADA5661-09C3-E111-B0D2-0018F3D09650.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/EAD72E53-8DC3-E111-81F5-003048679296.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/EAD30793-82C3-E111-9E9D-001A92810AA6.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/EABAD84D-B1C2-E111-A5AD-002618943877.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/EA775CFD-97C3-E111-BCBA-0018F3D09630.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/EA5EAC7E-86C2-E111-98B0-003048FFD730.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/EA5123FC-B7C2-E111-BED3-001A92971B8A.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/EA3FDAAE-14C3-E111-A5FD-0018F3D096A0.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/E8565988-7AC2-E111-9FA5-00304867BEDE.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/E8489F1C-94C3-E111-91B4-0018F3D09630.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/E6F2E623-07C3-E111-9AAE-003048FF9AA6.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/E6EE72C4-06C3-E111-8B52-003048FFD7D4.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/E6D232E8-76C2-E111-AA97-003048678F02.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/E6C8C573-07C3-E111-93E9-001A92971B94.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/E6BEA965-D3C1-E111-B106-003048FFD736.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/E6BD370E-A1C3-E111-BD47-001A92971B8A.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/E6A16F67-09C3-E111-9AC7-00261894392F.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/E66C4B9C-ABC2-E111-BCB9-00261894397B.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/E65D74DC-6EC3-E111-ACC8-002618943927.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/E624E2DA-09C3-E111-813D-0018F3D096BC.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/E4F5FFB6-91C2-E111-8BD2-003048FFCB74.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/E4BF6E1B-4EC3-E111-B614-002618943935.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/E4BD0ACF-2DC3-E111-8574-0026189438BF.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/E4A8B681-07C3-E111-941F-003048679228.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/E49980F9-93C2-E111-8E67-003048FFD736.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/E4794C89-75C3-E111-9ED0-003048FFCB8C.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/E469BFFC-59C2-E111-85C5-00248C0BE016.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/E443D890-96C2-E111-AB63-003048FFCC18.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/E2C11EE3-72C2-E111-89EE-0018F3D096BE.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/E29B3391-07C3-E111-B4CB-003048679182.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/E277118C-67C2-E111-A2F0-003048679248.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/E26726C1-81C3-E111-8E8C-001A92971B62.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/E2642588-B0C2-E111-9DF6-002618943877.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/E245CF6B-6AC2-E111-B43C-001A92971B48.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/E0CE5073-1DC3-E111-B958-001A928116B8.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/E06C2A38-09C3-E111-B520-002618943943.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/DED8F18D-72C3-E111-A911-003048678EE2.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/DE76B8DA-11C3-E111-9ECB-001A92971B3C.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/DE607182-77C2-E111-AC6D-001A92810AC8.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/DE32B9E2-74C3-E111-AE4A-001A92971B82.root"
,"/store/mc/Fall11/TT_noCorr_7TeV-mcatnlo/AODSIM/PU_S6_START42_V14B-v1/0000/DE268DA1-58C2-E111-9715-0026189437ED.root"
])
