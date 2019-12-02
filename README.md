# msk-hpc-utils

## Jupyter Notebook on HPC

### Installation

Add your private key identity to the authentication agent and log in to Lilac:

```bash
$ ssh-add -K <YOUR-PRIVATE-KEY>
$ ssh -A lilac
```

Install [miniconda](https://docs.conda.io/en/latest/miniconda.html) on HPC:

```
$ export MINICONDA_VERSION=4.5.1
$ curl -O https://repo.anaconda.com/miniconda/Miniconda3-${MINICONDA_VERSION}-Linux-x86_64.sh
$ bash Miniconda3-${MINICONDA_VERSION}-Linux-x86_64.sh -b -p $HOME/miniconda
$ echo ". $HOME/miniconda/etc/profile.d/conda.sh" >> $HOME/.bash_profile
```

Log out, log back in, and make sure you can run `conda`. For example, you should be able to check the conda version:

```bash
$ conda -V
conda 4.5.1
```

Create a conda environment with Python, pip, and Jupyter Notebook:

```bash
$ conda create -n notebook python=3.6.5 pip jupyter
```

Download and decompress the `msk-hpc-utils` package:

```bash
curl -L https://github.com/hisplan/msk-hpc-utils/archive/v0.0.2.tar.gz | tar xz
```

You should now be able to run `launch.py`:

```
$ cd msk-hpc-utils-0.0.2/jupyter-notebook/

$ python launch.py --help
usage: launch.py [-h] --hours NUM_RUN_HOURS [--cores NUM_CORES]
                 [--memory MEMORY_GB]

optional arguments:
  -h, --help            show this help message and exit
  --hours NUM_RUN_HOURS
                        Number of hours you need
  --cores NUM_CORES     Number of cores you need
  --memory MEMORY_GB    Amount of memory per CPU core in GB
```

## Launching Notebook

Log in to Lilac and run the command below which will launch Jupyter Notebook in Lilac's compute node. For example, below will request 2 cores and 16 GB memory per CPU core for 8 hours. Make sure to use Python 2.7.x which is the default in Lilac.

```bash
$ python launch.py \
    --hours=8 \
    --cores=2 \
    --memory=16
```

The output would look something like below. Follow the instructions shown in the output, which will automatically set up a SSH tunnel to the Jupyter Notebook, and you should be able to access the notebook from your browser:

```
2019-11-16 09:47:50,604 - INFO - Starting...
2019-11-16 09:47:50,604 - INFO - Requesting 2 cores, 16 GB memory for 1 hours...
2019-11-16 09:47:50,660 - INFO - Job <13298296> is submitted to default queue <cpuqueue>.
2019-11-16 09:47:50,660 - INFO - LSF Job ID: 13298296
2019-11-16 09:47:50,685 - INFO - Job status: PEND
2019-11-16 09:47:52,709 - INFO - Job status: PEND
2019-11-16 09:47:56,736 - INFO - Job status: RUN
2019-11-16 09:47:56,736 - INFO - Your job appears to be running now...
2019-11-16 09:48:06,749 - INFO - Instructions:

From your local workstation, run the command below:

$ ssh -o ServerAliveInterval=120 -A -L 7777:localhost:7777 chunj@lilac.mskcc.org ssh -L 7777:localhost:7777 -N lt11

Open `http://localhost:7777/?token=9122a28fe6901a9f883ba8766810d1f80c8be9e822cc1f6c` to access to the Jupyter Notebook.
```

## Shutting Down

### From Lilac

Run `bjob` to find the LSF Job ID and kill the job by running `bkill`. If the job has already expired, you can skip this part and go to the next step.

```bash
$ bjobs
       JOBID       USER     JOB_NAME   STAT      QUEUE  FROM_HOST    EXEC_HOST   SUBMIT_TIME    START_TIME  TIME_LEFT
    13298296      chunj     notebook    RUN   cpuqueue      lilac         lt11  Nov 17 20:42  Nov 17 20:42     0:51 L

$ bkill 13298296
Job <13298296> is being terminated

$ bkill 13298296
Job <13298296>: Job has already finished

$ bjobs
No unfinished job found
```

Run `ps ux` to find the process that binds to port 7777 and kill it by running `kill`:

```bash
$ ps ux
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
chunj      385  0.0  0.0 165652  1876 pts/133  R+   10:05   0:00 ps ux
chunj    33526  0.0  0.0 191164  4328 ?        Ss   09:56   0:00 ssh -L 7777:localhost:7777 -N lt11

$ kill 33526
```

### From Your Local Workstation

`CTRL+C` to terminate your SSH tunnel.

## Pre-installed Software

Please refer to [this page](./preinstalled-software/README.md).
