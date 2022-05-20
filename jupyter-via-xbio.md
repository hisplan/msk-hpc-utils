# Jupyter Notebook via xbio

This explains how to set up a Jupyter Notebook session when you are not on MSK Network and you do not have MSK VPN. However, this workaround still requires that you have an active xbio account.

## Step 1

Add the following to your `~/.ssh/config`. If you don’t have this file already, create one:

```
Host xbio
  HostName xbio.mskcc.org
  User chunj
  Port 2222

Host lilac
  HostName lilac.mskcc.org
  User chunj
ProxyCommand ssh -W %h:%p xbio
```

Make sure to replace `chunj` with your MSK HPC user name.

## Step 2

Follow the instructions [here](./README.md) until you get to the step where you're asked to run the following command:

```bash
$ ssh -o ServerAliveInterval=120 -A -L 7777:localhost:7777 chunj@lilac.mskcc.org ssh -L 7777:localhost:7777 -N lt11
```

Change `chunj@lilac.mskcc.org` to `lilac`, then run the command. It should look something like this:

```bash
$ ssh -o ServerAliveInterval=120 -A -L 7777:localhost:7777 lilac ssh -L 7777:localhost:7777 -N lt11
```

Once this is done, follow the rest of the instructions.
