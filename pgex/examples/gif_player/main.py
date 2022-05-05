import asyncio
import os

import pygame

from .gif_player import GIFPlayer


WIDTH, HEIGHT = 500, 400

pygame.init()


async def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    background_gif = GIFPlayer(
        os.path.join(os.path.dirname(__file__), "image.gif"),
        size=(WIDTH, HEIGHT),
        exclude=(0,),
    )

    running = True
    while running:
        clock.tick(60)
        screen.fill("black")

        background_gif.play(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        await asyncio.sleep(0)


def run():
    asyncio.run(main())


if __name__ == "__main__":
    run()