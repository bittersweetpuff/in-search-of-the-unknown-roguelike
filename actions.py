#Main action class. Other actions will be subclasses of this class. 
class Action:
    pass


class EscapeAction(Action):
    pass

#movement
class MovementAction(Action):
    def __init__(self, dx: int, dy: int):
        super().__init__()

        self.dx = dx
        self.dy = dy