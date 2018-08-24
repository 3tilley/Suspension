from alphabet import count_vowels

alphabet = map(chr, range(65, 91))

def test_count_vowels():
    assert count_vowels(alphabet) == 5

def test_count_vowels():
    assert count_vowels(alphabet[:12]) == 3
