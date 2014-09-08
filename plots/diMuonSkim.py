dataJobs = "/disk1/hoehle/CMSSW_4_2_8_patch7/MySCAnalysis/runData/Data_DiMuonOnly_DoubleMuRunB_Skim_Grid_2014-08-22_02-17-58/crabJobResults.JSON"
#remDataJobs = '/disk1/hoehle/CMSSW_4_2_8_patch7/MySCAnalysis/runData/Data_DiMuonOnly_OtherThanDoubleMuRunB_Skim_Grid__2014-08-14_00-44-57/crabJobResults.JSON'

#bkgJobs = "/disk1/hoehle/CMSSW_4_2_8_patch7/MySCAnalysis/testAnalysis/OtherBackgrounds_DiMuonOnly_Skim_Grid_2014-08-05_15-22-53/crabJobResults.JSON"
bkgJobs = "/disk1/hoehle/CMSSW_4_2_8_patch7/MySCAnalysis/testAnalysis/OtherBackgrounds_DiMuonOnly_Skim_Grid_2014-08-19_21-20-04/crabJobResults.JSON"

#ttbarBkgCorr = "/disk1/hoehle/CMSSW_4_2_8_patch7/MySCAnalysis/runSignal/TTBkg_DiMuonOnly_Skim_Grid_2014-08-03_18-55-45/crabJobResults.json"
#ttbarSigCorr = "/disk1/hoehle/CMSSW_4_2_8_patch7/MySCAnalysis/runSignal/TTSignal_DiMuonOnly_Skim_Grid__2014-08-03_17-06-49/crabJobResults.json"

#ttbarSigNoCorr = "/disk1/hoehle/CMSSW_4_2_8_patch7/MySCAnalysis/runSignal/TTnoCorrSigSamples_DiMuonOnly_Skim_Grid__2014-08-06_16-54-29/crabJobResults.json"
#ttbarBkgNoCorr = "/disk1/hoehle/CMSSW_4_2_8_patch7/MySCAnalysis/runSignal/TTnoCorrSamples_DiMuonOnly_Skim_Grid__2014-08-06_15-02-12/crabJobResults.json"

ttbar = "/disk1/hoehle/CMSSW_4_2_8_patch7/MySCAnalysis/runSignal/TTSamples_DiMuonOnly_Skim_Grid__2014-08-19_21-19-09/crabJobResults.JSON"
#/disk1/hoehle/CMSSW_4_2_8_patch7/MySCAnalysis/runSignal/TTSamples_DiMuonOnly_Skim_Grid__2014-08-15_12-21-08/crabJobResults.json"

