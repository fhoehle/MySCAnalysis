#!/bin/bash
pkgs=(
  "DiLeptonicSelection  $CMSSW_BASE ./install/installMyFWK.sh" 
  "MyCMSSWAnalysisTools  $CMSSW_BASE ./install.sh" #"MyCMSSWAnalysisTools  $CMSSW_BASE ./install.sh testSLC6"
)
cmsswVer=CMSSW_5_3_
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
if [ "X$SCRAM_ARCH" != "Xslc6_amd64_gcc472" ]; then 
  echo "missing/wrong SCRAM_ARCH: $SCRAM_ARCH"
  exit 1
fi
if [ ! "$CMSSW_BASE" =~ "CMSSW_5_3_"  -a ! "$CMSSW_BASE" =~ "CMSSW_4_2_7"]; then
  echo "missing CMSSW_BASE cmsenv"
  exit 1
fi
cd $CMSSW_BASE
if [ ! -d "$CMSSW_BASE/src/.git" ]; then
  git cms-init
fi
#set -e
# install my packages
for idx in ${!pkgs[*]}; do
  cd `echo ${pkgs[$idx]} | awk '{print $2}'`
  getGitPackage `echo ${pkgs[$idx]} | awk '{print $1}'`
  if  [ "X`echo ${pkgs[$idx]} | awk '{print $4}'`" != "X" ]; then
    git checkout `echo ${pkgs[$idx]} | awk '{print $4}'`
  fi
  if  [ "X`echo ${pkgs[$idx]} | awk '{print $3}'`" != "X" ]; then
    echo "calling additional command "`echo ${pkgs[$idx]} | awk '{print $3}'`
    eval `echo ${pkgs[$idx]} | awk '{print $3}'`
  fi
  cd $CMSSW_BASE
done

