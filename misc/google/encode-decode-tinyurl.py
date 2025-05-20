# Encode and Decode TinyURL
# TinyURL is a URL shortening service where you enter a URL such as https://lintcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

# Design the encode and decode methods for the TinyURL service. 
# There is no restriction on how your encode/decode algorithm should work. 
# You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

import random
class Solution:
    def __init__(self):
        self._map = dict()
        self.key = random.randint(0, 10000000)

    def encode(self, longUrl):
        while self.key in self._map: self.key = random.randint(0, 10000000)
        self._map[self.key] = longUrl
        print(self._map)
        return f"https://tinyurl.com/{self.key}"

    def decode(self, shortUrl):
        print(shortUrl[20:])
        return self._map[int(shortUrl[20:])]

sol = Solution()
print(sol.encode("https://lintcode.com/problems/design-tinyurl"))
# print(sol.decode("https://tinyurl.com/4e9iAk"))