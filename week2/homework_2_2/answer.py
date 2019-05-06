
import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)

# get a handle to the school database
db=connection.students
grades = db.grades


def go():

    try:
        cursor = grades.find({'type':'homework'},{"_id":0}).sort([('student_id',pymongo.ASCENDING),('score',pymongo.ASCENDING)])
        id = -1
        for doc in cursor:
            if id != doc['student_id']:
                id = doc['student_id']
                grades.remove(doc)
		
    except:
        print "Unexpected error:", sys.exc_info()[0]

    
        
        

go()

