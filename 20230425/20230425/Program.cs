using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _20230425
{
    class Program
    {
        static int[] lista = new int[50];
        static List<int> oszthato = new List<int>();
        static List<int> nemoszthato = new List<int>();
        static Random rnd = new Random();

        static void Main(string[] args)
        {
            feltoltes();
            eldontes();
            Console.WriteLine("Nyomd le az entert!");
            Console.ReadLine();
        }
        static void feltoltes()
        {
            for (int i = 0; i < lista.Length; i++)
            {
                int fel = rnd.Next(0, 50);
                Console.Write($"{fel}, ");
                lista[i]=fel;
            }
         
        }

        static void eldontes()
        {
            Console.WriteLine();
            Console.WriteLine($"Oszthatóak 3-al és maradék 2: ");
            for (int i = 0; i < lista.Length; i++)
            {
                if (lista[i]%3==2)
                {
                    oszthato.Add(lista[i]);
                }
                else
                {
                    nemoszthato.Add(lista[i]);
                }
               
            }
            foreach (var item in oszthato)
            {
                Console.Write($"{item}, ");
            }
        }
       
    }

}
