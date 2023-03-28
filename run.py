def rungame(iterations):
	import gamelogic as gl
	for x in range(iterations):
		gameoutput = gl.player_run()

	return gameoutput
