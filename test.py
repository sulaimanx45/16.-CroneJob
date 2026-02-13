from redis_init import r
import datetime
from db_loop import run_scheduler


def create_task(name, description, execution_time, status='pending'):

    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    execution_time=execution_time.strftime("%Y-%m-%d %H:%M:%S")
    task_id = r.incr('task_counter')
    task = {
        'task_id': task_id,
        'name': name,
        'description': description,
        'curr_time': current_time,
        'exec_time': execution_time,
        'status': status}
    r.hset(f'task:{task_id}', mapping=task)
    return task

name = input("Enter task name: ")
description = input("Enter description: ")
user_input = input("Enter date and time (YYYY-M-D H:M:S): ")
execution_time = datetime.datetime.strptime(user_input, "%Y-%m-%d %H:%M:%S")

task = create_task(name, description, execution_time)
print(task)
run_scheduler()