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
       static List<int> alacsonyak = new List<int>();
        class Tanulo
        {

            public String nev;
            public int kor, azonosito, magassag, suly;


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
            feladat4();
            feladat5();
            feladat6();
            feladat7();
            feladat8(); 
            Console.ReadLine();
            Console.WriteLine("Nyomd meg az entert!");
        }

        static void feladat2()
        {
            int szamlalo = 0;
            for (int i = 0; i < tanulok.Count; i++)
            {
                szamlalo = szamlalo + 1;
            }
            Console.WriteLine($"2 feladat: Ennyi tanuló van {szamlalo}");
        }

        static void feladat3()
        {

          
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
        static void feladat4()
        {
            for (int i = alacsonyak.Count - 1; i >= 0; i--)
            {
                int maxindex = i;
                for (int j = 0; j < i; j++)
                {
                    if (alacsonyak[j] > alacsonyak[maxindex])
                    {
                        maxindex = j;
                    }
                }
                int tmp = alacsonyak[i];
                alacsonyak[i] = alacsonyak[maxindex];
                alacsonyak[maxindex] = tmp;
            }

            Console.WriteLine("Feladat 4: A rendezett tanulók azonosítója:");
            foreach (var tanulo in alacsonyak)
            {
                Console.WriteLine(tanulo);
            }
        }
        static void feladat5()
        {
            Console.WriteLine("Feladat 5:");
           int osszeg = 0;
            for (int i = 0; i < tanulok.Count; i++)
            {
                osszeg = osszeg + tanulok[i].magassag;
            }
            Console.WriteLine($"Az osztály átlag magassága: {osszeg / tanulok.Count} cm.");
            
        }
        static void feladat6()
        {
            Console.WriteLine("Feladat 6:");
            Console.WriteLine("Kérem, adjon meg egy monogramot számot:");
            string bemonogram = Console.ReadLine();
            List<string> monogramok = new List<string>();
            for (int i = 1; i < beolvas.Length; i++)
            {
                string[] elemek = beolvas[i].Split(';');
                string nev = elemek[0];
                string[] nevReszek = nev.Split(' ');
                string monogram = "";
                foreach (string resz in nevReszek)
                {
                    monogram += resz[0];
                }
                monogramok.Add(monogram);
            }
            int szamlalo = 0;
            for (int i = 0; i < monogramok.Count; i++)
            {
                if (monogramok[i] == bemonogram)
                {
                    szamlalo = szamlalo + 1;
                }
            }
            Console.WriteLine($"Az osztály monogramai közül a te megadott monogramoddal {szamlalo} egyezést találtunk.");
        }
        static void feladat7()
        {
            Console.WriteLine("Feladat 7:");
            int legmagasabb = tanulok[0].magassag;
            string legmagasabb_neve = tanulok[0].nev;
            for (int i = 1; i < tanulok.Count; i++)
            {
                if (tanulok[i].magassag > legmagasabb)
                {
                    legmagasabb = tanulok[i].magassag;
                    legmagasabb_neve = tanulok[i].nev;
                }
            }
            Console.WriteLine($"A legmagasabb gyerek az osztályban a: {legmagasabb_neve} {legmagasabb} cm-vel. ");
        }

        static void feladat8()
        {
            Console.WriteLine("Feladat 8:");
            int i = 0;
            while (i < tanulok.Count && tanulok[i].suly / Math.Pow(tanulok[i].magassag, 2) <= 25)
            {
                i++;
            }

            if (i < tanulok.Count)
            {
                Console.WriteLine($"Az osztályban a {tanulok[i].azonosito} azonosítójú tanuló túlsúlyos, tömege {tanulok[i].suly}");
            }
            else
            {
                Console.WriteLine("Nincs túlsúlyos a osztályban.");
            }
        }
    }
}

