using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _20221201
{
    class Program
    {
        static Random rn = new Random();
        static void Main(string[] args)
        {
            // feladat1();
            //feladat2();
          //  feladat4();

            //feladat3();
            feladat5();
         Console.WriteLine("Nyomd le az entert!");
         Console.ReadLine();

        }
    

        static void feladat1()
        {
            int[] sorozat = new int[10];
            for (int i = 0; i < sorozat.Length; i++)
            {
                sorozat[i] = 22 + 4 * i;

            }

            foreach (var item in sorozat)
            {
                Console.Write($"{item} ");
            }
            Console.WriteLine();


            int[] sorozat1 = new int[10];
            sorozat1[0] = 22;
            for (int i = 1; i < sorozat1.Length; i++)
            {
                sorozat1[i] = sorozat1[i - 1] + 4;
            }
            foreach (var item in sorozat1)
            {
                Console.Write($"{item} ");
            }
            Console.WriteLine();
        }


        static void feladat2()
        {
            int[] dobokocka = new int[50];
            for (int i = 0; i < dobokocka.Length; i++)
            {
                int a = rn.Next(1, 6);
                Console.Write($"{a} ");
            }
            Console.WriteLine();
        }

        static void feladat3()
        {
            int[] kicsik = new int[10];
            for (int i = 0; i < kicsik.Length; i++)
            {
                int a = rn.Next(1, 50);
                Console.Write($"{a} ");
            }
            Console.WriteLine();
        }
       /* static void feladat4()
        {
            List<string> orszagok = new List<string>();
            for (int i = 1; i < 11; i++)
            {
                Console.WriteLine($"adj meg orszagokat");
                string a = Console.ReadLine();
                orszagok.Add(a);
                Console.WriteLine($"{orszagok} ");
            }
            
        }

        */

        static void feladat5()
        {
            int[] toto = new int[14];
            for (int i = 0; i < toto.Length; i++)
            {
                int a = rn.Next(1, 4);
                if (a==1)
                {

                    Console.Write($"1 ");
                }
                if (a==2)
                {
                    Console.Write($"2 ");
                }
                if (a==3)
                {
                    Console.Write($"x ");
                }
                foreach (var item in toto)
                {
                    Console.Write($"{item} ");
                }
               

            }
            Console.WriteLine();
        }




    }


}


