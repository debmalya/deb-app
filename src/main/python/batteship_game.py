import random

	
class Ship:
	"""
	This describes characteristics common to all the ships.
	locations - set of locations occupied by the ship. Location always means a pair (tuple of two elements) (row,column).
	hits - set of locations where this ship has been "hits". Hit is always a subset of locations.
	When all the locations are hit, then ship will be sunken.
	This version works with python 2.x.x
	"""
	locations=set()
	hits=set()
	lenght=0
	ship_type=""
	
	def __init__(self):
		"""
		Constructor
		"""
		self.ship_type="ship"
		length=0
		locations=set()
		hits=set()
	
	def get_ship_type(self):
		"""
		returns one of the strings 
		'battleship',
		'cruiser',
		'destroyer',
		'submarine'
		"""
		return self.ship_type
	
	def ok_to_place_ship_at(self, location, horizontal, length, ocean):
		"""
		Returns True if it is okay to place a ship of this length with its bow in the row and column,
	    with the given orientation, and returns False otherwise. 
		 The ship must not overlap another ship, or touch another ship (vertically, horizontally, or diagonally), 
		 and it must not "stick out" beyond the grid. 
		 
		 row,column,length must be integer.
		 horizontal should be a boolean.
		 ocean a ocean object.
		 location tuple. Within this tuple we will have row and column
		 location[0] is row and location[1] is column.
		"""
		# the location should not be occupied.
		if (ocean.is_occupied(location))==True:
			#print 1
			return False
		else:
			len = 0
			while len < length:
				if (ocean.is_open_sea(location))==False:
					#print 2
					return False
				row = location[0]
				col = location[1]
				if horizontal:
					#horizontal increment col value
					col+=1
				else:
					#vertical
					row+=1	
				len +=1	
				if row < 0 or row > 9 or col < 0 or col > 9:
					#print "3a"
					return False
				if (ocean.is_open_sea((row,col)))==False:
					#print 3
					return False
				location=(row,col)										
		#print 4
		return True
		
	def shoot_at(self,location):
		"""
		If a part of ship occupies the given row and column and the ship hasn't 
		been sunk, mark that part of the ship as "hit" (in the hits set) and 
		return True.
		Otherwise return False.				
		"""			
		#print str(location)+" "+str(self.locations)
		if location in self.locations:
			self.hits.add(location)
			return True
		else:
			return False	
		
		
	def place_ship_at(self,location,horizontal,length,ocean):
		"""
		Puts the ship at ocean.
		This gives values to the location instance variable in the ship.
		and also putting reference to the ship in each of the one (or more locations)
		in the ships dictionary in the Ocean object.
		"""	
		if self.ok_to_place_ship_at(location,horizontal,length,ocean):
			# now place the ship here
			len = 0
			row=location[0]
			col=location[1]
			
			while len < length:					
				self.locations.add((row,col))
								
				# update ocean dictionary
				
				ocean.get_ocean()[(row,col)]=self
				#print str(row)+" , "+str(col)+" "+str(ocean.get_ocean()[(row,col)].locations)
				len +=1					
				if (len < length):
					if horizontal:
						#horizontal increment col value
						col+=1
					else:
						#vertical
						row+=1	
			return True
		else:
			return False			
				
				
			
		
	def is_sunk(self):
		"""
		returns True if all locations of this Ship have been hit, and False otherwise. 
		"""	
		
		if len(self.locations) != len(self.hits):
			return False
		else:
			ship_locations=list(sorted(self.locations))
			hit_locations=list(sorted(self.hits))
			#print " locations :" + str(ship_locations)
			#print " hits :" + str(hit_locations)
			for x in range(len(ship_locations)):
				if ship_locations[x] != hit_locations[x]:					
					return False		
				
		return True	
		
	def __str__(self):
		"""
		returns a single character string to use in the Ocean's print method.
		"""
		return self.ship_type[0:1]
			
	
