from itertools import permutations as permut


def get_words(characters: str, digits: int) -> list:
    # create all possible word combinations
    permutations = permut(characters, digits)
    result = ["".join(word) for word in permutations]
    return result


def validate_words(prev_searches: dict, characters: str, length: int) -> str:
    path = r"words.txt"
    if len(characters) == 0 or len(characters) < length:
        return "You need more Cyrillic letters"
    # If a number that is more than the range is picked,
    # A default 3-letter one is chosen
    if length < 3 or length > 6:
        length = 3
    # check our previous queries before running the search,
    # to reduce response time
    if (characters, length) in prev_searches:
        return prev_searches[(characters, length)]
    else:  # no cached results for our query
        result = ""
        words = get_words(characters, length)
        try:
            with open(path, "r", encoding="utf-8") as txt_file:
                for word in txt_file:
                    word = word.strip()
                    if word in words:
                        result += f"{word} "
        except FileNotFoundError:
            result = "Missing words.txt, or path for words.txt is incorrect"
            return result
        # Add the query to the cache before returning it
        prev_searches[(characters, length)] = result
        return prev_searches[(characters, length)]
