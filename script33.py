class Computer:
    def __init__(self, owner, processor, os, ram, monitor):
        self.owner = owner
        self.processor = processor
        self.os = os
        self.ram = ram
        self.monitor = monitor
    def __str__(self):
        return f'Владельцам компьютера является {self.owner}'
    def compare_ram(self, other_computer):
        if self.ram > other_computer.ram:
            return f'У {self.owner} больше оперативной памяти, чем у {other_computer.owner}'
        elif self.ram < other_computer.ram:
            return f'У {other_computer.owner} больше оперативной памяти, чем у {self.owner}'
        else:
            return 'У обоих компьютеров одинаково оперативной памяти.'
pc_ivan = Computer("Иван", "Intel i7", "Windows 11", 16, "27 дюймов")
pc_bob = Computer("Боб", "Apple M2", "macOS", 32, "24 дюйма")
print(pc_ivan)
print(pc_bob)
print(pc_ivan.compare_ram(pc_bob))
