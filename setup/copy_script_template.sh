#!/bin/bash

CLUSTER_ALIAS=<cluster_name>

scp condarc "${CLUSTER_ALIAS}:/path/to/setup/dir"
scp get_tutorial.sh "${CLUSTER_ALIAS}:/path/to/setup/dir"

rsync -rtlv --chmod=D755 "tutorial" "${CLUSTER_ALIAS}:/path/to/tutorial/cloze/texts"
rsync -rtlv --chmod=D755 "solutions" "${CLUSTER_ALIAS}:/path/to/tutorial/solutions"
