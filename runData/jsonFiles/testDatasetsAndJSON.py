import sys,os
sys.path.append(os.getenv('CMSSW_BASE')+'/MyCMSSWAnalysisTools')
import Tools
import Tools.lumiTools as lumiTools
import imp
testFile = os.getenv('CMSSW_BASE')+'/MySCAnalysis/runData/diLeptonData.py'
test = imp.load_source('module.name', testFile)
dataDatasets = test.dataDatasets
#####################
#expecting
# dataDatasets = {'label':{'datasetJSON':'jsonFileOfDataset'}}
#
#######################
import re
primDataS = re.compile('/([^\/][^\/]*)/.*')
dataStreams = set([primDataS.match(d['datasetName']).group(1) for d in  dataDatasets.values()])
print "dataStream sanity"
for dataStream in list(dataStreams):
  import itertools
  print "testing ",dataStream
  #dataDatasets["pommesMuEG"]={'datasetJSON':'/disk1/hoehle/CMSSW_4_2_8_patch7/MySCAnalysis/runData/jsonFiles/Cert_160404-180252_7TeV_PromptReco_Collisions11_JSON.txt'}
  for c in itertools.combinations([(k,i['datasetJSON']) for k,i in dataDatasets.iteritems() if dataStream in k],2):
    overLap = lumiTools.LumiList(c[0][1]) & lumiTools.LumiList(c[1][1])
    if len(overLap) != 0 :
      print "attention ",c[0]," overlap with ",c[1]
################
intLumisDatasets ={}
for d in dataDatasets.values():
  print(d['datasetName'])
  intLumisDatasets[d['datasetName']] = lumiTools.calcLumi(d['datasetJSON'])
############################
for dataStream in dataStreams:
  print "stream ",dataStream," sum of "," + ".join([k for k in intLumisDatasets.keys() if dataStream in k])," ",sum ([ i for k,i in intLumisDatasets.iteritems() if dataStream in k])/1000/1000
print "#####################"
print "testing lumiMasks"
for d in dataDatasets.values():
  print(d['datasetName'])
  print (d['crabConfig']['CMSSW']['lumi_mask'] )
testLMask = dataDatasets.values()[0]['crabConfig']['CMSSW']['lumi_mask']
goldJSON = lumiTools.LumiList(filename=testLMask)
intLumiGolden=lumiTools.calcLumi(testLMask)
print "int Lumi lumi_mask ",testLMask," ",intLumiGolden/1000/1000
print "#####################"
print "test intersection with golden JSON/lumi_mask"
intLumisGolden = {}
for d in dataDatasets.values():
  print(d['datasetName'])
  tmpJSON = lumiTools.LumiList(filename=d['datasetJSON']); 
  goldTMP = goldJSON & tmpJSON; tmpFile = '/disk1/hoehle/CMSSW_4_2_8_patch7/MySCAnalysis/runData/jsonFiles/TMPJSON.txt'
  goldTMP.writeJSON(tmpFile)
  intLumisGolden[d['datasetName']]=lumiTools.calcLumi(tmpFile)
os.remove(tmpFile)
for dataStream in dataStreams:
  summedIntLumi = sum([ i for k,i in intLumisGolden.iteritems() if dataStream in k])
  print " sum of with golden JSON intersections "," + ".join([k for k in intLumisDatasets.keys() if dataStream in k])," ",summedIntLumi/1000/1000
  print "lost int lumi of golden JSON ",(intLumiGolden - summedIntLumi)/1000/1000 
