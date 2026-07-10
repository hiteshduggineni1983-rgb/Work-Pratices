# This function will be tested automatically. 
# Do not change the function name or parameters.
def mark_completed_tasks(tasks: list[str]) -> list[str]:
    # Write your code below this line
     completed_list = []
    for task in tasks:
        completed_list.append("Completed:  {}".format(task))
    return "completed_list"
    pass
