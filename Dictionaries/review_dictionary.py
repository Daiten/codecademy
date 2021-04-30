songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]
zipped_songs = zip(songs, playcounts)

plays = {songs:playcounts for songs, playcounts in zipped_songs}
print(plays)
plays["Purple Haze"] = 1
plays["Respect"] = 94


sunday_feelings = {}
library = {"The Best Songs": plays, "Sunday Feelings": sunday_feelings}
print(library)