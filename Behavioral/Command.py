from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass, field

class Command(ABC):
    """
    The Command interface declares a method for executing a command.
    """
    @abstractmethod
    def execute(self,) -> None:
        raise NotImplementedError("You should implement this method.")
    
    
@dataclass
class NotifyCommand(Command):
    
    _receiver: object
    _message: dict
    _consumer: dict
    
    async def execute(self) -> any:
        
        data = self._receiver.notify(self._message)
    
        await self._consumer.send_json({
            "data": data,
            "status": 200
        })
        
@dataclass
class ChatMessageCommand(Command):
    _receiver: object
    _message: dict
    _consumer: dict
    
    async def execute(self) -> None:
        print(f"ChatMessageCommand: {self._message}")
        await self._receiver.chat_message(self._message)
    
class Receiver:
    def notify(self, msg: dict) -> dict:
        print(f"Message sent: {msg}")
        return "Hello from Notification event"
    
    def chat_message(self, msg: dict) -> None:
        print(f"Message sent: {msg}")

@dataclass
class Invoker:
    
    _commands: dict = field(default_factory=dict)
    
    def register(self, event_name, command):
        self._commands[event_name] = command
    
    async def execute(self, event_name):
        if event_name in self._commands:
            await self._commands[event_name].execute()
        else:
            print(f"Command for event {event_name} not found")
        
                
if __name__ == "__main__":
    sender = Invoker()
    receiver = Receiver()
    sender.register('chat', NotifyCommand(self.receiver, event, consumer))
    await sender.execute('chat')
