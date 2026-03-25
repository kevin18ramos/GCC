import subprocess



def script_order(sh,x):
    template = open("deploy/startup.sh").read()

    for y in x:
        script = template.replace("{{y}}", y)


    for x in sh:
        print(f"...executing {x}...")
        result = subprocess.run(
            ["bash", script],
            check=True,
            repo={repo},
            main_file={main_file}
        )
    return result

def run(template,x=False):
    script = template
    print(f"...Running {script}...")
    if x:
        for y in x:
            script = script.replace("{{y}}", y)
    subprocess.run(["bash", script], check=True)



def create_vm(vm_name: str,zone: str, startup_script_path: str) -> None:
    subprocess.run([
        "gcloud",
        "compute",
        "instances",
        "create",
        vm_name,
        "--zone",zone,
        "--metadata-from-file", f"startup-script={startup_script_path}"
    ], check=True)








