def mergeAlternately(word1: str, word2: str) -> str:
        rst = []
        i = j = 0
        while i < len(word1) and j < len(word2):
            rst.append(word1[i])
            rst.append(word2[j])
            i += 1
            j += 1
        
        while i < len(word1):
            rst.append(word1[i])
            i += 1
        
        while j < len(word2):
            # rst.append(' ')
            rst.append(word2[j])
            j += 1
        
        return ''.join(rst)