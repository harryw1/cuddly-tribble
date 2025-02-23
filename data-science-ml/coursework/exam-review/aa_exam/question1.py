class HashtagsCreator:
    def __init__(self, list_of_terms):
        self.hashtags = []

        for term in list_of_terms:
            # Fix this section of code
            if "@" in term:
                self.hashtags.append(term.replace("@", "#"))
            elif "#" in term:
                self.hashtags.append(term)
            elif not "#" or "@" in term:
                self.hashtags.append("#" + term)
            else:
                self.hashtags.append("#" + term)

    def list_hashtags(self):
        for hashtag in self.hashtags:
            print(hashtag)


# Do not edit testing code
test_hashtags = HashtagsCreator(["@codecademy", "#python", "programming", "#strings"])
test_hashtags.list_hashtags()
