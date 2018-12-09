from flask import Flask, request, jsonify,json

class Response():
    
    illness=""
    remedy=""
    
    
    def __init__(self,illness,remedy):
          self.illness=illness
          self.remedy=remedy
          
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)