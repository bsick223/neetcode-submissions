class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        """

        get count with dictionary

        bucket sort

        the index is the quantity

        loop through the end to, the beginning

        until result array is the length of k

        """

        count = {}

        freq = [[] for i in range(len(nums) + 1)]
        # nums=[1,2,2,3,3,3]

        res =[]

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for n, c in count.items():
            freq[c].append(n)

        for i in range(len(freq) -1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
            

        # score 3

        # count = {}
        # freq = [[] for i in range(len(nums) + 1)]
        # # [[][][7]]

        # # for n in nums:
        # #     count[n] = 1 + count.get(n, 0)

        # for n in nums:
        #     count[n] = 1 + count.get(n, 0)


        # # 7 : 2

        # for n, c in count.items(): 
        #     print(c)
        #     freq[c].append(n)

        # res = []
        # for i in range(len(freq) - 1, 0, -1):
        #     for n in freq[i]:
        #         res.append(n)
        #         if len(res) == k:
        #             return res






        

































        # count = {}

        # freq = [[] for i in range(len(nums) + 1)]

        # for n in nums:
        #     count[n] = 1 + count.get(n, 0)

        # for n, c in count.items():
        #     freq[c].append(n)

        # res = []

        # for i in range(len(freq) - 1, 0, -1):

        #     for n in freq[i]:
        #         res.append(n)
        #         if len(res) == k:
        #             return res


        # count = {}
        # freq = [[] for i in range(len(nums) + 1)]

        # for n in nums:
        #     count[n] = 1 + count.get(n, 0)
        
        # for n, c in count.items():
        #     freq[c].append(n)

        # res = []

        # for i in range(len(freq) - 1, 0, -1):
        #     for n in freq[i]:
        #         res.append(n)
        #         if len(res) == k:
        #             return res

        
        