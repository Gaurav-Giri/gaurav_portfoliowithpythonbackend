from app import create_app
from models import db, User, Project

def initialize_database():
    app = create_app()
    
    with app.app_context():
        # Create tables
        db.create_all()
        print("✅ Database tables created successfully!")
        
        # Create sample data
        if not User.query.first():
            admin = User(username="admin", password="securepassword")
            admin.password = "securepassword"  # Hashes the password
            db.session.add(admin)
            
            project = Project(
                title="FullStack Portfolio Website",
                description="full stack website with flask backend and database, admin login, password hashing .",
                technologies="Python, Flask",
                project_link="https://github.com/Gaurav-Giri/gaurav_portfoliowithpythonbackend"
            )
            db.session.add(project)
            
            db.session.commit()
            print("✅ Sample data created!")

if __name__ == "__main__":
    initialize_database()
