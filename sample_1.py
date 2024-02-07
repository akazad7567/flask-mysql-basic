from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# db = SQLAlchemy(app)

names = {"sharifa": {"age": 30, "gender": "female"},
         "sharif": {"age": 35, "gender": "male"}}

class HelloWorld(Resource):

    def get(self, name):
        if name in names:
            return names[name]
        else:
            abort(404, message=f"Name '{name}' not found.")


api.add_resource(HelloWorld, '/helloworld/<string:name>')  # Use 'api' instead of 'app' here

if __name__ == '__main__':
    app.run(debug=True)
