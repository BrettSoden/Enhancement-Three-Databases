from pymongo import MongoClient

from bson.objectid import ObjectId

from pymongo import cursor

from bson.json_util import dumps


class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, userval: str, passval: str) -> None:
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        self.client = MongoClient(f'mongodb://{userval}:{passval}@localhost:45565/AAC')
        self.database = self.client['AAC']

    # Complete this create method to implement the C in CRUD.
    def create(self, data: dict) -> bool:
        """Insert a document into the AAC database."""
        if data is not None and type(data) is dict:  # endures data is their and able to be searched
            try:
                self.database.animals.insert_one(data)  # data should be dictionary
                return True
            except Exception as e:
                print("An exception has occured ::", e)
            return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")  # throws exception for empty database

    # inserts multiple files into the database
    def insertMany(self, data: dict) -> bool:
        """Insert multiple documents into the AAC database."""
        if data is not None and type(data) is dict:  # ensures data is their and able to be searched
            try:
                self.database.animals.insert_many(data)  # data should be dictionary
                return True
            except Exception as e:
                print("An exception has occured ::", e)
            return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")  # throws exception for empty database

    # reads and displays data
    def read(self, query: dict) -> cursor.Cursor:  # allows for the cursor to search database
        """Query a result from the AAC database"""
        if query is not None and type(query) is dict:
            return self.database.animals.find(query, {"_id": False})
        else:
            raise Exception("Read error: invalid query parameter")

    # updates a single file
    def updateOne(self, query: dict, changes: dict) -> str:
        """Update a document in the AAC database"""
        if (query is not None and type(query) is dict) and (changes is not None and type(changes) is dict):
            updated = self.database.animals.update_one(query, changes)    # queries changes
            return dumps(updated.raw_results)                # updates raw results using dumps
        else:
            raise Exception("Update error: invalid update parameters")    # throws exception when file cannot be updated

    # updates multiple files at once
    def updateMany(self, query: dict, changes: dict) -> str:
        """Update multiple documents in the AAC database"""
        if (query is not None and type(query) is dict) and (changes is not None and type(changes) is dict):
            updated = self.database.animals.update_many(query, changes)   # queries changes
            return dumps(updated.raw_results)
        else:
            raise Exception("Update error: invalid update parameters")    # throws exception when file cannot be updated

    # deletes a single file
    def deleteOne(self, remove: dict) -> str:
        """Delete multiple documents from the AAC database"""
        if remove is not None and type(remove) is dict:
            deleted = self.database.animals.delete_one(remove)  # delete one command
            return dumps(deleted.raw_results)    # deletes file from the raw results
        else:
            raise Exception("Delete error: invalid delete parameter")

    # deletes multiple files from database
    def deleteMany(self, remove: dict) -> str:
        """Delete a document from the AAC database"""
        if remove is not None and type(remove) is dict:
            deleted = self.database.animals.delete_many(remove)  # delete multiple files command
            return dumps(deleted.raw_result)   # deletes files from results
        else:
            raise Exception("Delete error: invalid delete parameter")    # exception thrown for invalid deletion

    # replaces one files from database
    def replaceOne(self, query: dict, changes: dict) -> str:
        """Replace a document in the AAC database"""
        if (query is not None and type(query) is dict) and (changes is not None and type(changes) is dict):
            replaced = self.database.animals.replace_one(query, changes)   # replace one command
            return dumps(replaced.raw_results)   # replaced from results
        else:
            raise Exception("Update error: invalid replacement parameters")  # exception thrown for invalid replacement

    # replaces multiple files from database
    def replaceMany(self, query: dict, changes: dict) -> str:
        """Replace a document in the AAC database"""
        if (query is not None and type(query) is dict) and (changes is not None and type(changes) is dict):
            replaced = self.database.animals.replace_many(query, changes)   # replace many command
            return dumps(replaced.raw_results)   # replaced from results
        else:
            raise Exception("Update error: invalid replacement parameters")   # exception thrown for invalid replacements

    # counts the number of files in the database
    def count(self, query: dict) -> cursor.Cursor:
        """Query a specific result from the AAC database"""
        if query is not None and type(query) is dict:
            return self.database.animals.count(query, {"_id": False})   # counts the database files by _id
        else:
            raise Exception("Read error: invalid count parameters")    # throws exception for invalid count
