class Node:
    """Класс для представления узла стека.

    Атрибуты:
        data: Данные, хранящиеся в узле.
        next_node: Ссылка на следующий узел в стеке.
    """

    def __init__(self, data, next_node=None):
        """Инициализация узла с заданными данными и указателем на следующий узел.

        Аргументы:
            data: Данные, которые будут храниться в узле.
            next_node: Ссылка на следующий узел (по умолчанию None).
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для представления стека.

    Атрибуты:
        stack_size: Максимальный размер стека.
        top: Узел, указывающий на вершину стека.
    """

    def __init__(self, stack_size=5, top=None):
        """Инициализация стека с заданным размером и пустой вершиной.

        Аргументы:
            stack_size: Максимальный размер стека (по умолчанию 5).
            top: Узел, указывающий на вершину стека (по умолчанию None).
        """
        self.stack_size = stack_size
        self.top = top  # через топ обращаемся к атрибутам ноды

    def push(self, data):
        """Добавление элемента на вершину стека.

        Аргументы:
            data: Данные, которые нужно добавить в стек.

        Возвращает:
            str: Сообщение о переполнении стека, если он заполнен.
        """
        if self.size_stack() < self.stack_size:
            new_node = Node(data)
            new_node.next_node = self.top  # та вершина которая была
            self.top = new_node  # переназначаем вершину
        else:
            print("Стэк переполнен")
            return "Стэк переполнен"

    def pop(self):
        """Удаление элемента с вершины стека.

        Возвращает:
            data: Данные удаленного узла или сообщение о пустом стеке.
        """
        if self.top:
            remove_last = self.top
            self.top = self.top.next_node
            return remove_last.data
        else:
            return "Стэк пуст"

    def is_empty(self):
        """Проверка, пуст ли стек.

        Возвращает:
            bool: True, если стек пуст, иначе False.
        """
        return self.top is None

    def is_full(self):
        """Проверка, заполнен ли стек.

        Возвращает:
            bool: True, если стек заполнен, иначе False.
        """
        return self.stack_size == self.size_stack()

    def clear_stack(self):
        """Очистка стека, удаляя все элементы."""
        while self.top:
            self.pop()

    def get_data(self, index):
        """Получение данных по индексу.

        Аргументы:
            index: Индекс элемента, который нужно получить.

        Возвращает:
            data: Данные элемента по заданному индексу или сообщение "Out of range".
        """
        counter = 0
        stack_item = self.top
        while stack_item:
            if counter == index:
                return stack_item.data
            stack_item = stack_item.next_node
            counter += 1
        return "Out of range"

    def size_stack(self):
        """Получение текущего размера стека.

        Возвращает:
            int: Текущий размер стека.
        """
        counter = 0
        stack_item = self.top
        while stack_item:
            counter += 1
            stack_item = stack_item.next_node
        return counter

    def counter_int(self):
        """Подсчет количества целочисленных значений в стеке.

        Возвращает:
            int: Количество целых чисел в стеке.
        """
        counter = 0
        stack_item = self.top
        while stack_item:
            if isinstance(stack_item.data, int):
                counter += 1
            stack_item = stack_item.next_node
        return counter