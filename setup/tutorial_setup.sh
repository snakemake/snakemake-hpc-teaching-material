# 1. create the environment for the tutorial
mamba env create --name snakemake-tutorial

# 2. activate the environment
conda activate snakemake-tutorial

# TODO: This step is necessary because of the outdated 
#       setup, where Python >= 3.10 does not work
#       with pysam
mamba install Python=3.9

cat environment.yaml | tail -n+5 | cut -c5- > environment2.txt

# 3. install all necessary software
mamba install --file environment2.txt
