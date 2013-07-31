import ROOT,math
from DataFormats.FWLite import Events, Handle
import getopt, sys, decimal,signal,os
sys.path.extend(['/user/hoehle/SpinCHelpers/',os.getenv('HOME')+'/PyRoot_Helpers/'])
from SpinCorrelationCalculations.CosTheta1Theta2SpinCorrlation_cfi import CosTheta1Theta2
from SpinCorrelationCalculations.CosPhiSpinCorrlation_cfi import CosPhi
from PyRoot_Functions.MyHistFunctions_cfi import MyHistManager
#
def findBinsNZero(h1):
  for i in range(h1.GetNbinsX()):
    if h1.GetBinContent(i+1) != 0:
      print "i+1 ",i+1," ",h1.GetBinContent(i+1)
# catch ctrl C
stopIt=False
def mySignalHandler(signal, frame):
 print "stopping it"
 global stopIt
 stopIt = True
signal.signal(signal.SIGINT, mySignalHandler)
#
opts, args = getopt.getopt(sys.argv[1:], 'i:p:m:',['inputfile=','postfix=','maxEvents=','skipEvents='])
postfix=''
maxEvents=-1; skipEvents=-1
for opt,arg in opts:
 #print opt , " :   " , arg
 if opt in  ("-i","--inputfile"):
  filename=arg
 if opt in ("-p","--postfix"):
  postfix=arg
 if opt in ("-m","--maxEvents"):
  maxEvents=decimal.Decimal(arg)
 if opt in ("--skipEvents"):
  skipEvents=decimal.Decimal(arg)
