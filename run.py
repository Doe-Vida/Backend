from flask_app import app


app = app

if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)