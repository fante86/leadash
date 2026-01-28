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
</style>
""", unsafe_allow_html=True)

# Título principal
st.markdown('<h1 class="main-header">🎯 Enriquecimento de Leads B2B</h1>', unsafe_allow_html=True)
st.markdown("### 📊 Ferramenta de Pre Sales para encontrar decisores e contatos")

# ===== FUNÇÕES DE BUSCA MELHORADAS =====

def try_multiple_search_engines(query):
    """Tenta buscar em múltiplos motores até conseguir"""
    
    # Lista de User-Agents rotativos
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    ]
    
    # Tentar DuckDuckGo primeiro (não bloqueia tanto)
    try:
        headers = {
            'User-Agent': user_agents[0],
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
            'Accept-Encoding': 'gzip, deflate',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        }
        
        # DuckDuckGo HTML
        url = f"https://html.duckduckgo.com/html/?q={quote_plus(query)}"
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html5lib')
            text = soup.get_text()
            if len(text) > 500:  # Se conseguiu conteúdo relevante
                return text
    except:
        pass
    
    # Tentar Google como fallback
    try:
        headers = {'User-Agent': user_agents[1]}
        url = f"https://www.google.com/search?q={quote_plus(query)}"
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html5lib')
            return soup.get_text()
    except:
        pass
    
    return ""

def extract_emails(text):
    """Extrai emails válidos de um texto"""
    if not text:
        return []
    
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_pattern, text)
    
    # Filtrar emails inválidos
    blacklist = ['example', 'domain', 'email', 'test', 'noreply', 'no-reply', 
                 'mailer', 'dummy', 'sample', 'localhost', 'sentry', 'wixpress']
    
    filtered = []
    for email in emails:
        email_lower = email.lower()
        if not any(word in email_lower for word in blacklist):
            if len(email) > 5 and '.' in email.split('@')[1]:  # Validação básica
                filtered.append(email)
    
    return list(set(filtered))[:3]

def extract_phones_br(text):
    """Extrai telefones brasileiros de um texto"""
    if not text:
        return []
    
    patterns = [
        r'\+55[\s\-]?\(?\d{2}\)?[\s\-]?9?\d{4,5}[\s\-]?\d{4}',
        r'\(?\d{2}\)?[\s\-]?9\d{4}[\s\-]?\d{4}',
        r'\d{2}[\s\-]9\d{4}[\s\-]\d{4}',
        r'\(?\d{2}\)?[\s\-]?\d{4}[\s\-]?\d{4}',
    ]
    
    phones = []
    for pattern in patterns:
        matches = re.findall(pattern, text)
        phones.extend(matches)
    
    # Limpar e validar
    cleaned_phones = []
    for phone in phones:
        # Remover formatação
        digits = re.sub(r'\D', '', phone)
        # Validar tamanho (10 ou 11 dígitos)
        if len(digits) in [10, 11] and digits[0:2] in ['11', '12', '13', '14', '15', '16', '17', '18', '19', '21', '22', '24', '27', '28']:
            cleaned_phones.append(phone)
    
    return list(set(cleaned_phones))[:3]

def extract_linkedin(text, profile_type='company'):
    """Extrai perfis do LinkedIn"""
    if not text:
        return []
    
    if profile_type == 'company':
        pattern = r'(?:https?://)?(?:www\.)?linkedin\.com/company/[\w-]+'
    else:
        pattern = r'(?:https?://)?(?:www\.)?linkedin\.com/in/[\w-]+'
    
    profiles = re.findall(pattern, text)
    return list(set(profiles))[:5]

def extract_websites(text):
    """Extrai websites válidos"""
    if not text:
        return []
    
    pattern = r'https?://(?:www\.)?[\w.-]+\.[\w]{2,}'
    websites = re.findall(pattern, text)
    
    # Filtrar redes sociais
    blacklist = ['google.', 'facebook.', 'twitter.', 'instagram.', 'youtube.', 
                 'linkedin.', 'tiktok.', 'whatsapp.', 'duckduckgo.']
    
    filtered = []
    for site in websites:
        if not any(bl in site.lower() for bl in blacklist):
            filtered.append(site)
    
    return list(set(filtered))[:2]

def generate_common_emails(company_name, domain=""):
    """Gera emails comuns baseado no nome da empresa"""
    emails = []
    
    # Limpar nome da empresa
    clean_name = re.sub(r'[^a-zA-Z0-9\s]', '', company_name.lower())
    words = clean_name.split()
    
    if not domain:
        # Tentar gerar domínio baseado no nome
        if len(words) > 0:
            domain = words[0] + ".com.br"
    
    if domain:
        # Padrões comuns brasileiros
        patterns = [
            f"contato@{domain}",
            f"comercial@{domain}",
            f"vendas@{domain}",
            f"atendimento@{domain}",
            f"sac@{domain}",
        ]
        emails.extend(patterns)
    
    return emails

def generate_phone_suggestions(city, state):
    """Sugere DDDs baseado na localização"""
    ddd_map = {
        'São Paulo': '11', 'Campinas': '19', 'Santos': '13', 'Sorocaba': '15',
        'Rio de Janeiro': '21', 'Belo Horizonte': '31', 'Brasília': '61',
        'Salvador': '71', 'Curitiba': '41', 'Porto Alegre': '51',
        'Recife': '81', 'Fortaleza': '85', 'Manaus': '92'
    }
    
    ddd = ddd_map.get(city, '11')
    return f"DDD provável: ({ddd})"

def enrich_company_data(company_name, city, state):
    """Enriquece dados de uma empresa"""
    
    results = {
        'telefone': '',
        'email': '',
        'website': '',
        'linkedin_empresa': '',
        'linkedin_decisores': '',
        'status': '🔍 Buscando...'
    }
    
    found_data = []
    
    try:
        # Busca 1: Informações gerais com cidade e estado
        query1 = f'"{company_name}" {city} {state} telefone contato'
        st.info(f"🔍 Buscando: {query1}")
        text1 = try_multiple_search_engines(query1)
        
        if text1:
            # Extrair dados
            phones = extract_phones_br(text1)
            if phones:
                results['telefone'] = phones[0]
                found_data.append('telefone')
            
            emails = extract_emails(text1)
            if emails:
                results['email'] = '; '.join(emails[:2])
                found_data.append('email')
            
            websites = extract_websites(text1)
            if websites:
                results['website'] = websites[0]
                found_data.append('website')
        
        time.sleep(2)
        
        # Busca 2: Website da empresa
        if not results['website']:
            query2 = f'"{company_name}" {city} site oficial'
            text2 = try_multiple_search_engines(query2)
            
            if text2:
                websites = extract_websites(text2)
                if websites:
                    results['website'] = websites[0]
                    found_data.append('website')
        
        time.sleep(2)
        
        # Busca 3: LinkedIn empresa
        query3 = f'"{company_name}" {city} linkedin empresa'
        text3 = try_multiple_search_engines(query3)
        
        if text3:
            linkedin = extract_linkedin(text3, 'company')
            if linkedin:
                results['linkedin_empresa'] = linkedin[0]
                found_data.append('linkedin')
        
        time.sleep(2)
        
        # Gerar sugestões se não encontrou dados
        suggestions = []
        
        if not results['email']:
            domain = results['website'].replace('https://', '').replace('http://', '').split('/')[0] if results['website'] else ''
            suggested_emails = generate_common_emails(company_name, domain)
            if suggested_emails:
                results['email'] = f"💡 Sugestões: {'; '.join(suggested_emails[:2])}"
                suggestions.append('emails sugeridos')
        
        if not results['telefone']:
            ddd_info = generate_phone_suggestions(city, state)
            results['telefone'] = f"💡 {ddd_info}"
            suggestions.append('DDD')
        
        # Status final
        if found_data:
            results['status'] = f"✅ Encontrado: {', '.join(found_data)}"
        elif suggestions:
            results['status'] = f"💡 Sugestões: {', '.join(suggestions)}"
        else:
            results['status'] = "⚠️ Nenhum dado encontrado"
            
    except Exception as e:
        results['status'] = f"❌ Erro: {str(e)[:50]}"
    
    return results

# ===== INTERFACE STREAMLIT =====

uploaded_file = st.file_uploader("📁 Faça upload do arquivo Excel com as empresas", type=['xlsx', 'xls'])

if uploaded_file:
    try:
        # Ler arquivo
        df = pd.read_excel(uploaded_file, header=1)
        
        st.success(f"✅ Arquivo carregado com sucesso! {len(df)} empresas encontradas.")
        
        # Mostrar preview
        with st.expander("👀 Visualizar dados originais"):
            st.dataframe(df.head(10))
        
        # Configurações
        st.markdown("---")
        st.markdown("### ⚙️ Configurações de Processamento")
        
        col1, col2 = st.columns(2)
        
        with col1:
            num_empresas = st.number_input(
                "Número de empresas para processar",
                min_value=1,
                max_value=len(df),
                value=min(5, len(df)),
                help="Recomendado: 5-10 empresas por vez para melhor resultado"
            )
        
        with col2:
            delay_seconds = st.slider(
                "Delay entre buscas (segundos)",
                min_value=2,
                max_value=10,
                value=3,
                help="Tempo maior = menos chance de bloqueio"
            )
        
        # Botão de processamento
        if st.button("🚀 Iniciar Enriquecimento", type="primary", use_container_width=True):
            
            # Preparar DataFrame
            df_enriched = df.copy()
            new_cols = ['telefone_encontrado', 'email_encontrado', 'website_encontrado',
                       'linkedin_empresa', 'linkedin_decisores', 'status_enriquecimento']
            
            for col in new_cols:
                if col not in df_enriched.columns:
                    df_enriched[col] = ''
            
            # Progress
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            # Processar empresas
            for idx in range(min(num_empresas, len(df))):
                row = df.iloc[idx]
                company_name = row['name']
                city = row.get('city', '')
                state = row.get('state', '')
                
                status_text.text(f"🔍 Processando {idx + 1}/{num_empresas}: {company_name}...")
                
                # Enriquecer
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
                
                # Delay
                time.sleep(delay_seconds)
            
            status_text.text("✅ Processamento concluído!")
            
            # Estatísticas
            st.markdown("---")
            st.markdown("### 📊 Estatísticas de Enriquecimento")
            
            col1, col2, col3, col4 = st.columns(4)
            
            processed = df_enriched.head(num_empresas)
            
            with col1:
                telefones = (processed['telefone_encontrado'].str.len() > 0).sum()
                st.metric("📞 Telefones", telefones)
            
            with col2:
                emails = (processed['email_encontrado'].str.len() > 0).sum()
                st.metric("📧 Emails", emails)
            
            with col3:
                websites = (processed['website_encontrado'].str.len() > 0).sum()
                st.metric("🌐 Websites", websites)
            
            with col4:
                linkedin = (processed['linkedin_empresa'].str.len() > 0).sum()
                st.metric("💼 LinkedIn", linkedin)
            
            # Mostrar dados
            st.markdown("---")
            st.markdown("### 📋 Dados Enriquecidos")
            
            display_cols = ['name', 'city', 'telefone_encontrado', 'email_encontrado',
                           'website_encontrado', 'linkedin_empresa', 'status_enriquecimento']
            
            st.dataframe(
                processed[display_cols],
                use_container_width=True
            )
            
            # Download
            st.markdown("---")
            output = BytesIO()
            with pd.ExcelWriter(output, engine='openpyxl') as writer:
                df_enriched.to_excel(writer, index=False)
            
            st.download_button(
                "📥 Download Excel Enriquecido",
                output.getvalue(),
                "empresas_enriquecidas.xlsx",
                "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                use_container_width=True
            )
            
    except Exception as e:
        st.error(f"❌ Erro: {str(e)}")

else:
    st.info("""
    ### 📝 Como usar esta ferramenta:
    
    1. **Faça upload** do arquivo Excel com suas empresas
    2. **Configure** quantas empresas deseja processar (recomendado: 5-10)
    3. **Clique em "Iniciar Enriquecimento"**
    4. **Aguarde** o processamento
    5. **Baixe** o arquivo enriquecido
    
    ### 🎯 O que será buscado:
    - 📞 Telefone de contato
    - 📧 Email corporativo (+ sugestões de emails comuns)
    - 🌐 Website oficial
    - 💼 LinkedIn da empresa
    - 💡 Sugestões de DDD baseado na localização
    
    ### ⚠️ Dicas para melhores resultados:
    - Processe poucas empresas por vez (5-10)
    - Use delay maior entre buscas (3-5 segundos)
    - Nomes completos das empresas funcionam melhor
    - Valide manualmente os dados encontrados
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 2rem;'>
    <p>🎯 Ferramenta de Enriquecimento de Leads B2B | Desenvolvida para Pre Sales</p>
    <p style='font-size: 0.8rem;'>⚠️ Use com responsabilidade e respeite a LGPD</p>
</div>
""", unsafe_allow_html=True)
