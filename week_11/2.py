import psycopg2

conn = psycopg2.connect(
	database="phone",
	user='postgres',
	password='123456',
	host='localhost',
	port='5432'
)

''' my SQL in DATAGRIP:
create or replace procedure addPhone(first_name varchar, last_name varchar, phone_number varchar)
as
$$
begin
    update phonebook_lab11
    set phone_num = $3
    where (phonebook_lab11.first_name = $1) and (phonebook_lab11.last_name = $2);
    IF NOT FOUND THEN
        insert into phonebook(first_name,last_name,phone_num) values ($1, $2, $3);
    END IF;
end;
$$
    LANGUAGE plpgsql;'''

cursor = conn.cursor()
conn.autocommit = True
first_name = str(input("First_name: "))
last_name = str(input("Last_name: "))
num= str(input("Num: "))


cursor.execute('CALL addPhone(%s,%s,%s)', (first_name, last_name, num))



cursor.callproc('getStudentNameSurnamePhone', [first_name])
result = cursor.fetchall()
print(result)