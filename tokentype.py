### Python Imports
from dataclasses import dataclass


@dataclass
class TokenType():
    tokenType: str
    tokenValue: str
    tokenLine: int
    tokenColumn: int
