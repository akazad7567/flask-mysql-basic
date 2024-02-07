from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# db = SQLAlchemy(app)
videos_put_args = reqparse.RequestParser()
videos_put_args.add_argument("name", type = str, help = "Name of the video is required", required = True)
videos_put_args.add_argument("views", type = int, help = "Views of the video is required", required = True)
videos_put_args.add_argument("reaction", type = int, help = "Reaction of the video is required", required = True)

videos = {}

class Video(Resource):

    def get(self, video_id):
        return "ok", 200
    
    def put(self, video_id):
        args = videos_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201
                       


api.add_resource(Video, '/video/<int:video_id>')  # Use 'api' instead of 'app' here

if __name__ == '__main__': 
    app.run(debug=True)
