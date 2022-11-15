#make music
import music
#make a new score
s = music.new()
#make a new part
p = music.new('part')
#make a new note
n = music.new('note')
#set the pitch of the note
music.set('pitch', n, 60)
#set the duration of the note
music.set('duration', n, 1)
#add the note to the part
music.add(p, n)
#add the part to the score
music.add(s, p)
#play the score
music.play(s)

# Path: test-site/test.py