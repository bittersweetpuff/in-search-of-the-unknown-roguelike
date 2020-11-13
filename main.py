import tcod


def main() -> None:
    #screen size setup
    screen_width = 80
    screen_height = 50

    #player position setup
    player_x = int(screen_width/2)
    player_y = int(screen_height / 2)

    #tileset setup
    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
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
            #print player as @ 
            root_console.print(x=player_x, y=player_y, string="@")
            
            context.present(root_console)

            for event in tcod.event.wait():
                if event.type == "QUIT":
                    raise SystemExit()


if __name__ == "__main__":
    main()