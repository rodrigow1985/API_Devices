from datetime import datetime
from pytz import timezone

class Date(dict): 
  
    # __init__ function 
    def __init__(self): 
        self.now = datetime.now(timezone('America/Argentina/Buenos_Aires'))
          
    # Function to set a datetime to an argument
    def getDatetimeNow(self):
        return self.now.strftime('%Y-%m-%d %H:%M:%S')