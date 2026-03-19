import connection as cn

def read_host_file(file_path):
    with open(file_path, "r") as f:
        line = f.readline().strip()

    parts = [p.strip() for p in line.split("|")]

    if len(parts) != 4:
        raise ValueError("Invalid host file format")

    db_name, host, user, password = parts

    return {
        "db_name": db_name,
        "host": host,
        "user": user,
        "password": password
    }
