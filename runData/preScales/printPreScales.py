#!/usr/bin/env python
import argparse,csv,sys,os
sys.path.append(os.getenv('CMSSW_BASE')+'/MyCMSSWAnalysisTools')
from Tools.tools import executeCommandSameEnv,getTimeStamp
parser = argparse.ArgumentParser()
parser.add_argument('-j',dest='jsonFile',help='jsonFile used for trigger checking')
parser.add_argument('--trigger',help='trigger to be checked for prescales')
parser.add_argument('--lumiContentTriggerByLS',default=None,help='output of lumiContent with trgbyls and json')
parser.add_argument('--usage',action='store_true',default=False,help="print help")
args = parser.parse_args()
if args.usage:
  parser.print_help()
  sys.exit()
print args.jsonFile," ",args.trigger
lumiContentCSV = args.lumiContentTriggerByLS
if not lumiContentCSV:
  # calling lumiContent
  lumiContentCSV = os.path.basename(args.jsonFile)+"_lumiContentOutput_"+getTimeStamp()
  lumiContent = executeCommandSameEnv(os.getenv('CMSSW_BASE')+os.path.sep+'src/RecoLuminosity/LumiDB/scripts/lumiContext.py hltbyls -i '+args.jsonFile+" --name "+args.trigger+" -o "+lumiContentCSV)
  lumiContent.wait()
# processing lumiCotent CSV
reader = csv.reader(open(lumiContentCSV),delimiter=',',quotechar='"')
header = reader.next()
print header
hltInfoByLs = []
for row in reader:
  hltInfo = row[2][1:-1].split(',')
  hltInfoByLs.append(row[:2]+[(hltInfo)])
##sorting and print prescaled lumis
hltInfoByLs.sort(key=lambda hlt : hlt[0]+hlt[1])
for hltInf in hltInfoByLs:
  if hltInf[2][1] != '1':
    print hltInf
