class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # dictionary for count

        # count 2D array

        # append to the res array

        count = {}

        freq = [[] for i in range(len(nums) + 1)]

        res = []

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for n, c in count.items():
            freq[c].append(n)

        for i in range(len(freq)-1, 0,-1):

            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res

        # O(n) time
        # O(1) space


























       

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

        
        