from datetime import datetime


class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d")
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "В ожидании"
        return f"Task: {self.description}, Due: {self.due_date.strftime('%Y-%m-%d')}, Status: {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date):
        task = Task(description, due_date)
        self.tasks.append(task)

    def mark_task_completed(self, description):
        for task in self.tasks:
            if task.description == description and not task.completed:
                task.mark_completed()
                return f"Task '{description}'отмечены как завершенные"
        return f"Task '{description}' не найдено или уже завершено."

    def display_uncompleted_tasks(self):
        uncompleted_tasks = [task for task in self.tasks if not task.completed]
        if not uncompleted_tasks:
            return "Нет невыполненных заданий."
        return "\n".join(str(task) for task in uncompleted_tasks)


class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
        else:
            print(f"Item '{item_name}' Не найдено в ассортименте магазина.")

    def get_price(self, item_name):
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
        else:
            print(f"Item '{item_name}' Не найдено в ассортименте магазина.")

    def __str__(self):
        return f"Store: {self.name}, Address: {self.address}, Items: {self.items}"


if __name__ == "__main__":
    manager = TaskManager()
    manager.add_task("Закончить отчет по проекту", "2025-04-01")
    manager.add_task("Подготовка к встрече", "2025-03-30")
    print(manager.display_uncompleted_tasks())
    manager.mark_task_completed("Закончить отчет по проекту")
    print(manager.display_uncompleted_tasks())

    store1 = Store(" Магазин Магия", "123 Проспект Мира")
    store2 = Store(" Магазин Троечка", "456 Улица Всех")
    store3 = Store("Сапун", "789 Шоссе Победы")

    store1.add_item("Яблоки", 0.5)
    store1.add_item("Бананы", 0.75)
    store1.add_item("Мясо", 1.75)

    store2.add_item("Молоко", 1.5)
    store2.add_item("Хлеб", 2.0)
    store2.add_item("Курица", 1.05)

    store3.add_item("Яйца", 3.0)
    store3.add_item("Сыр", 5.5)
    store3.add_item("Колбаса", 2.75)

    print(store1)
    print(store2)
    print(store3)



    # Testing Store Methods
    if __name__ == "__main__":
        # Create a store instance
        test_store1 = Store("Магазин Магия", "123 Проспект Мира")

        # Add items
        test_store1.add_item("Яблоки", 0.5)
        test_store1.add_item("Бананы", 0.75)
        test_store1.add_item("Мясо", 1.75)


        print("Сохраняйте после добавления элементов:")
        print(test_store1)

        # Get price of an item
        print("Цена яблок:", test_store1.get_price("Яблоки"))

        # Update price of an item
        test_store1.update_price("Яблоки", 0.9)
        print("Обновленная цена на яблоки:", test_store1.get_price("Яблоки"))

        # Remove an item
        test_store1.remove_item("Бананы")
        print("Сохранить после завершения бананов:")
        print(test_store1)

