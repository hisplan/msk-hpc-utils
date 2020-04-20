# Pre-installed Software

Software such as `samtools`, `STAR`, `bedtools`, `htslib`, ... are already pre-installed in Lilac and can be found in `/opt/common/CentOS_7`:

```
$ pwd
/opt/common/CentOS_7

drwxr-xr-x  4 root  root 4.0K May 14  2018 abyss
drwxr-xr-x  5 root  root 4.0K Apr 18 20:15 anaconda
drwxr-xr-x  4 root  root 4.0K Jul 27  2018 bamtools
drwxr-xr-x  4 root  root 4.0K Mar 29  2018 bedtools
drwxr-xr-x  4 root  root 4.0K Apr 26  2018 blat
drwxr-xr-x  4 root  root 4.0K Apr 20  2018 boost
drwxr-xr-x  5 root  root 4.0K Apr 25  2018 bowtie
drwxr-xr-x  4 root  root 4.0K Oct 18  2018 bwa
drwxr-xr-x  5 root  root 4.0K Oct 30  2018 cellranger
drwxr-xr-x  5 root  root 4.0K Apr 25  2018 defuse
drwxr-xr-x  4 root  root 4.0K Jul 27  2018 dropEst
drwxr-xr-x  7 root  root 4.0K Oct 11  2018 Drop-seq
drwxr-xr-x  4 root  root 4.0K May 15 15:31 ensembl-vep
drwxr-xr-x  4 root  root 4.0K Feb 25 12:31 EQ-R
drwxr-xr-x  3 root  root 4.0K Apr 26  2018 faToTwoBit
drwxr-xr-x  4 root  root 4.0K Apr 10  2018 gcc
drwxr-xr-x  5 root  root 4.0K Jul  2 16:46 glibc
drwxr-xr-x  4 root  root 4.0K Apr 26  2018 gmap-gsnap
drwxr-xr-x  4 root  root 4.0K Dec  6  2018 go
drwxr-xr-x  5 root  root 4.0K Nov 21  2017 gromacs
drwxr-xr-x  4 root  root 4.0K Feb  6  2018 htslib
drwxr-xr-x  5 root  root 4.0K Feb  6  2018 htstools
drwxr-xr-x  4 root  root 4.0K Oct  5  2018 java
drwxr-xr-x 12 root  root 4.0K Jul  2 12:21 jax
drwxr-xr-x  3 zhaoh root 4.0K Mar 29  2018 linuxbrew
drwxr-xr-x  3 root  root 4.0K Jul  2 15:59 make
drwxr-xr-x  4 root  root 4.0K Sep  4  2018 mono
drwxr-xr-x  4 root  root 4.0K Jan 23  2018 opencv
drwxr-xr-x  3 root  root 4.0K Jul  6  2017 openjpeg
drwxr-xr-x  4 root  root 4.0K May 14  2018 openmpi
drwxr-xr-x  4 root  root 4.0K Feb 21  2018 perl
drwxr-xr-x  6 root  root 4.0K Dec  7  2017 picard
drwxr-xr-x  6 root  root 4.0K Dec 10  2018 python
drwxr-xr-x  7 root  root 4.0K Jul  2 14:27 R
drwxr-xr-x  5 root  root 4.0K May 20 12:32 rclone
drwxr-xr-x  5 root  root 4.0K Oct 30  2018 rsem
drwxr-xr-x  5 root  root 4.0K Apr 25  2018 samtools
drwxr-xr-x  3 root  root 4.0K Apr 26  2018 scala
drwxr-xr-x 12 root  root 4.0K May 28 13:48 Schrodinger
drwxr-xr-x  6 root  root 4.0K Dec 20  2018 singularity
drwxr-xr-x  4 root  root 4.0K May 14  2018 sparsehash
drwxr-xr-x  5 root  root 4.0K Sep  6  2018 src
drwxr-xr-x  3 root  root 4.0K Sep 18  2018 stack
drwxr-xr-x  5 root  root 4.0K Dec 11  2017 star
drwxr-xr-x  4 root  root 4.0K Apr  3 11:53 TagGrpah
drwxr-xr-x  4 root  root 4.0K May 11  2018 velvet
```

## Available via `module`

```bash
$ module avail

------------------------------------------------------------------- /usr/share/Modules/modulefiles -------------------------------------------------------------------
dot         module-git  module-info modules     null        use.own

-------------------------------------------------------------------------- /etc/modulefiles --------------------------------------------------------------------------
mpi/mpich-3.0-x86_64 mpi/mpich-3.2-x86_64 mpi/mpich-x86_64     mpi/openmpi-x86_64

---------------------------------------------------------------------- /opt/common/modulefiles -----------------------------------------------------------------------
bamtools/2.5.1                         cudnn/6.0                              openmpi/4.0.0                          scala/2.12.5
bedtools/2.29.2                        cudnn/7.0                              parabricks/2.3.6                       schrodinger/schrodinger2017-4
boost/1.59(default)                    cudnn/7.0-cuda9                        perl/perl-5.26.1                       schrodinger/schrodinger2018-1
boost/1.61                             cudnn/7.6-cuda10.1                     python/2.7.13                          schrodinger/schrodinger2018-1_Advanced
caffe/1.0                              easybuild/3.1.2                        python/3.6.4                           schrodinger/schrodinger2018-2_Advanced
caffe/rc3(default)                     easybuild/3.6.2                        python/3.7.1                           schrodinger/schrodinger2018-3_Advanced
caffe/rc4                              ExpeDat/1.17E-P                        pythonlsf/1.0.1                        schrodinger/schrodinger2018-4_Advanced
cmake/3.7.2(default)                   gpfsutil/1.0.0                         pythonlsf/1.0.6                        schrodinger/schrodinger2019-1_Advanced
conda/conda3                           gromacs/gromacs-2019.4                 pythonlsf/1.0.6.1                      schrodinger/schrodinger2019-2_Advanced
cuda/10.0                              java/1.8.0_31                          pythonlsf/1.0.6.2                      schrodinger/schrodinger2019-3_Advanced
cuda/10.1                              java/8.0                               R/R-3.3.3                              schrodinger/schrodinger2019-4_Advanced
cuda/10.2                              Matlab/R2017a                          R/R-3.5.0                              schrodinger/schrodinger2020-1_Advanced
cuda/7.0                               mono/5.14.0                            R/R-3.5.1                              singularity/2.4.2
cuda/7.5                               nccl/1.0(default)                      R/R-3.6.0                              singularity/2.5.1
cuda/8.0(default)                      nccl/2.1-cuda9                         relion/2.0                             singularity/2.6.1
cuda/9.0                               nvidia-tools/healthmon                 relion/2.1-stable(default)             singularity/3.0.1
cuda/9.1                               opencv/3.0.0                           relion/3.0-beta                        star/2.5.3a
cuda/9.2                               opencv/3.1.0(default)                  relion/3.1-beta                        torch/7
cudnn/4.0                              openmpi/2.0.2(default)                 samtools/1.10
cudnn/5.0                              openmpi/3.0.0                          samtools/1.7
cudnn/5.1(default)                     openmpi/3.1.3                          samtools/1.8
```

```bash
$ module add R
```
