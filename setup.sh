#!/bin/bash

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
git clone git@github.com:fhoehle/DiLeptonicSelection.git
cd DiLeptonicSelection
git checkout V00-04
./install/installMyFWK.sh
# tools
cd $CMSSW_BASE
git clone git@github.com:fhoehle/MyCMSSWAnalysisTools.git
cd MyCMSSWAnalysisTools
git checkout V00-03
#
cd $CMSSW_BASE

