class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        k will be the length of the res

        it's also the most frequent amount

        I could get a count witha  dictionary

        or I could use an array with the index being the freq.

        list of lists, append the number to that listed,

        """

        res = []

        freq = [[] for i in range(len(nums) + 1)]

        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # 1:1
        # 2: 2
        # 3: 3

        for n, c in count.items():

            freq[c].append(n)
         

        for i in range(len(freq)-1, 0, -1):

            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res




        