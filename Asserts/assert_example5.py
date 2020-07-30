"""
This is another example of assert
"""

def update_counts(letter,count_d):
    for c in letter:
        initial_count = count_d[c]
        if c in count_d:
            count_d[c] = initial_count+1

count_letter = {'a':3,'b':2}
letters1 = 'aaab'
update_counts(letters1,count_letter)
assert count_letter['a'] == 6
assert count_letter['b'] == 3