from SystemManager import systemLoad
from routes import app

GourmetBurgers = systemLoad()

if __name__=='__main__':
    app.run(port=5015, debug=True)

