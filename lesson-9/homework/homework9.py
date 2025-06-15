from datetime import datetime
import math
import string
import os

# 1. Circle Class
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

# 2. Person Class
class Person:
    def __init__(self, name, country, birth_date):
        self.name = name
        self.country = country
        self.birth_date = datetime.strptime(birth_date, "%Y-%m-%d")

    def age(self):
        today = datetime.today()
        return today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))

# 3. Calculator Class
class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        return a / b if b != 0 else "Cannot divide by zero"

# 4. Shape and Subclasses
class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass

class CircleShape(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):
        return 2 * math.pi * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2
    def perimeter(self):
        return 4 * self.side

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def perimeter(self):
        return self.a + self.b + self.c
    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

# 5. Binary Search Tree Class
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return Node(key)
        else:
            if key < root.val:
                root.left = self.insert(root.left, key)
            else:
                root.right = self.insert(root.right, key)
        return root

    def search(self, root, key):
        if root is None or root.val == key:
            return root is not None
        if key < root.val:
            return self.search(root.left, key)
        return self.search(root.right, key)

# 6. Stack Data Structure
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop() if self.stack else "Stack is empty"

# 7. Linked List Data Structure
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = ListNode(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        temp = self.head
        if temp is not None and temp.data == key:
            self.head = temp.next
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp:
            prev.next = temp.next

    def display(self):
        elements = []
        temp = self.head
        while temp:
            elements.append(temp.data)
            temp = temp.next
        return elements

# 8. Shopping Cart Class
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, price):
        self.items[item] = price

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]

    def total_price(self):
        return sum(self.items.values())

# 9. Stack with Display
class DisplayStack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop() if self.stack else "Stack is empty"

    def display(self):
        return self.stack

# 10. Queue Data Structure
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0) if self.queue else "Queue is empty"

# 11. Bank Class
class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, customer_id, initial_balance=0):
        self.accounts[customer_id] = initial_balance

    def deposit(self, customer_id, amount):
        if customer_id in self.accounts:
            self.accounts[customer_id] += amount

    def withdraw(self, customer_id, amount):
        if customer_id in self.accounts and self.accounts[customer_id] >= amount:
            self.accounts[customer_id] -= amount
            return True
        return False

    def get_balance(self, customer_id):
        return self.accounts.get(customer_id, "Account not found")
