from flask import Flask
from flask_graphql import GraphQLView
from models import db
from schema import schema

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///agriculture.db'
db.init_app(app)


@app.before_first_request
def create_tables():
    db.create_all()


app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

if __name__ == '__main__':
    app.run(debug=True)
