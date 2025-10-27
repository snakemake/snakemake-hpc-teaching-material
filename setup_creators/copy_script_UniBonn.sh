#!/bin/bash

# This script is used to teach on the cluster "Mogon II"

CLUSTER_ALIAS="marvin" # nox stands for "no X11 forwarding"
BASEPATH="/lustre/scratch/data/fboecker-snakemake_workshop/" # repeated use

# creating remote directory:
ssh ${CLUSTER_ALIAS} "mkdir -p ${BASEPATH}/snakemake_profile"

scp condarc_mogon "${CLUSTER_ALIAS}:${BASEPATH}/condarc"
scp get_tutorial.sh "${CLUSTER_ALIAS}:${BASEPATH}/get_tutorial.sh"
#scp install_micromamba.sh "${CLUSTER_ALIAS}:${BASEPATH}/install_conda.sh"
scp environment.yaml "${CLUSTER_ALIAS}:." # to HOME as this cluster provides conda and we only need to provide a software environment - no self installation of conda
scp config.yaml "${CLUSTER_ALIAS}:${BASEBATH}/snakemake_profile/."

rsync -rtlv --chmod=D755 "tutorial" "${CLUSTER_ALIAS}:${BASEPATH}"
rsync -rtlv --chmod=D755 "solutions" "${CLUSTER_ALIAS}:${BASEPATH}"
