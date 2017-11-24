import os

from beerinv import initApp

app = initApp(os.environ['APP_SETTINGS'])

if __name__ == '__main__':
    
    app.run()