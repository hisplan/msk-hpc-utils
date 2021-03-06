#!/usr/bin/env python

import sys
import os
import subprocess
import logging
import argparse
import re
import time


# create logger
logger = logging.getLogger("notebook-launcher")
logger.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

# create console handler and set level to debug
console_log_handler = logging.StreamHandler(sys.stdout)
console_log_handler.setLevel(logging.DEBUG)
console_log_handler.setFormatter(formatter)
logger.addHandler(console_log_handler)

log_file_handler = logging.FileHandler("notebook.launcher.log")
log_file_handler.setLevel(logging.DEBUG)
log_file_handler.setFormatter(formatter)
logger.addHandler(log_file_handler)


def bsub(bsubline):
    "execute lsf bsub"

    process = subprocess.Popen(
        bsubline, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    )
    output = process.stdout.readline()

    if type(output) is bytes:
        output = output.decode()

    # fixme: need better exception handling
    logger.info(output.rstrip())

    lsf_job_id = int(output.strip().split()[1].strip("<>"))

    return lsf_job_id


def get_lsf_job_info(lsf_job_id):
    "get working directory, path to stdout/stderr log, and cmd of LSF leader job"

    bjobs = ["bjobs", "-o", "stat exec_host", "-noheader", str(lsf_job_id)]

    process = subprocess.Popen(bjobs, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    line = process.stdout.read()

    if type(line) is bytes:
        line = line.decode()

    line = line.rstrip("\n")

    try:
        if line:
            status, exec_host = line.split(" ")
            return status, exec_host

    except Exception:
        pass

    return None, None


def parse_execution_host_string(input_str):
    "parse LSF execution host string"

    if input_str == "-":
        return 1, "Unknown"

    # fixme: pre-compile regex

    num = None
    host = None
    match = re.search(r"^((\d+)\*)?(.*)$", input_str)
    if match:
        num = 1 if match.group(2) is None else match.group(2)
        host = match.group(3)
    else:
        num = 1
        host = "Unknown"

    return int(num), host


def launch(hours, cpu, memory, gpu, queue_name):

    logger.info(
        "Requesting {cpu} CPUs, {gpu} GPUs, {memory} GB memory for {hours} hours...".format(
            cpu=cpu, gpu=gpu, memory=memory, hours=hours
        )
    )

    # job = "./test-job.sh"
    job = "./lsf-job.sh"

    cmd = [
        "bsub",
        "-q",
        queue_name,
        "-J",
        "notebook",
        "-W",
        "{}:00".format(hours),
        "-eo",
        "./notebook.stderr.log",
        "-n",
        str(cpu),
        "-R",
        "rusage[mem={}]".format(memory),
    ]

    if gpu > 0:
        cmd.extend(["-gpu", '"num=1:mode=exclusive_process"'])

    cmd.append(job)

    lsf_job_id = bsub(cmd)

    logger.info("LSF Job ID: {}".format(lsf_job_id))

    return lsf_job_id


def wait_till_running(lsf_job_id):

    wait_sec = 2

    while True:

        # status: PEND, RUN, ...
        # exec_host: ls01, 2*ls01
        status, exec_host = get_lsf_job_info(lsf_job_id)

        # 2*ls01 --> ls01
        _, exec_host = parse_execution_host_string(exec_host)

        logger.info("Job status: {}".format(status))

        if status == "RUN":
            break

        time.sleep(wait_sec)

        # double the wait time until hitting 1 minute
        if wait_sec < 60:
            wait_sec *= 2

    logger.info("Your job appears to be running now...")

    return exec_host


def get_notebook_url(stdout_log):

    with open(stdout_log, "rt") as fin:
        stdout = fin.read()

    # http://localhost:7777/?token=8cd3e3b2e7c404be225dc749db8dc3d87c14ea90dca26bca
    match = re.search(r"(http://localhost:(\d+)/\?token=.*)", stdout)

    if match:
        return match.group(1), match.group(2)

    return None, None


def show_next_step(exec_host, notebook_url, notebook_port):

    msg = """Instructions:

From your local workstation, run the command below:

$ ssh -o ServerAliveInterval=120 -A -L {notebook_port}:localhost:{notebook_port} {user}@lilac.mskcc.org ssh -L {notebook_port}:localhost:{notebook_port} -N {exec_host}

Open `{notebook_url}` to access the Jupyter Notebook.
""".format(
        exec_host=exec_host,
        user=os.environ["USER"],
        notebook_url=notebook_url,
        notebook_port=notebook_port,
    )

    logger.info(msg)


def parse_arguments():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--hours",
        action="store",
        dest="num_run_hours",
        type=int,
        help="Number of hours you need",
        required=True,
    )

    parser.add_argument(
        "--cpu",
        action="store",
        dest="num_cpu",
        type=int,
        default=1,
        help="Number of CPUs you need",
    )

    parser.add_argument(
        "--gpu",
        action="store",
        dest="num_gpu",
        type=int,
        default=0,
        help="Number of GPUs you need",
    )

    parser.add_argument(
        "--memory",
        action="store",
        dest="memory_gb",
        type=int,
        default=8,
        help="Amount of memory per CPU core in GB",
    )

    parser.add_argument(
        "--queue",
        action="store",
        dest="queue_name",
        default="cpuqueue",
        help="LSF queue name",
    )

    parser.add_argument(
        "--max-attempts", action="store", dest="max_attempts", type=int, default=20,
    )

    # parse arguments
    params = parser.parse_args()

    return params


def determine_queue(queue_name, gpu):
    # mononoke supports both cpu and gpu
    if queue_name == "mononoke":
        return queue_name
    else:
        if gpu > 0:
            # gpu request must goes to gpuqueue
            return "gpuqueue"
        else:
            # cpu request should go to cpuqueue
            return "cpuqueue"


def main():

    params = parse_arguments()

    logger.info("Starting...")

    # determine which queue to use
    params.queue_name = determine_queue(params.queue_name, params.num_gpu)

    lsf_job_id = launch(
        hours=params.num_run_hours,
        cpu=params.num_cpu,
        memory=params.memory_gb,
        gpu=params.num_gpu,
        queue_name=params.queue_name,
    )

    exec_host = wait_till_running(lsf_job_id)

    attempt = 1
    while attempt <= params.max_attempts:
        try:
            notebook_url, notebook_port = get_notebook_url("./notebook.stdout.log")

            if notebook_url and notebook_port:
                logger.info("We're ready!")
                show_next_step(exec_host, notebook_url, notebook_port)
                exit(0)

            logger.warning(
                "No token found yet. Trying again... ({}/{})".format(
                    attempt, params.max_attempts
                )
            )
        except Exception as ex:
            logger.warning(str(ex))

        attempt += 1
        time.sleep(5)

    logger.error(
        "Please check the log file and see if your job {} is still alive.".format(
            lsf_job_id
        )
    )
    exit(1)


if __name__ == "__main__":
    main()
