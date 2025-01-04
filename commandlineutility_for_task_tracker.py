import argparse
import json
import os
Task_file="task.json"
if not os.path.exists(Task_file):
    with open(Task_file,"w") as f:
        json.dump([],f)
def load_tasks():
    with open(Task_file,"r") as f:
        return json.load(f)
def save_tasks(tasks):
    with open(Task_file,"w") as f:
        json.dump([],f,indent=4)
def add_tasks(description,due_date=None):
    tasks=load_tasks()
    task_id = len(tasks) +1
    tasks.append({"id":task_id, "description": description, "due_date":due_date,"completed": False})
def view_tasks(status=None):
    tasks=load_tasks()
    if status:
        tasks=[task for task in tasks if task ["completed"]==(status=="complete")]
    for task in tasks:
        status="``" if task ["completed"] else "X"
        print(f"{task[id]}: {task["description"]}: (Due:{task["due_date"]})[{status}]")
def mark_completedtasks(task_id):
    tasks=load_tasks()
    for task in tasks:
        if task[id]==task_id:
            task["completed"]= True
            save_tasks(tasks)
            print(f"task{task_id} marked as completed")
            return
    print(f"task{task_id} not found")
def delete_tasks(task_id):
    tasks=load_tasks()
    tasks=[task for task in tasks[id] != task_id]
    save_tasks(tasks)
    print(f"task{task_id} deleted")
def main():
    parser=argparse.ArgumentParser(description="task tracker CLI")
    subparsers=parser.add_subparsers(dest="command")

    parser_add=subparsers.add_parser("add", help= "add new task")
    parser_add.add_argument("description",help="description of task")
    parser_add.add_argument("due_date",help="Due date to the task")
    parser_view=subparsers.add_parser("view",help="view the task")
    parser_view.add_argument("--status",choices=["pending","completed"], help="filter task by status")
    parser_complete=subparsers.add_parser("complete", help="marked as completed")
    parser_complete.add_argument("task_id",type=int,help="id of the task mark as complete")
    parser_delete=subparsers.add_parser("delete", help="delete a task")
    parser_delete.add_argument("task_id", type=int,help="id of the task to delete")
    args=parser.parse_args()
    if args.command == "add":
        add_tasks(args.description, args.due_date)
    elif args.command=="view":
        view_tasks(args.status)
    elif args.command == "complete":
        mark_completedtasks(args.task_id)
    elif args.command == "delete":
        delete_tasks(args.task_id)
    else:
        parser.print("help")
if __name__ == "main":
    main()
