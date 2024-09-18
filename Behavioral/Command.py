from __future__ import annotations
from dataclasses import dataclass
from abc import ABC, abstractmethod

class ICommand(ABC):
    ''' This interface Command '''
    @abstractmethod
    def execute(self,):
        pass
    
@dataclass
class SimpleCommand(ICommand):
    _payload : str
    def execute(self) -> None:
        print(f"SimpleCommand: See, I can do simple things like printing"
            f"({self._payload})"
        )
    
@dataclass
class ComplexCommand(ICommand):
    _reciever: Receiver
    _param: str
    def execute(self) -> None:
        self._reciever.do_something(self._param)
    
@dataclass
class Receiver:
    def do_something(self, param: str) -> None:
        print(f"\nReceiver: Working on ({param}.)", end="")

@dataclass
class Invoker:
    ''' Commands '''
    _on_light = None
    _off_light = None
    
    ''' set of commands'''
    def set_on_light(self, command: ICommand):
        self._on_light = command
    
    def set_off_light(self,command: ICommand):
        self._off_light = command
    
    '''Excute command '''
    def executeCommand(self,):
        print("Invoker: Does anybody want something done before I begin?")
        if isinstance(self._on_light, ICommand):
            self._on_light.execute()
            
        print("Invoker: Does anybody want something done after I finish?")
        if isinstance(self._off_light, ICommand):
            self._off_light.execute()
        
                
if __name__ == "__main__":
    
    sender = Invoker()
    cmd = SimpleCommand("ON")
    sender.set_on_light(cmd)
    # sender.executeCommand()
  
    receiver = Receiver()
    param = "Hello"
    cmd = ComplexCommand(receiver, "Send email")
    sender.set_off_light(cmd)
    
    sender.executeCommand()  
