import sys
import FWCore.ParameterSet.Config as cms
print "called with: "," ".join(sys.argv)
process = cms.Process("ADDOWNPARTICLESGENEVENT")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
        'file:myfile.root'
    )
)

process.MyTTbarGenEvent10Parts = cms.EDProducer('MyTTbarGenEvent10Parts',
   genTag = cms.untracked.InputTag("genParticles")
)

process.diLepMcFilter = cms.EDFilter('DiLepMcFilter', 
  ttbarEventTag = cms.untracked.InputTag("MyTTbarGenEvent10Parts"),
  invert = cms.bool(False)
)

process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('myMCatNLO_big_OutputFile.root'),
    outputCommands = cms.untracked.vstring('drop *','keep *GenEventInfoProduct*_*_*_*','keep *_*_*_'+process.name_())
)
process.out.SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring(['p']))
  
process.p = cms.Path(process.MyTTbarGenEvent10Parts*process.diLepMcFilter)

process.e = cms.EndPath(process.out)
process.MessageLogger.cerr.FwkReport.reportEvery = 100
#
import sys
if "crab" not in sys.argv[0]:
 print "use commandline parsing"
 from FWCore.ParameterSet.VarParsing import VarParsing
 options = VarParsing ('analysis')
 options.register ('eventsToProcess',
                   '',
                   VarParsing.multiplicity.list,
                   VarParsing.varType.string,
                   "Events to process")
 options.register('skipEvents', 0, VarParsing.multiplicity.singleton, VarParsing.varType.int, "skip N events")
 options.parseArguments()
 if options.inputFiles != cms.untracked.vstring():
  process.source.fileNames=options.inputFiles
 if options.skipEvents > 0:
  process.source.skipEvents = cms.untracked.uint32(options.skipEvents)
 if options.maxEvents != '':
  process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(options.maxEvents))
 if options.eventsToProcess:
  process.source.eventsToProcess = cms.untracked.VEventRange (options.eventsToProcess)
