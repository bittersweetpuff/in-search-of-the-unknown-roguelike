import tcod

from engine import Engine
from entity import Entity
from game_map import GameMap
from input_handlers import EventHandler

def main() -> None:
    #screen size setup
    screen_width = 80
    screen_height = 50

    #map size setup
    map_width = 80
    map_height = 45

    #tileset setup
    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    #add event handler
    event_handler = EventHandler()

    player = Entity(int(screen_width / 2), int(screen_height / 2), "@", (255, 255, 255))
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), "@", (255, 255, 0))
    entities = {npc, player}

    #map setup
    game_map = GameMap(map_width, map_height)

    #engine setup
    engine = Engine(entities=entities, event_handler=event_handler, game_map=game_map, player=player)

    #building new terminal window
    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="In Search of the Unknown",
        vsync=True,
    ) as context:
        #Setup console (order="F" makes Numpy array [x, y] instead of [y, x])
        root_console = tcod.Console(screen_width, screen_height, order="F")
        while True:
            engine.render(console=root_console, context=context)

            events = tcod.event.wait()

            engine.handle_events(events)



if __name__ == "__main__":
    main()