class Battleship(Ship):
	"""
	a ship of length 4.
	"""	
	def __init__(self):
		"""
		Constructor
		"""
		self.ship_type="battleship"		
		self.length=4
		self.locations=set()
		self.hits=set()
	
class Cruiser(Ship):
	"""
	a ship of length 3.
	"""	
	def __init__(self):
		"""
		Constructor
		"""
		self.ship_type="cruiser"
		self.length=3
		self.locations=set()
		self.hits=set()
	
class Destroyer(Ship):
	"""
	a ship of length 2.
	"""
	def __init__(self):
		"""
		Constructor
		"""
		self.ship_type="destroyer"
		self.length=2
		self.locations=set()
		self.hits=set()		
	
class Submarine(Ship):
	"""
	a ship of length 1.	
	"""
	def __init__(self):
		"""
		Constructor
		"""
		self.ship_type="submarine"
		self.length=1
		self.locations=set()
		self.hits=set()
	
class Ocean:
	"""	
	Contains a dictionary of ships representing the ocean and some methods to manipulate it.
	As best possible score is 20. Assumption is 
	1. There can one battleship (Shot needed - 4), 2 Crusier ( Total Shots needed 6)
	3 Destroyer ( Total shots need 6) 4 Submarine (Total shots needed 4).
	
	Members
	Ships - a dictionary whose keys are location and whose values are Ships. 
	Used to quickly determine which ship is in any particular location.
	
	shots_fired = the total number of shots fired by the user.
	hit_count =  the number of times a shot hit a ship. 
	If the user shoots the same part of a ship more than once, every hit is counted.
	Even though the additional "hits" don't do the user any good!
	number_of_ships_sank=The number of ships sunk.
	"""	
		
	shots_fired=0
	hit_count=0
	number_of_ships_sank=0
	ships={}
	hits=set()
	
	def __init__(self):
		"""
		Initialized occean.
		During initialization all the places are free.
		As the occean is 10X10. So there is total 100 locations.
		As soon as any location got occupied by a ship. Occean will be updated.
		"""
		#occupied = [False] * 100
		shots_fired=0
		hit_count=0
		number_of_ships_sank=0
		ships={}
		hits=set()
		self.place_all_ships_randomly()
		
	def is_occupied(self,location):
		"""
		To check whether mentioned row, col is occupied or not.
		0<= row <= 9 and 0 <= column <= 9
		"""		
		return location in self.ships
		
	def is_open_sea(self,location):
		"""
		True - if the position is free and not surrounded by any one horizontally ,vertically , diagonally.
		False - otherwise.
		"""	
		row = location[0]
		col = location[1]
		
		if self.validate_position(row,col)> -1:
			# location is within sea and not occupied
			# now check surroundings
			drow=[0,1,1,1,0,-1,-1,-1]
			dcol=[-1,-1,0,1,1,1,0,-1]
			for x in range(len(drow)):
				search_row = row+drow[x]
				search_col = col+dcol[x]
				
				if search_row > -1 and  search_row < 10 and search_col > -1 and search_col < 10:
					#print "search_row :" + str(search_row)+" search_col : "+str(search_col)+ " occupied ? "+str(self.is_occupied((search_row,search_col)))
					if self.is_occupied((search_row,search_col)) == True:
						#print "search_row :" + str(search_row)+" search_col : "+str(search_col)+ " occupied."
						return False
						
			return True
		else:			
			return False
			
	def shoot_at(self,location):
		"""
		returns True if the given location contains a ship that is still aflost (before this shot)
		False if it does not.
		Updates number of shoot that have been fired, and the number of hits.
		
		If a location conains a "real" ship, shoot_at should return True every time
		the user shoot at the same location.
		
		Once a ship has been "sunk", additional shots at its location should return False.
		"""	
		self.shots_fired+=1
		self.hits.add(location)
		if location in self.get_ocean():
			ship_locations = self.get_ocean()
			self.hit_count+=1
			ship=self.get_ocean()[location]
			#print str(ship.locations)
			if ship.is_sunk():
				# already sunken ship
				return False 
			ship.shoot_at(location)
			
			if ship.is_sunk():
				# this hit makes ship sunken
				print "You just sank a " + ship.get_ship_type()				
				self.number_of_ships_sank+=1
			else:
				
				print "hit"	
			return True 
				
			
				
		else:
			
			print "miss"
			return False	
		
	def get_shots_fired(self):
		"""
		returns the number of shot fired.
		"""
		return self.shots_fired
		
	def get_hit_count(self):
		"""
		returns the number of hits recorded (in this game).
		All hits are counted, 
		not just the first time a given square is hit.
		"""
		return self.hit_count
		
	def get_ships_sunk(self):
		"""
		returns the number of ships sunk (in this game).
		"""	
		return self.number_of_ships_sank
			
	def validate_position(self,row,col):
		"""
		validate a position. 
		Whether is it inside the ocean or not.
		To be inside the ocean 0<= row <= 9 and 0 <= column <= 9
		
		if inside ocean return position in terms row * 10 + col
		False otherwise.
		"""	
		if row > -1 and row < 10 and col > -1 and col < 10:
			position = row * 10 + col
			return position
		else:
			return False		
			
			
				
	def __print__(self):
		"""
		This will print ocean.
		. to indicate a location that has never been shot at.
		- to indicate a location that has been shot at, but nothing was there.
		* to indicate a location containing ship (of unknown type) that has been hit
		but not yet sunk.
		B,C,D or S  - to indicate a ship that has been sunk; 
		"""
		print "    0 1 2 3 4 5 6 7 8 9"
		print "    -------------------"
		str_list = ''
		row = 0
		col = 0 
		for row in range(10):
			for col in range(10):
				if col == 0:
					str_list = ''
					str_list+=str(row)
					str_list+=" | "					
				else:
					str_list+=" "	
				location=(row,col)
				
				if location in self.ships:
					ship=self.ships[location]
					if ship.is_sunk():
						str_list+=ship.get_ship_type()[0:1].upper()
					elif location in self.hits:
						str_list+="*"
					else:
						str_list+="."							
				elif location in self.hits:
					str_list+="-"			
				else:
					str_list+="."
				if col==9:
					print str_list	
		
	def game_is_over(self):
		"""
		Returns True if al ten ships have been sunk.
		Oterwise False
		"""
		return self.number_of_ships_sank == 10
		
	def get_ocean(self):
		"""
		returns the dictionary of ships	
		"""
		return self.ships	
		
	def place_battle_ship_randomly(self):
		"""
		This will place a battle ship randomly.
		"""	
		is_ok=False
		while is_ok==False:
			position=random.randint(0,99)
			battle_ship=Battleship()
			row=position/10
			col=position%10
		
			is_ok=battle_ship.ok_to_place_ship_at((row,col),True,4,self)
			if is_ok:
				battle_ship.place_ship_at((row,col),True,4,self)
				#print "Placed battle ship at " + str(row)+","+str(col)
			else:
				is_ok=battle_ship.ok_to_place_ship_at((row,col),False,4,self)
				if is_ok:
					battle_ship.place_ship_at((row,col),False,4,self)
					#print "Placed battle ship at " + str(row)+","+str(col)
				else:
					# Not able to allocate this battle_ship, release memory
					battle_ship=None	
					
	def place_cruiser_randomly(self):
		"""
		This will place a cruiser ship randomly.
		"""	
		is_ok=False
		while is_ok==False:
			position=random.randint(0,99)
			cruiser=Cruiser()
			row=position/10
			col=position%10
		
			is_ok=cruiser.ok_to_place_ship_at((row,col),True,3,self)
			if is_ok:
				cruiser.place_ship_at((row,col),True,3,self)
				#print "Placed cruiser ship at " + str(row)+","+str(col)
			else:
				is_ok=cruiser.ok_to_place_ship_at((row,col),False,3,self)
				if is_ok:
					cruiser.place_ship_at((row,col),False,3,self)
					#print "Placed cruiser ship at " + str(row)+","+str(col)	
				else:
					# not able to allocate this cruiser, release memory
					cruiser=None	
					
	def place_destroyer_randomly(self):
		"""
		This will place a destroyer ship randomly.
		"""	
		is_ok=False
		while is_ok==False:
			position=random.randint(0,99)
			destroyer=Destroyer()
			row=position/10
			col=position%10
			length=destroyer.length
			is_ok=destroyer.ok_to_place_ship_at((row,col),True,length,self)
			if is_ok:
				destroyer.place_ship_at((row,col),True,length,self)
				#print "Placed destroyer ship at " + str(row)+","+str(col)
			else:
				is_ok=destroyer.ok_to_place_ship_at((row,col),False,length,self)
				if is_ok:
					destroyer.place_ship_at((row,col),False,length,self)
					#print "Placed destroyer ship at " + str(row)+","+str(col)
				else:
					# not able to allocate this destroyer, release memory
					destroyer=None									

	def place_submarine_randomly(self):
		"""
		This will place a submarine ship randomly.
		"""	
		is_ok=False
		while is_ok==False:
			position=random.randint(0,99)
			submarine=Submarine()
			row=position/10
			col=position%10
			length=submarine.length
			is_ok=submarine.ok_to_place_ship_at((row,col),True,length,self)
			if is_ok:
				submarine.place_ship_at((row,col),True,length,self)
				#print "Placed submarine at " + str(row)+","+str(col)
			else:
				is_ok=submarine.ok_to_place_ship_at((row,col),False,length,self)
				if is_ok:
					submarine.place_ship_at((row,col),False,length,self)
					#print "Placed submarine at " + str(row)+","+str(col)
				else:
					# not able to allocate this submarine, release memory
					submarine=None												
		
	def place_all_ships_randomly(self):
		"""
		create all ten ships and place them randomly on the ocean. 
		Place larger ships before smaller ones.
		"""	
		# place 1 battle ship.
		self.place_battle_ship_randomly()
		
		# place 2 Cruiser.
		i=0
		while i < 2:
			self.place_cruiser_randomly()
			i+=1
			
		# place 3 destroyer	
		i=0
		while i < 3:
			self.place_destroyer_randomly()
			i+=1
			
		
		# place 4 submarine
		i=0
		while i < 4:
			self.place_submarine_randomly()
			i+=1
			
		#print "place_all_ships_randomly"

