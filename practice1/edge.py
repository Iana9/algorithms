from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .node import Node


@dataclass
class Edge:
    target: "Node" # куда ведет ребро
    speed: int # пропускная способность в МБ
    loss: float # потери (0.9 = 90%)

    def __str__(self):
        return f"{self.target.name} ({self.speed}, {int(self.loss * 100)}%)"