using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace prog_1
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Szász Gergő");

            int magassag, szelesseg;
            szelesseg = Console.WindowWidth;
            magassag = Console.WindowHeight;
            Console.SetCursorPosition(magassag / 2, szelesseg / 2);
            Console.WriteLine("Szász Gergő");
            Console.SetCursorPosition(0, magassag);

            string gyumi;
            int a;
            long ft;
            Console.WriteLine("Kérem a gyümölcs nevét!");
            gyumi =(Console.ReadLine());
            Console.Write("Kérem a gyümölcs mennyiségét!");
            a = int.Parse(Console.ReadLine());
            Console.Write("Kérem a gyümölcs egységárát!");
            ft = int.Parse(Console.ReadLine());

            Console.ReadLine();


        }
    }
}
