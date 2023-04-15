"""
Created on Sat Apr 15 13:23:54 2023

@author: Sean James 
"""

import sqlite3

########################################################
#
# Relation:
#
# Constructor(...)
# Properties:
#   Type_One: string 
#   ID_One: int
#   Type_Two: string 
#   ID_Two: int
#   Score: float
#   Total_Votes: int
#

class Relation: 

    def __init__(self, dbConn, Type_One, ID_One, Type_Two, ID_Two, Score, Total_Votes): 
      self.Type_One =  Type_One
      self.ID_One = ID_One
      self.TypeTwo = TypeTwo
      self.ID_Two = ID_Two
      self.Score = Score
      self.TotalVotes = TotalVotes

    @property
    def Type_One(self):
        return self.Type_One

    @property
    def ID_One(self): 
        return self.ID_One

    @property
    def Type_Two(self): 
        return self.Type_Two

    @property
    def ID_Two(self): 
        return self.ID_Two
    
    @property
    def Score(self): 
        return self.Score

    @property 
    def TotalVotes(self): 
        return self.TotalVotes