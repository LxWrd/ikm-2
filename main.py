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
        for number, way in data:
            flag = True
            try:
                if isinstance(int(number),int) != True:
                    print('Ошибка')
            except ValueError:
                print(f'Ошибка в значений - {number}')
                flag = False
            for i in way:
                if i != '0' and i != '1':
                    print(f"Некорректный путь - {way}")
                    flag = False
            current = head
            # Проходим через путь, при необходимости добавляя узлы, доходя до элемента стоящего перед нужным
            if flag:
                for bit in way[:-1]:
                    if bit == '0':
                        if current.left is None:
                            current.left = Tree(0)
                        current = current.left
                    else:
                        if current.right is None:
                            current.right = Tree(0)
                        current = current.right
                # Берется последний элемент пути и по нему добавляется узел с значением
                last_bit = way[-1]
                if last_bit == '0':
                    current.left = Tree(number)
                else:
                    current.right = Tree(number)

        return head

def print_tree(node, level=0, prefix="Head - "):
    """Выводит дерево в читаемом виде."""
    if node is not None:
        print(" " * (level * 4) + prefix + str(node.value))
        print_tree(node.left, level + 1, "L--- ")
        print_tree(node.right, level + 1, "R--- ")

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

    print_tree(tree)

if __name__ == "__main__":
    main()