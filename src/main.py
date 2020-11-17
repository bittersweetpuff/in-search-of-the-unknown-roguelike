import tcod

from engine import Engine
from entity import Entity
from procgen import generate_dungeon
from input_handlers import EventHandler

def main() -> None:
    #screen size setup
    screen_width = 80
    screen_height = 50

    #map size setup
    map_width = 80
    map_height = 45

    #dungeon map info setup
    room_max_size = 10
    room_min_size = 6
    max_rooms = 30

    #tileset setup
    tileset = tcod.tileset.load_tilesheet(
        "./resources/dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    #add event handler
    event_handler = EventHandler()

    player = Entity(int(screen_width / 2), int(screen_height / 2), "@", (255, 255, 255))
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), "@", (255, 255, 0))
    entities = {npc, player}

    #map setup
    game_map = generate_dungeon(
        max_rooms=max_rooms,
        room_min_size=room_min_size,
        room_max_size=room_max_size,
        map_width=map_width,
        map_height=map_height,
        player=player
    )

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