import ROOT
from DataFormats.FWLite import Events,Handle # cmssw
import json
import sys,os
sys.path.extend([os.getenv('CMSSW_BASE')+'/MyCMSSWAnalysisTools/Tools',os.getenv('CMSSW_BASE')+'/MyCMSSWAnalysisTools',os.getenv('HOME')+'/PyRoot_Helpers'])
import coreTools
#import MyStyles_cfi
#MyStyles_cfi.NormalStyle()
#ROOT.gROOT.SetStyle("Plain")
import plotHelpers
########################
class fillDistributions(object):
  def __init__(self,evts,label,debug=False):
    self.events = evts
    self.debug=debug
    self.plots={}
    self.label=label
    self.myTH1D = plotHelpers.MyHistFunctions_cfi.myTH1DCreator(label)
  def loop(self,maxEvents=-1):
    muonHandle = Handle('std::vector<pat::Muon>'); muonLabel = "mySelectedPatMuons" #mySelectedPatMuons2p1" 
    muonPt = ROOT.TH1D("muonPt"+"_"+self.label,"muonPt",50,0,200)
    muonNum = ROOT.TH1D("muonNum"+"_"+self.label,"muonNum",5,-0.5,4.5)
    leadingMuonPt = ROOT.TH1D("leadingMuonPt"+"_"+self.label,"leadingMuonPt",50,0,200)
    secondLeadingMuonPt = ROOT.TH1D("secondLeadingMuonPt"+"_"+self.label,"secondLeadingMuonPt",50,0,200)
    ################
    metHandle = Handle('std::vector<pat::MET>'); metLabel = "DiMuonmyselectedPatMETs"
    metPt = ROOT.TH1D("firstMETPt"+"_"+self.label,"firstMETPt",50,0,200)
    metNum = ROOT.TH1D("metNum"+"_"+self.label,"metNum",5,-0.5,4.5)
    #######################
    diLepMuonCandHandle = Handle('std::vector<pat::CompositeCandidate>') ;diLepMuonCandLabel="DiLepCandMuons"
    diLepMuonCandMass = ROOT.TH1D("diLepMuonCandMass"+"_"+self.label,"diLepMuonCandMass",100,0.0,200)
    diLepMuonCandNum = ROOT.TH1D("diLepMuonCandNum"+"_"+self.label,"diLepMuonCandNum",5,-0.5,4.5)
    #############
    offlinePVtxsHandle = Handle('std::vector<reco::Vertex>'); offlinePVtxsLabel = "offlinePrimaryVertices"
    offlinePVtxsNum = self.myTH1D.create("offlinePVtxs",51,-0.5,50.5)
    ##################
    if self.events.size() > 0:
      for i,event in enumerate(self.events):
        if maxEvents > 0 and i >= maxEvents:
          break
        ####### muons
        event.getByLabel(muonLabel,muonHandle)
        muons = muonHandle.product()
        muonNum.Fill(muons.size())
        leadingMuonPt.Fill(muons[0].pt())
	secondLeadingMuonPt.Fill(muons[1].pt())
        for muon in muons:
          muonPt.Fill(muon.pt())
        ######## mets
        event.getByLabel(metLabel,metHandle)
        mets = metHandle.product()
        metNum.Fill(mets.size())
        metPt.Fill(mets[0].pt())
        ########## diLepMuonCand
        event.getByLabel(diLepMuonCandLabel,diLepMuonCandHandle);
	diLepMuonCands = diLepMuonCandHandle.product();diLepMuonCandNum.Fill(diLepMuonCands.size())
        for cand in diLepMuonCands:
          diLepMuonCandMass.Fill(cand.mass())
        ################# Vtxs
        event.getByLabel(offlinePVtxsLabel,offlinePVtxsHandle); offlinePVtxs = offlinePVtxsHandle.product()
	offlinePVtxsNum.Fill(offlinePVtxs.size())
    else:
      print "warning no events in ",self.events._filenames
    ## save hists
    self.plots.update({"muonNum":muonNum.Clone(),"muonPt":muonPt.Clone(),"metNum":metNum,"metPt":metPt,"diLepMuonCandNum":diLepMuonCandNum,"diLepMuonCandMass":diLepMuonCandMass,"leadingMuonPt":leadingMuonPt.Clone(),"secondLeadingMuonPt":secondLeadingMuonPt.Clone(),"offlinePVtxsNum":offlinePVtxsNum.Clone() })
    for h in self.plots.values():
      setattr(h,'label',self.label)
#################
import copy
#ROOT.gROOT.SetBatch()
timeStamp =  coreTools.getTimeStamp()
######################
def loopDatasets(dataS,silent=False):
  plts = {}
  for l,j in dataS.iteritems():
    if not silent:
      print "dataSet job ",l
    crabJ = json.load(open(j["crabJson"]))
    plts[l] = {'plots':{},'additive':[]};
    if crabJ.has_key('sample') and crabJ['sample'].has_key('xSec'):
      plts[l]['color'] = crabJ['sample']['color']
      plts[l]['label'] = crabJ['sample']['label']
      plts[l]['xSec'] = crabJ['sample']['xSec'];plts[l]['additive'].append('xSec')
      plts[l]['inputEvents'] = j['EventsRead'];plts[l]['additive'].append('inputEvents')
      if not silent:
        print "adding additional information ","color ",crabJ['sample']['color']," label ",crabJ['sample']['label']," xSec ",crabJ['sample']['xSec']," inputEvts ",j['EventsRead']
      if j['EventsRead'] != int(j['dasNeventsInput']):
        print "warning ",l," input events differ ",j['EventsRead']," ",j['dasNeventsInput']
    if j.has_key('crabIntLumi'):
      plts[l]['intLumi'] = j['crabIntLumi']; plts[l]['additive'].append('intLumi')
    mergedFile = str(crabJ['mergedFilename'])
    if not silent:
      print "mergedFile: ",mergedFile
    events = Events(mergedFile)
    if not silent:
      print "events ",events.size()
    dists = fillDistributions(events,l)
    dists.loop()
    plts[l]['plots'].update(copy.deepcopy(dists.plots))
  return plts
