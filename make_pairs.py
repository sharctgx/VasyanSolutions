from collections import defaultdict
from itertools import combinations

def calculate_score(lhs, rhs):
    score = min(len(lhs["tags"] - rhs["tags"]),
                len(rhs["tags"] - lhs["tags"])
                lhs["tags"].intersection(rhs["tags"])
    )
    
    return score

def make_pairs_hash_table(photos):
    tag_photos_dict = defaultdict(list)

    for photo in photos :
        for tag in photo["tags"] :
            tag_photos_dict[tag].append(photo["num"])

    pair_score_dict = dict()  # only for photos, that have at least one tag in common

    for tag, photos in tag_photos_dict.items():
        for pair in combinations(photos, 2):
            pair_score_dict[pair] = calculate_score(photos[pair[0]], photos[pair[1]])

    return pair_score_dict
    