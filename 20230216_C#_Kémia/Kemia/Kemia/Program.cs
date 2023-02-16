using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace Kemia
{

    class Elem
    {
        public string ev, nev, vegyjel, felfedezo;
        public int rendszam;
        public Elem(string egysor)
        {
            string[] darabok = egysor.Split(';');
            ev = darabok[0];
            nev = darabok[1];
            vegyjel = darabok[2];
            rendszam = int.Parse(darabok[3]);
            felfedezo = darabok[4];

        }
    }
    class Program
    {

      static  Elem[] elemek;
       static List<Elem> elemek1 = new List<Elem>();
      static string vegyjel;
        static void Main(string[] args)
        {

            feladat2();
            feladat3();
            feladat4();
            feladat5();
            feladat6();
            Console.WriteLine("Enter");
            Console.ReadLine();

        }

        static void feladat2()
        {
            string[] beolvas = File.ReadAllLines("felfedezesek.txt", Encoding.UTF8);
            elemek = new Elem[beolvas.Length-1];

            for (int i = 0; i < elemek.Length; i++)
            {
                elemek[i] = new Elem(beolvas[i+1]);
            }

            //listában
            foreach (var item in File.ReadAllLines("felfedezesek.txt", Encoding.UTF8).Skip(1))
            {
                elemek1.Add(new Elem(item));
            }
            
        }


        static void feladat3()
        {
            Console.WriteLine($"3.feladat:Elemek száma: {elemek.Length}");
            Console.WriteLine($"{elemek1.Count}");
        }


        static void feladat4()
        {
            int okordb = 0, okordb1=0;
            foreach (var item in elemek)
            {
                if (item.ev=="Ókor")
                {
                    okordb++;
                }
            }
            Console.WriteLine($"4.feladat felfedezések száma az okorban: {okordb}");



            foreach (var item in elemek1)
            {
                if (item.ev == "Ókor")
                {
                    okordb1++;
                }
            }
            Console.WriteLine($"4.feladat felfedezések száma az okorban: {okordb1}");

        }


        static void feladat5()
        {
           
            
            bool helytelen = true;
            do
            {
                Console.Write("5f:Kérek egy vegyjelet!");
                vegyjel = Console.ReadLine();
                if (vegyjel.Length==1 && "qwertzuiopasdfghjklyxcvbnm".Contains(vegyjel.ToLower()))
                {
                    helytelen = false;
                }
                else if (vegyjel.Length==2 && "qwertzuiopasdfghjklyxcvbnm".Contains(Convert.ToString(vegyjel[0]).ToLower()) && "qwertzuiopasdfghjklyxcvbnm".Contains(Convert.ToString(vegyjel[1]).ToLower()))
                {
                    helytelen = false;
                }
                
      
            } while (helytelen);
        }


        static void feladat6()
        {
            bool vanbenne = false;
            Console.WriteLine("f6Keresés");
            foreach (var item in elemek)
            {
                if (item.vegyjel.ToLower()==vegyjel.ToLower())
                {
                    Console.WriteLine($"\t Az elem vegyjele: {item.vegyjel}");
                    Console.WriteLine($"\t Az elem neve: {item.nev}");
                    Console.WriteLine($"\t Az elem rendszáma: {item.rendszam}");
                    Console.WriteLine($"\t Az elem felfedezés éve: {item.ev}");
                    Console.WriteLine($"\t Az elem felfedezője: {item.felfedezo}");
                    vanbenne = true;
                    break;
                }
                
            }
            if (vanbenne == false)
            {
                Console.WriteLine("\t Nics ilyen elem az adatt forrásban");
            }
        }
    }
}
