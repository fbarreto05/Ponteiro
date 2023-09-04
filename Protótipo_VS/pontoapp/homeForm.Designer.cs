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
            logoPAN = new Panel();
            inputPAN = new Panel();
            ppllistSPLT = new Splitter();
            ppllistTXT = new Label();
            profilesPAN = new Panel();
            namelistLISTB = new ListBox();
            cadastrarBT = new Button();
            apagarBT = new Button();
            botoesPAN = new Panel();
            ((System.ComponentModel.ISupportInitialize)logoPIC).BeginInit();
            logoPAN.SuspendLayout();
            inputPAN.SuspendLayout();
            profilesPAN.SuspendLayout();
            botoesPAN.SuspendLayout();
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
            loginTXT.Size = new Size(164, 23);
            loginTXT.TabIndex = 4;
            // 
            // senhaTXT
            // 
            senhaTXT.Location = new Point(64, 51);
            senhaTXT.Name = "senhaTXT";
            senhaTXT.PasswordChar = '*';
            senhaTXT.Size = new Size(164, 23);
            senhaTXT.TabIndex = 5;
            // 
            // baterBT
            // 
            baterBT.Location = new Point(73, 1);
            baterBT.Name = "baterBT";
            baterBT.Size = new Size(85, 33);
            baterBT.TabIndex = 6;
            baterBT.Text = "BATER";
            baterBT.UseVisualStyleBackColor = true;
            baterBT.Click += baterBT_Click;
            // 
            // logoPAN
            // 
            logoPAN.Controls.Add(logoPIC);
            logoPAN.Controls.Add(titleLBL);
            logoPAN.Location = new Point(76, 12);
            logoPAN.Name = "logoPAN";
            logoPAN.Size = new Size(112, 111);
            logoPAN.TabIndex = 7;
            // 
            // inputPAN
            // 
            inputPAN.Controls.Add(senhaTXT);
            inputPAN.Controls.Add(loginLBL);
            inputPAN.Controls.Add(senhaLBL);
            inputPAN.Controls.Add(loginTXT);
            inputPAN.Location = new Point(3, 121);
            inputPAN.Name = "inputPAN";
            inputPAN.Size = new Size(231, 83);
            inputPAN.TabIndex = 8;
            // 
            // ppllistSPLT
            // 
            ppllistSPLT.BackColor = SystemColors.ButtonShadow;
            ppllistSPLT.BorderStyle = BorderStyle.FixedSingle;
            ppllistSPLT.Dock = DockStyle.Right;
            ppllistSPLT.Location = new Point(252, 0);
            ppllistSPLT.Name = "ppllistSPLT";
            ppllistSPLT.Size = new Size(287, 287);
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
            // profilesPAN
            // 
            profilesPAN.BackColor = SystemColors.ButtonShadow;
            profilesPAN.BorderStyle = BorderStyle.FixedSingle;
            profilesPAN.Controls.Add(namelistLISTB);
            profilesPAN.Controls.Add(ppllistTXT);
            profilesPAN.Location = new Point(271, 15);
            profilesPAN.Name = "profilesPAN";
            profilesPAN.Size = new Size(246, 264);
            profilesPAN.TabIndex = 30;
            // 
            // namelistLISTB
            // 
            namelistLISTB.BackColor = SystemColors.ButtonShadow;
            namelistLISTB.FormattingEnabled = true;
            namelistLISTB.ItemHeight = 15;
            namelistLISTB.Location = new Point(-1, 19);
            namelistLISTB.Name = "namelistLISTB";
            namelistLISTB.Size = new Size(246, 244);
            namelistLISTB.TabIndex = 4;
            // 
            // cadastrarBT
            // 
            cadastrarBT.Location = new Point(13, 40);
            cadastrarBT.Name = "cadastrarBT";
            cadastrarBT.Size = new Size(85, 30);
            cadastrarBT.TabIndex = 31;
            cadastrarBT.Text = "CADASTRAR";
            cadastrarBT.UseVisualStyleBackColor = true;
            cadastrarBT.Click += cadastrarBT_Click;
            // 
            // apagarBT
            // 
            apagarBT.Location = new Point(134, 40);
            apagarBT.Name = "apagarBT";
            apagarBT.Size = new Size(85, 30);
            apagarBT.TabIndex = 32;
            apagarBT.Text = "APAGAR";
            apagarBT.UseVisualStyleBackColor = true;
            apagarBT.Click += apagarBT_Click;
            // 
            // botoesPAN
            // 
            botoesPAN.Controls.Add(apagarBT);
            botoesPAN.Controls.Add(baterBT);
            botoesPAN.Controls.Add(cadastrarBT);
            botoesPAN.Location = new Point(12, 209);
            botoesPAN.Name = "botoesPAN";
            botoesPAN.Size = new Size(222, 78);
            botoesPAN.TabIndex = 31;
            // 
            // homeForm
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            BackColor = SystemColors.Control;
            ClientSize = new Size(539, 287);
            Controls.Add(botoesPAN);
            Controls.Add(profilesPAN);
            Controls.Add(ppllistSPLT);
            Controls.Add(inputPAN);
            Controls.Add(logoPAN);
            Icon = (Icon)resources.GetObject("$this.Icon");
            Name = "homeForm";
            Text = "pontoapp";
            ((System.ComponentModel.ISupportInitialize)logoPIC).EndInit();
            logoPAN.ResumeLayout(false);
            logoPAN.PerformLayout();
            inputPAN.ResumeLayout(false);
            inputPAN.PerformLayout();
            profilesPAN.ResumeLayout(false);
            profilesPAN.PerformLayout();
            botoesPAN.ResumeLayout(false);
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
        private Panel logoPAN;
        private Panel inputPAN;
        private Splitter ppllistSPLT;
        private Label ppllistTXT;
        private Panel profilesPAN;
        private Button cadastrarBT;
        private Button apagarBT;
        private Panel botoesPAN;
        private ListBox namelistLISTB;
    }
}
