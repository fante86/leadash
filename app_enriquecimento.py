import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
import re
from urllib.parse import quote_plus
import json
from io import BytesIO

# Configuração da página
st.set_page_config(
    page_title="Enriquecimento de Leads - Pre Sales",
    page_icon="🎯",
    layout="wide"
)

# Estilo CSS customizado
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .status-box {
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    .success-box {
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
    }
    .info-box {
        background-color: #d1ecf1;
        border: 1px solid #bee5eb;
    }
    .warning-box {
        background-color: #fff3cd;
        border: 1px solid #ffeaa7;
    }
</style>
""", unsafe_allow_html=True)

# Título principal
st.markdown('<h1 class="main-header">🎯 Enriquecimento de Leads B2B</h1>', unsafe_allow_html=True)
st.markdown("### 📊 Ferramenta de Pre Sales para encontrar decisores e contatos")

# Funções de busca web
def search_google(query, num_results=5):
    """Simula busca no Google através de uma API de pesquisa"""
    try:
        # URL de busca do Google
        search_url = f"https://www.google.com/search?q={quote_plus(query)}&num={num_results}"
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(search_url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            return soup
        return None
    except Exception as e:
        st.warning(f"Erro na busca: {str(e)}")
        return None

def extract_emails(text):
    """Extrai emails de um texto"""
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_pattern, text)
    # Filtrar emails comuns/genéricos
    filtered_emails = [e for e in emails if not any(x in e.lower() for x in ['example', 'domain', 'email', 'test', 'noreply'])]
    return list(set(filtered_emails))[:3]  # Retorna até 3 emails únicos

def extract_phones(text):
    """Extrai telefones brasileiros de um texto"""
    phone_patterns = [
        r'\(?\d{2}\)?\s*9?\d{4}[-.\s]?\d{4}',  # (11) 99999-9999 ou variações
        r'\d{2}\s*9?\d{4}[-.\s]?\d{4}',        # 11 99999-9999
        r'\+55\s*\(?\d{2}\)?\s*9?\d{4}[-.\s]?\d{4}'  # +55 (11) 99999-9999
    ]
    
    phones = []
    for pattern in phone_patterns:
        phones.extend(re.findall(pattern, text))
    
    return list(set(phones))[:3]  # Retorna até 3 telefones únicos

def extract_linkedin_profiles(text):
    """Extrai perfis do LinkedIn de um texto"""
    linkedin_pattern = r'(?:https?://)?(?:www\.)?linkedin\.com/(?:in|company)/[\w-]+'
    profiles = re.findall(linkedin_pattern, text)
    return list(set(profiles))[:5]  # Retorna até 5 perfis únicos

def extract_website(text):
    """Extrai possíveis websites de um texto"""
    website_pattern = r'https?://(?:www\.)?[\w.-]+\.[\w]{2,}'
    websites = re.findall(website_pattern, text)
    # Filtrar URLs comuns de redes sociais
    filtered = [w for w in websites if not any(x in w.lower() for x in ['google', 'facebook.com', 'twitter.com', 'instagram.com'])]
    return list(set(filtered))[:2]

def enrich_company_data(company_name, city, state):
    """Enriquece dados de uma empresa através de buscas na web"""
    
    results = {
        'telefone': '',
        'email': '',
        'website': '',
        'linkedin_empresa': '',
        'linkedin_decisores': '',
        'status': 'Não processado'
    }
    
    try:
        # Busca 1: Informações gerais da empresa
        query1 = f"{company_name} {city} {state} telefone email contato"
        soup1 = search_google(query1)
        
        if soup1:
            text1 = soup1.get_text()
            
            # Extrair dados
            phones = extract_phones(text1)
            if phones:
                results['telefone'] = phones[0]
            
            emails = extract_emails(text1)
            if emails:
                results['email'] = '; '.join(emails)
            
            websites = extract_website(text1)
            if websites:
                results['website'] = websites[0]
        
        time.sleep(1)  # Delay entre requisições
        
        # Busca 2: LinkedIn da empresa
        query2 = f"{company_name} {city} site:linkedin.com/company"
        soup2 = search_google(query2)
        
        if soup2:
            text2 = soup2.get_text()
            linkedin_profiles = extract_linkedin_profiles(text2)
            company_profiles = [p for p in linkedin_profiles if '/company/' in p]
            if company_profiles:
                results['linkedin_empresa'] = company_profiles[0]
        
        time.sleep(1)
        
        # Busca 3: Decisores no LinkedIn
        query3 = f"{company_name} {city} diretor gerente CEO site:linkedin.com/in"
        soup3 = search_google(query3)
        
        if soup3:
            text3 = soup3.get_text()
            linkedin_profiles = extract_linkedin_profiles(text3)
            person_profiles = [p for p in linkedin_profiles if '/in/' in p]
            if person_profiles:
                results['linkedin_decisores'] = '; '.join(person_profiles[:3])
        
        # Determinar status
        if results['telefone'] or results['email'] or results['website']:
            results['status'] = 'Enriquecido'
        else:
            results['status'] = 'Sem dados encontrados'
            
    except Exception as e:
        results['status'] = f'Erro: {str(e)}'
    
    return results

# Interface principal
uploaded_file = st.file_uploader("📁 Faça upload do arquivo Excel com as empresas", type=['xlsx', 'xls'])

if uploaded_file:
    try:
        # Ler arquivo
        df = pd.read_excel(uploaded_file, header=1)
        
        st.success(f"✅ Arquivo carregado com sucesso! {len(df)} empresas encontradas.")
        
        # Mostrar preview dos dados
        with st.expander("👀 Visualizar dados originais"):
            st.dataframe(df.head(10))
        
        # Configurações de processamento
        st.markdown("---")
        st.markdown("### ⚙️ Configurações de Processamento")
        
        col1, col2 = st.columns(2)
        
        with col1:
            num_empresas = st.number_input(
                "Número de empresas para processar",
                min_value=1,
                max_value=len(df),
                value=min(10, len(df)),
                help="Limite de empresas para enriquecimento (evita timeout)"
            )
        
        with col2:
            delay_seconds = st.slider(
                "Delay entre buscas (segundos)",
                min_value=1,
                max_value=5,
                value=2,
                help="Tempo de espera entre cada busca (evita bloqueio)"
            )
        
        # Botão de processamento
        if st.button("🚀 Iniciar Enriquecimento", type="primary", use_container_width=True):
            
            # Criar colunas para os novos dados
            df_enriched = df.copy()
            df_enriched['telefone_encontrado'] = ''
            df_enriched['email_encontrado'] = ''
            df_enriched['website_encontrado'] = ''
            df_enriched['linkedin_empresa'] = ''
            df_enriched['linkedin_decisores'] = ''
            df_enriched['status_enriquecimento'] = ''
            
            # Barra de progresso
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            # Container para resultados em tempo real
            results_container = st.container()
            
            # Processar empresas
            for idx in range(min(num_empresas, len(df))):
                row = df.iloc[idx]
                company_name = row['name']
                city = row.get('city', '')
                state = row.get('state', '')
                
                status_text.text(f"🔍 Processando {idx + 1}/{num_empresas}: {company_name}...")
                
                # Enriquecer dados
                enriched_data = enrich_company_data(company_name, city, state)
                
                # Atualizar DataFrame
                df_enriched.at[idx, 'telefone_encontrado'] = enriched_data['telefone']
                df_enriched.at[idx, 'email_encontrado'] = enriched_data['email']
                df_enriched.at[idx, 'website_encontrado'] = enriched_data['website']
                df_enriched.at[idx, 'linkedin_empresa'] = enriched_data['linkedin_empresa']
                df_enriched.at[idx, 'linkedin_decisores'] = enriched_data['linkedin_decisores']
                df_enriched.at[idx, 'status_enriquecimento'] = enriched_data['status']
                
                # Atualizar progresso
                progress_bar.progress((idx + 1) / num_empresas)
                
                # Delay entre requisições
                time.sleep(delay_seconds)
            
            status_text.text("✅ Processamento concluído!")
            
            # Estatísticas
            st.markdown("---")
            st.markdown("### 📊 Estatísticas de Enriquecimento")
            
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                telefones_encontrados = df_enriched['telefone_encontrado'].str.len() > 0
                st.metric("📞 Telefones", telefones_encontrados.sum())
            
            with col2:
                emails_encontrados = df_enriched['email_encontrado'].str.len() > 0
                st.metric("📧 Emails", emails_encontrados.sum())
            
            with col3:
                websites_encontrados = df_enriched['website_encontrado'].str.len() > 0
                st.metric("🌐 Websites", websites_encontrados.sum())
            
            with col4:
                linkedin_encontrados = df_enriched['linkedin_empresa'].str.len() > 0
                st.metric("💼 LinkedIn", linkedin_encontrados.sum())
            
            # Mostrar dados enriquecidos
            st.markdown("---")
            st.markdown("### 📋 Dados Enriquecidos")
            
            # Filtrar apenas empresas processadas
            df_display = df_enriched.head(num_empresas)
            
            st.dataframe(
                df_display[[
                    'name', 'city', 'telefone_encontrado', 'email_encontrado',
                    'website_encontrado', 'linkedin_empresa', 'linkedin_decisores',
                    'status_enriquecimento'
                ]],
                use_container_width=True
            )
            
            # Exportar resultados
            st.markdown("---")
            st.markdown("### 💾 Exportar Resultados")
            
            # Criar arquivo Excel em memória
            output = BytesIO()
            with pd.ExcelWriter(output, engine='openpyxl') as writer:
                df_enriched.to_excel(writer, index=False, sheet_name='Empresas Enriquecidas')
            
            excel_data = output.getvalue()
            
            st.download_button(
                label="📥 Download Excel Enriquecido",
                data=excel_data,
                file_name="empresas_enriquecidas.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                use_container_width=True
            )
            
            # Opções adicionais
            with st.expander("🔧 Opções Avançadas"):
                st.markdown("""
                **Próximos passos recomendados:**
                - Verificar manualmente os dados encontrados
                - Complementar com pesquisa em redes sociais
                - Validar emails usando ferramentas especializadas
                - Enriquecer com dados de ferramentas como Hunter.io, Apollo.io
                """)
    
    except Exception as e:
        st.error(f"❌ Erro ao processar arquivo: {str(e)}")

else:
    # Instruções quando não há arquivo
    st.info("""
    ### 📝 Como usar esta ferramenta:
    
    1. **Faça upload** do arquivo Excel com suas empresas
    2. **Configure** quantas empresas deseja processar
    3. **Clique em "Iniciar Enriquecimento"**
    4. **Aguarde** o processamento (pode levar alguns minutos)
    5. **Baixe** o arquivo enriquecido com os dados encontrados
    
    ### 🎯 Dados que serão buscados:
    - 📞 Telefone de contato
    - 📧 Email corporativo
    - 🌐 Website oficial
    - 💼 LinkedIn da empresa
    - 👔 LinkedIn de decisores (CEO, Diretor, Gerente)
    
    ### ⚠️ Observações importantes:
    - O processamento pode levar tempo dependendo da quantidade de empresas
    - Recomendamos processar em lotes de 10-20 empresas por vez
    - Alguns dados podem não ser encontrados automaticamente
    - É importante validar manualmente os resultados
    """)
    
    # Exemplo de estrutura esperada
    with st.expander("📄 Estrutura esperada do arquivo"):
        st.markdown("""
        Seu arquivo Excel deve conter pelo menos estas colunas:
        - `name`: Nome da empresa
        - `city`: Cidade
        - `state`: Estado
        - `address`: Endereço (opcional)
        
        Outras colunas serão mantidas no arquivo de saída.
        """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 2rem;'>
    <p>🎯 Ferramenta de Enriquecimento de Leads B2B | Desenvolvida para Pre Sales</p>
    <p style='font-size: 0.8rem;'>⚠️ Use com responsabilidade e respeite a LGPD</p>
</div>
""", unsafe_allow_html=True)
