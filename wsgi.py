from app import create_app
from app import db

application = create_app()

from flask_migrate import Migrate
from app.models import Tweet
    
migrate = Migrate(application, db)

if __name__ == '__main__':
    application.run(debug=True)
