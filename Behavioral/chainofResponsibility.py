from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional

class Handler(ABC):
    @abstractmethod
    def handle(self, amount: int) -> Optional[int]:
        pass
    
    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass
    
class AbstractHandler(Handler):
    _next_handler: Handler = None
    
    @abstractmethod
    def handle(self, amount: int) -> Optional[int]:
        if self._next_handler:
            return self._next_handler.handle(amount)
        return None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler
    
class Currency500K(AbstractHandler):
    def handle(self, amount: int) -> Optional[int]:
        if amount >= 500:
            num = amount // 500
            print(f"Currency 500K VND - Amount {num}")
        else:
            return super().handle(amount)
        
class Currency200K(AbstractHandler):
    def handle(self, amount: int) -> Optional[int]:
        if amount >= 200:
            num = amount // 200
            print(f"Currency 200K VND - Amount {num}")
        else:
            return super().handle(amount)
        
class Currency100K(AbstractHandler):
    def handle(self, amount: int) -> Optional[int]:
        if amount >= 100 :
            num = amount // 100
            print(f"Currency 100K VND - Amount {num}")
        else:
            return super().handle(amount)
        
class Currency50K(AbstractHandler):
    def handle(self, amount: int) -> Optional[int]:
        if amount >= 50 :
            num = amount // 50
            print(f"Currency 50K VND - Amount {num}")
        else:
            return super().handle(amount)

class Currency20K(AbstractHandler):
    def handle(self, amount: int) -> Optional[int]:
        if amount >= 20 :
            num = amount // 20
            print(f"Currency 20K VND - Amount {num}")
        else:
            return super().handle(amount)
        
class Currency10K(AbstractHandler):
    def handle(self, amount: int) -> Optional[int]:
        if amount >= 10 :
            num = amount // 100
            print(f"Currency 10K VND - Amount {num}")
        else:
            return super().handle(amount)

class CurrencyChain:
    def __init__(self):
        # Calling chains
        self.firstChain  = Currency500K()
        self.secondChain = Currency200K()
        self.thirdChain  = Currency100K()
        self.fourthChain = Currency50K()
        self.fifthChain  = Currency20K()
        self.lastChain   = Currency10K()
        
        # Setting-up chains:
        self.firstChain.set_next(self.secondChain).set_next(self.thirdChain).set_next(self.fourthChain).set_next(self.fifthChain).set_next(self.lastChain)
        
if __name__ == "__main__":
    
    amount = int(input("Input amount: "))
    if amount < 10 or amount %10 != 0:
        print(f"Please check your code again...!")
        exit()
        
    CurrencyChain = CurrencyChain()
    CurrencyChain.firstChain.handle(amount)
    print("="*20)
    print(f"Done...!")
