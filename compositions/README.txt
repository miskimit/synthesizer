///////////////////////////////////////////////////////////////////////////////
// HOW TO COMPOSE
// (I SWEAR IT'S SIMPLE)
//
// comment lines START WITH "//" and are ignored.
//
// write down 1 note per line.
// E#4 25   -->		play E#4 for 25 units of time.
// - 50		-->		rest for 50 units of time.
//
// ("units of time" is currently arbitrary)
// (you can just think of it as milliseconds)
//
// if your music has multiple instruments (tracks):
// you add the tracks one after the other,
// by separating them with a '+'
// make sure it is on a separate line, just like a note.
// +		-->		start a new track
//
// if you want to play with sounds effects,
// check "songsettings.py" before you run the program.
//
// that's all -- you are now ready to compose
///////////////////////////////////////////////////////////////////////////////


///////////////////////////////////////////////////////////////////////////////
// FURTHER DETAILS (which you don't have to know)
//
// heres a quick explanation about "units of time" for the curious.
// if you had a metronome and set it up for standard tempo (120bpm):
// 200 units of time would correspond to 1 "normal length" note. (1/4th)
// 800 units of time would correspond to 1 bar. (4 "normal length notes")
// 
// heres a slightly-less-quick explanation for the slighly-more-curious:
// 1 bar in 120bmp takes 2000ms in the real world. that makes 500ms per beat.
// in other words, 500ms for a Quarter note. but that sucks. 
// we (just me actually) want a universe where we can type 200 for a quarter note.
// a universe where 800 would mean "1 bar". and 200 would mean 1 quarter note.
// so here we are. you type 200, i multiply that by 2.5 and make a 500ms note.
// i know. i'll be applying for the Nobel.
// all you have to worry about is, 200 is how long 1 beat takes in standard tempo.
//
// virtually any music can be written using this format.
// only problem: it's impractical :D
// if you think this format sucks, you are correct.
// the next version will feature a rework as well as MIDI support (or something).
///////////////////////////////////////////////////////////////////////////////
