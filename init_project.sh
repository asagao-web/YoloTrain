#!/bin/bash

# Check if a project name was provided
if [ -z "$1" ]
then
  echo "Error: No project name provided."
  echo "Usage: $0 <projectname>"
  exit 1
fi

# Set the project name with "PROJECT_" prefix
projectname="PROJECT_$1"

# Create the directories
mkdir -p "$projectname"/img/{train,valid}/{images,labels}

echo "Directories created under $projectname"
