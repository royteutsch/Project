"""
Uses serialisation with the dictionary
"""
import os
import pickle


class DatabaseWriter:

    def __init__(self, file_location: str):
        self.data = []

        self.file_loc = file_location

        db_file = open(self.file_loc, 'wb')  # Creates the file location if it didn't exist
        db_file.close()

    def change_value(self, key, val):
        try:
            self.data[key] = val
            return 0
        except:
            return 1

    def set_value(self, key, val):
        self.change_value(key, val)
        # start critical section
        db_file = open(self.file_loc, 'wb')  # Changes the file
        if self.data is not []:
            pickle.dump(self.data, db_file)
        db_file.close()
        # end critical section
        print(f"DatabaseWriter.set_value:{os.getpid()} exit")

    def get_value(self, key):
        print("DatabaseWriter.get_value: enter")
        # start critical section
        if os.stat(self.file_loc).st_size != 0:
            db_file = open(self.file_loc, 'rb')
            self.data = pickle.load(db_file)
            print(f"DatabaseWriter.get_value:{os.getpid()} Data: {self.data}")
            db_file.close()
        else:
            print("DatabaseWriter.get_value: Database: Empty")
            self.data = []
        print("DatabaseWriter.get_value: exit")

        ret_val = None
        if key in self.data:
            ret_val = self.data[key]
        return ret_val
        # end critical section

    def delete_value(self, key):
        ret_val = None
        if key in self.data:
            ret_val = self.data[key]

        print("DatabaseWriter.delete_value: enter")
        # start critical section
        db_file = open(self.file_loc, 'wb')  # Removes the key from the file
        pickle.dump(self.data, db_file)
        db_file.close()
        # end critical section
        print("DatabaseWriter.delete_value: exit")

        return ret_val
