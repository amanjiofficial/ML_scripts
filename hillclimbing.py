import random,sys,copy
# code by Aman Ahuja
from optparse import OptionParser
try:
  import psyco
  psyco.full()
except ImportError:
  pass
 
"""
cowboy code, but seems to work
USAGE: python prog <numberruns=1> <verbocity=False>
"""
 
class board:
  def __init__(self, list=None):
    if list == None:
      self.board = [[0 for i in range(0,8)] for j in range(0,8)]
      #initialize queens at random places
      for i in range(0,8):
        while 1:
          rand_row = random.randint(0,7)
          rand_col = random.randint(0,7)
          if self.board[rand_row][rand_col] == 0:
            self.board[rand_row][rand_col] = "Q"
            break
