import connection as cn

def connection_run(db,user,pwsd):
    conn = cn.connection(db,user,pwsd)

def insert_table(db,user,pwsd,schema,table,values):
    conn = cn.connection(db,user,pwsd)
