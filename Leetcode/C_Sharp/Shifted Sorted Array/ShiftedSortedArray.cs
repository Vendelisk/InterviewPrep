using System;

namespace Shifted_Sorted_Array
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] nums = { 7, 9, 1, 4, 6 };
            int target = 4;
            Program instance = new Program();
            Console.WriteLine(instance.Search(nums, target));
        }

        public int Search(int[] nums, int target)
        {
            int pivot = nums[0] < nums[nums.Length - 1] ? 0 : PivotSearch(0, nums.Length - 1, nums);
            if (pivot == 0) return BinarySearch(0, nums.Length - 1, target, nums);

            if (target < nums[pivot]) return -1;
            else if (nums[nums.Length - 1] < target) // number in lower half 
                return BinarySearch(0, nums[0..pivot].Length - 1, target, nums[0..pivot]);
            else if (nums[nums.Length - 1] > target)
            {// number in upper half
                int temp = BinarySearch(0, nums[pivot..(nums.Length)].Length - 1, target, nums[pivot..(nums.Length)]);
                return temp == -1 ? temp : temp + pivot;
            }
            else
                return nums.Length - 1;
        }

        public int BinarySearch(int first, int last, int goal, int[] nums)
        {
            int mid = first + (last - first) / 2;
            Console.WriteLine("Binary - first: " + first + "\tmid: " + mid + "\tlast: " + last);
            if (nums.Length == 1) return nums[0] == goal ? 0 : -1;
            else if (last < first) return -1;
            else if (first == mid && goal != nums[first]) return goal == nums[last] ? last : -1;
            else if (nums[mid] > goal) return BinarySearch(first, mid, goal, nums);
            else if (nums[mid] < goal) return BinarySearch(mid, last, goal, nums);
            else return mid;
        }

        public int PivotSearch(int first, int last, int[] nums)
        {
            int mid = first + (last - first) / 2;
            Console.WriteLine("Pivot - first: " + first + "\tmid: " + mid + "\tlast: " + last);
            if (mid == first) return mid == last ? mid : mid + 1;
            else if (nums[mid] > nums[last]) return PivotSearch(mid, last, nums);
            else return PivotSearch(first, mid, nums);
        }
    }
}
