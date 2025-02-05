#!/bin/bash

# 1. we are going to work in a dedicated directory:
mkdir snakemake-tutorial && cd snakemake-tutorial

# 2. download the sample data
curl -L https://api.github.com/repos/snakemake/snakemake-tutorial-data/tarball -o snakemake-tutorial-data.tar.gz

# 3. unpack the sample data
tar --wildcards -xf snakemake-tutorial-data.tar.gz --strip 1 "*/data" "*/environment.yaml"

