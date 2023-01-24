tables = {
    1: [],
    2: [],
    3: []
}

# this function will accept positional arguments 
def assign_tables_positional(table_number, name, vip_status):
    tables[table_number] = [name,vip_status]
    return tables

# this function is for keyword arguments
def assign_tables_keywords(table_number, name, vip_status):
    tables[table_number] = [name,vip_status]
    return tables

# this function will use some parameter default if not passed while calling function
def assign_tables_default(table_number, name, vip_status = False):
    tables[table_number] = [name, vip_status]
    return tables

print(assign_tables_positional(1,"satinder",True))
print(assign_tables_keywords(vip_status=True, table_number=2, name="sam"))
print(assign_tables_default(3,"nuhaar"))