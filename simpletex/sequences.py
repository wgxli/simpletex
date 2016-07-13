from simpletex.core import Formatter
from simpletex.base import Environment


class ItemList(Formatter):
    @staticmethod
    def format_text(text) -> str:
        """Accepts either iterable of pairs or iterable of items."""
        try:
            return '\n'.join(r'\item[{}] {}'.format(key, item)
                             for key, item in text)
        except ValueError:
            return '\n'.join(r'\item {}'.format(item) for item in text)


class OrderedList(Environment):
    def __init__(self):
        super().__init__('enumerate')

    def format_text(self, text) -> str:
        return super().format_text(ItemList()(text))


class UnorderedList(Environment):
    bullet = None

    def __init__(self):
        super().__init__('itemize')

    def format_text(self, text) -> str:
        if self.bullet is None:
            return super().format_text(ItemList()(text))
        else:
            list_item_pairs = [(self.bullet, item) for item in text]
            return super().format_text(ItemList()(list_item_pairs))
