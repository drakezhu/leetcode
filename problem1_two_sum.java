class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        Map<Integer, Integer> map = new HashMap<>();
    
        // using hash map to store the array

        for (int i = 0; i < nums.length; i++) 
        {
        
            map.put(nums[i], i);
        }


    
        for (int i = 0; i < nums.length; i++) 
        {   
            // define the value of i's complement

            int complement = target - nums[i];

            // if the complement exists in the map and meanwhile it is not identical to i itself, we return the choosen value
            if (map.containsKey(complement) && map.get(complement) != i) {
                return new int[] { i, map.get(complement) };
            }
        }
    
        throw new IllegalArgumentException("No two sum solution");
    }
}