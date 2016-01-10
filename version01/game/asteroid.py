import random
from game import resources
from version01.game.physicalObject import PhysicalObject

class Asteroid(PhysicalObject):
    def __init__(self, *args, **kwargs):
        super(Asteroid, self).__init__(img=resources.asteroid_image, *args, **kwargs)
        self.rotate_speed = random.random() * 100 - 50

    def __str__(self):
        result_string = "Type: Asteroid | (x, y)=, " , self.x , "," , self.y , " | v(x,y)=" , self.velocity_x , "," , self.velocity_y , "| scale=" , self.scale
        return str(result_string)

    def handle_collision_with(self, other_object):
        super(Asteroid, self).handle_collision_with(other_object)
        if self.dead and self.scale >= 0.25:
            num_asteroids = random.randint(2, 3)
            for i in range(num_asteroids):
                new_asteroid = Asteroid(x=self.x, y=self.y, batch=self.batch)
                new_asteroid.rotation = random.randint(0, 360)
                new_asteroid.velocity_x = random.random() * 70 + self.velocity_x
                new_asteroid.velocity_y = random.random() * 70 + self.velocity_y
                new_asteroid.scale = self.scale * 0.5
                #print("creating new asteroid: ", str(new_asteroid))
                #print("vx: ", new_asteroid.velocity_x, " | vy: ", new_asteroid.velocity_y, " | scale: ", new_asteroid.scale)
                self.new_objects.append(new_asteroid)
                #print("appended that asteroid to new objects: ", self.new_objects)
            print("new objects to add: ", str(self.new_objects))

    def update(self, dt):
        super(Asteroid, self).update(dt)
        #if len(self.new_objects) != 0:
        print("Asteroid class: have following new objects to add: \n", self.new_objects)
        self.rotation += self.rotate_speed * dt
