import sqlite3
conn = sqlite3.connect('data.db',check_same_thread=False)
c = conn.cursor()


def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS taskstable(task TEXT)')


def add_data(task):
	c.execute('INSERT INTO taskstable(task) VALUES (?)',(task,))
	conn.commit()


def view_all_data():
	c.execute('SELECT * FROM taskstable')
	data = c.fetchall()
	return data

def view_all_task_names():
	c.execute('SELECT DISTINCT task FROM taskstable')
	data = c.fetchall()
	return data

def delete_data(task):
	c.execute('DELETE FROM taskstable WHERE task="{}"'.format(task))
	conn.commit()
