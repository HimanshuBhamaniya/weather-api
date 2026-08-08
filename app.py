from flask import Flask, render_template
from routes.weather_routes import weather_bp
from utils.error_handler import register_error_handlers
from core.rate_limiter import init_limiter

app = Flask(__name__)
limiter = init_limiter(app)

app.register_blueprint(weather_bp)

register_error_handlers(app)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)