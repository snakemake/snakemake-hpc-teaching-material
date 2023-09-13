#!/bin/bash

# 0. we are going to use ONE environment with the same
#    name as the workflow we are going to create
NAME="snakemake-tutorial"

# 1. On many HPC systems we are going to install via a proxy.
#    This might ignore TLS, hence we turn off all warnings.
#    Note: TLS might still be used, but not ALL proxies use it.
export PYTHONWARNINGS="ignore:Unverified HTTPS request"

# 1. create the environment for the tutorial
mamba create --name $NAME

# 2. activate the environment
mamba activate $NAME

# TODO: This step is necessary because of the outdated 
#       setup, where Python >= 3.10 does not work
#       with pysam
mamba install Python=3.9

