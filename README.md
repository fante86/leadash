# 🎯 Enriquecedor de Leads B2B

Sistema web para enriquecer bases de empresas com dados de contato e decisores através de buscas automatizadas.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io)

## 🚀 Acesso Rápido

**Demo Online:** [Clique aqui para acessar o app](https://share.streamlit.io) *(adicione seu link após deploy)*

## 📋 Funcionalidades

- ✅ Upload de arquivo Excel com lista de empresas
- 🔍 Busca automatizada de:
  - 📞 Telefone
  - 📧 Email corporativo
  - 🌐 Website
  - 💼 LinkedIn da empresa
  - 👔 LinkedIn de decisores
- 📊 Dashboard com estatísticas
- 💾 Exportação de resultados

## 🖥️ Screenshots

*Adicione screenshots do seu app aqui após o deploy*

## 🛠️ Tecnologias

- Python 3.11
- Streamlit
- Pandas
- BeautifulSoup4
- Requests

## 📦 Instalação Local

```bash
# Clone o repositório
git clone https://github.com/SEU-USUARIO/SEU-REPO.git

# Entre na pasta
cd SEU-REPO

# Instale dependências
pip install -r requirements.txt

# Execute o app
streamlit run app_enriquecimento.py
```

## ☁️ Deploy no Streamlit Cloud

1. Fork este repositório
2. Acesse [share.streamlit.io](https://share.streamlit.io)
3. Conecte seu repositório
4. Deploy! 🚀

[Guia detalhado de deploy](DEPLOY_STREAMLIT_CLOUD.md)

## 📖 Documentação

- [README Completo](README.md) - Documentação técnica completa
- [Guia de Instalação](GUIA_INSTALACAO.md) - Instalação local passo a passo
- [Deploy Streamlit Cloud](DEPLOY_STREAMLIT_CLOUD.md) - Deploy na nuvem

## 🎯 Como Usar

1. **Upload:** Faça upload do arquivo Excel
2. **Configure:** Defina quantas empresas processar
3. **Processe:** Clique em "Iniciar Enriquecimento"
4. **Download:** Baixe o arquivo enriquecido

### Formato do Arquivo Excel

Seu arquivo deve conter:
- `name`: Nome da empresa
- `city`: Cidade
- `state`: Estado

## 📊 Taxa de Sucesso

| Dado | Taxa Esperada |
|------|---------------|
| Telefone | 30-60% |
| Email | 20-50% |
| Website | 40-70% |
| LinkedIn | 30-60% |

## ⚙️ Configuração de APIs (Opcional)

Para melhor qualidade dos dados, configure no Streamlit Cloud:

```toml
# .streamlit/secrets.toml
[api_keys]
hunter = "sua-chave-hunter-io"
serper = "sua-chave-serper"
```

APIs gratuitas disponíveis:
- [Hunter.io](https://hunter.io) - 50 buscas/mês
- [Serper](https://serper.dev) - 2500 buscas/mês

## 🔒 Privacidade e LGPD

⚠️ **Importante:**
- Use apenas para prospecção B2B legítima
- Respeite a LGPD
- Ofereça opt-out em comunicações
- Não compartilhe dados pessoais

## 🤝 Contribuindo

Contribuições são bem-vindas!

1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto é de código aberto para uso comercial e não comercial.

## 👨‍💻 Autor

Desenvolvido para profissionais de Pre Sales

## 🆘 Suporte

- 📖 Consulte a [documentação completa](README.md)
- 🐛 [Reporte bugs](https://github.com/SEU-USUARIO/SEU-REPO/issues)
- 💬 Dúvidas? Abra uma [issue](https://github.com/SEU-USUARIO/SEU-REPO/issues/new)

## ⭐ Star o projeto

Se este projeto foi útil para você, considere dar uma ⭐!

---

**Desenvolvido com ❤️ para equipes de Pre Sales**
