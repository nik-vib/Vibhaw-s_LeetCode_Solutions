class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        '''Step 1 -> The main idea behind it is that the minimum number to be found will always be in the range [1....n]
		             where 'n' is the length of list. So keep numbers in this range and mark others
					 (here we are marking them with (n+1) value) in the list provided.'''
        
        n = len(nums)
        for i in range(n):
            if nums[i] < 1 or nums[i] > n:
                nums[i] = n + 1
        
        '''Step 2 -> Ignoring the values greater than 'n', mark the indexes of the numbers in the range [1...n]
					 so as to ensure that this values are present. To mark the indexes, 
					 I am negating the value present at that index.'''
        
        for i in range(n):
            val = abs(nums[i])
            if val > n:
                continue
            val -= 1  #since the list is zero indexed,so every value will be at position val - 1
            
            if nums[val] > 0: 
                # For similar numbers, it will keep on fluctuating between negative and positive 
				# which is not our motive here.
                
                nums[val] = -1 * nums[val]
        
        '''Step 3 -> Return the first occurence of the non-negative numbers from the list'''
        
        for i in range(n):
            if nums[i] >=0:
                return (i + 1) # bcoz list is zero indexed
        
        '''Step 4 -> We will encounter this if no positives were found. This means that all the 
			         numbers are in the range [1....n]. So the missing positive number will be n+1'''
        
        return (n + 1)
