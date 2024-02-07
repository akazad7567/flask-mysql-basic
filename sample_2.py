from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# db = SQLAlchemy(app)


videos = {}

class Video(Resource):

    def get(self, video_id):
        return videos[video_id]
    
    def put(self, video_id):
        print(request.form)
        return {"data": request.form, "id": video_id}
                       


api.add_resource(Video, '/video/<int:video_id>')  # Use 'api' instead of 'app' here

if __name__ == '__main__':
    app.run(debug=True)
