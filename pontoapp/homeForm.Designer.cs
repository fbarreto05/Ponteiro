namespace pontoapp
{
    partial class homeForm
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(homeForm));
            logoPIC = new PictureBox();
            titleLBL = new Label();
            loginLBL = new Label();
            senhaLBL = new Label();
            loginTXT = new TextBox();
            senhaTXT = new TextBox();
            baterBT = new Button();
            panel1 = new Panel();
            panel2 = new Panel();
            ppllistSPLT = new Splitter();
            ppllistTXT = new Label();
            name1LBL = new Label();
            name2LBL = new Label();
            name3LBL = new Label();
            name4LBL = new Label();
            name5LBL = new Label();
            name6LBL = new Label();
            name7LBL = new Label();
            name8LBL = new Label();
            name9LBL = new Label();
            name10LBL = new Label();
            state1LBL = new Label();
            state2LBL = new Label();
            state3LBL = new Label();
            state4LBL = new Label();
            state5LBL = new Label();
            state6LBL = new Label();
            state7LBL = new Label();
            state8LBL = new Label();
            state9LBL = new Label();
            state10LBL = new Label();
            profilesPAN = new Panel();
            state13LBL = new Label();
            name13LBL = new Label();
            state12LBL = new Label();
            name12LBL = new Label();
            state11LBL = new Label();
            name11LBL = new Label();
            ((System.ComponentModel.ISupportInitialize)logoPIC).BeginInit();
            panel1.SuspendLayout();
            panel2.SuspendLayout();
            profilesPAN.SuspendLayout();
            SuspendLayout();
            // 
            // logoPIC
            // 
            logoPIC.Image = (Image)resources.GetObject("logoPIC.Image");
            logoPIC.Location = new Point(12, 3);
            logoPIC.Name = "logoPIC";
            logoPIC.Size = new Size(85, 83);
            logoPIC.SizeMode = PictureBoxSizeMode.StretchImage;
            logoPIC.TabIndex = 0;
            logoPIC.TabStop = false;
            // 
            // titleLBL
            // 
            titleLBL.AutoSize = true;
            titleLBL.Location = new Point(30, 89);
            titleLBL.Name = "titleLBL";
            titleLBL.Size = new Size(46, 15);
            titleLBL.TabIndex = 1;
            titleLBL.Text = "PONTO";
            // 
            // loginLBL
            // 
            loginLBL.AutoSize = true;
            loginLBL.Location = new Point(16, 19);
            loginLBL.Name = "loginLBL";
            loginLBL.Size = new Size(45, 15);
            loginLBL.TabIndex = 2;
            loginLBL.Text = "NOME:";
            // 
            // senhaLBL
            // 
            senhaLBL.AutoSize = true;
            senhaLBL.Location = new Point(16, 54);
            senhaLBL.Name = "senhaLBL";
            senhaLBL.Size = new Size(48, 15);
            senhaLBL.TabIndex = 3;
            senhaLBL.Text = "SENHA:";
            // 
            // loginTXT
            // 
            loginTXT.Location = new Point(64, 16);
            loginTXT.Name = "loginTXT";
            loginTXT.Size = new Size(141, 23);
            loginTXT.TabIndex = 4;
            // 
            // senhaTXT
            // 
            senhaTXT.Location = new Point(64, 51);
            senhaTXT.Name = "senhaTXT";
            senhaTXT.Size = new Size(141, 23);
            senhaTXT.TabIndex = 5;
            // 
            // baterBT
            // 
            baterBT.Location = new Point(88, 228);
            baterBT.Name = "baterBT";
            baterBT.Size = new Size(85, 33);
            baterBT.TabIndex = 6;
            baterBT.Text = "BATER";
            baterBT.UseVisualStyleBackColor = true;
            baterBT.Click += baterBT_Click;
            // 
            // panel1
            // 
            panel1.Controls.Add(logoPIC);
            panel1.Controls.Add(titleLBL);
            panel1.Location = new Point(76, 12);
            panel1.Name = "panel1";
            panel1.Size = new Size(112, 111);
            panel1.TabIndex = 7;
            // 
            // panel2
            // 
            panel2.Controls.Add(senhaTXT);
            panel2.Controls.Add(loginLBL);
            panel2.Controls.Add(senhaLBL);
            panel2.Controls.Add(loginTXT);
            panel2.Location = new Point(12, 129);
            panel2.Name = "panel2";
            panel2.Size = new Size(222, 93);
            panel2.TabIndex = 8;
            // 
            // ppllistSPLT
            // 
            ppllistSPLT.BackColor = SystemColors.ButtonShadow;
            ppllistSPLT.BorderStyle = BorderStyle.FixedSingle;
            ppllistSPLT.Dock = DockStyle.Right;
            ppllistSPLT.Location = new Point(252, 0);
            ppllistSPLT.Name = "ppllistSPLT";
            ppllistSPLT.Size = new Size(287, 280);
            ppllistSPLT.TabIndex = 9;
            ppllistSPLT.TabStop = false;
            // 
            // ppllistTXT
            // 
            ppllistTXT.AutoSize = true;
            ppllistTXT.BackColor = SystemColors.ButtonShadow;
            ppllistTXT.Location = new Point(0, 0);
            ppllistTXT.Name = "ppllistTXT";
            ppllistTXT.Size = new Size(38, 15);
            ppllistTXT.TabIndex = 2;
            ppllistTXT.Text = "LISTA:";
            // 
            // name1LBL
            // 
            name1LBL.AutoSize = true;
            name1LBL.BackColor = SystemColors.ButtonShadow;
            name1LBL.BorderStyle = BorderStyle.FixedSingle;
            name1LBL.Location = new Point(60, 30);
            name1LBL.Name = "name1LBL";
            name1LBL.Size = new Size(2, 17);
            name1LBL.TabIndex = 6;
            // 
            // name2LBL
            // 
            name2LBL.AutoSize = true;
            name2LBL.BackColor = SystemColors.ButtonShadow;
            name2LBL.BorderStyle = BorderStyle.FixedSingle;
            name2LBL.Location = new Point(60, 47);
            name2LBL.Name = "name2LBL";
            name2LBL.Size = new Size(2, 17);
            name2LBL.TabIndex = 10;
            // 
            // name3LBL
            // 
            name3LBL.AutoSize = true;
            name3LBL.BackColor = SystemColors.ButtonShadow;
            name3LBL.BorderStyle = BorderStyle.FixedSingle;
            name3LBL.Location = new Point(60, 64);
            name3LBL.Name = "name3LBL";
            name3LBL.Size = new Size(2, 17);
            name3LBL.TabIndex = 11;
            // 
            // name4LBL
            // 
            name4LBL.AutoSize = true;
            name4LBL.BackColor = SystemColors.ButtonShadow;
            name4LBL.BorderStyle = BorderStyle.FixedSingle;
            name4LBL.Location = new Point(60, 81);
            name4LBL.Name = "name4LBL";
            name4LBL.Size = new Size(2, 17);
            name4LBL.TabIndex = 12;
            // 
            // name5LBL
            // 
            name5LBL.AutoSize = true;
            name5LBL.BackColor = SystemColors.ButtonShadow;
            name5LBL.BorderStyle = BorderStyle.FixedSingle;
            name5LBL.Location = new Point(60, 98);
            name5LBL.Name = "name5LBL";
            name5LBL.Size = new Size(2, 17);
            name5LBL.TabIndex = 13;
            // 
            // name6LBL
            // 
            name6LBL.AutoSize = true;
            name6LBL.BackColor = SystemColors.ButtonShadow;
            name6LBL.BorderStyle = BorderStyle.FixedSingle;
            name6LBL.Location = new Point(60, 115);
            name6LBL.Name = "name6LBL";
            name6LBL.Size = new Size(2, 17);
            name6LBL.TabIndex = 14;
            // 
            // name7LBL
            // 
            name7LBL.AutoSize = true;
            name7LBL.BackColor = SystemColors.ButtonShadow;
            name7LBL.BorderStyle = BorderStyle.FixedSingle;
            name7LBL.Location = new Point(60, 132);
            name7LBL.Name = "name7LBL";
            name7LBL.Size = new Size(2, 17);
            name7LBL.TabIndex = 15;
            // 
            // name8LBL
            // 
            name8LBL.AutoSize = true;
            name8LBL.BackColor = SystemColors.ButtonShadow;
            name8LBL.BorderStyle = BorderStyle.FixedSingle;
            name8LBL.Location = new Point(60, 149);
            name8LBL.Name = "name8LBL";
            name8LBL.Size = new Size(2, 17);
            name8LBL.TabIndex = 16;
            // 
            // name9LBL
            // 
            name9LBL.AutoSize = true;
            name9LBL.BackColor = SystemColors.ButtonShadow;
            name9LBL.BorderStyle = BorderStyle.FixedSingle;
            name9LBL.Location = new Point(60, 166);
            name9LBL.Name = "name9LBL";
            name9LBL.Size = new Size(2, 17);
            name9LBL.TabIndex = 17;
            // 
            // name10LBL
            // 
            name10LBL.AutoSize = true;
            name10LBL.BackColor = SystemColors.ButtonShadow;
            name10LBL.BorderStyle = BorderStyle.FixedSingle;
            name10LBL.Location = new Point(60, 183);
            name10LBL.Name = "name10LBL";
            name10LBL.Size = new Size(2, 17);
            name10LBL.TabIndex = 18;
            // 
            // state1LBL
            // 
            state1LBL.AutoSize = true;
            state1LBL.BackColor = SystemColors.ButtonShadow;
            state1LBL.BorderStyle = BorderStyle.FixedSingle;
            state1LBL.Location = new Point(3, 30);
            state1LBL.Name = "state1LBL";
            state1LBL.Size = new Size(2, 17);
            state1LBL.TabIndex = 20;
            // 
            // state2LBL
            // 
            state2LBL.AutoSize = true;
            state2LBL.BackColor = SystemColors.ButtonShadow;
            state2LBL.BorderStyle = BorderStyle.FixedSingle;
            state2LBL.Location = new Point(3, 47);
            state2LBL.Name = "state2LBL";
            state2LBL.Size = new Size(2, 17);
            state2LBL.TabIndex = 21;
            // 
            // state3LBL
            // 
            state3LBL.AutoSize = true;
            state3LBL.BackColor = SystemColors.ButtonShadow;
            state3LBL.BorderStyle = BorderStyle.FixedSingle;
            state3LBL.Location = new Point(3, 64);
            state3LBL.Name = "state3LBL";
            state3LBL.Size = new Size(2, 17);
            state3LBL.TabIndex = 22;
            // 
            // state4LBL
            // 
            state4LBL.AutoSize = true;
            state4LBL.BackColor = SystemColors.ButtonShadow;
            state4LBL.BorderStyle = BorderStyle.FixedSingle;
            state4LBL.Location = new Point(3, 81);
            state4LBL.Name = "state4LBL";
            state4LBL.Size = new Size(2, 17);
            state4LBL.TabIndex = 23;
            // 
            // state5LBL
            // 
            state5LBL.AutoSize = true;
            state5LBL.BackColor = SystemColors.ButtonShadow;
            state5LBL.BorderStyle = BorderStyle.FixedSingle;
            state5LBL.Location = new Point(3, 98);
            state5LBL.Name = "state5LBL";
            state5LBL.Size = new Size(2, 17);
            state5LBL.TabIndex = 24;
            // 
            // state6LBL
            // 
            state6LBL.AutoSize = true;
            state6LBL.BackColor = SystemColors.ButtonShadow;
            state6LBL.BorderStyle = BorderStyle.FixedSingle;
            state6LBL.Location = new Point(3, 115);
            state6LBL.Name = "state6LBL";
            state6LBL.Size = new Size(2, 17);
            state6LBL.TabIndex = 25;
            // 
            // state7LBL
            // 
            state7LBL.AutoSize = true;
            state7LBL.BackColor = SystemColors.ButtonShadow;
            state7LBL.BorderStyle = BorderStyle.FixedSingle;
            state7LBL.Location = new Point(3, 132);
            state7LBL.Name = "state7LBL";
            state7LBL.Size = new Size(2, 17);
            state7LBL.TabIndex = 26;
            // 
            // state8LBL
            // 
            state8LBL.AutoSize = true;
            state8LBL.BackColor = SystemColors.ButtonShadow;
            state8LBL.BorderStyle = BorderStyle.FixedSingle;
            state8LBL.Location = new Point(3, 149);
            state8LBL.Name = "state8LBL";
            state8LBL.Size = new Size(2, 17);
            state8LBL.TabIndex = 27;
            // 
            // state9LBL
            // 
            state9LBL.AutoSize = true;
            state9LBL.BackColor = SystemColors.ButtonShadow;
            state9LBL.BorderStyle = BorderStyle.FixedSingle;
            state9LBL.Location = new Point(3, 166);
            state9LBL.Name = "state9LBL";
            state9LBL.Size = new Size(2, 17);
            state9LBL.TabIndex = 28;
            // 
            // state10LBL
            // 
            state10LBL.AutoSize = true;
            state10LBL.BackColor = SystemColors.ButtonShadow;
            state10LBL.BorderStyle = BorderStyle.FixedSingle;
            state10LBL.Location = new Point(3, 183);
            state10LBL.Name = "state10LBL";
            state10LBL.Size = new Size(2, 17);
            state10LBL.TabIndex = 29;
            // 
            // profilesPAN
            // 
            profilesPAN.BackColor = SystemColors.ButtonShadow;
            profilesPAN.BorderStyle = BorderStyle.FixedSingle;
            profilesPAN.Controls.Add(state13LBL);
            profilesPAN.Controls.Add(ppllistTXT);
            profilesPAN.Controls.Add(name13LBL);
            profilesPAN.Controls.Add(state12LBL);
            profilesPAN.Controls.Add(name12LBL);
            profilesPAN.Controls.Add(state11LBL);
            profilesPAN.Controls.Add(name11LBL);
            profilesPAN.Controls.Add(state4LBL);
            profilesPAN.Controls.Add(state10LBL);
            profilesPAN.Controls.Add(name1LBL);
            profilesPAN.Controls.Add(state9LBL);
            profilesPAN.Controls.Add(name2LBL);
            profilesPAN.Controls.Add(state8LBL);
            profilesPAN.Controls.Add(name3LBL);
            profilesPAN.Controls.Add(state7LBL);
            profilesPAN.Controls.Add(name4LBL);
            profilesPAN.Controls.Add(state6LBL);
            profilesPAN.Controls.Add(name5LBL);
            profilesPAN.Controls.Add(state5LBL);
            profilesPAN.Controls.Add(name6LBL);
            profilesPAN.Controls.Add(name7LBL);
            profilesPAN.Controls.Add(state3LBL);
            profilesPAN.Controls.Add(name8LBL);
            profilesPAN.Controls.Add(state2LBL);
            profilesPAN.Controls.Add(name9LBL);
            profilesPAN.Controls.Add(state1LBL);
            profilesPAN.Controls.Add(name10LBL);
            profilesPAN.Location = new Point(271, 15);
            profilesPAN.Name = "profilesPAN";
            profilesPAN.Size = new Size(246, 253);
            profilesPAN.TabIndex = 30;
            // 
            // state13LBL
            // 
            state13LBL.AutoSize = true;
            state13LBL.BackColor = SystemColors.ButtonShadow;
            state13LBL.BorderStyle = BorderStyle.FixedSingle;
            state13LBL.Location = new Point(3, 232);
            state13LBL.Name = "state13LBL";
            state13LBL.Size = new Size(2, 17);
            state13LBL.TabIndex = 35;
            // 
            // name13LBL
            // 
            name13LBL.AutoSize = true;
            name13LBL.BackColor = SystemColors.ButtonShadow;
            name13LBL.BorderStyle = BorderStyle.FixedSingle;
            name13LBL.Location = new Point(60, 232);
            name13LBL.Name = "name13LBL";
            name13LBL.Size = new Size(2, 17);
            name13LBL.TabIndex = 34;
            // 
            // state12LBL
            // 
            state12LBL.AutoSize = true;
            state12LBL.BackColor = SystemColors.ButtonShadow;
            state12LBL.BorderStyle = BorderStyle.FixedSingle;
            state12LBL.Location = new Point(3, 217);
            state12LBL.Name = "state12LBL";
            state12LBL.Size = new Size(2, 17);
            state12LBL.TabIndex = 33;
            // 
            // name12LBL
            // 
            name12LBL.AutoSize = true;
            name12LBL.BackColor = SystemColors.ButtonShadow;
            name12LBL.BorderStyle = BorderStyle.FixedSingle;
            name12LBL.Location = new Point(60, 217);
            name12LBL.Name = "name12LBL";
            name12LBL.Size = new Size(2, 17);
            name12LBL.TabIndex = 32;
            // 
            // state11LBL
            // 
            state11LBL.AutoSize = true;
            state11LBL.BackColor = SystemColors.ButtonShadow;
            state11LBL.BorderStyle = BorderStyle.FixedSingle;
            state11LBL.Location = new Point(3, 200);
            state11LBL.Name = "state11LBL";
            state11LBL.Size = new Size(2, 17);
            state11LBL.TabIndex = 31;
            // 
            // name11LBL
            // 
            name11LBL.AutoSize = true;
            name11LBL.BackColor = SystemColors.ButtonShadow;
            name11LBL.BorderStyle = BorderStyle.FixedSingle;
            name11LBL.Location = new Point(60, 200);
            name11LBL.Name = "name11LBL";
            name11LBL.Size = new Size(2, 17);
            name11LBL.TabIndex = 30;
            // 
            // homeForm
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            BackColor = SystemColors.Control;
            ClientSize = new Size(539, 280);
            Controls.Add(profilesPAN);
            Controls.Add(ppllistSPLT);
            Controls.Add(panel2);
            Controls.Add(panel1);
            Controls.Add(baterBT);
            Name = "homeForm";
            Text = "pontoapp";
            ((System.ComponentModel.ISupportInitialize)logoPIC).EndInit();
            panel1.ResumeLayout(false);
            panel1.PerformLayout();
            panel2.ResumeLayout(false);
            panel2.PerformLayout();
            profilesPAN.ResumeLayout(false);
            profilesPAN.PerformLayout();
            ResumeLayout(false);
        }

        #endregion

        private PictureBox logoPIC;
        private Label titleLBL;
        private Label loginLBL;
        private Label senhaLBL;
        private TextBox loginTXT;
        private TextBox senhaTXT;
        private Button baterBT;
        private Panel panel1;
        private Panel panel2;
        private Splitter ppllistSPLT;
        private Label ppllistTXT;
        private Label name1LBL;
        private Label name2LBL;
        private Label name3LBL;
        private Label name4LBL;
        private Label name5LBL;
        private Label name6LBL;
        private Label name7LBL;
        private Label name8LBL;
        private Label name9LBL;
        private Label name10LBL;
        private Label name11LBL;
        private Label name12LBL;
        private Label name13LBL;
        private Label state1LBL;
        private Label state2LBL;
        private Label state3LBL;
        private Label state4LBL;
        private Label state5LBL;
        private Label state6LBL;
        private Label state7LBL;
        private Label state8LBL;
        private Label state9LBL;
        private Label state10LBL;
        private Label state11LBL;
        private Label state12LBL;
        private Label state13LBL;
        private Panel profilesPAN;
    }
}