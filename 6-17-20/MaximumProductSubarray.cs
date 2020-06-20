// https://leetcode.com/problems/maximum-product-subarray/


using System;

public class Test
{
	public static void Main()
	{
		int[] nums = {0, 0, 2, 10, 0};
    Console.WriteLine(largestProductLinear(nums));
	}
  
  public static int largestProductBruteForce(int[] nums) {
    if (nums == null) return 0;
    if (nums.Length == 1) return nums[0];
    
    int max = nums[0];
    
    for (int i = 0; i < nums.Length; i++) {
      int[] numsSubArray = new int[nums.Length - i];
      Array.Copy(nums, i, numsSubArray, 0, nums.Length - i);
      int currMax = Int32.MinValue;
      foreach (int val in numsSubArray) {
        if (currMax == Int32.MinValue) currMax = val;
        else currMax *= val;
        if (currMax > max) max = currMax;
      }
    }
    
    return max;
  }
  
  public static int largestProductLinear(int[] nums) {
      if (nums == null) return 0;
      
      int max = nums[0];
      int currMax = Int32.MinValue;
      bool negative = false;
      int negativeVal = 1;
      
      foreach (int val in nums) {
        if (val == 0) {
          negative = false;
          negativeVal = 1;
          currMax = Int32.MinValue;
          if (0 > max) max = 0;
          continue;
        } 
        
        if (currMax == Int32.MinValue) currMax = val;
        else currMax *= val;
        
        if (currMax/negativeVal > max) max = currMax/negativeVal;
        if (currMax > max) max = currMax;
        
        if (val < 0 && !negative) {
          negativeVal = currMax;
          negative = true;
        }
      }
      return max;
  }
}

// if it's all positive (non-zero), whole array
// if it is zero
// negative, it can overturned



//[-2, -3, -6, -5, -2, -10, -5000] 
//[0, 0, 2, 10, 0]
//Input: [2,3,-2,4]
//beginningPointer
//endPointer
//currProduct

//Input: [-2,-1,5]
//Output: 10

//Input: [-50]
//Output: -50