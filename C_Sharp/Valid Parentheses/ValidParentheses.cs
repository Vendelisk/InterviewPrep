using System;
using System.Collections;

namespace Valid_Parentheses
{
    class Program
    {
        public static string s = "()[]{}";
        static void Main(string[] args)
        {
            Hashtable match = GetTable();
            // Queue opens = new Queue();
            Stack opens = new Stack();

            foreach (char c in s)
            {
                if (match.ContainsKey(c))
                {
                    if (opens.Count == 0 || (char)opens.Pop() != (char)match[c]) Console.WriteLine(false);
                }
                else
                {
                    opens.Push(c);
                }

            }

            if (opens.Count != 0) Console.WriteLine(false);
            else Console.WriteLine(true);
        }

        public static Hashtable GetTable()
        {
            Hashtable table = new Hashtable();
            table.Add('}', '{');
            table.Add(')', '(');
            table.Add(']', '[');
            return table;
        }
    }
}
