using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace kozmondasok
{
    class Program
    {
        static  string[] beolvas;
        
        static void Main(string[] args)
        {
              
  
            beolvasas();
            // feladat2();
            //  feladat3();
            // f4();
            // f5();
            f9();
            Console.WriteLine("Enter");
            Console.ReadLine();
           
        }

        static void beolvasas()
        {
            beolvas = File.ReadAllLines("kozmondasok.txt", Encoding.Default);
          //  for (int i = 0; i < beolvas.Length; i++)
           // {
             //   Console.WriteLine(beolvas[i]);
           // }


        }

        static void feladat2()
        {
            Console.WriteLine($"A közmondások száma : {beolvas.Length}");
        }

        static void feladat3()
        {
            Console.WriteLine("3.feladat:");
            for (int i = 0; i < beolvas.Length; i++)
            {
                if (beolvas[i].ToLower().Contains("malacz"))
                {
                    Console.WriteLine($"\t{beolvas[i]}");
                }
            }

            Console.WriteLine();

            foreach (var item in beolvas)
            {
                if (item.ToLower().Contains("malacz"))
                {
                    Console.WriteLine($"\t{item}");
                }
            }
        }

        static void f4()
        {
            Console.WriteLine("f4.");

            int db = 0;
            for (int i = 0; i < beolvas.Length; i++)
            {
                if (beolvas[i].ToLower().Contains("ló"))
                {
                    db  ++ ;
                }
                
            }
            Console.WriteLine($"Ennyi:{db} közmondás tartalmaza a ló szavat.");
        }
/*
        static void f5()
        {
            Console.WriteLine("f5.");
            for (int i = 0; i < beolvas.Length; i++)
            {
               int legnagyobb = beolvas[i].Length;
                Console.WriteLine(legnagyobb.Max());
            }
*/
            static void f9()
        {
            int uh_betuk = 0;
            for (int i = 0; i < beolvas.Length; i++)
            {
               
                if (beolvas[i].ToLower().Contains("ű"))
                {
                    uh_betuk++;
                }
            }
            Console.WriteLine(uh_betuk);
        }
          
        }
    }

