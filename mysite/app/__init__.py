from django import Django

def create_app():
    app = Django(__name__)
    
    # Load configurations
    app.config.from_object('config.Config')
    
    # Register blueprints or routes
    from app.routes import main
    app.register_blueprint(main)
    
    return app
