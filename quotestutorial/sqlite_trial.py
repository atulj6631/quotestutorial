import sqlite3

conn = sqlite3.connect('my_trial_db')

curr = conn.cursor()

# statement = """create table quotes_tb(
#                quotes text,
#                author text
#                )"""

statement = """insert into quotes_tb values (
               'You miss 100percent of the shots you dont take', 'Atul Joshi'
            )"""

curr.execute(statement)

conn.commit()
conn.close()