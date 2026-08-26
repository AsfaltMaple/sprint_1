new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
completed_tasks = ['task_002', 'task_012', 'task_006'] 


if 'task_005' in new_tasks:
    completed_tasks.append(new_tasks.pop()) 

new_tasks.remove('task_007')

new_tasks.insert(0, new_tasks.pop(-1))

print(new_tasks[0])
