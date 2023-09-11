using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Diagnostics;

namespace _20230911_1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button5_Click(object sender, EventArgs e)
        {

        }

        private void btn_Kilep_Click(object sender, EventArgs e)
        {
            if (MessageBox.Show("Ki szeretnél lépni?","Kilépés", MessageBoxButtons.YesNo,MessageBoxIcon.Question) == DialogResult.Yes)
            {
                this.Close();
            }
            else
            {

            }
            
        }

        private void btn_kek_Click(object sender, EventArgs e)
        {
            Color color = Color.FromArgb(45, 39, 226);
            lbl_hazi.ForeColor = color;
        }

        private void btn_Fekete_Click(object sender, EventArgs e)
        {
            Color color = Color.FromArgb(0, 0, 0);
            lbl_hazi.ForeColor = color;
        }

        private void btn_Kozepre_Click(object sender, EventArgs e)
        {

        }

        private void lbl_hazi_Click(object sender, EventArgs e)
        {

        }

        private void btn_nagybetus_Click(object sender, EventArgs e)
        {
            string txt1 = lbl_hazi.Text;
            lbl_hazi.Text = txt1.ToUpper();
        }

        private void btn_Kisbetus_Click(object sender, EventArgs e)
        {
            string txt1 = lbl_hazi.Text;
            lbl_hazi.Text = txt1.ToLower();
        }

        private void btn_Torol_Click(object sender, EventArgs e)
        {
            if (MessageBox.Show("Ki szeretnéd törölni?", "Törlés", MessageBoxButtons.YesNo, MessageBoxIcon.Question) == DialogResult.Yes)
            {
                
            }
            else
            {

            }
        }

        private void btn_kiir_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Házi feladat ", "Kiíratás");
        }
    }
}
