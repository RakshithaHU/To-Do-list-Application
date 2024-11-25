import datetime

# Task data structure
class Task:
    def __init__(self, title, due_date=None, priority="Low"):
        self.title = title
        self.due_date = due_date
        self.priority = priority

    def __str__(self):
        due_date_str = self.due_date if self.due_date else "No due date"
        return f"{self.title} (Due: {due_date_str}, Priority: {self.priority})"

# To-Do List class to manage tasks
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, due_date=None, priority="Low"):
        task = Task(title, due_date, priority)
        self.tasks.append(task)
        print(f"Added: {task}")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("To-Do List:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

    def delete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Deleted: {removed_task}")
        else:
            print("Invalid task number.")

# Function to parse the due date
def parse_due_date(date_str):
    try:
        return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD.")
        return None

# Main function to interact with the user
def main():
    to_do_list = ToDoList()
    
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            title = input("Enter the task title: ")
            due_date_str = input("Enter the due date (YYYY-MM-DD) or leave blank: ")
            due_date = parse_due_date(due_date_str) if due_date_str else None
            priority = input("Enter the priority (Low, Medium, High): ").capitalize()
            if priority not in ["Low", "Medium", "High"]:
                print("Invalid priority, defaulting to Low.")
                priority = "Low"
            to_do_list.add_task(title, due_date, priority)

        elif choice == "2":
            to_do_list.view_tasks()

        elif choice == "3":
            try:
                task_number = int(input("Enter the task number to delete: "))
                to_do_list.delete_task(task_number)
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == "4":
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

