# Homework 1: ToDo List Application

class Task:
    def __init__(self, title, description, due_date, status=False):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def mark_complete(self):
        self.status = True


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_task_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()

    def list_all_tasks(self):
        return self.tasks

    def list_incomplete_tasks(self):
        return [task for task in self.tasks if not task.status]


# Homework 2: Simple Blog System

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author


class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def list_all_posts(self):
        return self.posts

    def display_by_author(self, author):
        return [post for post in self.posts if post.author == author]

    def delete_post(self, title):
        self.posts = [post for post in self.posts if post.title != title]

    def edit_post(self, title, new_title=None, new_content=None):
        for post in self.posts:
            if post.title == title:
                if new_title:
                    post.title = new_title
                if new_content:
                    post.content = new_content

    def display_latest_posts(self, n=5):
        return self.posts[-n:]


# Homework 3: Simple Banking System

class Account:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance


class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_number] = account

    def get_account(self, account_number):
        return self.accounts.get(account_number)

    def transfer(self, from_acc, to_acc, amount):
        sender = self.get_account(from_acc)
        receiver = self.get_account(to_acc)
        if sender and receiver and sender.withdraw(amount):
            receiver.deposit(amount)
            return True
        return False

    def display_account_details(self, account_number):
        acc = self.get_account(account_number)
        if acc:
            return vars(acc)
        return None
