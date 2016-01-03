import pyglet

from version01.game import load
from version01.game import resources
from version01.game.Player import Player

main_batch = pyglet.graphics.Batch()
game_window = pyglet.window.Window(800, 600)

score_label = pyglet.text.Label(text="Score: 0", x=10, y=575, batch=main_batch)
level_label = pyglet.text.Label(text="myAsteroidClone", x=400, y=575, anchor_x='center', batch=main_batch)

player_ship = Player(x=400, y=300, batch=main_batch)
game_window.push_handlers(player_ship)
game_window.push_handlers(player_ship.key_handler)
asteroids = load.asteroids(3, player_ship.position, batch=main_batch)
game_objects = [player_ship] + asteroids

player_lives = load.player_lives(4, batch=main_batch)


@game_window.event()
def on_draw():
    # draw things here
    game_window.clear()

    main_batch.draw()


def update(dt):
    to_add = []

    for obj in game_objects:
        obj.update(dt)
        to_add.extend(obj.new_objects)
        obj.new_objects = []

    for i in range(len(game_objects)):
        for j in range(i + 1, len(game_objects)):
            obj_1 = game_objects[i]
            obj_2 = game_objects[j]
            if not obj_1.dead and not obj_2.dead:
                if obj_1.collides_with(obj_2):
                    obj_1.handle_collision_with(obj_2)
                    obj_2.handle_collision_with(obj_1)

    for to_remove in [obj for obj in game_objects if obj.dead]:
        to_remove.delete()
        game_objects.remove(to_remove)

    game_objects.extend(to_add)


if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1 / 120.0)
    pyglet.app.run()
