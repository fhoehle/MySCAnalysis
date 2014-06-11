import sys,os,re,ConfigParser
sys.path.append(os.getenv('CMSSW_BASE')+'/MyCMSSWAnalysisTools/')
import CrabTools
########################
allCJsCfgs = CrabTools.getListOfCrabCfgs()
allCJs = [ CrabTools.loadCrabJob(c) for c in allCJsCfgs]
getPart = re.compile('.*(_part_[0-9]).*')
crabCfgParser = ConfigParser.ConfigParser()
for cJ in allCJs:
  print "testing ",cJ.postfix
  if not getPart.match(cJ.postfix).group(1) == getPart.match(cJ.crabCfg['CMSSW']['pset']).group(1):
    print "not matching parts: cJ.postfix: ",cJ.postfix, " cJ.crabCfg['CMSSW']['pset']: ",cJ.crabCfg['CMSSW']['pset']
    #print cJ.crabCfgFilename
    crabCfgParser.read(cJ.crabCfgFilename)
    for k,i in crabCfgParser._sections.iteritems():
      if i.has_key('__name__'):
        if k == i['__name__']:
          del i['__name__']
    #print crabCfgParser._sections
    cJ.crabCfg = crabCfgParser._sections
    CrabTools.saveCrabProp(cJ) 
    
