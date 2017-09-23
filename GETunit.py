from flask import Flask, jsonify

import unittest

class GETTest(unittest.TestCase):
  
  """Since I want to test that the we can get some sort of communication with the server
  this function is not meant to test the database interface, but to open a file to help testing only the GET protocol.
  This through creating a dict of elements which is going to be sent over JSON"""
  """Later on I discovered I am not really testing our own 'get' functions but the Flask json_get, this can be fixed later down the road,
  lets keep it this way for a while, I guess."""  


  def testFile2Dict(self):
    f = open("test.txt", "r")
    catid = f.readline(1)
    textID = f.readline(3)
    title = f.readline(5)
    text = f.readline(7)
    createdAt = f.readline(9)
    createdBy = f.readline(11)
    
    return {catid, textID, title, text, createdAt, createdBy}

  #Just see this as a part of my, the programmers learning process.
  def testGetJsonOnTestFile(self):
    app = Flask(__name__)
    app.testing = True
    client = app.test_client()
    resp = client.get_json(testFile2Dict())
    assert resp.status == 200
  #def performGetTestOnTestDb():
    #TODO Implement, this ^^


if __name__ == '__main__':
    unittest.main()
