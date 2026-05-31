class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # List of Lists
        # Loop through and compare sorted string with sorted first elements in sub-array
        # and if it matches then add to that sub-array, 
        # if not matched with any first sub-array string append as a new sub-array
        # TC: O(n * m) * O(log n) sorting
        # SC: O(n)

        # Hashmaps -> to store the sorted string as key 
        #               and then add the related strings into values array
        # At the end, combine all the hashmap value arrays as the result and return it.

        result = {}
        
        for i in range(len(strs)):
            key = "".join(sorted(strs[i]))
            if key in result:
                result[key].append(strs[i])
            else:
                result[key] = [strs[i]]

        return list(result.values())