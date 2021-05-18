from . import *
current_num=[0]

@socketio.on('connect')
def joinning_add():

	emit('update', current_num[-1])


@socketio.on('plusone' )
def tell_add(msg):
 	current_num
 	result=current_num[-1]+1
 	current_num.append(result)
 	emit('update', result,broadcast=True)