####################
data = json.load(open(dataJobs))
#remData = json.load(open(remDataJobs))
allDataPlots = loopDatasets(data)
dataDoubleMu = [
	'DoubleMu_Run2011A-PromptReco-v4_part_0',
	'DoubleMu_Run2011B-PromptReco-v1_part_0',
	'DoubleMu_Run2011A-PromptReco-v6_part_0',
	'DoubleMu_Run2011A-PromptReco-v4_part_1',
	'DoubleMu_Run2011B-PromptReco-v1_part_1',
	'DoubleMu_Run2011B-PromptReco-v1_part_2',
	'DoubleMu_Run2011A-May10ReReco-v1_part_0',
	'DoubleMu_Run2011A-05Aug2011-v1_part_1',
	'DoubleMu_Run2011A-05Aug2011-v1_part_0'
	]
dataPlots = getInterestingSamples( dataDoubleMu , allDataPlots )
#remDataPlots = loopDatasets(remData)
#dataPlots.update(remDataPlots)
#######################
##########################
hists = dataPlots.values()[0]['plots'].keys()
##############
##plotting
#####################
cans = plotHelpers.plotHistDict(hists,dataPlots,postfix="data_"+timeStamp)
myColors = {
	"singleTop":ROOT.kOrange+1 #46 #ROOT.kMagenta
 	,"diBoson":ROOT.kBlue
	,"drellYan":ROOT.kRed
	,"data":ROOT.kBlack
		}

myCol = ROOT.TColor(1234,255.0/255,128.0/255,0.0/255)
######################
mergedDataHists,mergeLabels = plotHelpers.mergePlots(dataPlots)  
dataMergedPlots = {"DoubleMu_Run2011AB": mergedDataHists }
for pd in dataMergedPlots.values():
  for h in pd['plots'].values():
    setattr(h,"myDrawOption","E1")
    setattr(h,"label",'data')
    setattr(h,"legDrawOpt","lep")
    h.SetMarkerStyle(21)
    h.SetLineWidth(2)
    setattr(h,'myColor',myColors['data']);setattr(h,'myDrawOption','E1')
dataCans = plotHelpers.plotHistDict(hists,dataMergedPlots,"DoubleMu_Run2011AB_merged_"+timeStamp)
###################
singleTop = [
	"T_TuneZ2_t-channel_7TeV-powheg-tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM"
	,"T_TuneZ2_s-channel_7TeV-powheg-tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM"
	#,"T_TuneZ2_tW-channel-DR_7TeV-powheg-tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM"
	,"T_TuneZ2_tW-channel-DS_7TeV-powheg-tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM"
	,"Tbar_TuneZ2_s-channel_7TeV-powheg-tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM"
	,"Tbar_TuneZ2_t-channel_7TeV-powheg-tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM"
	#,"Tbar_TuneZ2_tW-channel-DR_7TeV-powheg-tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM"
	,"Tbar_TuneZ2_tW-channel-DS_7TeV-powheg-tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM"
	]
diBoson = [
        "WWJetsTo2L2Nu_TuneZ2_7TeV-madgraph-tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM"
        #,"WZ_TuneZ2_7TeV_pythia6_tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM"
        ,"WZJetsTo2L2Q_TuneZ2_7TeV-madgraph-tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM"
        #,ZZ_TuneZ2_7TeV_pythia6_tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM"
        ,"ZZJetsTo2L2Nu_TuneZ2_7TeV-madgraph-tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM"
        ,"ZZJetsTo2L2Q_TuneZ2_7TeV-madgraph-tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM"
        ,"ZZTo2mu2tau_mll4_7TeV-powheg-pythia6__Fall11-PU_S6_START42_V14B-v1__AODSIM"
	]
