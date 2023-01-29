core = []

with open("raw/core.txt", "r") as f:
	lines = f.readlines()
	for line in lines:
		line = line.strip()
		# skip over irrelevant lines
		if len(line) > 2:
			word = line.split(" ")[0]
			core.append(word)

new = []

with open("raw/new.txt", "r") as f:
	lines = f.readlines()
	for line in lines:
		word = line.strip()
		new.append(word)

new = [word for word in new if word not in core]

with open("core.txt", "w+") as f:
	f.write("\n".join(core))

with open("new.txt", "w+") as f:
	f.write("\n".join(new))
