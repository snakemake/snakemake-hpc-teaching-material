#!/bin/bash

# This script is used to teach on the cluster "Mogon KI"

CLUSTER_ALIAS="mogon-nhr" # nox stands for "no X11 forwarding"
BASEPATH="/lustre/project/ki-workflow/" # repeated used

# creating remote directory:
ssh ${CLUSTER_ALIAS} "mkdir -p ${BASEPATH}/snakemake_profile"

scp condarc_mogon "${CLUSTER_ALIAS}:${BASEPATH}/condarc"
scp get_tutorial.sh "${CLUSTER_ALIAS}:${BASEPATH}/get_tutorial.sh"
scp install_micromamba.sh "${CLUSTER_ALIAS}:${BASEPATH}/install_conda.sh"
scp environment.yaml "${CLUSTER_ALIAS}:."
scp config.yaml "${CLUSTER_ALIAS}:${BASEPATH}/snakemake_profile/."

rsync -rtlv --chmod=D755 "tutorial" "${CLUSTER_ALIAS}:${BASEPATH}"
rsync -rtlv --chmod=D755 "solutions" "${CLUSTER_ALIAS}:${BASEPATH}"
