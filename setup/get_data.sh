# 1. cd into HOME directory
echo "changing to HOME directory, even, if we are there already"
cd

# 2. download the sample data
echo "downloading sample data"
curl -L https://api.github.com/repos/snakemake/snakemake-tutorial-data/tarball -o snakemake-tutorial-data.tar.gz

# 3. unpack the sample data
echo "unpacking sample data"
tar --wildcards -xf snakemake-tutorial-data.tar.gz --strip 1 "*/data" "*/environment.yaml"

