# coding: utf-8
import random
import pygame


class Maze(pygame.sprite.Sprite):
	"""Grid with coordinate keys and values
	Player start at "D" if he pick up all items
	he win, else he lose the game"""
	def __init__(self):
		super().__init__()
		"""A dict for coordinates
		   a list for the way. And a method to set position
		   of the objects"""
		self.grid = {}
		self.way_list = []
		self.macGyver = None
		self.guardian = None
		self.inventory = []
		self.read_maze()
		self.set_objects()
		

	def read_maze(self):
		x, y = 0, 0
		with open("Maze.txt", "r") as line:
			l = line.read()
			for element in l:
				if element == '\n':
					x, y = 0, y+1
				else :
					self.grid[(x, y)] = element
					if element == "0":
						self.way_list.append((x, y))
					if element == "D":
						self.macGyver = x, y 
					if element == "F":
						self.guardian = x, y
					x += 1

	def set_objects(self):
		objects = ["T", "S", "E"]
		random.shuffle(self.way_list)
		for key, value in enumerate(objects):
			self.grid[self.way_list[key]] = value

	########################
	###### DESTINATION #####
	########################             

	def check_move(self, a, b):
		"""check the destination"""
		return ((a, b) in self.grid and self.grid[a, b] != "#")

	def check_items(self, a, b):
		"""	check if an object is on the way
			pick up this object. 
			add object in MacGyver inventory"""
		if self.grid[a, b] == "T" or self.grid[a, b] == "S" or self.grid[a, b] ==  "E":
			self.inventory.append(self.grid[a, b])
			print(self.grid[a, b])
			self.grid[a, b] = "0"

	def check_pos_guardian(self, a, b):
		"""check the guardian position"""
		if self.grid[a, b] == self.grid[self.guardian]:
			if len(self.inventory) == 3:
				print("You win")
			else:
				print("Repose en paix, fils du Gondor.")
		
	########################
	######    MOVES    #####
	########################
	def top(self):
		x = self.macGyver[0]
		y = self.macGyver[1] - 1	
		if self.check_move(x, y):
			self.macGyver = x, y
			self.check_items(x, y)
			self.check_pos_guardian(x, y)
			# update rect position
			self.rect.x , self.rect.y = x*20, y*20
			

	def bot(self):
		x = self.macGyver[0]
		y = self.macGyver[1] + 1
		if self.check_move(x, y):
			self.macGyver = x, y
			self.check_items(x, y)
			self.check_pos_guardian(x, y)
			# update rect position
			self.rect.x , self.rect.y = x*20, y*20
			

	def left(self):
		x = self.macGyver[0] - 1
		y = self.macGyver[1] 
		if self.check_move(x, y):
			self.macGyver = x, y
			self.check_items(x, y)
			self.check_pos_guardian(x, y)
			# update rect position
			self.rect.x , self.rect.y = x*20, y*20
			
	def right(self):
		x = self.macGyver[0] + 1 
		y = self.macGyver[1] 
		if self.check_move(x, y):
			self.macGyver = x, y
			self.check_items(x, y)
			self.check_pos_guardian(x, y)
			# update rect position
			self.rect.x , self.rect.y = x*20, y*20
			

	

