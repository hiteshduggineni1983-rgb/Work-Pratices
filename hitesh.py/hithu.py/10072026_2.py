# This function will be tested automatically. 
# Do not change the function name or parameters.
def generate_numbered_tasks(tasks: list[str]) -> list[str]:
	# Write your code below this line
    numbered_tasks = []
    for index, task in enumerate(task, start=1):
        numbered_tasks.append(f"{index}. {task}")
    return numbered_tasks

    pass