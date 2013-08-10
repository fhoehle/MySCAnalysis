#!/bin/bash
pkgs=(
  "DiLeptonicSelection ./ " 
  'MyCMSSWAnalysisTools ./ '
)
cmsswVer=CMSSW_4_2_8_patch7
scrArch=slc5_amd64_gcc434
#
if [ "X$CMS_PATH" == "X" ]; then
  echo "source cms environment"
  return 1
fi
####
if [ "X$SCRAM_ARCH" != "X$scrArch" ]; then 
  export SCRAM_ARCH=$scrArch 
fi
if [  "$(basename $PWD)" != "$cmsswVer" ]; then
  echo "not in an CMSSW_X_Y area"
fi
###
eval `scramv1 runtime -sh` # cmsenv
cd $CMSSW_BASE
## setup my packages
for idx in ${!pkgs[*]}; do
  cd $CMSSW_BASE/`echo ${pkgs[$idx]} | awk '{print $2}'`
  cd `echo ${pkgs[$idx]} | awk '{print $1}'`
  if  [ -e "setup.sh" ]; then
    echo "additional setup"
    source setup.sh
  fi
  cd $CMSSW_BASE
done
echo "Sourced MySCAnalysis"
#
#
