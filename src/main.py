import tcod

import copy

import color
from engine import Engine
import entity_factories
from procgen import generate_dungeon

def main() -> None:
    #screen size setup
    screen_width = 80
    screen_height = 50

    #map size setup
    map_width = 80
    map_height = 43

    #dungeon map info setup
    room_max_size = 10
    room_min_size = 6
    max_rooms = 30
    max_monsters_per_room = 2

    #tileset setup
    tileset = tcod.tileset.load_tilesheet(
        "./resources/dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    player = copy.deepcopy(entity_factories.player)

    engine = Engine(player=player)

    #map setup
    engine.game_map = generate_dungeon(
        max_rooms=max_rooms,
        room_min_size=room_min_size,
        room_max_size=room_max_size,
        map_width=map_width,
        map_height=map_height,
        max_monsters_per_room=max_monsters_per_room,
        engine=engine,
    )

    engine.update_fov()

    engine.message_log.add_message(
        "You are in a middle of the dungeon. You have no idea where you are. The only source of light is a small torch in your hand.", color.welcome_text
    )

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
            root_console.clear()
            engine.event_handler.on_render(console=root_console)
            context.present(root_console)

            engine.event_handler.handle_events(context)



if __name__ == "__main__":
    main()