class BattleshipGame:	
	"""
	This is the "main" class, containing the main method. 
	Activities : 
	1.Set up the game.
	2.Accept shots from the user.
	3.Display the result.
	4.Print final score.
	5.Ask user if s/he wants to play again.
	"""
	def main(self):
		ocean=Ocean()
		#ocean.place_all_ships_randomly()
		print "Computer places the ships randomly. Try to find those ships."
		user_turn=True
		while user_turn==True:
			try:		
				called_row = int(raw_input("Call a row [0 - 9]:"))
				called_col = int(raw_input("Call a col [0 - 9]:"))
				ocean.shoot_at((called_row,called_col))
				ocean.__print__()
				if ocean.game_is_over():
					shots = ocean.get_shots_fired()
					if shots < 31:
						print "Outstanding! Game over. Number of shots made : " + str(shots)
						break
					else:
						print "Game over. Number of shots made : " + str(shots)	
						break
				question = "Would you like to continue? (y/Y or n/N): "
				choice = raw_input(question).upper()					
				while choice != 'Y' and choice !='N':					
					choice = raw_input("Continue(Y/N)?").upper()    								
				user_turn = choice == 'Y'				
			except ValueError:
				print "Please enter a number [0-9]"	
		
		
		
		
if __name__ == '__main__':
	game=BattleshipGame()
	game.main()		