events = Events (filename)#'patRefSel_muJets_semimuon_ttbar_MoreHyps_Reconstruction_SMAllPART.root')#patRefSel_muJets_nonsemimuon_ttbar_HitFit_Reconstruction.root')
handleMyTTbarEvent = Handle('std::vector<std::vector<reco::GenParticle> >')
labelMyTTbarEvent = ("MyTTbarGenEvent10Parts")#MyTTbarGenEventProd")
genEvtInfoHandle =  Handle("GenEventInfoProduct");genEvtInfoLabel = "generator"
#
ROOT.gROOT.SetBatch()
# Create histograms, etc.
ROOT.gROOT.SetStyle('Plain') # white background
ROOT.gStyle.SetOptStat("emrou"); ROOT.gStyle.SetPalette(1)
ROOT.gStyle.SetOptFit(1)
print "using this input ", filename
h2_cosTheta1Theta2_gen = ROOT.TH2D("h2_cosTheta1Theta2_gen","",11,-1.0,1.0,11,-1.0,1.0)
h2_cosTheta1Theta2_gen_NoMCWeights = ROOT.TH2D("h2_cosTheta1Theta2_gen_NoMCWeights","",11,-1.0,1.0,11,-1.0,1.0)
h2_cosTheta1Theta2_gen_lepPtCut = ROOT.TH2D("h2_cosTheta1Theta2_gen_lepPtCut","h2_cosTheta1Theta2_gen_lepPtCut",11,-1.0,1.0,11,-1.0,1.0)
h2_cosTheta1Theta2_gen_topPtweights = h2_cosTheta1Theta2_gen.Clone("h2_cosTheta1Theta2_gen_topPtweights")
h1_cosPhi_gen = ROOT.TH1D("h1_cosPhi_gen","",11,-1.0,1.0)
h1_cosPhi_gen_topReweighted = h1_cosPhi_gen.Clone("h1_cosPhi_gen_topReweighted");
h1_mcWeights = ROOT.TH1D("h1_mcWeights","",1000,-500,500)
h1_usedMCsings  = ROOT.TH1D("h1_usedMCsings","",5,-2,2)
h1_diffMomentumTopVtx = ROOT.TH1D("h1_diffMomentumTopVtx","h1_diffMomentumTopVtx",100,0,50)
h1_diffMomentumWVtx = ROOT.TH1D("h1_diffMomentumWVtx","h1_diffMomentumWVtx",100,0,50)
h1_topPt = ROOT.TH1D("h1_topPt","h1_topPt",200,0,400)
h1_topEnergy = ROOT.TH1D("h1_topEnergy", "h1_topEnergy",200,0,800)
h1_lepPt = ROOT.TH1D("h1_lepPt","h1_lepPt",200,0,400)
h1_lepEnergy = ROOT.TH1D("h1_lepEnergy","h1_lepEnergy",250,0,500)
h1_ptTopPair = ROOT.TH1D("h1_ptTopPair","h1_ptTopPair",200,0,200)
evtNum=0
myHists=MyHistManager("testSC",True)
# weights according to top pt
topPtWeightFunc = ROOT.TF1("topPtWeightFunc","TMath::Exp(0.199-0.00166*x)")
#particle choice
top0Idx=0;b0Idx=1;W0Idx=2;lep0Idx=3;nu0Idx=4;
top1Idx=5;b1Idx=6;W1Idx=7;lep1Idx=9;nu1Idx=8;
topSub=2;bSub=0;WSub=1;lepSub=0;nuSub=0;
corruptedEvents=0
for i,event in enumerate(events):
 if i%100 == 0:
  print "event: ",i
 if (maxEvents != -1 and i >= maxEvents) or stopIt:
  break
 if skipEvents >= i:
  continue
 event.getByLabel (labelMyTTbarEvent, handleMyTTbarEvent); myTTbarEvent = handleMyTTbarEvent.product()
 event.getByLabel(genEvtInfoLabel,genEvtInfoHandle); genEvtInfo = genEvtInfoHandle.product()
 mcWeight = genEvtInfo.weight(); mcSign = mcWeight/abs(mcWeight) 
 h1_mcWeights.Fill(mcWeight)
 if myTTbarEvent.size() < 10:
  print "ttbar gen event seems to be corrupted, run ",event._event.id ().run()," lumi ",event._event.id ().luminosityBlock()," eventNo ",event._event.id ().event()
  corruptedEvents+=1
  continue
 elif myTTbarEvent[top0Idx].size() <= topSub or myTTbarEvent[top1Idx].size() <= topSub or myTTbarEvent[W0Idx].size() <= WSub or myTTbarEvent[W1Idx].size() <= WSub or myTTbarEvent[b1Idx].size() <= bSub or myTTbarEvent[b0Idx].size() <= bSub or myTTbarEvent[lep1Idx].size() <= lepSub or  myTTbarEvent[lep0Idx].size() <= lepSub or myTTbarEvent[nu1Idx].size() <= nuSub or  myTTbarEvent[nu0Idx].size() <= nuSub :
  print "ttbar gen event seems to be corrupted, run ",event._event.id ().run()," lumi ",event._event.id ().luminosityBlock()," eventNo ",event._event.id ().event()
  print " myTTbarEvent.size() ", myTTbarEvent.size(), " myTTbarEvent[top0Idx].size() ",myTTbarEvent[top0Idx].size()," myTTbarEvent[top1Idx].size() ",myTTbarEvent[top1Idx].size()," myTTbarEvent[W0Idx].size() ",myTTbarEvent[W0Idx].size()," myTTbarEvent[W1Idx].size() ",myTTbarEvent[W1Idx].size()," myTTbarEvent[b1Idx].size() ",myTTbarEvent[b1Idx].size()," myTTbarEvent[b0Idx].size() ",myTTbarEvent[b0Idx].size() 
  continue
  corruptedEvents+=1
  #sys.exit(1)
 b0 = myTTbarEvent[b0Idx][bSub]; 
 top0 = myTTbarEvent[top0Idx][topSub]; 
 W0 = myTTbarEvent[W0Idx][WSub];
 lep0= myTTbarEvent[lep0Idx][lepSub];
 nu0= myTTbarEvent[nu0Idx][nuSub];
 top1 = myTTbarEvent[top1Idx][topSub];
 b1 = myTTbarEvent[b1Idx][bSub];
 W1 = myTTbarEvent[W1Idx][WSub];
 lep1= myTTbarEvent[lep1Idx][lepSub];
 nu1= myTTbarEvent[nu1Idx][nuSub];
 #top pt weight
 topPtWeight = math.sqrt(topPtWeightFunc(top0.pt())*topPtWeightFunc(top1.pt()))
 h1_diffMomentumTopVtx.Fill((top0.p4()-W0.p4()-b0.p4()).P());h1_diffMomentumTopVtx.Fill((top1.p4()-W1.p4()-b1.p4()).P())
 h1_diffMomentumWVtx.Fill((W0.p4()-lep0.p4()-nu0.p4()).P()); h1_diffMomentumWVtx.Fill((W1.p4()-lep1.p4()-nu1.p4()).P())
 #print "status ",lep0.status()," ",nu0.status()," ",top0.status()," ",b0.status()
 if 11 <= math.fabs(lep0.pdgId()) <= 15 and  11 <= math.fabs(lep1.pdgId()) <= 15: 
  #print "test ",lep0.pdgId()," ",lep1.pdgId()
  cosTheta1Theta2 = CosTheta1Theta2 (lep0.p4(),lep1.p4(),top0.p4(),top1.p4())
  #print "cosTheta1Theta2 ",cosTheta1Theta2
  h2_cosTheta1Theta2_gen.Fill(cosTheta1Theta2[0],cosTheta1Theta2[1],mcSign)
  h2_cosTheta1Theta2_gen_topPtweights.Fill(cosTheta1Theta2[0],cosTheta1Theta2[1],topPtWeight*mcSign)
  h1_cosPhi_gen.Fill(CosPhi(lep0.p4(),lep1.p4(),top0.p4(),top1.p4()),mcSign)
  h1_cosPhi_gen_topReweighted.Fill(CosPhi(lep0.p4(),lep1.p4(),top0.p4(),top1.p4()),mcSign*topPtWeight)
  h2_cosTheta1Theta2_gen_NoMCWeights.Fill(cosTheta1Theta2[0],cosTheta1Theta2[1])
  h1_usedMCsings.Fill(mcSign)
  h1_topPt.Fill(top0.pt(),mcSign);h1_topPt.Fill(top1.pt(),mcSign)
  h1_topEnergy.Fill(top0.energy(),mcSign);h1_topEnergy.Fill(top1.energy(),mcSign)
  h1_lepPt.Fill(lep0.pt(),mcSign);h1_lepPt.Fill(lep1.pt(),mcSign)
  h1_lepEnergy.Fill(lep0.energy(),mcSign);h1_lepEnergy.Fill(lep1.energy(),mcSign)
  h1_ptTopPair.Fill((top0.p4()+top1.p4()).Pt(),mcSign)
  if lep0.pt() > 20 and lep1.pt() > 20:
    h2_cosTheta1Theta2_gen_lepPtCut.Fill(cosTheta1Theta2[0],cosTheta1Theta2[1],mcSign)
 #print "done" 
