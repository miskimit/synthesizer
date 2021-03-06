from envelope import Envelope, example_envelopes

def song_settings(tracks):
	""" ALL OF THIS IS OPTIONAL!
	If you don't care, just ignore this file completely, and your
	composition will be written with default settings.

	Continue if you care:
	
	You should know how many tracks you have in your composition.
	An example case is portrayed below.

	# I have 3 tracks, I name them for convenience.
-->	pad = tracks[0]
-->	bass = tracks[1]
-->	lead = tracks[2]
	
	# I use a pre-defined envelope for my pad track.
-->	pad.envelope = Envelope(*example_envelopes["pulse"])
	
	# I use another pre-defined envelope for my bass track.
-->	bass.envelope = example_envelopes["longrelease"]

	# I want my bass to be slighlty louder. (0.5 is the default volume)
-->	bass.volume = 0.65

	# I make a custom envelope for my lead.
	# See "envelope.py" for details.
-->	lead.envelope = Envelope(1, 10, 0.8, 40, 200)
-->	lead.volume = 0.65

	# I set custom harmonics for my lead.
	# 1st harmonic has 0.65 relative volume.
	# 2nd harmonic has 0.25 relative volume.
	# 3rd harmonic has 0.10 relative volume. ...
	# (They don't have to add up to 1)
-->	lead.harmonics = [0.65, 0.25, 0.10, 0.005]

	# I want my lead to have echo
-->	lead.echo = True
-->	lead.echo_delay = 200
-->	lead.echo_volume = 0.8  # this is relative to its own volume.

	------------------------------------------------
		example_envelopes:
			"standard": 		(1, 10, 0.75, 20, 25)
			"mediumrelease":	(1, 10, 1, 10, 350)
			"longrelease":		(1, 10, 1, 10, 1100)
			"pulse": 			(1, 10, .45, 25, 25)
			"heavenly":			(1, 800, 1, 1, 1200)
			"drawnout":			(1, 3000, 0.3, 1000, 2600)
	------------------------------------------------
	"""

	################# YOUR CODE HERE ###################

	my_awesome_track = tracks[0]

	####################################################
