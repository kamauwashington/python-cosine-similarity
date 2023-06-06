from cosine_similarity import cosine_similarity

def test_foo_bar () :
    assert cosine_similarity("This is a foo bar sentence","This sentence is similar to a foo bar sentence") ==  .86

def test_julie_jane () :
    assert cosine_similarity("Julie loves me more than Linda loves me","Jane likes me more than Julie loves me") == .82

def test_movies_work () :
    assert cosine_similarity("I love to go the movies","I love to go to work") == .72