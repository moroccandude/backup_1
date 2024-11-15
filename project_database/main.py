from app import connectTo_db,creation_table,insertation_des_tables
if __name__ == "__main__":
    engine=connectTo_db();
    creation_table(engine);
    insertation_des_tables(engine);