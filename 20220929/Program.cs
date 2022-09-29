using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _20220929
{
    class Program
    {
        static void Main(string[] args)
        {

            /*
             * 
             * 
             * operátorok:
             * aritmetikai: + - * /(egész osztás) %(maradék)
            logikai: !-tagadás &&-és ||-vagy
            beolvasás:
            1.mindig megelőzi egy kiírás , hogy mit szeretnénk 
            2.beolvasás-tárolás


            mindig szöveg típust olvasunk .
            ha kell átalakítjuk .
            tipus.Parse(Console.ReadLine())
            vagy
            Convert.TOtipus(Console.ReadLine())


             * */
            //feladat1();
            //feladat2(5,6,7);
            //feladat3();
            //feladat4();
            feladat5();
            // feladat6();
           // feladat7(12,25.378,"gumi kacsa");
            Console.WriteLine("Nyomd le az entert!");
            Console.ReadLine();
        }


         static void feladat1() {

            byte a = 28, b = 17, c = 6;
            Console.WriteLine($"{a}*{b}={a*b}");

            Console.WriteLine($"{b}/{c}={b / c}");
            Console.WriteLine($"{b}%{c}={b % c}");
        }

        static void feladat2(byte a, byte b, byte c)
        {


            Console.WriteLine($"{a} négyzete {a * a} ,köbe {a * a * a} ");
            Console.WriteLine($"{b} négyzete {Math.Pow(b,2)} ,köbe {Math.Pow(b,3)} ");
            Console.WriteLine($"{c} négyzetgyöke {Math.Pow(c, (double)1 / 2):0.00} ,köbgyöke {Math.Round(Math.Pow(c, (double)1 / 3),2)}");
            Console.WriteLine($"{c} négyzetgyöke {Math.Sqrt(c):0.00} ,köbgyöke {Math.Round(Math.Pow(c, (double)1 / 3), 2)}");


        }
    
    static void feladat3()
        {

            int d = 5;
            int r = d/2;
            int m = 15;
            Console.WriteLine($"A henger térfogata {Math.Pow(r,2)*Math.PI*m:0.00}");
            
        }

        static void feladat4()
        {
            int ora=15, perc=32, masodperc=24;
            Console.WriteLine($"{ora} óra {perc} perc {masodperc} mp ,{ora*60+perc*60+masodperc*60} felel meg");


        }

        static void feladat5()
        {

            int x = 796825;
            double ora1 = x / 60;
            double ora = x % 60;
            double perc = ora;
            Console.WriteLine($"{ora1}ora,{perc}perc");

            


        }

        static void feladat6()
        {
            double a = 5622 / 9;
           double b = a * 4;
            Console.WriteLine($"{Math.Pow(b,2)}");
        }

       static void feladat7(int a,double b,string c)
        {

            Console.WriteLine($"{a},{b},{c}");

        }


    }


}
