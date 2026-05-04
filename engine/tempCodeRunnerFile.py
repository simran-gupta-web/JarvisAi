query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)

query = "INSERT INTO sys_command VALUES (null,'one note', 'C:\Program Files\Microsoft Office\root\Office16\ONENOTE.EXE')"
cursor.execute(query)
con.commit()