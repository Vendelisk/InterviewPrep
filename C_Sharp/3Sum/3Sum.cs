using System;
using System.Collections.Generic;

/*
Given an integer array nums, return all the triplets 
[nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
WHY IS [0, 1, -1] NOT AN ANSWER? (2,3,5) vs (1,2,3)???

Constraints:
0 <= nums.length <= 3000
-105 <= nums[i] <= 105
*/

public class Program
{
    public static void Main()
    {
        int[] test = new int[] { -1, 0, 1, 2, -1, -4 };
        Program instance = new Program();
        PrintNestedIList(instance.ThreeSum(test));
    }

    public IList<IList<int>> ThreeSum(int[] nums)
    {
        IList<IList<int>> zeroSums = new List<IList<int>>();
        if (nums.Length < 3) return zeroSums;

        for (int i = 0; i < nums.Length - 1; ++i)
        {
            for (int j = i + 1, k = i + 1; k < nums.Length; ++k)
            {
                if (i == j || i == k || j == k)
                    continue;

                if (nums[i] + nums[j] + nums[k] == 0)
                {
                    IList<int> ans = new List<int>();
                    ans.Add(nums[i]);
                    ans.Add(nums[j]);
                    ans.Add(nums[k]);
                    zeroSums.Add(ans);
                }
            }
        }
        return zeroSums;
    }

    public static void PrintNestedIList(IList<IList<int>> list)
    {
        for (int i = 0; i < list.Count; ++i)
        {
            IList<int> inner = list[i];
            for (int j = 0; j < inner.Count; ++j)
            {
                Console.Write(inner[j] + " ");
            }
            Console.WriteLine();
        }
    }
}