#!/bin/bash

# 1. download mamba-forge
echo "downloading Mambaforge"
curl -L https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-Linux-x86_64.sh -o Mambaforge-Linux-x86_64.sh

# 2. inform the user that all requests have to be confirmed
echo "going to install Mambaforge. Please confirm all questions with 'yes'"
sleep 2

# 3. starting the installation process
bash Mambaforge-Linux-x86_64.sh
