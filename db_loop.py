import datetime
import time
from redis_init import r

def run_scheduler():
    while True:
        curr_time = datetime.datetime.now()
        keys = [key for key in r.keys('task:*') if key != "task:id"]
        for key in keys:
            task = r.hgetall(key)
            if task.get('status') == 'pending':
                exec_time = datetime.datetime.strptime(task['exec_time'], "%Y-%m-%d %H:%M:%S")
                if curr_time >= exec_time:
                    r.hset(key, 'status', 'completed')
                    print(f"{task['name']} completed successfully")
                    updated_task=r.hgetall(key)
                    print(updated_task)
        time.sleep(10)
