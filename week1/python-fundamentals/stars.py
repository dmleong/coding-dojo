def draw_stars(num):
	for item in num:
		try: 
			item = int(item)
			print "*" * item
		except ValueError:
			letter = item[0:1]
			print letter.lower() * len(item)

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars(x)