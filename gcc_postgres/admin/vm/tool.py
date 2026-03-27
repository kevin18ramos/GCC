def auth(user_id,vm_file):
    if user_id.id_valid(id):
        response= {
            'status':False,
            'response':'id_invalid'}


    return response


def id_valid(id):
    if not isinstance(id, int):
        return False
    if id > 1000:
        return False
    else:
        return True