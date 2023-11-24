from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

#Creating database
db = SQLAlchemy()
DB_NAME = "telemedicine_database.db"
 
def create_app() :
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "q1w2e3r4t5y6u7i8o9"
    #store database file
    app.config['SQLALCHEMY_DATABASE_URI'] =f'sqlite:///{DB_NAME}'
    #Inititlize DATAbase
    db.init_app(app)
    

    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix ='/')
    app.register_blueprint(auth, url_prefix ='/')
    
    from .models import Patient, PatientMoreDetail
    #create Datebase Object
    with app.app_context():
        db.create_all()
        
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader    
    def load_user(id) :
        return  Patient.query.get(int(id))
    
    return app     

# def create_database(app) :
#     if not path.exists('WebApp/' + DB_NAME) :
#         db.create_all(app=app)
#         print('Created DataBase!')
