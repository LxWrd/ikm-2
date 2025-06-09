import csv

class Tree:
    """Структура дерева"""
    def __init__(self, value = 0):
        self.value = value
        self.left = None
        self.right = None

    @staticmethod
    def build_tree(data):
        """Строит бинарное дерево на основе списка пар (число, путь)."""
        head = Tree(0) # Добавляю корень (по условию всегда 0)
        # Цикл проходящий через все кортежи (Значение, Путь) списка
        for number, path in data:
            current = head
            # Проходим через путь, при необходимости добавляя узлы, доходя до элемента стоящего перед нужным
            for bit in path[:-1]:
                if bit == '0':
                    if current.left is None:
                        current.left = Tree(0)
                    current = current.left
                else:
                    if current.right is None:
                        current.right = Tree(0)
                    current = current.right
            # Берется последний элемент пути и по нему добавляется узел с значением
            last_bit = path[-1]
            if last_bit == '0':
                current.left = Tree(number)
            else:
                current.right = Tree(number)

        return head

    def print_tree(self, level=0, prefix='Head - '):
        """Выводит дерево в читаемом виде."""
        if self is not None:
            print(" " * (level * 4) + prefix + str(self.value))
            if self.left:
                self.left.print_tree(level + 1, "L--- ")
            if self.right:
                self.right.print_tree(level + 1, "R--- ")

def file_reader():
    """Выводит список с кортежами"""
    file = open('file.csv', encoding='utf-8')
    reader = csv.DictReader(file)
    arr_for_data = []

    for i in reader:
        arr_for_data.append((i['Значение'],i['Путь']))
    return arr_for_data

def main():
    data = file_reader()

    tree = Tree.build_tree(data)

    tree.print_tree()

if __name__ == "__main__":
    main()