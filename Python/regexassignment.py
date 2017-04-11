import re
def get_matching_words(regex):
    words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]
    return [word for word in words if re.search(regex, word)]
# Allwordsthatcontaina v
print get_matching_words(r'v')

# All words that contain a double s
# print get_matching_words (r'ss')

# All words that end with an e
# print get_matching_words (r'e$')

# All words that contain an b, any character, then another b
# print get_matching_words(r'b.b')

# All words that contain an b, at least one character, then another b
# print get_matching_words(r'b.*b')

# All words that contain an n, any number of characters (including zero), then another b
# print get_matching_words(r'n'), get_matching_words(r'.'), get_matching_words(r'b')

# All words that include all five vowels in order
# print get_matching_words(r'.*a.*e.*i.*o.*u')

# All words that only use the letters in regular expression (each letter can appear any number of times)
# print get_matching_words (r'^[regular expression]+$')

# All words that contain a double letter
# print get_matching_words (r'(.)\1')
