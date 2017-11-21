import os

from beerinv import initApp

if __name__ == '__main__':
    
    app = initApp(os.environ['APP_SETTINGS'])
    app.run()