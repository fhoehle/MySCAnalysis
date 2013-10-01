import sys,os
sys.path.append(os.getenv('CMSSW_BASE')+'/MyCMSSWAnalysisTools')
import MyDASTools.dasTools as dasTools
dasClient = dasTools.myDasClient()
dasClient.limit=0
datasets = [
  #{'label':'singleMuRun2011APromptV4','name':'/SingleMu/Run2011A-PromptReco-v4/AOD run = 167746','jsonFilename':'singleMuRun2011APromptV4_JSON.txt'}
  {'label':'singleMuRun2011APromptV4','name':'/SingleMu/Run2011A-PromptReco-v4/AOD','jsonFilename':'singleMuRun2011APromptV4_JSON.txt'}
  ,{'label':'singleMuRun2011AMay10ReReco','name':'/SingleMu/Run2011A-May10ReReco-v1/AOD','jsonFilename':'singleMuRun2011AMay10ReReco_JSON.txt'}
  ,{'label':'singleMuRun2011A05Aug','name':'/SingleMu/Run2011A-05Aug2011-v1/AOD','jsonFilename':'singleMuRun2011A05Aug_JSON.txt'}
  ,{'label':'singleMuRun2011A08Nov','name':'/SingleMu/Run2011A-08Nov2011-v1/AOD','jsonFilename':'singleMuRun2011A08Nov_JSON.txt'}
  ,{'label':'singleMuRun2011APromptV6','name':'/SingleMu/Run2011A-PromptReco-v6/AOD','jsonFilename':'singleMuRun2011APromptV6_JSON.txt'}
  ,{'label':'singleMuRun2011BPromptV1','name':'/SingleMu/Run2011B-PromptReco-v1/AOD','jsonFilename':'singleMuRun2011BPromptV1_JSON.txt'}
]
locPrefix = ''
for d in datasets:
  jsonDict = dasClient.getJsonOfDataset(d['name'])
  JSONfilename = locPrefix+d['jsonFilename']
  jsonDict.writeJSON(JSONfilename)
  print 'written ',JSONfilename
