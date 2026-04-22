import os
from flask import Flask, render_template, redirect, url_for, request, abort
import db

app = Flask(__name__)

app.config.from_mapping(
    SECRET_KEY='secret_key_just_for_dev_environment',
    DATABASE=os.path.join(app.instance_path, 'todos.sqlite')
)
app.cli.add_command(db.init_db)
app.teardown_appcontext(db.close_db_con)

@app.route('/')
@app.route('/index')
def index():
    return redirect(url_for('lists'))

@app.route('/todos/', methods=['GET', 'POST'])
def todos():
    db_con = db.get_db_con()
    if request.method == 'GET':
        sql_query = 'SELECT * FROM todo ORDER BY id;'
        todos = db_con.execute(sql_query).fetchall()
        return render_template('todos.html', todos=todos)
    else:  # request.method == 'POST'
        sql_query = 'INSERT INTO todo (description) VALUES (?);'
        db_con.execute(sql_query, [request.form.get('description')])
        db_con.commit()
        return redirect(url_for('todos'))

@app.route('/todos/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def todo(id):
    db_con = db.get_db_con()
    if request.method == 'GET':
        sql_query = (
            'SELECT * FROM '
            '( SELECT * FROM todo '
                'LEFT JOIN todo_list '
                'ON todo.id=? AND todo_id=todo.id ) '
            'WHERE id=?;'
        )
        todo = db_con.execute(sql_query, [id, id]).fetchone()
        if todo:
            sql_query = 'SELECT id, name FROM list ORDER BY name;'
            lists = db_con.execute(sql_query).fetchall()
            return render_template('todo.html', todo=todo, lists=lists)
        else:
            abort(404)
    elif request.method == 'PATCH':
        complete = bool(request.form.get('complete'))
        description = request.form.get('description')
        list_id = int(request.form.get('list_id'))
        sql_query = 'UPDATE todo SET complete = ?, description = ? WHERE id = ?;'
        db_con.execute(sql_query, [complete, description, id])
        sql_query = 'DELETE FROM todo_list WHERE todo_id = ?;'
        db_con.execute(sql_query, [id])
        if list_id:
            sql_query = 'INSERT INTO todo_list (todo_id, list_id) VALUES (?, ?);'
            db_con.execute(sql_query, [id, list_id])
        db_con.commit()
        return redirect(url_for('todo', id=id))
    else:  # request.method == 'DELETE'
        sql_query = 'DELETE FROM todo WHERE id = ?;'
        db_con.execute(sql_query, [id])
        db_con.commit()
        return redirect(url_for('todos'), 303)

@app.route('/lists/')
def lists():
    db_con = db.get_db_con()
    sql_query = 'SELECT * from list ORDER BY name;'
    lists_temp = db_con.execute(sql_query).fetchall()
    lists = []
    for list_temp in lists_temp:
        list = dict(list_temp)
        sql_query = (
            'SELECT COUNT(complete) = SUM(complete) '
            'AS complete FROM todo '
            f'JOIN todo_list ON list_id={list["id"]} '
                'AND todo_id=todo.id; '
        )
        complete = db_con.execute(sql_query).fetchone()['complete']
        list['complete'] = complete
        lists.append(list)
    if request.args.get('json') is not None:
        return lists
    else:
        return render_template('lists.html', lists=lists)

@app.route('/lists/<int:id>')
def list(id):
    db_con = db.get_db_con()
    sql_query_1 = f'SELECT name FROM list WHERE id={id}'
    sql_query_2 = (
        'SELECT id, complete, description FROM todo '
        f'JOIN todo_list ON todo_id=todo.id AND list_id={id} '
        'ORDER BY id;'
    )
    list = {}
    result = db_con.execute(sql_query_1).fetchone()
    if result is not None:
        list['name'] = result['name']
        list['todos'] = db_con.execute(sql_query_2).fetchall()
        if request.args.get('json') is not None:
            list['todos'] = [dict(todo) for todo in list['todos']]
            return list
        else:
            return render_template('list.html', list=list)
    else:
        return redirect(url_for('lists'))

@app.route('/insert/sample')
def run_insert_sample():
    db.insert_sample()
    return 'Database flushed and populated with some sample data.'

@app.errorhandler(404)
def http_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def http_internal_server_error(e):
    return render_template('500.html'), 500