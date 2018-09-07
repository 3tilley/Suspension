from alphabet import count_vowels, charlotte

alphabet = map(chr, range(65, 91))

def test_count_all_vowels():
    assert count_vowels(alphabet) == 5

def test_count_vowels():
    assert count_vowels(alphabet[:12]) == 3

def test_charlotte():
    expected_output = "charlotte"
    assert charlotte(alphabet) == 8