#!/bin/bash

# 1. we are going to work in a dedicated directory:
mkdir snakemake-tutorial && cd snakemake-tutorial

# 2. download the sample data
echo "downloading sample data"
curl -L https://api.github.com/repos/snakemake/snakemake-tutorial-data/tarball -o snakemake-tutorial-data.tar.gz

# 3. unpack the sample data
echo "unpacking sample data"
tar --wildcards -xf snakemake-tutorial-data.tar.gz --strip 1 "*/data" "*/environment.yaml"

# 4. this is necessary, because we need a simple list of packages
#    after we downgraded the python version in the step afore.
cat environment.yaml | tail -n+5 | cut -c5- > environment2.txt

# 5. install all necessary software
mamba install --file environment2.txt

