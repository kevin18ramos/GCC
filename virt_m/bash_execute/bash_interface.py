def admin_vm_front_end():
    html = None
    css = None
    with open("templates/admin_vm.html", "r") as f:
        html = f.read()
    with open("static/admin_vm.css", "r") as f:
        css = f.read()

    return html,css