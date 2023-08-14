using System.Runtime.Intrinsics.X86;
using System.Xml;

namespace pontoapp
{
    public partial class homeForm : Form
    {
        public homeForm()
        {
            InitializeComponent();
        }

        private void baterBT_Click(object sender, EventArgs e)
        {
            string senhaNome1 = senhaTXT.Text;
            string senhaNome2 = senhaTXT.Text;
            string senhaNome3 = senhaTXT.Text;
            string senhaNome4 = senhaTXT.Text;
            string senhaNome5 = senhaTXT.Text;
            string senhaNome6 = senhaTXT.Text;
            string senhaNome7 = senhaTXT.Text;
            string senhaNome8 = senhaTXT.Text;
            string senhaNome9 = senhaTXT.Text;
            string senhaNome10 = senhaTXT.Text;
            string senhaNome11 = senhaTXT.Text;
            string senhaNome12 = senhaTXT.Text;
            string senhaNome13 = senhaTXT.Text;

            if (name1LBL.Text == loginTXT.Text && senhaNome1 == senhaTXT.Text)
            {
                if (state1LBL.Text == "Inativo")
                {
                    state1LBL.Text = "Ativo";
                    MessageBox.Show(name1LBL.Text + " Entrou");
                }
                else
                {
                    state1LBL.Text = "Inativo";
                    MessageBox.Show(name1LBL.Text + " Saiu");
                }
            }
            else if (name1LBL.Text == "" && state1LBL.Text == "")
            {
                senhaNome1 = senhaTXT.Text;
                name1LBL.Text = loginTXT.Text;
                state1LBL.Text = "Ativo";
                MessageBox.Show("Usuário cadastrado com sucesso!");
            }
            else
            {
                if (name2LBL.Text == loginTXT.Text && senhaNome2 == senhaTXT.Text)
                {
                    if (state2LBL.Text == "Inativo")
                    {
                        state2LBL.Text = "Ativo";
                        MessageBox.Show(name2LBL.Text + " Entrou");
                    }
                    else
                    {
                        state2LBL.Text = "Inativo";
                        MessageBox.Show(name2LBL.Text + " Saiu");
                    }
                }
                else if (name2LBL.Text == "" && state2LBL.Text == "")
                {
                    senhaNome2 = senhaTXT.Text;
                    name2LBL.Text = loginTXT.Text;
                    state2LBL.Text = "Ativo";
                    MessageBox.Show("Usuário cadastrado com sucesso!");
                }
                else
                {
                    if (name3LBL.Text == loginTXT.Text && senhaNome3 == senhaTXT.Text)
                    {
                        if (state3LBL.Text == "Inativo")
                        {
                            state3LBL.Text = "Ativo";
                            MessageBox.Show(name3LBL.Text + " Entrou");
                        }
                        else
                        {
                            state3LBL.Text = "Inativo";
                            MessageBox.Show(name3LBL.Text + " Saiu");
                        }
                    }
                    else if (name3LBL.Text == "" && state3LBL.Text == "")
                    {
                        senhaNome3 = senhaTXT.Text;
                        name3LBL.Text = loginTXT.Text;
                        state3LBL.Text = "Ativo";
                        MessageBox.Show("Usuário cadastrado com sucesso!");
                    }
                    else
                    {
                        if (name4LBL.Text == loginTXT.Text && senhaNome4 == senhaTXT.Text)
                        {
                            if (state4LBL.Text == "Inativo")
                            {
                                state4LBL.Text = "Ativo";
                                MessageBox.Show(name4LBL.Text + " Entrou");
                            }
                            else
                            {
                                state4LBL.Text = "Inativo";
                                MessageBox.Show(name4LBL.Text + " Saiu");
                            }
                        }
                        else if (name4LBL.Text == "" && state4LBL.Text == "")
                        {
                            senhaNome4 = senhaTXT.Text;
                            name4LBL.Text = loginTXT.Text;
                            state4LBL.Text = "Ativo";
                            MessageBox.Show("Usuário cadastrado com sucesso!");
                        }
                        else
                        {
                            if (name5LBL.Text == loginTXT.Text && senhaNome5 == senhaTXT.Text)
                            {
                                if (state5LBL.Text == "Inativo")
                                {
                                    state5LBL.Text = "Ativo";
                                    MessageBox.Show(name5LBL.Text + " Entrou");
                                }
                                else
                                {
                                    state5LBL.Text = "Inativo";
                                    MessageBox.Show(name5LBL.Text + " Saiu");
                                }
                            }
                            else if (name5LBL.Text == "" && state5LBL.Text == "")
                            {
                                senhaNome5 = senhaTXT.Text;
                                name5LBL.Text = loginTXT.Text;
                                state5LBL.Text = "Ativo";
                                MessageBox.Show("Usuário cadastrado com sucesso!");
                            }
                            else
                            {
                                if (name6LBL.Text == loginTXT.Text && senhaNome6 == senhaTXT.Text)
                                {
                                    if (state6LBL.Text == "Inativo")
                                    {
                                        state6LBL.Text = "Ativo";
                                        MessageBox.Show(name6LBL.Text + " Entrou");
                                    }
                                    else
                                    {
                                        state6LBL.Text = "Inativo";
                                        MessageBox.Show(name6LBL.Text + " Saiu");
                                    }
                                }
                                else if (name6LBL.Text == "" && state6LBL.Text == "")
                                {
                                    senhaNome6 = senhaTXT.Text;
                                    name6LBL.Text = loginTXT.Text;
                                    state6LBL.Text = "Ativo";
                                    MessageBox.Show("Usuário cadastrado com sucesso!");
                                }
                                else
                                {
                                    if (name7LBL.Text == loginTXT.Text && senhaNome7 == senhaTXT.Text)
                                    {
                                        if (state7LBL.Text == "Inativo")
                                        {
                                            state7LBL.Text = "Ativo";
                                            MessageBox.Show(name7LBL.Text + " Entrou");
                                        }
                                        else
                                        {
                                            state7LBL.Text = "Inativo";
                                            MessageBox.Show(name7LBL.Text + " Saiu");
                                        }
                                    }
                                    else if (name7LBL.Text == "" && state7LBL.Text == "")
                                    {
                                        senhaNome7 = senhaTXT.Text;
                                        name7LBL.Text = loginTXT.Text;
                                        state7LBL.Text = "Ativo";
                                        MessageBox.Show("Usuário cadastrado com sucesso!");
                                    }
                                    else
                                    {
                                        if (name8LBL.Text == loginTXT.Text && senhaNome8 == senhaTXT.Text)
                                        {
                                            if (state8LBL.Text == "Inativo")
                                            {
                                                state8LBL.Text = "Ativo";
                                                MessageBox.Show(name8LBL.Text + " Entrou");
                                            }
                                            else
                                            {
                                                state8LBL.Text = "Inativo";
                                                MessageBox.Show(name4LBL.Text + " Saiu");
                                            }
                                        }
                                        else if (name8LBL.Text == "" && state8LBL.Text == "")
                                        {
                                            senhaNome8 = senhaTXT.Text;
                                            name8LBL.Text = loginTXT.Text;
                                            state8LBL.Text = "Ativo";
                                            MessageBox.Show("Usuário cadastrado com sucesso!");
                                        }
                                        else
                                        {
                                            if (name9LBL.Text == loginTXT.Text && senhaNome9 == senhaTXT.Text)
                                            {
                                                if (state9LBL.Text == "Inativo")
                                                {
                                                    state9LBL.Text = "Ativo";
                                                    MessageBox.Show(name9LBL.Text + " Entrou");
                                                }
                                                else
                                                {
                                                    state9LBL.Text = "Inativo";
                                                    MessageBox.Show(name9LBL.Text + " Saiu");
                                                }
                                            }
                                            else if (name9LBL.Text == "" && state9LBL.Text == "")
                                            {
                                                senhaNome9 = senhaTXT.Text;
                                                name9LBL.Text = loginTXT.Text;
                                                state9LBL.Text = "Ativo";
                                                MessageBox.Show("Usuário cadastrado com sucesso!");
                                            }
                                            else
                                            {
                                                if (name10LBL.Text == loginTXT.Text && senhaNome10 == senhaTXT.Text)
                                                {
                                                    if (state10LBL.Text == "Inativo")
                                                    {
                                                        state10LBL.Text = "Ativo";
                                                        MessageBox.Show(name10LBL.Text + " Entrou");
                                                    }
                                                    else
                                                    {
                                                        state10LBL.Text = "Inativo";
                                                        MessageBox.Show(name10LBL.Text + " Saiu");
                                                    }
                                                }
                                                else if (name10LBL.Text == "" && state10LBL.Text == "")
                                                {
                                                    senhaNome10 = senhaTXT.Text;
                                                    name10LBL.Text = loginTXT.Text;
                                                    state10LBL.Text = "Ativo";
                                                    MessageBox.Show("Usuário cadastrado com sucesso!");
                                                }
                                                else
                                                {
                                                    if (name11LBL.Text == loginTXT.Text && senhaNome11 == senhaTXT.Text)
                                                    {
                                                        if (state11LBL.Text == "Inativo")
                                                        {
                                                            state11LBL.Text = "Ativo";
                                                            MessageBox.Show(name11LBL.Text + " Entrou");
                                                        }
                                                        else
                                                        {
                                                            state11LBL.Text = "Inativo";
                                                            MessageBox.Show(name11LBL.Text + " Saiu");
                                                        }
                                                    }
                                                    else if (name11LBL.Text == "" && state11LBL.Text == "")
                                                    {
                                                        senhaNome11 = senhaTXT.Text;
                                                        name11LBL.Text = loginTXT.Text;
                                                        state11LBL.Text = "Ativo";
                                                        MessageBox.Show("Usuário cadastrado com sucesso!");
                                                    }
                                                    else
                                                    {
                                                        if (name12LBL.Text == loginTXT.Text && senhaNome12 == senhaTXT.Text)
                                                        {
                                                            if (state12LBL.Text == "Inativo")
                                                            {
                                                                state12LBL.Text = "Ativo";
                                                                MessageBox.Show(name12LBL.Text + " Entrou");
                                                            }
                                                            else
                                                            {
                                                                state12LBL.Text = "Inativo";
                                                                MessageBox.Show(name12LBL.Text + " Saiu");
                                                            }
                                                        }
                                                        else if (name12LBL.Text == "" && state12LBL.Text == "")
                                                        {
                                                            senhaNome12 = senhaTXT.Text;
                                                            name12LBL.Text = loginTXT.Text;
                                                            state12LBL.Text = "Ativo";
                                                            MessageBox.Show("Usuário cadastrado com sucesso!");
                                                        }
                                                        else
                                                        {
                                                            if (name13LBL.Text == loginTXT.Text && senhaNome13 == senhaTXT.Text)
                                                            {
                                                                if (state13LBL.Text == "Inativo")
                                                                {
                                                                    state13LBL.Text = "Ativo";
                                                                    MessageBox.Show(name13LBL.Text + " Entrou");
                                                                }
                                                                else
                                                                {
                                                                    state13LBL.Text = "Inativo";
                                                                    MessageBox.Show(name13LBL.Text + " Saiu");
                                                                }
                                                            }
                                                            else if (name13LBL.Text == "" && state13LBL.Text == "")
                                                            {
                                                                senhaNome13 = senhaTXT.Text;
                                                                name13LBL.Text = loginTXT.Text;
                                                                state13LBL.Text = "Ativo";
                                                                MessageBox.Show("Usuário cadastrado com sucesso!");
                                                            }
                                                            else
                                                                MessageBox.Show("Usuário não cadastrado");
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}