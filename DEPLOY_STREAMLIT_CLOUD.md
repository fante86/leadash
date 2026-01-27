# 🚀 GUIA DE DEPLOY NO STREAMLIT CLOUD

## ✅ Por que usar Streamlit Cloud?

- 🆓 **Totalmente GRÁTIS**
- ☁️ **Sem servidor para gerenciar**
- 🌐 **Acessível de qualquer lugar**
- 🔄 **Atualização automática do código**
- 🔗 **Link compartilhável com sua equipe**

---

## 📋 Passo a Passo Completo

### 1️⃣ Preparar o Código no GitHub

#### Opção A: Criar Repositório pelo GitHub.com

1. Acesse [github.com](https://github.com) e faça login
2. Clique em **"New"** (botão verde) para criar um repositório
3. Configure:
   - **Nome:** `enriquecedor-leads` (ou o nome que preferir)
   - **Visibilidade:** Private (recomendado) ou Public
   - Marque: ✅ "Add a README file"
4. Clique em **"Create repository"**

#### Opção B: Usar GitHub Desktop (Mais Fácil)

1. Baixe [GitHub Desktop](https://desktop.github.com/)
2. Instale e faça login
3. Clique em **"New Repository"**
4. Configure e clique em **"Create Repository"**

---

### 2️⃣ Upload dos Arquivos

#### Via GitHub.com (Interface Web):

1. No seu repositório, clique em **"Add file"** → **"Upload files"**
2. Arraste estes arquivos:
   ```
   ✅ app_enriquecimento.py (ou app_enriquecimento_avancado.py)
   ✅ requirements.txt
   ✅ README.md
   ```
3. Na pasta `.streamlit`, crie arquivo `config.toml` com este conteúdo:
   ```toml
   [theme]
   primaryColor = "#1f77b4"
   backgroundColor = "#ffffff"
   secondaryBackgroundColor = "#f0f2f6"
   textColor = "#262730"
   font = "sans serif"

   [server]
   headless = true
   port = 8501
   enableCORS = false
   ```
4. Clique em **"Commit changes"**

#### Via GitHub Desktop:

1. Copie os arquivos para a pasta do repositório no seu computador
2. No GitHub Desktop, você verá os arquivos na aba "Changes"
3. Adicione uma mensagem: "Deploy inicial"
4. Clique em **"Commit to main"**
5. Clique em **"Push origin"**

---

### 3️⃣ Deploy no Streamlit Cloud

1. **Acesse:** [share.streamlit.io](https://share.streamlit.io)

2. **Login:** Use sua conta GitHub

3. **Novo App:** Clique em **"New app"**

4. **Configure:**
   ```
   Repository: seu-usuario/enriquecedor-leads
   Branch: main
   Main file path: app_enriquecimento.py
   ```
   
5. **Advanced settings** (opcional):
   - Python version: 3.11
   - Secrets: Configure APIs aqui (se usar versão avançada)

6. **Deploy!** Clique em **"Deploy"**

⏰ **Aguarde 2-5 minutos** - Seu app estará online!

---

## 🔑 Configurar APIs (Versão Avançada)

Se você está usando a versão avançada com APIs:

1. No Streamlit Cloud, vá em **"Settings"** → **"Secrets"**

2. Adicione suas chaves:
   ```toml
   [api_keys]
   hunter = "sua-chave-hunter-io"
   serper = "sua-chave-serper"
   ```

3. Modifique o código para ler os secrets:
   ```python
   import streamlit as st
   
   # Ler secrets
   hunter_key = st.secrets["api_keys"]["hunter"]
   serper_key = st.secrets["api_keys"]["serper"]
   ```

---

## 🌐 Estrutura de Pastas no GitHub

```
enriquecedor-leads/
│
├── .streamlit/
│   └── config.toml          # Configurações do Streamlit
│
├── app_enriquecimento.py    # App principal (ESCOLHA UM)
├── app_enriquecimento_avancado.py  # ou este
│
├── requirements.txt         # Dependências
├── README.md               # Documentação
└── .gitignore              # Arquivos a ignorar (opcional)
```

---

## 📝 Arquivo .gitignore (Recomendado)

Crie um arquivo `.gitignore` no repositório:

```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/

# Dados sensíveis
*.xlsx
*.xls
*.csv
config_local.py
.env

# Streamlit
.streamlit/secrets.toml
```

---

## 🔄 Atualizar o App

### Opção 1: Via GitHub.com
1. Vá até o arquivo que quer editar
2. Clique no ícone de lápis ✏️
3. Faça as alterações
4. Clique em **"Commit changes"**
5. O Streamlit Cloud atualiza automaticamente!

### Opção 2: Via GitHub Desktop
1. Edite os arquivos localmente
2. Commit as mudanças
3. Push para GitHub
4. App atualiza sozinho!

---

## 🎯 URLs e Compartilhamento

Após o deploy, você terá uma URL tipo:
```
https://seu-app.streamlit.app
```

**Compartilhar com a equipe:**
- ✅ Link público (se repositório público)
- ✅ Link privado (se repositório privado + convite)
- ✅ Incorporar em iframe
- ✅ Adicionar domínio customizado (planos pagos)

---

## 🔒 Segurança e Privacidade

### Para Repositório Privado:

1. No GitHub, vá em **Settings** → **Collaborators**
2. Adicione membros da equipe
3. Eles poderão acessar o app

### Proteger Dados Sensíveis:

- ❌ **NUNCA** commite:
  - Arquivos Excel com dados reais
  - Chaves de API no código
  - Senhas ou tokens

- ✅ **SEMPRE** use:
  - `.gitignore` para excluir arquivos
  - Streamlit Secrets para APIs
  - Repositório privado para projetos internos

---

## ⚙️ Limites do Plano Gratuito

| Recurso | Limite |
|---------|--------|
| Apps | 1 app público grátis* |
| Recursos | 1 GB RAM |
| Tempo ativo | 7 dias inativo = sleep |
| Usuários | Ilimitados |

*Para apps privados ou mais apps, há planos pagos a partir de $20/mês

---

## 🐛 Resolução de Problemas

### App não inicia
```
✅ Verifique requirements.txt
✅ Confirme nome do arquivo principal
✅ Veja os logs no Streamlit Cloud
```

### Erro de import
```
✅ Adicione o módulo em requirements.txt
✅ Use versões compatíveis
✅ Reinicie o app
```

### App muito lento
```
✅ Otimize o código com @st.cache
✅ Reduza número de requisições
✅ Considere plano pago para mais recursos
```

### Erro de permissão
```
✅ Repositório deve estar público ou você deve ser colaborador
✅ Conecte corretamente GitHub ao Streamlit
```

---

## 🚀 Otimizações para Produção

### 1. Cache de Dados
```python
@st.cache_data(ttl=3600)  # Cache por 1 hora
def buscar_empresa(nome):
    # sua função aqui
    pass
```

### 2. Progress e Feedback
```python
with st.spinner('Processando...'):
    # operação demorada
    pass
```

### 3. Tratamento de Erros
```python
try:
    # código
except Exception as e:
    st.error(f"Erro: {e}")
    st.info("Tente novamente ou contate o suporte")
```

---

## 📊 Monitoramento

No Streamlit Cloud você pode:

- 📈 Ver métricas de uso
- 📝 Acessar logs em tempo real
- 🔄 Reiniciar o app manualmente
- 📧 Receber alertas por email

---

## 💡 Dicas Pro

### 1. Versionamento
```bash
# Tag para releases
git tag -a v1.0 -m "Versão inicial"
git push origin v1.0
```

### 2. Branches para Testes
```bash
# Criar branch de desenvolvimento
git checkout -b dev

# Deploy separado para testes
# No Streamlit: crie outro app apontando para branch 'dev'
```

### 3. Documentação no App
```python
with st.expander("📚 Como usar"):
    st.markdown("""
    1. Faça upload do arquivo
    2. Configure opções
    3. Clique em processar
    """)
```

---

## 🎓 Recursos Adicionais

- 📖 [Documentação Streamlit Cloud](https://docs.streamlit.io/streamlit-community-cloud)
- 🎥 [Vídeo Tutorial](https://www.youtube.com/watch?v=HKoOBiAaHGg)
- 💬 [Comunidade Streamlit](https://discuss.streamlit.io/)
- 🐛 [Reportar Bugs](https://github.com/streamlit/streamlit/issues)

---

## ✅ Checklist de Deploy

Antes de fazer deploy:
- [ ] Código funciona localmente
- [ ] requirements.txt completo
- [ ] README.md documentado
- [ ] .gitignore configurado
- [ ] Sem dados sensíveis no código
- [ ] Repositório no GitHub criado
- [ ] Arquivos commitados e pushed

Durante o deploy:
- [ ] Conectar GitHub ao Streamlit
- [ ] Configurar repositório correto
- [ ] Definir arquivo principal
- [ ] Adicionar secrets (se necessário)
- [ ] Aguardar build completar

Após o deploy:
- [ ] Testar todas as funcionalidades
- [ ] Compartilhar URL com equipe
- [ ] Configurar alertas (opcional)
- [ ] Documentar URL e credenciais

---

## 🎯 Exemplo de Workflow Completo

```bash
# 1. Preparar localmente
git init
git add .
git commit -m "Initial commit"

# 2. Conectar ao GitHub
git remote add origin https://github.com/seu-usuario/seu-repo.git
git push -u origin main

# 3. Deploy no Streamlit Cloud
# Acesse share.streamlit.io e configure

# 4. Atualizações futuras
git add .
git commit -m "Melhorias no enriquecimento"
git push

# App atualiza automaticamente! 🎉
```

---

## 🆘 Suporte

**Precisa de ajuda?**

1. 📖 Consulte a [documentação oficial](https://docs.streamlit.io)
2. 💬 Pergunte na [comunidade](https://discuss.streamlit.io)
3. 🐛 Reporte bugs no [GitHub](https://github.com/streamlit/streamlit/issues)

---

**Pronto para colocar seu app no ar!** 🚀

Seu enriquecedor de leads estará disponível 24/7 na nuvem, acessível de qualquer lugar!
