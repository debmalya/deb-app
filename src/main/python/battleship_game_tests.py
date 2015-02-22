import battleship_game as game
import random

test_ocean=game.Ocean()
def assertSame(actual,expected,message,test_name):
	
	if actual==expected:
		print " PASSED : " + test_name
	else: 
		print " FAILED : " + test_name + " " + message 
		test_ocean.__print__()		
		raise SystemExit
		
			
class ShipTest:
	"""
	To test each method of Ship
	"""
	
	test_ship=game.Ship()
	ship_type=test_ship.get_ship_type()
	assertSame("ship",ship_type,"Expected 'ship' but found "+ship_type,"Ship.get_ship_type()") 
	
	test_ship=game.Battleship()
	ship_type=test_ship.get_ship_type()
	assertSame("battleship",ship_type,"Expected 'battleship' but found "+ship_type,"Battleship.get_ship_type()") 
	
	test_ship=game.Cruiser()
	ship_type=test_ship.get_ship_type()
	assertSame("cruiser",ship_type,"Expected 'cruiser' but found "+ship_type,"Cruiser.get_ship_type()")
	
	test_ship=game.Destroyer()
	ship_type=test_ship.get_ship_type()
	assertSame("destroyer",ship_type,"Expected 'destroyer' but found "+ship_type,"Destroyer.get_ship_type()")
	
	test_ship=game.Submarine()
	ship_type=test_ship.get_ship_type()
	assertSame("submarine",ship_type,"Expected 'submarine' but found "+ship_type,"Submarine.get_ship_type()")  
	
class OceanTest:
	"""
	To test each method of Ocean.
	"""
	#test_ocean=game.Ocean()
	position=test_ocean.validate_position(0,0)
	assertSame(0,position,"Expected 0 but found "+str(position),"Ocean.validate_position()")
	
	position=test_ocean.validate_position(-1,0)
	assertSame(False,position,"Expected 'False' but found "+str(position),"Ocean.validate_position(-1,0)")
	
	position=test_ocean.validate_position(0,10)
	assertSame(False,position,"Expected 'False' but found "+str(position),"Ocean.validate_position(0,10)")
	
	position=test_ocean.validate_position(10,10)
	assertSame(False,position,"Expected 'False' but found "+str(position),"Ocean.validate_position(10,10)")	
	
	position=test_ocean.validate_position(-10,-10)
	assertSame(False,position,"Expected 'False' but found "+str(position),"Ocean.validate_position(-10,-10)")	
	
	position=test_ocean.validate_position(0,4)
	assertSame(4,position,"Expected 4 but found "+str(position),"Ocean.validate_position(0,4)")	
	
	position=test_ocean.validate_position(7,0)
	assertSame(70,position,"Expected 70 but found "+str(position),"Ocean.validate_position(7,0)")
	
	position=test_ocean.validate_position(1,7)
	assertSame(17,position,"Expected 17 but found "+str(position),"Ocean.validate_position(1,7)")	
	
	# to test the method ok_to_place_ship_at
	test_ship=game.Battleship()
	type=str(test_ship)
	assertSame('b',type,"Expected 'b' but found "+str(test_ship),"Ship.str()")
	
	
	
	
	
	# traversing every position on the ocean.
	position = 0
	while position < 100:
		row=position/10
		col=position%10
		is_ok=test_ocean.shoot_at((row,col))
		position+=1
	
	is_game_over=test_ocean.game_is_over()
	assertSame(True,is_game_over,"Expected game over and value 'True' but found"+str(is_game_over),"Ocean.game_is_over()")
	
	
	
	
	
	
	test_ocean.__print__()
	
	print " All tests completed successfully. Thanks"
	
	
	
ship_test=ShipTest()
ocean_test=OceanTest()	
