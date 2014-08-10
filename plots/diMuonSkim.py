dataJobs = "/disk1/hoehle/CMSSW_4_2_8_patch7/MySCAnalysis/runData/Data_DiMuonOnly_DoubleMuRunB_Skim_Grid__2014-08-03_19-05-48/crabJobResults.JSON"
bkgJobs = "/disk1/hoehle/CMSSW_4_2_8_patch7/MySCAnalysis/testAnalysis/OtherBackgrounds_DiMuonOnly_Skim_Grid_2014-08-05_15-22-53/crabJobResults.JSON"

ttbarBkgCorr = "/disk1/hoehle/CMSSW_4_2_8_patch7/MySCAnalysis/runSignal/TTBkg_DiMuonOnly_Skim_Grid_2014-08-03_18-55-45/crabJobResults.json"
ttbarSigCorr = "/disk1/hoehle/CMSSW_4_2_8_patch7/MySCAnalysis/runSignal/TTSignal_DiMuonOnly_Skim_Grid__2014-08-03_17-06-49/crabJobResults.json"

ttbarSigNoCorr = "/disk1/hoehle/CMSSW_4_2_8_patch7/MySCAnalysis/runSignal/TTnoCorrSigSamples_DiMuonOnly_Skim_Grid__2014-08-06_16-54-29/crabJobResults.json"
ttbarBkgNoCorr = "/disk1/hoehle/CMSSW_4_2_8_patch7/MySCAnalysis/runSignal/TTnoCorrSamples_DiMuonOnly_Skim_Grid__2014-08-06_15-02-12/crabJobResults.json"

import ROOT
from DataFormats.FWLite import Events,Handle # cmssw
import json
import sys,os
sys.path.extend([os.getenv('CMSSW_BASE')+'/MyCMSSWAnalysisTools/Tools',os.getenv('CMSSW_BASE')+'/MyCMSSWAnalysisTools',os.getenv('HOME')+'/PyRoot_Helpers'])
import coreTools
import MyStyles_cfi
MyStyles_cfi.NormalStyle()
########################
class fillDistributions(object):
  def __init__(self,evts,label,debug=False):
    self.events = evts
    self.debug=debug
    self.plots={}
    self.label=label
  def loop(self,maxEvents=-1):
    muonHandle = Handle('std::vector<pat::Muon>'); muonLabel = "mySelectedPatMuons2p1" 
    muonPt = ROOT.TH1D("muonPt"+"_"+self.label,"muonPt",50,0,200)
    muonNum = ROOT.TH1D("muonNum"+"_"+self.label,"muonNum",5,-0.5,4.5)
    for i,event in enumerate(events):
      if maxEvents > 0 and i >= maxEvents:
        break
      ####### muons
      event.getByLabel(muonLabel,muonHandle)
      muons = muonHandle.product()
      muonNum.Fill(muons.size())
      for muon in muons:
        muonPt.Fill(muon.pt())
    ## save hists
    self.plots.update({"muonNum":muonNum.Clone(),"muonPt":muonPt.Clone()})
######################
data = json.load(open(dataJobs))
plots = {}
import copy
ROOT.gROOT.SetBatch()
timeStamp =  coreTools.getTimeStamp()
for l,j in data.iteritems():
  print "data ",l
  crabJ = json.load(open(j["crabJson"]))
  mergedFile = str(crabJ['mergedFilename'])
  print "mergedFile: ",mergedFile
  events = Events(mergedFile)
  print "events ",events.size()
  dists = fillDistributions(events,l)
  dists.loop()
  plots[l]=copy.deepcopy(dists.plots)
##########################
hists = plots.values()[0].keys()
cans = {}
import MyHistFunctions_cfi

#######
for h in hists:
  can = ROOT.TCanvas("c_"+h,h)
  for j,i in enumerate(plots.values()):
    i[h].SetLineColor(j+1);
    i[h].Draw("" if j == 0 else "sames")
  legAdder =  MyHistFunctions_cfi.myLegend(canvas=can,debug=True)
  legAdder.createLegend()
  legAdder.drawLegend()
  cans[h] = copy.deepcopy(legAdder.canvas)
  cans[h].SaveAs( cans[h].GetName()+"_"+timeStamp+".pdf") 





