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
                title="Sample Project",
                description="This is a sample project",
                technologies="Python, Flask",
                project_link="https://example.com"
            )
            db.session.add(project)
            
            db.session.commit()
            print("✅ Sample data created!")

if __name__ == "__main__":
    initialize_database()