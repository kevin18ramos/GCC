import script as s
import subprocess

def main(x: dict):
    vm = x["vm"]
    subprocess.run(["bash", "deploy/vm_start.sh", f"{vm["vm_name"]}", f"{vm["zone"]}"])








