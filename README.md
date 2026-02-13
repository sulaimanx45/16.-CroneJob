# Task Scheduler with Redis

**Project Overview**
A simple **Python task scheduler** using **Redis** for storage. This project allows creating tasks with a name, description, execution time, and status. The scheduler automatically updates the task status when the execution time is reached.

---

## Features

* Create tasks with:

  * **Name** – Task title
  * **Description** – Task details
  * **Execution Time** – When the task should be executed
  * **Status** – Automatically updated from `pending` → `completed`
* Tasks are stored in **Redis** as hashes for persistence
* Scheduler loop checks tasks periodically and updates status
* Sequential task IDs using Redis counter (`task_counter`)

---

## Folder Structure

```
CroneJob/
│
├─ .venv/                 # Python virtual environment (ignored in git)
├─ redis_init.py          # Redis connection
├─ test.py                # Task creation and scheduler run
├─ db_loop.py             # Scheduler logic
└─ README.md              # Project documentation
```

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/task-scheduler.git
cd task-scheduler
```

2. Create a Python virtual environment:

```bash
python -m venv .venv
```

3. Activate the virtual environment:

* **Windows**:

```bash
.venv\Scripts\activate
```

* **Linux/Mac**:

```bash
source .venv/bin/activate
```

4. Install dependencies:

```bash
pip install redis
```

5. Ensure a **Redis server** is running locally on `localhost:6379`.

---

## Usage

1. Run the task creation script:

```bash
python test.py
```

2. Enter the task details when prompted:

```
Enter task name: school
Enter description: go to school
Enter date and time (YYYY-M-D H:M:S): 2026-02-13 15:14:00
```

3. The scheduler will check tasks every 10 seconds and mark them completed once their execution time is reached:

```
school completed successfully
{'task_id': '1', 'name': 'school', 'description': 'go to school', 'curr_time': '2026-02-13 15:13:29', 'exec_time': '2026-02-13 15:14:00', 'status': 'completed'}
```

---

## How It Works

1. **Task Creation** (`test.py`):

* Generates a sequential task ID using `r.incr('task_counter')`
* Stores the task as a Redis hash with keys: `task_id`, `name`, `description`, `curr_time`, `exec_time`, `status`

2. **Scheduler** (`db_loop.py`):

* Loops every 10 seconds and fetches all tasks from Redis
* Checks if `curr_time >= exec_time`
* Updates task `status` to `completed` in Redis and prints a success message

---

## Dependencies

* Python 3.8+
* Redis server (local or remote)
* Python package: `redis`

Install Python package:

```bash
pip install redis
```

---

## Notes

* Make sure the execution time is **in the future**. Otherwise, the scheduler will immediately mark the task as completed
* The project uses a **simple loop scheduler**, suitable for learning or small projects
* For production, consider using **APScheduler** or **Celery** for scalable task scheduling
