# Totoro & Mononoke

Last Modified: 2020-07-22

1. Totoro
    1. CPU & GPU
    1. Disk
1. Mononoke
    1. CPU
    1. GPU
    1. Disk

## Totoro

- 32 cores (64 threads via Intel Hyperthreading)
- 768 GB of memory
- 8 GPUs (RTX 2080TI Blower Edition)
- Approximaltely 7 TB of disk space

```bash
ssh chunj@totoro.mskcc.org
```

### CPU & GPU

The CPUs/GPUs on Totoro are not currently managed by LSF (job scheduler). For this reason, these resources will be served on a first come, first served basis.

Also, if the number of jobs are greater than the number of CPUs on this machine, each job will have to fight hard for the CPU time, thus some of the jobs could slow down, the total running time could get longer.

For GPUs, once a GPU is acquired and assigned to your job, it cannot be shared with other users. When your job completes, make sure to release the GPU.

To coordinate with other users, please use this Slack channel:  `#reserve-totoro`.

### Disk

```
/dev/nvme0n1    3.5T  168G  3.1T   6% /fast
/dev/nvme1n1p1  3.5T  246G  3.1T   8% /fscratch
```

Before using these volumes, make sure to create a directory with your user name, for example:

```bash
cd /fast
mkdir $USER

cd /fscratch
mkdir $USER
```

## Mononoke

- 52 cores (104 threads via Intel Hyperthreading)
- 768 GB of memory
- 4 GPUs (RTX 2080TI Blower Edition)
- Approximaltely 30 TB of disk space

To access resources on Mononoke (`li01`), you must use LSF (job scheduler). This means you cannot directly SSH into Mononoke. We now have a LSF queue called `mononoke`. Use this queue to submit a job to Mononoke. You can do this from both `lilac` or `totoro`.

### CPU

```bash
bsub -J "adhoc" -W 1:00 -n 1 -R "rusage[mem=4"] -q mononoke -Is /bin/bash
```

### GPU

```bash
bsub -J "adhoc" -W 1:00 -n 1 -R "rusage[mem=4"] -gpu - -q mononoke -Is /bin/bash
```

whereg

- `-J adhoc`: setting the job name to `adhoc`,
- `-W 1:00`: setting the runtime limit to 1 hour,
- `-n 1`: asking for 1 CPU,
- `-gpu -`: asking for 1 GPU,
- `-R "rusage[mem=4"]`: asking for 1 GB of memory.

### Disk

```
/dev/nvme0n1p1   14T   25M   14T   1% /scratch
/dev/nvme1n1p1   14T   25M   14T   1% /fscratch
```

Before using these volumes, make sure to create a directory with your user name, for example:

```bash
cd /scratch
mkdir $USER

cd /fscratch
mkdir $USER
```
