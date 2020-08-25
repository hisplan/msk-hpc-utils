# msk-hpc-utils

## Jupyter Notebook on HPC

### Installation

Add your private key identity to the authentication agent and log in to Lilac:

```bash
$ ssh-add -K <YOUR-PRIVATE-KEY>
$ ssh -A lilac
```

If you don't have Miniconda already installed under your HPC account, follow the instruction here to install it first: https://docs.conda.io/en/latest/miniconda.html (technically, you can replace Miniconda with Python3 + Virtualenv, but this will require a small change in `lsf-job.sh`).

Log out, log back in, and make sure you can run `conda`. For example, you should be able to check the conda version:

```bash
$ conda --version
conda 4.8.2
```

Create a conda environment with Python, pip, and Jupyter Notebook:

```bash
$ conda create -n notebook python=3.7.6 pip jupyter
```

Download and decompress the `msk-hpc-utils` package:

```bash
curl -L https://github.com/hisplan/msk-hpc-utils/archive/v0.0.7.tar.gz | tar xz
```

You should now be able to run `launch.py`:

```
$ cd msk-hpc-utils-0.0.7/jupyter-notebook/

$ python launch.py --help
usage: launch.py [-h] --hours NUM_RUN_HOURS [--cpu NUM_CPU] [--gpu NUM_GPU]
                 [--memory MEMORY_GB] [--queue QUEUE_NAME]
                 [--max-attempts MAX_ATTEMPTS]

optional arguments:
  -h, --help            show this help message and exit
  --hours NUM_RUN_HOURS
                        Number of hours you need
  --cpu NUM_CPU         Number of CPUs you need
  --gpu NUM_GPU         Number of GPUs you need
  --memory MEMORY_GB    Amount of memory per CPU core in GB
  --queue QUEUE_NAME    LSF queue name
  --max-attempts MAX_ATTEMPTS
```

### Configuration

#### HTTP Port

Jupyter Notebook requires a HTTP port to be open and accessible so that you can use Jupyter Notebook from your web browser. Since Lilac is a common resource, the port that you're trying to use for Jupyter Notebook could be already being used by someone else. Unfortunately, there is no easy/legit way to find a port that is not being used (unless you scan all the ports). For this reason, you need to manually and randomly choose one port and see if that works or not by trial and error.

Suppose you picked a port 7779. Make sure to edit the `lsf-job.sh` file and update the port in the following lines:

```
jupyter_port=7777
```

#### Conda Environment

In the earlier section, we have created a new conda environment called `notebook`. If you're using a different conda environment, make sure you update the `lsf-job.sh` file accordingly:

```
conda_env="notebook"
```

### Launching Notebook

Log in to Lilac and run the command below which will launch Jupyter Notebook in Lilac's compute node. For example, below will request 2 CPUs, 1 GPU, and 16 GB memory per CPU for 8 hours.

```bash
$ python launch.py \
    --hours=8 \
    --cpu=2 \
    --gpu=1 \
    --memory=16
```

The output would look something like below. Follow the instructions shown in the output, which will automatically set up a SSH tunnel to the Jupyter Notebook, and you should be able to access the notebook from your browser:

```
2020-08-13 22:50:50,648 - INFO - Starting...
2020-08-13 22:50:50,681 - INFO - Requesting 2 CPUs, 1 GPUs, 16 GB memory for 8 hours...
2020-08-13 22:50:50,769 - INFO - Job <16499628> is submitted to queue <gpuqueue>.
2020-08-13 22:50:50,769 - INFO - LSF Job ID: 16499628
2020-08-13 22:50:50,792 - INFO - Job status: PEND
2020-08-13 22:50:52,818 - INFO - Job status: PEND
2020-08-13 22:50:56,849 - INFO - Job status: RUN
2020-08-13 22:50:56,850 - INFO - Your job appears to be running now...
2020-08-13 22:50:56,854 - INFO - We're ready!
2020-08-13 22:50:56,855 - INFO - Instructions:

From your local workstation, run the command below:

$ ssh -o ServerAliveInterval=120 -A -L 7777:localhost:7777 chunj@lilac.mskcc.org ssh -L 7777:localhost:7777 -N lt11

Open `http://localhost:7777/?token=9122a28fe6901a9f883ba8766810d1f80c8be9e822cc1f6c` to access to the Jupyter Notebook.
```

### Shutting Down

Shutting down rquires two steps, one needs to be done on Lilac, the other on your local machine.

#### From Lilac

Run `bjob` to find the LSF Job ID and kill the job by running `bkill`. If the job has already expired, you can skip this part and go to the next step.

```bash
$ bjobs
       JOBID       USER     JOB_NAME   STAT      QUEUE  FROM_HOST    EXEC_HOST   SUBMIT_TIME    START_TIME  TIME_LEFT
    16499628      chunj     notebook    RUN   cpuqueue      lilac         lt11  Nov 17 20:42  Nov 17 20:42     0:51 L

$ bkill 16499628
Job <16499628> is being terminated

$ bkill 16499628
Job <16499628>: Job has already finished

$ bjobs
No unfinished job found
```

Run `ps ux` to find the process that binds to port 7777 (or the port you're using for Jupyter Notebook) and kill it by running `kill`:

```bash
$ ps ux
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
chunj      385  0.0  0.0 165652  1876 pts/133  R+   10:05   0:00 ps ux
chunj    33526  0.0  0.0 191164  4328 ?        Ss   09:56   0:00 ssh -L 7777:localhost:7777 -N lt11

$ kill 33526
```

#### From Your Local Workstation

`CTRL+C` to terminate your SSH tunnel.

## Pre-installed Software

Please refer to [this page](./preinstalled-software/README.md).
