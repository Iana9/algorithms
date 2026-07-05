from dataclasses import dataclass

@dataclass
class Value:
    speed: int
    loss: float
    
    def __str__(self):
        return f"[{self.speed}, {self.loss}]"
