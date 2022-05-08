import pygame
import asyncio
from .colored_rectangle import ColoredRect


async def main():
    screen = pygame.display.set_mode((600, 500))
    pygame.display.set_caption("Timer!")
    clock = pygame.time.Clock()

    colored_rect = ColoredRect(
        pos=(50, 50),
        size=(500, 400),
        colors=("lightblue", "lightblue1", "lightblue2", "lightblue3"),
    )

    # A custom event that will change the rectangle's color
    color_change_event = pygame.event.custom_type()
    # color_change_event will occur every 1000 milliseconds (1 second)
    pygame.time.set_timer(color_change_event, 1000)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit
            elif event.type == color_change_event:
                colored_rect.change_color()

        screen.fill("black")
        colored_rect.draw(screen)

        clock.tick(60)
        pygame.display.flip()
        await asyncio.sleep(0)


def run():
    asyncio.run(main())


if __name__ == "__main__":
    run()