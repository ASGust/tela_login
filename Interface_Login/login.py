import customtkinter as ctk
from tkinter import *
import database
from tkinter import messagebox

#variável global
janela = ctk.CTk()

class Application():
    def __init__(self):
        self.janela=janela
        self.tema()
        self.tela()
        self.tela_login()
        janela.mainloop()



    #Função que contem a configuração do tema de fundo do APP   
    def tema(self):    
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")


    #Função que configura a tela do APP
    def tela(self):
        janela.geometry("700x400")
        janela.title("Sistema de Login")
        janela.iconbitmap("hat.ico")
        janela.resizable(False, False)


    #configurando imagens da tela de login
    def tela_login(self):
        
        #Imagem ao lado da Tela de Login
        img = PhotoImage(file="log.png")
        label_img = ctk.CTkLabel(master=janela, image=img).place(x=40, y=65)

        title_label = ctk.CTkLabel(master=janela, text="BEM-VINDO A PLATAFORMA", font=("Arial Black", 18), text_color="#00B0F0").place(x=40, y=10)

        #Frame 
        login_frame = ctk.CTkFrame(master=janela, width=350, height=396)
        login_frame.pack(side=RIGHT)

        #Frame Widgets - Tela de Login
        label = ctk.CTkLabel(master=login_frame, text="Login", font=("Roboto", 20)).place(x=25, y=30)

        #Frame - Entry - Usuário
        username_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Usuário", width=300, font=("Roboto", 14)).place(x=25, y=105)
        username_label = ctk.CTkLabel(master=login_frame, text="*Campo obrigatório.", text_color="green", font=("Roboto", 12)).place(x=25, y=135)

        #Frame - Entry - Senha
        password_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Senha", width=300, font=("Roboto", 14), show="*").place(x=25, y=175)
        password_label = ctk.CTkLabel(master=login_frame, text="*Campo obrigatório.", text_color="green", font=("Roboto", 12)).place(x=25, y=205)

        #checkbox - Lembrar Senha
        checkbox = ctk.CTkCheckBox(master=login_frame, text="Deseja lembrar sua senha?").place(x=25, y=240)

        def login():
            msg = messagebox.showinfo(title="Tela de Login", message="Login feito com sucesso!")
            pass

        #Botão - login
        login_button = ctk.CTkButton(master=login_frame, text="Login", font=("Roboto",16), width=300, command=login).place(x=25, y=285)

        #Mensagem ao lado de "cadastrar-se"
        register_spam = ctk.CTkLabel(master=login_frame, text="Ainda não possui uma conta?", font=("Arial", 10)).place(x=25, y=325)
        
        #criando a vinculação do botão "cadastre-se", com a tela cadastrar novo usuário
        def tela_register():

            #remover o frame de login
            login_frame.pack_forget()

            #Criando a tela de cadastro de usuário
            rg_frame = ctk.CTkFrame(master=janela, width=350, height=396)
            rg_frame.pack(side=RIGHT)

            #Frame tela de Cadastro
            label = ctk.CTkLabel(master=rg_frame, text="REALIZE SEU CADASTRO", font=("Roboto", 20)).place(x=25, y=30)

            spam = ctk.CTkLabel(master=rg_frame, text="Preencha todos os campos com dados corretos.", font=("Roboto", 12), text_color="gray").place(x=25, y=65)

            #Entry - Nome
            username = ctk.CTkEntry(master=rg_frame, placeholder_text="Nome de usuário", width=300, font=("Roboto", 14)).place(x=25, y=105)
            
            #Entry - Email
            email_entry = ctk.CTkEntry(master=rg_frame, placeholder_text="Digite seu e-mail", width=300, font=("Roboto", 14)).place(x=25, y=145)
            
            #Entry - Senha
            password_entry = ctk.CTkEntry(master=rg_frame, placeholder_text="Digite sua senha", width=300, font=("Roboto", 14), show="*").place(x=25, y=185)
            
            #Entry - Confirmação de senha
            cPassword_entry = ctk.CTkEntry(master=rg_frame, placeholder_text="Confirme sua senha", width=300, font=("Roboto", 14), show="*").place(x=25, y=225)

            #Checkbox - Termos e Condições
            checkbox = ctk.CTkCheckBox(master=rg_frame, text="Aceitar Termos & Condições").place(x=25, y=265)
            
            #Função voltar
            def back():
                #Removendo a tela de cadastro
                rg_frame.pack_forget()

                #Voltando a tela de login
                login_frame.pack(side=RIGHT)
                

            #Botão - Voltar
            back_button = ctk.CTkButton(master=rg_frame, text="Voltar", font=("Roboto",16),fg_color="gray", hover_color="#202020", width=145, command=back).place(x=25, y=315)

            #Função para salvar novo usuário
            def save_newUser():
                msg = messagebox.showinfo(title="Situação do Cadastro", message="Oba! Seu cadastro foi efetuado com sucesso")
                pass
                

            #Botão - Registrar-se
            save_button = ctk.CTkButton(master=rg_frame, text="Cadastrar", font=("Roboto",16), width=145, fg_color="green", hover_color="#014805", command=save_newUser).place(x=180, y=315) 


        #Botão - Cadastrar
        register_button = ctk.CTkButton(master=login_frame, text="Cadastre-se", font=("Roboto", 12), fg_color="green", hover_color="#2D9334", width=150, command=tela_register).place(x=175, y=325)




Application()
