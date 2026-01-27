# 🎯 Sistema de Enriquecimento de Leads B2B

Sistema desenvolvido para equipes de Pre Sales enriquecerem bases de empresas com informações de contato e decisores através de pesquisas automatizadas na web.

## 📋 Funcionalidades

- ✅ Upload de arquivo Excel com lista de empresas
- 🔍 Busca automatizada por:
  - 📞 Telefone de contato
  - 📧 Email corporativo
  - 🌐 Website oficial
  - 💼 LinkedIn da empresa
  - 👔 LinkedIn de decisores (CEO, Diretor, Gerente)
- 📊 Dashboard com estatísticas de enriquecimento
- 💾 Exportação de resultados em Excel
- ⚡ Processamento em lotes configurável

## 🚀 Como Instalar

### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Instalação

1. Clone ou baixe os arquivos do projeto

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## 💻 Como Usar

1. **Inicie o aplicativo:**
```bash
streamlit run app_enriquecimento.py
```

2. **Acesse no navegador:**
   - O Streamlit abrirá automaticamente em `http://localhost:8501`
   - Ou acesse manualmente esse endereço

3. **Faça upload do arquivo Excel:**
   - Clique em "Browse files" e selecione seu arquivo
   - O arquivo deve ter as colunas: `name`, `city`, `state`

4. **Configure o processamento:**
   - Defina quantas empresas processar (recomendado: 10-20 por vez)
   - Ajuste o delay entre buscas (padrão: 2 segundos)

5. **Inicie o enriquecimento:**
   - Clique no botão "Iniciar Enriquecimento"
   - Acompanhe o progresso em tempo real

6. **Baixe os resultados:**
   - Após o processamento, clique em "Download Excel Enriquecido"
   - O arquivo conterá todos os dados originais + dados enriquecidos

## 📁 Estrutura do Arquivo Excel

### Colunas Obrigatórias (Input)
- `name`: Nome da empresa
- `city`: Cidade
- `state`: Estado

### Colunas Adicionadas (Output)
- `telefone_encontrado`: Telefone(s) encontrado(s)
- `email_encontrado`: Email(s) encontrado(s)
- `website_encontrado`: Website encontrado
- `linkedin_empresa`: LinkedIn corporativo
- `linkedin_decisores`: LinkedIn de decisores
- `status_enriquecimento`: Status do processo

## ⚙️ Configurações

### Processamento em Lotes
Recomenda-se processar empresas em lotes de 10-20 para:
- Evitar bloqueios por excesso de requisições
- Manter performance adequada
- Facilitar validação manual dos resultados

### Delay entre Requisições
- **Mínimo:** 1 segundo
- **Recomendado:** 2-3 segundos
- **Conservador:** 5 segundos

## 🎯 Melhores Práticas

### Para Pre Sales
1. **Validação Manual**: Sempre valide os dados encontrados
2. **Complementação**: Use outras fontes (LinkedIn Sales Navigator, Apollo.io)
3. **Segmentação**: Processe por região/segmento para melhor qualidade
4. **Priorização**: Foque nas empresas com maior potencial primeiro

### Dados de Qualidade
- ✅ Priorize empresas com endereço completo
- ✅ Verifique se o nome está correto (sem abreviações)
- ✅ Confirme a cidade e estado antes do processamento
- ⚠️ Empresas com nomes genéricos podem ter resultados imprecisos

## ⚠️ Limitações e Considerações

### Técnicas
- **Taxa de sucesso:** Varia entre 30-70% dependendo da empresa
- **Tempo de processamento:** ~5-10 segundos por empresa
- **Dados públicos:** Apenas informações disponíveis publicamente
- **Validação necessária:** Resultados devem ser verificados manualmente

### Legais
- ✅ Respeite a LGPD (Lei Geral de Proteção de Dados)
- ✅ Use dados apenas para fins legítimos de prospecção B2B
- ✅ Ofereça opt-out em suas comunicações
- ⚠️ Não compartilhe dados sensíveis

## 🔧 Troubleshooting

### "Erro na busca"
- Verifique sua conexão com a internet
- Aumente o delay entre requisições
- Processe menos empresas por vez

### "Sem dados encontrados"
- Nome da empresa pode estar incorreto
- Empresa pode não ter presença digital
- Tente buscar manualmente para confirmar

### "Processamento lento"
- Normal para lotes grandes
- Reduza o número de empresas
- Aumente o delay se necessário

## 📈 Próximos Passos

Após enriquecer seus leads:

1. **Validação de Email:** Use Hunter.io ou ZeroBounce
2. **Enriquecimento Adicional:** Apollo.io, Clearbit
3. **Verificação de LinkedIn:** Confirme perfis manualmente
4. **Segmentação:** Agrupe por potencial e prioridade
5. **Ação:** Inicie cadência de prospecção

## 🤝 Suporte

Para melhorias ou problemas:
- Revise a documentação
- Verifique os logs de erro no terminal
- Teste com uma amostra pequena primeiro

## 📝 Changelog

### v1.0.0
- ✨ Versão inicial
- 🔍 Busca de telefone, email, website
- 💼 Busca de LinkedIn empresa e decisores
- 📊 Dashboard de estatísticas
- 💾 Exportação para Excel

---

**Desenvolvido para equipes de Pre Sales** 🎯
