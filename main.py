"""
Entry point into Flask app
"""

from template.flask.factory import create_flask_app

if __name__ == "__main__":
    app = create_flask_app()

    app.run(debug=True, port=8080, host="0.0.0.0")