drellYan = [
        "DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM"
        ,"DYJetsToLL_M-10To50_TuneZ2_7TeV-madgraph__Fall11-PU_S6_START42_V14B-v1__AODSIM"
	]
interestingBkgs = [
	"WWJetsTo2L2Nu_TuneZ2_7TeV-madgraph-tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM"
	#,"WZ_TuneZ2_7TeV_pythia6_tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM"
        ,"WZJetsTo2L2Q_TuneZ2_7TeV-madgraph-tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM"
	#,ZZ_TuneZ2_7TeV_pythia6_tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM"
	,"ZZJetsTo2L2Nu_TuneZ2_7TeV-madgraph-tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM"
	,"ZZJetsTo2L2Q_TuneZ2_7TeV-madgraph-tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM"
	,"ZZTo2mu2tau_mll4_7TeV-powheg-pythia6__Fall11-PU_S6_START42_V14B-v1__AODSIM"
	,"DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola__Fall11-PU_S6_START42_V14B-v1__AODSIM"
	,"DYJetsToLL_M-10To50_TuneZ2_7TeV-madgraph__Fall11-PU_S6_START42_V14B-v1__AODSIM"
	]
####################
import re

bkgJobsDict = json.load(open(bkgJobs))
bkgPlots = loopDatasets(bkgJobsDict)
#bkgCans = plotHelpers.plotHistDict(hists,bkgPlots,postfix="bkgs_"+timeStamp)
##############
def getInterestingSamples(samps,plots):
  return dict([ (k,it) for k,it in plots.iteritems() if re.match('(.*_[a-zA-Z]*)_[0-9]{4}-[0-9]{2}-[0-9]{2}_[0-9]{2}-[0-9]{2}-[0-9]{2}$',k).group(1) in samps ])
#################
singleTopPlots = getInterestingSamples( singleTop , bkgPlots )
singleTopMergedHists,singleTopMergedLabels = plotHelpers.mergePlots(singleTopPlots,debug=False,scaleWithLumis=True)

drellYanPlots = getInterestingSamples(drellYan,bkgPlots)
drellYanMergedHists,drellYanMergedLabels = plotHelpers.mergePlots(drellYanPlots,debug=False,scaleWithLumis=True)
diBosonPlots = getInterestingSamples(diBoson,bkgPlots)
diBosonMergedHists , diBosonMergedLabels = plotHelpers.mergePlots(diBosonPlots,debug=False,scaleWithLumis=True)
diBosonMergedHists.update({'label':"diBoson",'color':myColors["diBoson"]}); 
drellYanMergedHists.update({'label':"drellYan",'color':myColors["drellYan"]})
singleTopMergedHists.update({'color':myColors["singleTop"],'label':"singleTop"})
mergedPlots = {"singleTop": singleTopMergedHists,"diBoson":diBosonMergedHists,"drellYan":drellYanMergedHists}

globalIntLumi = sum( [d['intLumi'] for d in dataMergedPlots.values()] )/1000/1000
#print "intLumi ",globalIntLumi
#for h in dataMergedPlots['DoubleMu_Run2011AB']["plots"].values():
#  setattr(h,'myColor',myColors['data']);setattr(h,'myDrawOption','E1')
############################
bkgMCscaledPlots = {}; bkgMCscaledPlots.update(copy.deepcopy(mergedPlots))
#ttbarSigCorrPlots = loopDatasets(json.load(open(ttbarSigCorr)));
#ttbarBkgCorrPlots = loopDatasets(json.load(open(ttbarBkgCorr)));
ttbarPlots = loopDatasets(json.load(open(ttbar)));
ttbarCorr = [
	"TT_TuneZ2_7TeV-mcatnlo__Fall11-PU_S6_START42_V14B-v1__AODSIM_Bck"
	,"TT_TuneZ2_7TeV-mcatnlo__Fall11-PU_S6_START42_V14B-v1__AODSIM_Signal"]
