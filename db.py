import click
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import orm
from app import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.sqlite'

db = SQLAlchemy()
db.init_app(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    complete = db.Column(db.Boolean, default=False)
    description = db.Column(db.String, nullable=False)
    lists = db.relationship('List', secondary='todo_list', back_populates='todos')

    def populate_lists(self, list_ids):
        lists = []
        for id in list_ids:
            if id > 0: lists.append(db.session.get(List, id))
        self.lists = lists

class List(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String, nullable=False)
    todos = db.relationship(Todo, secondary='todo_list', back_populates='lists')
    complete = False
    
    @orm.reconstructor
    def check_complete(self):
        self.complete = all([todo.complete for todo in self.todos])

todo_list = db.Table(
    'todo_list',
    db.Column('todo_id', db.Integer, db.ForeignKey('todo.id'), primary_key=True),
    db.Column('list_id', db.Integer, db.ForeignKey('list.id'), primary_key=True)
)

with app.app_context():
    db.create_all()

@click.command('init-db')
def init():
    with app.app_context():
        db.drop_all()
        db.create_all()
    click.echo('Database has been initialized.')

app.cli.add_command(init) 

def insert_sample():
    # Delete all existing data, if any
    db.session.execute(db.delete(todo_list))
    db.session.execute(db.delete(Todo))
    db.session.execute(db.delete(List)) 

    # Create sample to-do items
    todo1 = Todo(complete=True, description='Get some food')
    todo2 = Todo(description='Drive the bike more often')
    todo3 = Todo(description='Implement web app')
    todo4 = Todo(complete=True, description='Call mom')
    todo5 = Todo(complete=True, description='Clean up') 

    # Create sample to-do list items
    list1 = List(name='Life')
    list2 = List(name='Work')
    list3 = List(name='Family')

    # Associate to-do items to lists by filling their `Todo.list` attribute
    todo1.lists.append(list1)
    todo2.lists.append(list1)
    todo2.lists.append(list2)
    todo3.lists.append(list2)
    todo4.lists.append(list3)
    todo5.lists.append(list3)   

    # Add all objects to the queue and commit them to the database
    db.session.add_all([todo1, todo2, todo3, todo4, todo5, list1, list2, list3])
    db.session.commit()