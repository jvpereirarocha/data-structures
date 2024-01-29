
type Item = list[float | int | str]

class Queue:
    def __init__(self) -> None:
        self.queue = []

    def is_empty(self) -> bool:
        return self.queue == []
    
    def add(self, item) -> None:
        self.queue.append(item)

    def remove(self) -> None:
        if not self.queue:
            raise ValueError("Nothing to remove into the queue")
        
        self.queue.pop(0)