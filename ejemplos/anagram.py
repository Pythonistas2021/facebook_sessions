def stringAnagram(dictionary, query):
    anagrams = 0
    query_int = []

    for i in range(len(query)):
        for j in range(len(dictionary)):
            if sorted(query[i]) == sorted(dictionary[j]):
                anagrams = anagrams + 1

        query_int.append(anagrams)
        anagrams = 0
    return query_int

print(stringAnagram(dictionary, query))
        
        

