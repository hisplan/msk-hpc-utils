# Install IGV

http://software.broadinstitute.org/software/igv/download

```bash
$ wget https://data.broadinstitute.org/igv/projects/downloads/2.8/IGV_Linux_2.8.4.zip
$ unzip IGV_Linux_2.8.4.zip
$ ln -snf IGV_Linux_2.8.4/igv.sh igv.sh
```

# Install XQuartz on Mac

https://www.xquartz.org/

Must log out and log back in.

# Set up config

```
$ cat ~/.ssh/config
Host lilac totoro
  ForwardAgent yes
  ForwardX11 yes
  ForwardX11Trusted yes
```

# How to Run IGV

## On Local

Set up your SSH key and SSH into Lilac.

```bash
$ ssh-add -K ~/.ssh/mskcc_id_rsa
$ ssh -AXY lilac
```

## On Lilac

Submit an interactive job:

```
$ bsub -Ip -J "igv" -W 9:00 -n 2 -R "rusage[mem=64"] -XF /bin/bash
```

Once you're on a compute node, run the following command:

```
$ ./igv.sh
```

# Copy / Paste with XQuartz

https://superuser.com/questions/517878/why-cant-i-paste-into-xterm-xquartz
