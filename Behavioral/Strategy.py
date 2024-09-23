from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass

class Strategy(ABC):
    @abstractmethod
    def execute(self,):
        pass
    
class AverageStrategy(Strategy):
    def execute(self, data) -> None:
        print(f"Calculate avarge list: {data}")
    
class MinMaxStrategy(Strategy):
    def execute(self, data) -> None:
        print(f"Search min-max in list: {data}")

@dataclass        
class DataContext(ABC):
    _strategy : Strategy
    
    @property
    def strategy(self,):
        return self._strategy
    
    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy
    
    def handle(self, data: any) -> None:
        self._strategy.execute(data)
        
if __name__ == "__main__":
    
    strategyOne = AverageStrategy()
    strategyTwo = MinMaxStrategy()
    
    data = DataContext(strategyOne)
    data.handle("Hello this is my strategyOne")

    data.strategy = strategyTwo
    data.handle("Hello this is my strategyTwo")
