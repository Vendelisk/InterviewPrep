using System;
using System.Linq;
using System.Collections.Generic;

namespace Combination_Sum
{
    class Program
    {
        static void Main(string[] args)
        {
            // find all combinations of "candidates" (with duplicates) that sum to target.
            // answers: [[2,2,2,2],[2,3,3],[3,5]]
            int[] candidates = { 2, 3, 5 };
            int target = 8;
            Program instance = new Program();
            ShowOutput(instance.CombinationSum(candidates, target));
        }

        // backtracking (naive solution that stops once solution is impossible)
        public IList<IList<int>> CombinationSum(int[] candidates, int target)
        {
            IList<IList<int>> ansList = new List<IList<int>>();
            Array.Sort(candidates);
            Array.Reverse(candidates);

            GetList(candidates, target, new List<int>(), ansList, target, 0);
            return ansList;
        }

        public void GetList(int[] nums, int target, IList<int> ans, IList<IList<int>> ansList, int fullTarget, int start)
        {
            IList<int> newAns = new List<int>();
            foreach (int num in ans)
            {
                newAns.Add(num);
            }

            if (nums.Length - 1 < 0 || target < 0) // overshot
                return;
            if (target == 0) // found answer
                ansList.Add(newAns);
            else
            {
                for (int i = start; i < nums.Length; ++i)
                {
                    newAns.Add(nums[i]);
                    GetList(nums, target - nums[i], newAns, ansList, fullTarget, i);
                    newAns.RemoveAt(newAns.Count() - 1);
                }
            }
        }

        public static void ShowOutput(IList<IList<int>> list)
        {
            int counter = 0;
            foreach (IList<int> sublist in list)
            {
                PrintList(sublist, "ansList at " + counter.ToString());
                ++counter;
            }
        }

        public static void PrintList(IList<int> list, string type)
        {
            Console.WriteLine(type + ":");
            foreach (int num in list)
            {
                Console.Write(num + " ");
            }
            Console.WriteLine();
        }
    }
}
