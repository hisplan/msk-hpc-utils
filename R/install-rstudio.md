# RStudio

## Install XQuartz on Your Mac

https://www.xquartz.org/

You must log out and log back in (or reboot might be required).

## Install RStudio on Lilac.

```bash
conda env create -f rstudio.yaml
```

## Log In

Make sure you SSH into Lilac with the `-AXY` options:

```bash
ssh -AXY lilac
```

Submit an interactive job to LSF:

```bash
bsub -Ip -J "rstudio" -W 9:00 -n 4 -R "rusage[mem=64"] -XF /bin/bash
```

Do this because we want RStudio to be running in the background:

```bash
screen -S rstudio
```

```bash
conda activate rstudio
rstudio
```

From the terminal you ran `rstudio`, press `CTRL+A+D` to detach yourself from the screen. This will help maintain RStudio to run in the background without interruption.
