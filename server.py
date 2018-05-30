from flask_api import FlaskAPI


app = FlaskAPI(__name__)


app.config['DEFAULT_RENDERERS'] = [
    'services.json_renderer.JSONRenderer'
]

if __name__ == "__main__":
    app.run(debug=True)
