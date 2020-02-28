from app import create_app, db
from app.models import User, Brewery, Beer

app = create_app()

@app.shell_context_processor
def get_context():
    return dict(User = User, Brewery=Brewery, Beer=Beer,app=app, db=db)