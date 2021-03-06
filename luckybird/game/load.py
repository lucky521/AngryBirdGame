import pyglet, random, math
import resources
import angrybird, egg
import config
from util import distance

global conf 
conf = config.config()

def angrybirds(num_asteroids, player_position, batch=None):
	asteroids = []
	for i in range(num_asteroids):
		asteroid_x, asteroid_y = player_position
		while distance((asteroid_x,asteroid_y), player_position) < conf.bird_pic_size:
			asteroid_x = random.randint(0, conf.windows_width)
			asteroid_y = random.randint(0, conf.windows_height)
		
		whichbird = [resources.red_bird_image1, resources.red_bird_image2, resources.red_bird_image3,
				resources.white_bird_image, resources.yellow_bird_image, resources.black_bird_image]
		img = whichbird[random.randint(0, len(whichbird)-1)]

		new_asteroid = angrybird.AngryBird(img=img, x=asteroid_x, y=asteroid_y, batch=batch)
		
		new_asteroid.rotation = random.randint(0, 360)
		new_asteroid.velocity_x = random.randint(-10,10) * conf.bird_speed/5
		new_asteroid.velocity_y = random.randint(-10,10) * conf.bird_speed/5

		asteroids.append(new_asteroid)
	return asteroids

def eggs(num_eggs, player_position, batch=None):
	eggs = []
	for i in range(num_eggs):
		asteroid_x, asteroid_y = player_position
		while distance((asteroid_x,asteroid_y), player_position) < conf.bird_pic_size:
			asteroid_x = random.randint(0, conf.windows_width)
			asteroid_y = random.randint(0, conf.windows_height)

		new_egg = egg.Egg(img=resources.egg_image, x=asteroid_x, y=asteroid_y, batch=batch)
		new_egg.rotation = random.randint(0, 360)
		new_egg.velocity_x = random.randint(-10,10) * conf.bird_speed/5
		new_egg.velocity_y = random.randint(-10,10) * conf.bird_speed/5
		
		eggs.append(new_egg)
	return eggs


def player_lives(num_icons, batch=None):
	player_lives = []
	for i in range(num_icons):
		new_sprite = pyglet.sprite.Sprite(img=resources.player_image,
							x=conf.windows_width-(i+1)*conf.life_pic_size,
							y=5,
							batch=batch)
		new_sprite.scale = 0.5
		player_lives.append(new_sprite)
	return player_lives
