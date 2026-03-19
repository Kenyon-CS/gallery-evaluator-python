from dataclasses import dataclass
from typing import List

@dataclass
class ScoreBreakdown:
    name: str
    score: float

@dataclass
class Layout:
    name: str
    scores: List[ScoreBreakdown]
