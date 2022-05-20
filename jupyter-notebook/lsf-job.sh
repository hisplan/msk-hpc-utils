#!/bin/bash

# customize to fit your own environment
conda_env="notebook"
jupyter_port=7777
projects_folder="${HOME}/projects"

# customize if you want a different version of cuda/cudnn
module add cuda/11.3
module add cudnn/8.1.0-cuda11.2

# LSF parameters
export job_id=$1
cd $LS_SUBCWD

stdout_log="notebook.stdout.log"

source ~/.bash_profile

conda activate ${conda_env}

unset XDG_RUNTIME_DIR

mkdir -p ${projects_folder}

jupyter notebook \
  --no-browser \
  --port ${jupyter_port} \
  --notebook-dir ${projects_folder} 2>&1 | tee ${stdout_log}

conda deactivate
