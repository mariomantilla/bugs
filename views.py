from manage import app
from models import Bug


@app.route('/')
def hello_world():
    
    bug1 = Bug() 
    return 'There are '+str(Bug.select().count())+' bugs'