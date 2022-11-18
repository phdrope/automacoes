import streamlit as st
import time
import pandas as pd




st.title('Automação e Processos')

def outras_solicitacoes():
    form = st.form('Dúvidas')
    with form:
        assunto = st.text_input('Assunto:')
        descricao = st.text_area('Descrição:')
        arquivo = st.file_uploader('Anexe um arquivo:',accept_multiple_files=True)
        enviar = st.form_submit_button('Enviar')
        if enviar:
            st.success('Solicitação enviada com sucesso!', icon="✅")

def nf():
    form = st.form('nf')
    with form:
        texto = st.text_input("Observações:")
        c1, c2, c3, c4 = st.columns([1,1,1,1])
        c1.text_input('ORDEM DE VENDA')
        c2.text_input('NF')
        c3.date_input('DATA EMISSAO')
        c4.text_input('VALOR')
        arquivo = st.file_uploader('Inserir print da nf', accept_multiple_files=True)
        enviar = st.form_submit_button('Enviar')
        if enviar:
            st.success('Solicitação enviada com sucesso!', icon="✅")

def permite_fatura_s_conciliar():
    form = st.form('permite_fatura_s_conciliar')
    with form:
        texto = st.text_input('Assunto:')
        observacoes = st.text_area('Observações:')
        arquivo = st.file_uploader('Selecionar o arquivo (csv, xlsx',accept_multiple_files=True,)
        enviar = st.form_submit_button('Enviar')
        if enviar:
            st.success('Solicitação enviada com sucesso!', icon="✅")

def alteracoes_valores():
    form = st.form('alteracoes_valores')
    with form:
        pedido = st.text_input('Insira o RLOC:')

        opcoes = st.selectbox('Selecione o campo que será alterado:',
        ('...','Taxa Adm','FEE', 'Markup' ))

        if opcoes:
            obsevacao = st.text_area('Observacao:')
            arquivo = st.file_uploader('Insira um arquivo:')
            enviar = st.form_submit_button('Enviar')

            if enviar:
                st.success('Solicitação enviada com sucesso!', icon="✅")

def integracao_argo():
    os = st.text_input('Informe o Número do Pedido ou OS:', placeholder='Inserir apenas um pedido')

    cliente = st.selectbox('Informar/Selecionar o cliente:',
        ('Vale S.A','BRF','MAGALU','TIM','CCR','BUREAU VERITAS')
        )
    url = st.date_input('Data de Emissão')
    arquivo = st.file_uploader('Inserir um arquivo')
    enviar = st.button('Enviar')

    if enviar:
        st.write(os, cliente, url)

def integracao_reserve():
    os = st.text_input('Informe o Número do Pedido ou Requisição:')
    cliente = st.selectbox('Selecione o cliente:',
    ('...','SENIOR','A YOSHI','TOTVS','RNP', 'UMC SAO SIMAO', 'COPASTUR', 'OUTRO' )
    )
    if cliente != '...':
        if cliente == 'OUTRO':
            cliente = st.text_input('Descreve o nome do cliente:')

            enviar = st.button('Enviar')
            if enviar:
                st.success('Solicitação enviada com sucesso!', icon="✅")
        else:
            enviar = st.button('Enviar')

            if enviar:
                st.success('Solicitação enviada com sucesso!', icon="✅")

def integracao_wooba():
    os = st.text_input('Informe o Rloc:')
    enviar = st.button('Enviar')

    if enviar:
        st.success('Solicitação enviada com sucesso!', icon="✅")

def integracao_geral():
    os = st.text_input('Informe o número do pedido:')
    enviar = st.button('Enviar')

    if enviar:
        st.success('Solicitação enviada com sucesso!', icon="✅")

def solicitacao():
    tipo = st.selectbox(
        'Selecione o tipo de solicitação:',
        ('...','Integração de Pedido','Lista de Pedido','Erro Faturas/Lotes','Alterações via Update','Alterar Origem Pedido','Cancelar/Autorizar/Emitir NF','Outras Solicitações','Dúvidas')
        )
    
    if ((tipo == 'Outras Solicitações') or (tipo=='Dúvidas') or (tipo=='Alterar Origem Pedido')or (tipo=='Erro Faturas/Lotes')or (tipo=='Lista de Pedido')):
        outras_solicitacoes()
    
    if tipo == 'Cancelar/Autorizar/Emitir NF':
        nf()

    if tipo == 'Alterações via Update':
        tipo_alteracao = st.selectbox(
            'Selecione o tipo de alteração:',
            ('...','Permite Faturar S/ Conciliar',
            'Autorizações Divergentes',
            'Taxa Adm, Markup, Fee, etc',
            'Agente',
            'Fornecedor',
            'Cliente',
            'Copastools')

        )
        if tipo_alteracao == 'Taxa Adm, Markup, Fee, etc':
            alteracoes_valores()

        if ((tipo_alteracao == 'Permite Faturar S/ Conciliar') or (tipo_alteracao == 'Autorizações Divergentes')):
            permite_fatura_s_conciliar()

    if tipo == 'Integração de Pedido':
        obt = st.radio('Selecione o OBT:',
        ('Argo','Reserve','Lemontech','Paytrack','Wooba','Inteegra'))

        if obt == 'Argo':
            integracao_argo()
        if obt == 'Reserve':
            integracao_reserve()
        if obt == 'Wooba':
            integracao_wooba()
        if  ((obt =='Paytrack') or (obt =='Lemontech') or (obt =='Inteegra')):
            integracao_geral()    

solicitacao()

