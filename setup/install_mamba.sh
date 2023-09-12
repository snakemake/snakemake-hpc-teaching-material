# 1. ensure to be executing in the HOME directory (on clusters, this script
# should not be running on data file systems.
echo "changing to HOME directory (even if already there)"
cd

# 2. download mamba-forge
echo "downloading Mambaforge"
curl -L https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-Linux-x86_64.sh -o Mambaforge-Linux-x86_64.sh

# 3. inform the user that all requests have to be confirmed
echo "going to install Mambaforge. Please confirm all questions with 'yes'"
sleep 2

# 4. starting the installation process
bash Mambaforge-Linux-x86_64.sh
