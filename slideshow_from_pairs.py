def build_slideshow(pairs_dict):
	sorted_pairs = sorted(pairs_dict, key=lambda x: pairs_dict[x], reverse=True)
	sorted_pairs[:1000]
	path = list(sorted_pairs.pop(0))
	while True:
		to_forget = -1
		for pair in sorted_pairs:
			if path[0] in pair:
				to_forget = path[0]
				path = [get_other(path[0], pair)] + path
				sorted_pairs.remove(pair)
				break
			elif path[-1] in pair:
				to_forget = path[-1]
				path = path + [get_other(path[0], pair)]
				sorted_pairs.remove(pair)
				break
		else:
			break
		if to_forget != -1:
			sorted_pairs = [pair for pair in sorted_pairs if to_forget not in pair]
	tail = [pic for pair in sorted_pairs for pic in pair]
	path += tail
	# print(test_pairs)
	# print(sorted_pairs)
	# print(path)
	return path


def get_other(i, pair):
	if i == pair[0]:
		return pair[1]
	return pair[0]


if __name__ == '__main__':
	test_pairs = {(2, 5): 2, (2, 4): 3, (2, 1): 3, (1, 3): 1, (6, 7): 2}
	# path: 3 1 2 4 6 7 5
	build_slideshow(test_pairs)