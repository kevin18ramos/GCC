from . import pcn

def insert_statement_s(schema_name, table_name, dict_list):
    insert_sql_list = []

    for value_dict in dict_list:
        columns = ", ".join(value_dict.keys())

        values = []
        for value in value_dict.values():
            if value is None:
                values.append("NULL")
            elif isinstance(value, str):
                escaped = value.replace("'", "''")
                values.append(f"'{escaped}'")
            else:
                values.append(str(value))

        values_sql = ", ".join(values)

        single_insert = f"""
        INSERT INTO {schema_name}.{table_name} ({columns})
        VALUES ({values_sql});
        """
        insert_sql_list.append(single_insert.strip())

    return "\n".join(insert_sql_list)


def di_table(caller_file, schema_name, table_name, dict_list):
    sql = f"""
    BEGIN;
    {insert_statement_s(schema_name, table_name, dict_list)}
    COMMIT;
    """


    conn,cursor = pcn.d_cn(caller_file)
    cursor.execute(sql)
    conn.commit()

def delete_statement_s(schema_name, table_name, dict_list):
    delete_sql_list = []
    where_clause = ''

    for value_dict in dict_list:
        x = 0
        for value in value_dict.values():
            x+=1
            if x > 1:
                sql = f""" AND {value["name"]} = '{value["value"]}' """
                where_clause.append(sql)
            else:
                sql = f"""
            WHERE {value["name"]} = '{value["value"]}'
            """
                where_clause.append(sql)

        single_delete = f"""
        DELETE FROM {schema_name}.{table_name} {where_clause}
        """
        delete_sql_list.append(single_delete.strip())

    return "\n".join(delete_sql_list)


def dd_table(caller_file, schema_name, table_name, dict_list):
    sql = f"""
    BEGIN;
    {delete_statement_s(schema_name, table_name, dict_list)}
    COMMIT;
    """


    conn,cursor = pcn.d_cn(caller_file)
    cursor.execute(sql)
    conn.commit()