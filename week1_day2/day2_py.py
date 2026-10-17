from collections import Counter
# P4: ignore case and non-alphanumeric characters
# "A man, a plan, a canal: Panama" -> True
def is_palindrome(s : str) -> bool:
    cleaned = ""

    for char in s:
        if char.isalnum():
            cleaned += char.lower()

    return cleaned == cleaned[::-1]

print(is_palindrome("hELLO"))

# P5: return the most frequent word (use Counter)
def most_common_word(text: str) -> str:
    words = text.lower().split()
    counts = Counter(words)
    return counts.most_common(1)
print(most_common_word("python sql python python sql"))

# P6: group words that are anagrams of each other
# ["eat","tea","tan","ate","nat","bat"] -> [["eat","tea","ate"],["tan","nat"],["bat"]]
def group_anagrams(words: list) -> list:
    groups = {}

    for word in words:
        key = "".join(sorted(word))

        if key not in groups:
            groups[key] = []

        groups[key].append(word)

    return list(groups.values())

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

