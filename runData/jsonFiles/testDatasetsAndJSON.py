import sys,os
sys.path.append(os.getenv('CMSSW_BASE')+'/MyCMSSWAnalysisTools')
import Tools
import Tools.lumiTools as lumiTools
import imp
testFile = os.getenv('CMSSW_BASE')+'/MySCAnalysis/runData/diLeptonData.py'
test = imp.load_source('module.name', testFile)
dataDatasets = test.dataDatasets
intLumisDatasets ={}
for d in dataDatasets.values():
  print(d['datasetName'])
  intLumisDatasets[d['datasetName']] = lumiTools.calcLumi(d['datasetJSON'])
import re
primDataS = re.compile('/([^\/][^\/]*)/.*')
dataStreams = set([primDataS.match(k).group(1) for k in intLumisDatasets.keys()])
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
print "test intersection woth golden JSON/lumi_mask"
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
  print "lost int lumi of golden JSON ",(lumiTools.calcLumi(goldJSON.filename) - summedIntLumi)/1000/1000 
