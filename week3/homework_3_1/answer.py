#!/usr/bin/env python

import pymongo
import gridfs

# establish a connection to the database
connection = pymongo.MongoClient()

#get a handle to the test database
db = connection.school
students = db.students


def main():
	list = students.find()
	for student in list:
		scr = 100
		ctr = -1
		idx = -1
		for score in student["scores"]:
			ctr = ctr + 1
			if score["type"] == "homework":
				if score["score"] < scr:
					idx = ctr
					scr = score["score"]
		del student["scores"][idx]
		students.update({"_id": student["_id"]}, {"$set": {"scores": student["scores"]}})	

if __name__ == '__main__':
	main()
