import psycopg2
import csv
# Connect to the database by creating a connection object
conn = psycopg2.connect(
    host='localhost', 
    dbname='phone', 
    user='postgres', 
    password='123456'
    )

# Create a cursor to work with the database
cur = conn.cursor()

# # Delete table
cur.execute('DROP TABLE phones_data;')

conn.commit()

#1
# Create a new table
cur.execute("""CREATE TABLE phones_data (
            name VARCHAR(255),
            phone_number VARCHAR(20)
);
""")

conn.commit()

#2
#upload data from csv file
filename = r'people.csv'

with open(filename, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        name, phone_number = row
        
        # Create new students
        cur.execute(f"""INSERT INTO phones_data (name, phone_number) VALUES 
                    ('{name}', '{phone_number}');
        """)

        conn.commit()
#entering user name, phone from console
kboard_name = str(input("Name: "))
num = str(input("Num: "))

postgres_insert_query = """ INSERT INTO  phones_data (name, phone_number) VALUES (%s,%s)"""
record_to_insert = (kboard_name, num)
cur.execute(postgres_insert_query, record_to_insert)

conn.commit()

#3 Implement updating data in the table (change user first name or phone)

cur.execute("""UPDATE phones_data
            SET name = '(changed)'
            WHERE phone_number = '+770200000';
""")

conn.commit()

#4 Querying data from the tables (with different filters)

cur.execute("SELECT * FROM phones_data WHERE name = 'salta'")
print(cur.fetchall())

#5 Implement deleting data from tables by username of phone

cur.execute("""DELETE FROM phones_data
            WHERE name = 'samal';
""")

conn.commit()