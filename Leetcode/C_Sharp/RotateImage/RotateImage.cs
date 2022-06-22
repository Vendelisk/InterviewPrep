using System;

namespace RotateImage
{
    class Program
    {
        static void Main(string[] args)
        {
            // Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
            // Output: [[7,4,1],[8,5,2],[9,6,3]]

            // Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
            // Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

            int[][] matrix = new int[3][];
            matrix[0] = new int[] { 1, 2, 3 };
            matrix[1] = new int[] { 4, 5, 6 };
            matrix[2] = new int[] { 7, 8, 9 };
            // matrix[3] = new int[] { 15, 14, 12, 16 };
            Program instance = new Program();

            // Console.WriteLine(matrix[0, 1]); // 2 -> Row, Col
            instance.PrintMatrix(matrix);
            Console.WriteLine();
            instance.Rotate(matrix);
            instance.PrintMatrix(matrix);
        }

        public void Rotate(int[][] matrix)
        {
            int inner = 0;
            int size = matrix.Length - 1;
            while (inner < matrix.Length / 2)
            {
                int shift = 0;
                while (shift < size)
                {
                    // Console.WriteLine("size: " + size + " inner: " + inner + " shift: " + shift);
                    Swap(matrix, 0 + inner, shift + inner, shift + inner, size + inner); // 1, 1, 1, 1
                    // Console.WriteLine("2nd: " + (size - shift - inner) + " " + (inner) + " " + (size + inner) + " " + (size - shift - inner));
                    Swap(matrix, size - shift + inner, 0 + inner, size + inner, size - shift + inner); // 1, 1, 1, 1
                    Swap(matrix, 0 + inner, shift + inner, size + inner, size - shift + inner); // 1, 1, 1, 1
                    ++shift;
                }
                ++inner;
                size -= 2;
            }
        }

        public void Swap(int[][] matrix, int r1, int c1, int r2, int c2)
        {
            // Console.WriteLine("Swapping " + matrix[r1][c1] + " with " + matrix[r2][c2]);
            int temp = matrix[r1][c1];
            matrix[r1][c1] = matrix[r2][c2];
            matrix[r2][c2] = temp;
        }

        public void PrintMatrix(int[][] matrix)
        {
            foreach (int[] arr in matrix)
            {
                foreach (int num in arr)
                {
                    Console.Write(num + " ");
                }
                Console.WriteLine();
            }
        }
    }
}
