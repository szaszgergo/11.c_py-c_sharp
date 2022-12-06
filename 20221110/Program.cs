using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace _20221110
{
    class Program
    {
        static Random rn = new Random();
        static void Main(string[] args)
        {
            veletlenek();
            //negyzetek();
            //novekvo();
           
            Console.WriteLine("Nyomd le az entert!");
            Console.ReadLine();
        }

        static void novekvo()
        {
            for (int i = 1; i < 11; i++)
            {
                Console.WriteLine(i);
            }

            for (int i = 1; i < 11; i++)
            {
                File.AppendAllText("novekvo.txt,", Convert.ToString(i) + "\n");
            }


            FileStream fs = new FileStream("novekvo1.txt", FileMode.OpenOrCreate);
            StreamWriter sw = new StreamWriter(fs);

            for (int i = 1; i < 11; i++)
            {

                sw.WriteLine(i);

            }
            sw.Close();
            fs.Close();

        }



        static void negyzetek()
        {

            for (int a = 1; a <= 15; a++)
            {
                Console.WriteLine(Math.Pow(a,2));
            }
            for (int a = 1; a <= 15; a++)
            {
                File.AppendAllText("negyzetek.txt", Convert.ToString(Math.Pow(a,2))+"\n");
            }

        }


        static void veletlenek()
        {
           
           int a = rn.Next(0, 100);

            for (int x = 0; x < 11; x++)
            {
                Console.WriteLine(a);
            }
            for (int x = 1; x < 11; x++)
            {
                File.AppendAllText("vletlenek.txt", Convert.ToString(x) + "\n");

            }

        }
    }
}
