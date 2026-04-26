class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # input is an array     

        # process:  
        # use a dictionary to track the frequency
        # we could loop through original array and check the key value pairs and if it's ==k then append to res.

        # or we could use a list and index as it's count

        # for example:
            # [1,2,2,3,3,3]
            # [[],[1],[],[2,3],[],[],[]]

        # output is an array of k most frequent elements within the array


        freq = [[] for _ in range(len(nums) + 1)]
        res = []
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for num, cnt in count.items():
            freq[cnt].append(num)

        for i in range(len(freq) - 1, 0, -1):

            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
    