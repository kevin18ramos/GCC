import subprocess





def status(vm_file):
    config = read_vm_file(vm_file)
    sh = 'vm_status_check.sh'
    result = run(template=sh, x=config)
    if result == "Running":
        return True
    else:
        return False

def stop_vm(vm_file):
    config = read_vm_file(vm_file)
    sh = 'vm_status_check.sh'
    run(template=sh, x=False)

def pause_vm(vm_file):
    config = read_vm_file(vm_file)
    sh = 'vm_status_check.sh'
    run(template=sh, x=False)


def start_vm(vm_file):
    config = read_vm_file(vm_file)
    sh = 'vm_status_check.sh'
    run(template=sh, x=False)

def run(template,x:list):
    script = template
    print(f"...Running {script}...")
    if x:
        for y in x:
            script = script.replace("{{y}}", y)
    x = subprocess.run(["bash", script], check=True)
    return x


def create_vm(vm_name: str, zone: str, startup_script_path: str) -> str:
    try:
        result = subprocess.run(
            [
                "gcloud",
                "compute",
                "instances",
                "create",
                vm_name,
                "--zone", zone,
                "--metadata-from-file", f"startup-script={startup_script_path}"
            ],
            check=True,
            capture_output=True,
            text=True
        )

        # add db logging here (success)
        result = result.stdout
        print(result)
        return True

    except subprocess.CalledProcessError as e:
        # add db logging here (failure)

        exception = Exception(
            f"VM creation failed\n"
            f"STDERR:\n{e.stderr}\n"
            f"STDOUT:\n{e.stdout}"
        )
        print(exception)
        return False




def read_vm_file(file_path):
    with open(file_path, "r") as f:
        line = f.readline().strip()

    parts = [p.strip() for p in line.split("|")]

    if len(parts) != 4:
        raise ValueError("Invalid host file format")

    vm_name , zone , project_id , instance_id= parts


    return [vm_name,
         zone,
         project_id,
         instance_id]



