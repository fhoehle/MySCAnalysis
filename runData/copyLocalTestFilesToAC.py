import sys,os,re
sys.path.append(os.getenv('CMSSW_BASE')+"/GridTools")
import copyExampleFilesToAC
import  dataSamples
debug=True
filesToCopy=[]
for key,item in dataSamples.dataDatasets.iteritems():
  if not item["localFile"]:
    print "fetching for ",key, " a local file"
    if not item["datasetName"]:
      print "dataset missing for ",key
    jsondict = copyExampleFilesToAC.das_client.get_data(copyExampleFilesToAC.host, "file dataset = "+item["datasetName"], copyExampleFilesToAC.idx, 10, copyExampleFilesToAC.debug, copyExampleFilesToAC.thr, copyExampleFilesToAC.ckey, copyExampleFilesToAC.cert)
    files = [ str(ele.get('file')[0].get('name')) for ele in jsondict.get('data')]
    filesToCopy.append({"f":files[0],"d":item["datasetName"]})
        
nodetarget=copyExampleFilesToAC.targetAc
for f in filesToCopy:
    filename = f["f"]
    datasetname = f["d"]
    if debug:
      print filename," ",datasetname
    foldername = re.sub('\/','__',datasetname.lstrip('\/'))
    filenameNew = re.match('.*\/([^\/]*\.root)',filename).group(1)
    targetFileName = nodetarget+"/"+foldername+"/"+filenameNew
    f["origin"]=filename;f["target"]=targetFileName;f["folder"]=foldername
print filesToCopy 
print "starting copy"
copyStep = copyExampleFilesToAC.gridCopyFiles(filesToCopy,debug)
#copyStep.copy()
copyStep.checking()
#copyStep.end()

