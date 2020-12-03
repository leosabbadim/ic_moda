import requests
import json
import os

class TelegramBot:
    def __init__(self):
        token = ('1440430682:AAEJC1RFFvGVY_T8PqX_pKlTzZCcncb2QAk')
        self.url_base = f'https://api.telegram.org/bot{token}/'

    def Iniciar(self):
        update_id = None
        while True:
            atualizacao = self.obter_novas_mensagens(update_id)
            mensagens = atualizacao["result"]
            if mensagens:
                for mensagem in mensagens:
                    update_id = mensagem['update_id']
                    chat_id = mensagem["message"]["from"]["id"]
                    eh_primeira_mensagem = int(
                        mensagem["message"]["message_id"]) == 1
                    resposta = self.criar_resposta(mensagem, eh_primeira_mensagem)
                    self.responder(resposta, chat_id)

    # Obter mensagens
    def obter_novas_mensagens(self, update_id):
        link_requisicao = f'{self.url_base}getUpdates?timeout=100'
        if update_id:
            link_requisicao = f'{link_requisicao}&offset={update_id + 1}'
        resultado = requests.get(link_requisicao)
        return json.loads(resultado.content)

    # Criar uma resposta
    def criar_resposta(self, mensagem, eh_primeira_mensagem):
        mensagem = mensagem['message']['text']

        frentista = f'''O frentista usa os seguintes equipamentos e uniformes:
                     {os.linesep}Camisa Polo com o tecido Brim Leve - Que é um tecido confortável, além de fornecer protecão anti-chama.
                     {os.linesep}Calça Tecido com o tecido Brim -  Que é um tecido confortável e fornece conforto e proteção a exposição a possiveis contaminações químicas.
                     {os.linesep}Boné, luva, óculos e mascára de segunça - Para proteger a cabeça e identifiçacão do funcionario. Evita o contato com produtos químicos.
                     {os.linesep}Sapato de couro legítimo na cor preta - Que contém a parte interna macia e externa rigida.
                     {os.linesep}Cremes especiais - Que evitam a contaminação por produtos químicos que compõem os combustíveis.
                    '''
        bombeiro = f'''O bombeiro usa os seguintes equipamentos e uniformes:
                    {os.linesep}Camiseta na cor vermelha de algodão - Que proporciona conforto, alta resistência e leveza.
                    {os.linesep}Calça de tecido Ripstop - Feito com nylon e outro material, que ao entrelaçar cria uma superfície protetora.
                    {os.linesep}Gandola de tecido Ripstop - É essêncial para o uniforme por ser resistente impedindo rasgos e dando durabilidade.
                    {os.linesep}Boné de tecido Ripstop - Para proteção e identificação.
                    {os.linesep}Bota de combate a incêncio - Tendo a parte interna macia e a externa rígida.
                    {os.linesep}Cinto tático - Utilizado como porta objetos, com ajuste e trava "fecha fácil".
                    {os.linesep}Além desses equipamentos, os bombeiros devem ter:
                    {os.linesep}Capacete, Luvas anti-chama, EPR, Lanterna, Mosquetão e cordas, Protetor auricular e Rádio comunicador.'''
        minerador = f'''O minerador usa os seguintes equipamentos e uniformes:
                    {os.linesep}Luvas anti-corte - Composta por fios de aço inoxidáveis o que a torna altamente resistentes impedindo a penetração de qualquer material cortante.
                    {os.linesep}Máscara de respiração - Uso de máscaras é extremamente importante contêm um filtro que impede a inalação de substâncias indesejadas.
                    {os.linesep}Camiseta com faixas reflexivas - Proporcionam um destaque no meio atuante, visando anular ou reduzir possíveis acidentes.
                    {os.linesep}Além desses equipamentos, devem ter também:
                    {os.linesep}Óculos de Proteção, Capacete, Protetores Auditi-auriculares.
                    {os.linesep}E a calça e o calçado que devem ser adequados para suportar confições climáticas e químicas.


'''
        petroleo_gas = f'''O profissional da área de Petróleo e Gás deve usar os seguintes equipamentos e uniformes:
                    {os.linesep}Óculos de Proteção - Que impedem machucados por estilhaços, pedras e poeira.
                    {os.linesep}Macacão com cores fortes e faixas refletoras - Proporcionando proteção contra calor e chamas e podendo ser de Algodão, Microfibra, Poliéster, Plutônio, 100% algodão
                    {os.linesep}Capacete nas cores amarelo, branco e vermelho - Protege contra impactos externos 
                    {os.linesep}Luvas de tecido grosso - Proteção da mão. 
                    {os.linesep}Calçados na cor preta - Contendo a parte interna macia e a externa rigida.'''
        eletricista = f'''O eletricista deve usar os seguintes equipamentos e uniformes:
                    {os.linesep}Camisa de gola - Tecido FR 100% algodão.
                    {os.linesep}Gandola com faixas reflexivas - Com Gola italiana e manga cumprida, fornecendo proteção Anti- chama e a acidente eletrico.
                    {os.linesep}Calça com faixas reflexivas - Tecido FR 100% Algodão.
                    {os.linesep}Sapatos na cor preta - Sendo de borracha e contendo a parte interna macia e a externa rígida.
                    {os.linesep}Além desses itens, é importante que o eletricista utilize também capote, cinto de segurança, capacete, luvas e óculos de proteção.'''
        construcao_civil = f'''O profissional da área de construção civil deve usar os seguintes equipamentos e uniformes:
                            {os.linesep}Camiseta e Calça - Com tecido grosso e confortavel.
                            {os.linesep}Calçado na cor preta - Sendo rígido, completamente fechado e com a parter interna macia.
                            {os.linesep}Óculos e Máscara de proteção - Impedindo machucados por estilhaços, pedra e poeiras.
                            {os.linesep}Capacete em cores chamativas - Para proteção contra impactos externos. 
                            {os.linesep}Além desses equipamentos, é importante que seja utilizado abafador de ruídos, cinto e trava de segurança e Luvas anti-corte.'''
        saude = f'''O profissional da área de Saúde deve usar os seguintes equipamentos e uniformes:
                            {os.linesep}Calças e camiseta - Tecidos confortáveis
                            {os.linesep}Calçado - Completamente fechado
                            {os.linesep}Jaleco - Para proteção contra possíveis contaminações.
                            {os.linesep}Além desse uniforme, é importante a utilização dos seguintes itens descartáveis: 
                            {os.linesep}Face Shield, Máscara, Luvas e Toucas'''

        if eh_primeira_mensagem == True or mensagem.lower() == 'menu':
            return f'''Olá, Bem vindo, sou um BOT programado para trazer informativos sobre uniformes de trabalho e EPIs.
Sobre qual atividade profissional gostaria de saber:
            {os.linesep}1 - Frentista
            {os.linesep}2 - Bombeiro
            {os.linesep}3 - Minerador
            {os.linesep}4 - Petróleo e gás
            {os.linesep}5 - Eletricista
            {os.linesep}6 - Construção civíl
            {os.linesep}7 - Saúde'''
        if mensagem == '1' or mensagem.lower() == 'frentista':
            return f'''{frentista}'''
        if mensagem == '2' or mensagem.lower()== 'bombeiro':
            return f'''{bombeiro}'''
        if mensagem == '3' or mensagem.lower() == 'minerador':
            return f'''{minerador}'''
        if mensagem == '4' or mensagem.lower() == 'petroleo e gas' or mensagem.lower() == 'petróleo e gás' or mensagem.lower() == 'petróleo e gas' or mensagem.lower() == 'petroleo e gás':
            return f'''{petroleo_gas}'''
        if mensagem == '5' or mensagem.lower() == 'eletricista' or mensagem.lower() == 'eletricísta':
            return f'''{eletricista}'''
        if mensagem == '6' or mensagem == 'construção civil' or mensagem == 'construcao civil' or mensagem == 'construçao civil' or mensagem == 'construçao civil' :
            return f'''{construcao_civil}'''
        if mensagem == '7' or mensagem == 'saude' or mensagem == 'saúde':
            return f'''{saude}'''
        else:
            return 'Para acessar as opções de profissões, digite "menu"'


    # Responder
    def responder(self, resposta, chat_id):
        link_requisicao = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(link_requisicao)


bot = TelegramBot()
bot.Iniciar()
