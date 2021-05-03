#!/bin/bash
# Before running this script it is necessary to create a subfolder with running config files
exec >> check_ios.rep
REQUIRED_IOS='16.9b'
VERSION_SEARCH_TEXT='version'

echo $(date +"%F") 
echo
echo "STARTING IOS CHECK " 
for f in ios_configs/* 
do 
  cat $f | grep hostname  
  IOS_VERSION=$(cat $f | grep $VERSION_SEARCH_TEXT | cut -d' ' -f2)
  
  echo $IOS_VERSION 
  if [  $REQUIRED_IOS != $IOS_VERSION ] ; then
    echo Upgrade ios version to: $REQUIRED_IOS 
  else 
    echo No Upgrade needed 
  fi

  echo 
done

echo "ENDING IOS CHECK" 
