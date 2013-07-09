#!/bin/bash
function getGitPackage {
echo "getting "$1
if [ -d "$1" ]; then
  cd $1
  git fetch
else
  git clone git@github.com:fhoehle/$1.git
  cd $1
fi
  
}
cmsswVer=CMSSW_4_2_8_patch7


echo "Installing SC analysis "
#
if [ "X$SCRAM_ARCH" != "Xslc5_amd64_gcc434" ]; then 
  echo "missing SCRAM_ARCH"
fi
if [[ ! "$CMSSW_BASE" =~ "$cmsswVer" ]]; then
  echo "missing CMSSW_BASE"
fi
cd $CMSSW_BASE
set -e
# di lep selection
getGitPackage "DiLeptonicSelection" 
git checkout V00-07
./install/installMyFWK.sh
cd $CMSSW_BASE
# tools
getGitPackage "MyCMSSWAnalysisTools"
git checkout V00-03
#
cd $CMSSW_BASE

