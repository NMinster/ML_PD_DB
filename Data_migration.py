import psycopg2
from psycopg2 import sql

dbname = "ML_PD_DB"
user = "username"
password = "password"
host = "host"
port = "port"

# Connect postgres DB
conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
cur = conn.cursor()

# Create a table 
cur.execute("""
    CREATE TABLE genes (
        gene_identifier varchar(255),
        associated_study varchar(255),
        association_details varchar(255),
        gene_description text,
        protein_information text,
        variants text
    )
""")

with open('genes.csv', 'r') as f:
    next(f)  
    cur.copy_from(f, 'genes', sep=',')


conn.commit()

cur.close()
conn.close()
