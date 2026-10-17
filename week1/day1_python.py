#problem 1
def find_duplicates(nums : list):
    duplicates = set()
    seen = set()

    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return duplicates

print(find_duplicates([1,2,2,3,4,5,6,6,7,7,6,3,7,8,9,11]))

# problem 2
def first_non_recurring_character(s):
    for char in s:
        if s.count(char) == 1:
            return char
  
    return None

print(first_non_recurring_character("aasccdddeed"))

# PROBLEM 3
def word_frequency(words):
    frequency = {}
    text = words.lower().split()

    for char in text:
        frequency[char] = frequency.get(char,0)+1

    return frequency
words = "a e b b b g t p o g i c b m i l o g"
print(word_frequency(words))

# problem 4
def is_anagram(a,b: str):
    a = a.lower()
    b = b.lower()

    if len(a) != len(b):
        return False

    char_count = {}

    for char in a:
        char_count[char] = char_count.get(char, 0) + 1

    for char in b:
        if char not in char_count:
            return False

        char_count[char] -= 1

        if char_count[char] < 0:
            return False

    return True
print(is_anagram("Listen", "Silent"))