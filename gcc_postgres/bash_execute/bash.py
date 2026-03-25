import script as s


def main(x):
    vm = x["vm"]
    result = s.create_vm(
    vm_name=f"{vm["vm_name"]}",
    zone=f"{vm["zone"]}",
    startup_script_path="infra/startup.sh")