myHists.saveHist(h2_cosTheta1Theta2_gen,"COLZ")
myHists.saveHist(h2_cosTheta1Theta2_gen_topPtweights,"COLZ")
myHists.saveHist(h2_cosTheta1Theta2_gen_NoMCWeights,"COLZ")
myHists.saveHist(h2_cosTheta1Theta2_gen_lepPtCut,"COLZ")
myHists.saveHist(h1_mcWeights,"h")
myHists.saveHist(h1_usedMCsings,"h")
myHists.saveHist(h1_diffMomentumWVtx,"h")
myHists.saveHist(h1_diffMomentumTopVtx,"h")
myHists.saveHist(h1_cosPhi_gen,"h")
myHists.saveHist(h1_cosPhi_gen_topReweighted,"h")
myHists.saveHist(h1_topPt,"h")
myHists.saveHist(h1_topEnergy,"h")
myHists.saveHist(h1_lepPt,"h")
myHists.saveHist(h1_lepEnergy,"h")
myHists.saveHist(h1_ptTopPair,"h")
### CLOSING 
myHists.done()
#fitting
fitCosT1CosT2 = ROOT.TF2("fitCosT1CosT2","[0]*(1/4.0*(1-[1]*x*y)+[2]*x+[3]*y)",-1.0,1.0,-1.0,1.0)
h2_cosTheta1Theta2_gen.GetEntries()
print "fitting with only MC weights"
h2_cosTheta1Theta2_gen.Fit(fitCosT1CosT2.GetName(),"N")
print "chi2/ndf cosTheta1Theta2 ",fitCosT1CosT2.GetChisquare()/fitCosT1CosT2.GetNDF()," weigths used"
print "fitting with additional top pt weights and MC sign"
h2_cosTheta1Theta2_gen_topPtweights.Fit(fitCosT1CosT2.GetName(),"N")
print "chi2/ndf cosTheta1Theta2 ",fitCosT1CosT2.GetChisquare()/fitCosT1CosT2.GetNDF()," also additional top pt weights used"
fitCosPhi = ROOT.TF1("fitCosPhi","[0]*(1-[1]*x)",-1.0,1.0)
print "fit 1D cosPhi mcWeights"
h1_cosPhi_gen.Fit(fitCosPhi.GetName(),"N")
print "chi2/ndf cosPhi: ",fitCosPhi.GetChisquare()/fitCosPhi.GetNDF()," MC weights used"
print  "fit 1D cosPhi mcWeights topPtweight"
h1_cosPhi_gen_topReweighted.Fit(fitCosPhi.GetName(),"N")
print "chi2/ndf cosPhi: ",fitCosPhi.GetChisquare()/fitCosPhi.GetNDF()," MC weights used top pt"
fitCosT1CosT2_NoWeights = fitCosT1CosT2.Clone("fitCosT1CosT2_NoWeights")
print "fitting no weights"
h2_cosTheta1Theta2_gen_NoMCWeights.Fit(fitCosT1CosT2_NoWeights.GetName(),"N")
print "chi2/ndf ",fitCosT1CosT2_NoWeights.GetName()," ",fitCosT1CosT2_NoWeights.GetChisquare()/fitCosT1CosT2_NoWeights.GetNDF()," NO weights used"
print "fitting with weights lepPtCut pt > 20"
fitCosPhi_lepPtCut = fitCosT1CosT2.Clone("fitCosPhi_lepPtCut")
h2_cosTheta1Theta2_gen_lepPtCut.Fit(fitCosPhi_lepPtCut.GetName(),"N")
print "chi2/ndf ",fitCosPhi_lepPtCut.GetName()," ",fitCosPhi_lepPtCut.GetChisquare()/fitCosPhi_lepPtCut.GetNDF()," lepPtCut pt > 20"
### additional output
myHists.additionalObjects.append(fitCosT1CosT2)


print "corruptedEvents ",corruptedEvents
