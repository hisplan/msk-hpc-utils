#!/bin/bash

# customize to fit your own environment
conda_env="notebook"
projects_folder="~/projects"



# LSF parameters
export job_id=$1
cd $LS_SUBCWD

stdout_log="notebook.stdout.log"

source ~/.bash_profile

conda activate ${conda_env}

unset XDG_RUNTIME_DIR

mkdir -p ${projects_folder}projects_folder

jupyter notebook \
  --no-browser \
  --port 7777 \
  --notebook-dir ${projects_folder} 2>&1 | tee ${stdout_log}

conda deactivate
