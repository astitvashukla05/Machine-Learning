from flask import Flask,render_template,request

items=[
    {'id':1,'name':'Astitva',"num":20},
    {'id':2,'name':'Asti',"num":24},
    {'id':3,'name':'Ast',"num":12}
    ]
app=Flask(__name__)

@app.route('/tasks',methods=['get'])
def viewTask():
   return render_template('tasks.html',items=items)

# TO Get a specific item
@app.route('/tasks/<task_id>',methods=['get'])
def getTask(task_id):
    for item in items:
        if(item['id']==int(task_id)):
            return render_template('tasks.html',items=[item])
    return render_template('error.html',mess="NO TASK FOUND")
    
# ADD TASKS
@app.route('/addtasks',methods=['GET','POST'])
def addTasks():
    if request.method=='POST':
        name=request.form['name']
        id=request.form['id']
        num=request.form['number']
        new_task={'name':name,'id':int(id),'num':int(num)}
        items.append(new_task)
        return render_template('tasks.html',items=items )
    return render_template('addtask.html')

@app.route('/updatetask/<task_id>',methods=['GET','POST'])
def updateTasks(task_id):
    if(request.method=='POST'):
        id=int(request.form['id'])
        name=request.form['name']
        num=int(request.form['number'])
        for item in items:
            if(item['id']==int(task_id)):
                item['name']=name
                item['id']=id
                item['num']=num
        return render_template('tasks.html',items=items)
    for item in items:
        if item['id']==int(task_id):
          return  render_template('update.html',item=item)
    return render_template('error.html',mess='NO task to udpate')
# Delete Item
@app.route('/deletetask/<task_id>',methods=['GET'])

def delteItem(task_id):
    global items
    items=[item for item in items if item['id']!=int(task_id)]
    return render_template('tasks.html',items=items)
    
          

if(__name__=='__main__'):
    app.run(debug=True)