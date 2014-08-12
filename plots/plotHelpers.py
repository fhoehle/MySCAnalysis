import sys,os,ROOT,copy
sys.path.extend([os.getenv('CMSSW_BASE')+'/MyCMSSWAnalysisTools/Tools',os.getenv('CMSSW_BASE')+'/MyCMSSWAnalysisTools',os.getenv('HOME')+'/PyRoot_Helpers'])
import coreTools
import MyStyles_cfi
MyStyles_cfi.NormalStyle()
import MyHistFunctions_cfi
######################
def mergePlots(plots,debug=False,scaleWithLumis=False):
  if debug:
    print "begin merging"
  resMerged={'plots':{}};
  resPlots=resMerged['plots']
  resMerged['additive']=[]
  merging=[]
  for (i,(l,pd)) in enumerate(plots.iteritems()):
    merging.append(l)
    scaleFac = 1.
    if scaleWithLumis:
      if debug:
        print l,"scaling, inputEvents ",pd['inputEvents']," xSec ",pd['xSec']," intLum ",float(pd['inputEvents'])/float(pd['xSec'])," 1pb fac. ",
      scaleFac = 1.0*float(pd['xSec'])/float(pd['inputEvents'])
      if debug:
        print scaleFac 
    for k,p in [ (key , pl.Clone()) for key,pl in pd['plots'].iteritems()]:
      p.Sumw2()
      p.Scale(scaleFac)
      if i == 0:
        resPlots[k]=p.Clone()
      else:
        resPlots[k].Add(p)
    
    for k in pd['additive']:
      if i == 0:
        resMerged[k]=float(pd[k])*(scaleFac if k == 'inputEvents' else 1.0)
        resMerged['additive'].append(k)
      else:
        resMerged[k]+=float(pd[k])*(scaleFac if k == 'inputEvents' else 1.0)
    if debug:
      print "steps ",i,resMerged
  if debug:
    print "final ",resMerged
  return resMerged,merging
#############
def plotHistDict(hs,plts,postfix):
  cans={}
  for h in hs:
    cans[h] = plotHDict(h,plts,postfix)
    cans[h].SaveAs( cans[h].GetName()+"_"+postfix+".pdf")
  return cans
#####################
def plotHDict(h,plts,postfix):
    can = ROOT.TCanvas("c_"+h,h)
    for j,i in enumerate(plts.values()):
      plots=i['plots']
      #print plots
      plots[h].SetLineColor(getattr(plots[h],"myColor") if hasattr(plots[h],"myColor") else j+1);
      plots[h].Draw(("" if j == 0 else "sames")+(getattr(plots[h],"myDrawOption") if hasattr(plots[h],"myDrawOption") else "") )
    legAdder =  MyHistFunctions_cfi.myLegend(canvas=can)#,debug=True)
    legAdder.createLegend()
    legAdder.drawLegend()
    return copy.deepcopy(legAdder.canvas)
