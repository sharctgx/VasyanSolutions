from make_pairs import make_pairs_hash_table
from slideshow_from_pairs import build_slideshow


def read_input():
    t = int(input())
    photos = list()
    for i in range(0, t):
        orient, num, tags = [x for x in input().split(' ', 2)]
        tags = tags.split()
        if orient == 'H':
            photos.append({"num" : i, "is_horizontal" : True, "tags" : set(tags)})
        else:
            photos.append({"num" : i, "is_horizontal" : False, "tags" : set(tags)})
    return photos


if __name__ == '__main__':
	photos = read_input()
	pairs_dict = make_pairs_hash_table(photos)
	print('AAAA')
	path = build_slideshow(pairs_dict)
	with open('out.txt', 'w') as f:
		f.write('\n'.join([str(i) for i in path]))