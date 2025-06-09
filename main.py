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

tree = Tree.build_tree([(11,'100'),
                        (23,'1'),
                        (45,'0000')])
tree.print_tree()