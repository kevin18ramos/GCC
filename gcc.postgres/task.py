import cn as cn

def insert_statement_s(value_dict):
    #for loop statement
    ...

def di_table(caller_file,schema_name,table_name,value_dict,cn):
    sql = f"""
    BEGIN;
            {insert_statement_s(value_dict)}
            COMMIT;
            """
    cn.d_cn(caller_file)
