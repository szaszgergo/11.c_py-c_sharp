using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace mazakfeladat_beadando
{
    class Program
    {

        static string[] beolvas = File.ReadAllLines("diakok.txt");
        static List<Tanulo> tanulok = new List<Tanulo>();
     
        class Tanulo
        {
          
            public String nev;
            public int kor,azonosito,magassag , suly;

           
            public Tanulo(String line)
            {
                string[] elemek = line.Split(';');
                this.nev = elemek[0];
                this.kor = int.Parse(elemek[1]);
                this.azonosito = int.Parse(elemek[2]);
                this.magassag = int.Parse(elemek[3]);
                this.suly = int.Parse(elemek[4]);
              
            }

        }

        static void Main(string[] args)
        {
        

            for (int i = 1; i < beolvas.Length; i++)
            {
                tanulok.Add(new Tanulo(beolvas[i]));

        
            }

            feladat2();
            feladat3();
            Console.ReadLine();
            Console.WriteLine("NYomd");
        }

        static void feladat2()
        {
          int  szamlalo = 0;
            for (int i = 0; i < tanulok.Count; i++)
            {
                szamlalo = szamlalo + 1;
            }
            Console.WriteLine($"2 feladat: Ennyi tanuló van {szamlalo}");
        }

        static void feladat3()
        {
          
            List<int> alacsonyak = new List<int>();
            for (int i = 0; i < tanulok.Count; i++)
            {
                if (tanulok[i].magassag > 170)
                {
                    alacsonyak.Add(tanulok[i].azonosito);
                    
                }

            }
            Console.WriteLine("Feladat 3 : A 170cm-nél alacsonyabb gyerekek azonositoja");
            foreach (var item in alacsonyak)
            {
                Console.WriteLine(item);
            }
            
        }
    }
}

