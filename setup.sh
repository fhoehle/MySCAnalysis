#!/bin/bash
pkgs=(
  "DiLeptonicSelection ./ V00-09 ./install/installMyFWK.sh" 
  "MyCMSSWAnalysisTools ./ V00-03"
)
cmsswVer=CMSSW_4_2_8_patch7
###################
function getGitPackage {

if [ -d "$1" ]; then
  echo "updating "$1
  cd $1
  git fetch
else
  echo "installing "$1
  git clone git@github.com:fhoehle/$1.git
  cd $1
fi
  
}

echo "Installing/Updating SC analysis "
#
if [ "X$SCRAM_ARCH" != "Xslc5_amd64_gcc434" ]; then 
  echo "missing SCRAM_ARCH"
fi
if [[ ! "$CMSSW_BASE" =~ "$cmsswVer" ]]; then
  echo "missing CMSSW_BASE"
fi
cd $CMSSW_BASE
set -e
# install my packages
for idx in ${!pkgs[*]}; do
  cd $CMSSW_BASE/`echo ${pkgs[$idx]} | awk '{print $2}'`
  getGitPackage `echo ${pkgs[$idx]} | awk '{print $1}'`
  git checkout `echo ${pkgs[$idx]} | awk '{print $3}'`
  if  [ "X`echo ${pkgs[$idx]} | awk '{print $4}'`" != "X" ]; then
    echo "calling additional command "`echo ${pkgs[$idx]} | awk '{print $4}'`
    eval `echo ${pkgs[$idx]} | awk '{print $4}'`
  fi
  cd $CMSSW_BASE
done