ttbarCorrPlots = getInterestingSamples( ttbarCorr , ttbarPlots )
################# FIX BEGIN
#ttbarSigCorrPlots['TT_TuneZ2_7TeV-mcatnlo__Fall11-PU_S6_START42_V14B-v1__AODSIM_Signal_2014-08-03_17-06-49']['inputEvents'] *= 4.0/81.0
#ttbarBkgCorrPlots['TT_TuneZ2_7TeV-mcatnlo__Fall11-PU_S6_START42_V14B-v1__AODSIM_Bck_2014-08-03_18-55-45']['inputEvents'] *= 77.0/81.0 
ttbarCorrPlots["TT_TuneZ2_7TeV-mcatnlo__Fall11-PU_S6_START42_V14B-v1__AODSIM_Bck_2014-08-19_21-19-09"]['inputEvents'] *= 77.0/81.0
ttbarCorrPlots["TT_TuneZ2_7TeV-mcatnlo__Fall11-PU_S6_START42_V14B-v1__AODSIM_Signal_2014-08-19_21-19-09"]['inputEvents'] *= 4.0/81.0
#####################FIX END
#bkgMCscaledPlots.update(copy.deepcopy(ttbarSigCorrPlots))
#bkgMCscaledPlots.update(copy.deepcopy(ttbarBkgCorrPlots))
bkgMCscaledPlots.update(copy.deepcopy(ttbarCorrPlots))
####################
#bkgMCscaledPlots.update( getInterestingSamples(interestingBkgs , bkgPlots) )
print "scaling to luminositiy ",globalIntLumi
for s,dct in bkgMCscaledPlots.iteritems():
  for h in dct["plots"].values():
    print "sample ",s," hist ",h," fac ",(dct['xSec']*globalIntLumi*1.0)/float(dct['inputEvents'])," xSec ",dct['xSec']," lum ",globalIntLumi," inputEvts ",dct['inputEvents']
    h.Scale((dct['xSec']*globalIntLumi)/float(dct['inputEvents']));setattr(h,'myDrawOption','HIST');setattr(h,'myColor',dct['color']);h.SetLineColor(dct['color'])
    if dct.has_key('label'):
      setattr(h,'label',dct['label'])
plotsToCompare = {}
plotsToCompare.update(dataMergedPlots)

bkgHists  = dict( [ ( k , [ samPl['plots'][k] for samPl in bkgMCscaledPlots.values()] )  for k in bkgMCscaledPlots.values()[0]['plots'].keys() ])
#for l,h in bkgHists.iteritems():
#   print (l)
#   for h1 in h:
#      print (" ",h1.GetName(),h1.myColor)
bkgStacks = dict(  [ (h,plotHelpers.MyHistFunctions_cfi.stackHists(bkgHists[h])) for h in bkgHists.keys() ] )
#print "testing stacks"
#for l,h in bkgStacks.iteritems():
#   print (l)
#   for h1 in h.hists:
#      print (" ",h1.GetName(),h1.myColor)
#
#######
dataMCplots = {};dataMcPlotsLabel="dataVSmc"
for h in dataMergedPlots['DoubleMu_Run2011AB']["plots"].keys():
  tmpPlot = plotHelpers.plotdataVsMC(h,dataMergedPlots['DoubleMu_Run2011AB']["plots"][h],bkgHists[h])
  tmpPlot.plot()
  tmpPlot.can.SaveAs( tmpPlot.can.GetName()+"_"+dataMcPlotsLabel+".pdf")
  dataMCplots[h]=tmpPlot
###############
#print "testing after"
#for l,h in bkgStacks.iteritems():
#   print (l)
#   for h1 in h.histsStacked:
#      print (" ",h1.GetName(),h1.myColor)
#   print "stacked"
#   for h1 in h.histsStacked:
#     print (" ",h1.GetName(),h1.myColor)
############
#plotsToCompare.update(bkgMCscaledPlots)
#dataMCcanvas = plotHelpers.plotHistDict(hists,plotsToCompare,postfix="firstDataMC")




