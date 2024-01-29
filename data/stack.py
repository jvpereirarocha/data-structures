
type Item = list[float | int | str]

class Stack:
    def __init__(self, fifo: bool) -> None:
        """
        Note: FIFO means first in first out
        If this flag is True, then we will remove the first item added
        otherwise, we will remove the last item added
        """
        self.stack = []
        self.fifo = fifo

    def is_empty(self) -> bool:
        return self.stack == []
    
    def add(self, item) -> None:
        self.stack.append(item)

    def remove(self) -> Item:
        if not self.stack:
            raise ValueError("Nothing to remove into the stack")
        
        if self.fifo:
            item_to_remove = self.stack[0]
        else:
            item_to_remove = self.stack[-1]
        
        self.stack.remove(item_to_remove)

        return item_to_remove