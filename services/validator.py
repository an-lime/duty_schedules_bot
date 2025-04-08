def validate_pair(pairs_str: str) -> dict[int, str]:
    pairs = pairs_str.replace('\n', '').split(',')
    pairs_dict = {}
    for idx, pair in enumerate(pairs):
        pairs_dict[idx + 1] = pair

    return pairs_dict
