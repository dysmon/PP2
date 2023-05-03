import psycopg2


hostname = 'localhost'
database = 'postgres'
username = 'postgres'
pwd = 'Admin'
port_id = 5432
conn, cur = None, None

conn = psycopg2.connect(
     host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id
)
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS book (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        phone VARCHAR(255) NOT NULL
    );
""")

cur.execute(
    '''CREATE OR REPLACE FUNCTION search_from_book(a VARCHAR, b VARCHAR)
      RETURNS SETOF book 
   AS
   $$
      SELECT * FROM book WHERE name = a AND phone = b;
   $$
   language sql;
   '''
)

cur.execute(
   '''CREATE OR REPLACE PROCEDURE insert_list_of_users(
  IN users TEXT[][]
)
LANGUAGE plpgsql
AS $$
DECLARE
  i TEXT[];
BEGIN 
   Foreach i slice 1 in array users
   LOOP
      INSERT INTO book (name, phone) VALUES (i[1], i[2]);
   END LOOP;
 
END
$$;
'''
)

cur.execute(
   '''CREATE OR REPLACE PROCEDURE insert_to_book(nm VARCHAR, phon VARCHAR)
      LANGUAGE plpgsql
      AS $$
      DECLARE 
         cnt INTEGER;
      BEGIN
         SELECT INTO cnt (SELECT count(*) FROM book WHERE name = nm);
         IF cnt > 0 THEN
            UPDATE book
               SET phone = phon
               WHERE name = nm;
         ELSE
            INSERT INTO book(name, phone) VALUES (nm, phon);
            END IF;
      END;
      $$;''')


cur.execute("""CREATE OR REPLACE PROCEDURE delete_from_book(nm VARCHAR)
LANGUAGE plpgsql
AS $$
DECLARE cnt INTEGER;
BEGIN
    SELECT into cnt (SELECT count(*) FROM book WHERE name = nm);
	IF cnt IS NOT NULL THEN
        DELETE FROM book
		WHERE name=nm;
    END IF;
END;
$$;""")

cur.execute("""CREATE OR REPLACE FUNCTION paginating(a integer, b integer)
RETURNS SETOF book
AS $$
   SELECT * FROM book
	ORDER BY name
	LIMIT a OFFSET b;
$$
language sql;""")


a = input('search\ninsert\ninsertloop\ndelete\npaginating\n')
if a == 'search':
   cur.execute("SELECT search_from_bk('Python', '87771535415')")
   data = cur.fetchall()
   for row in data:
        print(row)

elif a == 'insert':
   cur.execute("CALL insert_to_book('Python','87771535415')")

elif a == 'insertloop':
  cur.execute('''CALL insert_list_of_users(ARRAY[
    ARRAY['Golang', '87076052769'],
    ARRAY['Java', '87079815569'],
    ARRAY['Cpp', '87074793780']
]);''')  

elif a == 'delete':
   cur.execute("CALL delete_from_book('Golang')")

elif a == 'paginating':
   cur.execute(
      '''SELECT * FROM paginating(1, 1);'''
   )
   data = cur.fetchall()
   for row in data:
      print(row)
conn.commit()
cur.close()
conn.close()