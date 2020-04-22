#  Jupyter Notebook on Totoro via xbio

*** Please be aware that this is a tentative solution until Totoro gets its own LSF.

## Step 1

SSH into `xbio`:

```bash
ssh -A -p 2222 chunj@xbio.mskcc.org
```

SSH into `Totoro`:

```bash
ssh -A totoro
```

Configure the first three variables in `lsf-job.sh` according to your work environment:

```
conda_env="notebook"
jupyter_port=7777
projects_folder="${HOME}/projects"
```

Launch Jupyter Notebook in the background:

```
screen -S notebook
./lsf-job.sh
```

Once the notebook is up and running, you should see something like below on your screen:

```
    To access the notebook, open this file in a browser:
        file:///lila/home/chunj/.local/share/jupyter/runtime/nbserver-170478-open.html
    Or copy and paste one of these URLs:
        http://localhost:7777/?token=0b6731925b4e2f1ebf352f507eeced814a6783f148ee3a92
     or http://127.0.0.1:7777/?token=0b6731925b4e2f1ebf352f507eeced814a6783f148ee3a92
```

Make a note of the URL (one that starts with either `http://localhost` or `http://127.0.0.1`). Be aware that the `token` value always changes.

`CTRL + A + D` to detach yourself from the screen (this will let the notebook be running in the background).

## Step 2

Now, open up a new terminal on your local machine, and run the following command to set up a two-hop tunneling between your local host and `Totoro`:

```bash
ssh -o ServerAliveInterval=120 -A -p 2222 -L 7777:localhost:7777 chunj@xbio.mskcc.org ssh -L 7777:localhost:7777 -N totoro
```

In the above commands, make sure to replace the user name `chunj` and the Jupyter Notebook port `7777` to yours.

Finally, open the URL (from Step 1) in your browser to access the notebook.
