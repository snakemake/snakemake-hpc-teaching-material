#!/bin/bash

# This script is used to teach on the cluster "Mogon II"

CLUSTER_ALIAS="barnard" 
BASEPATH="/projects/p_nhr_snakemake"

# creating remote directory:
ssh ${CLUSTER_ALIAS} "mkdir -p ${BASEPATH}"

scp condarc_barnard "${CLUSTER_ALIAS}:${BASEPATH}/condarc"
scp get_tutorial.sh "${CLUSTER_ALIAS}:${BASEPATH}/get_tutorial.sh"
scp install_conda.sh "${CLUSTER_ALIAS}:${BASEPATH}/install_conda.sh"
scp environment.yaml "${CLUSTER_ALIAS}:${BASEPATH}/environment.yaml"

rsync -rtlv --chmod=D755 "tutorial" "${CLUSTER_ALIAS}:${BASEPATH}"
rsync -rtlv --chmod=D755 "solutions" "${CLUSTER_ALIAS}:${BASEPATH}"
