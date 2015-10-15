#!/usr/bin/env python
import web
import MySQLdb
import pymysql.cursors

urls = (
	'/book', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/')

class Index(object):
	def GET(self):
		return render.book_form()

	def POST(self):
		form = web.input(name="Someone", title="Something", publish_date="1776-01-01")
		book = "%s, by %s in %s" % (form.title, form.name, form.publish_date)
		connection = MySQLdb.Connect(host='localhost', 
			user='root', 
			db='library', 
	       		)
		cursor = connection.cursor()
		add_book_info = """INSERT INTO `books` (`title`, `author`, `publish_date`) VALUES (%s, %s, %s)"""
		cursor.execute(add_book_info, (form.title, form.name, form.publish_date))
		# connection is not autocommit by default. So you must commit to save your changes
		connection.commit()

		# Read a single record
		sql = "SELECT `book_number`, `title`, `author` FROM `books`"
		cursor.execute(sql)
		result = cursor.fetchone()
		print(result)

		return render.index(book = book)
		connection.close()


if __name__ == "__main__":
	app.run()
