#! usr/bin/python3

### Part:-
### to maintain data in single files ###


import os
import sys

import pickle  # just using it for now, sure to impliment a better one in future

class mtain_rec:

    def __init__(self, user_data,file):
        self.user_data = user_data
        self.file = file

    def check_if_exist(self):
        pass
        

    def write_rec(self):
        try:
             with open(f"{self.file}", "ab") as rec_file:
                 pickle.dump(self.user_data,rec_file)
                 
        except Exception as e:
                 assert e != None, "ERRoR OpeNNiNg FiLe!"
                
    def read_rec(self,file):
        try:
        
             with open(f"{self.file}", "rb") as rec_file:
                 rec_data = pickle.load(rec_file)
                 return rec_data
        except Exception as e:
                 assert e != None, "ERRoR OpeNNiNg FiLe!"
    
        

if __name__ == "__main__":
    pass
