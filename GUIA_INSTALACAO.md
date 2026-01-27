# 🚀 GUIA RÁPIDO DE INSTALAÇÃO

## Instalação em 3 Passos

### 1️⃣ Instalar Python
Se você ainda não tem Python instalado:
- Windows: Baixe em https://www.python.org/downloads/
- Mac: `brew install python3`
- Linux: `sudo apt install python3 python3-pip`

### 2️⃣ Instalar Dependências
Abra o terminal/prompt de comando na pasta do projeto e execute:
```bash
pip install -r requirements.txt
```

### 3️⃣ Executar o Aplicativo
```bash
streamlit run app_enriquecimento.py
```

## 📱 Escolha sua Versão

### Versão Básica (app_enriquecimento.py)
- ✅ Pronta para usar imediatamente
- ✅ Não precisa de APIs externas
- ✅ Ideal para começar
- ⚠️ Taxa de sucesso: 30-50%

**Como usar:**
```bash
streamlit run app_enriquecimento.py
```

### Versão Avançada (app_enriquecimento_avancado.py)
- 🚀 Maior taxa de sucesso (50-70%)
- 🔑 Suporta APIs especializadas
- 📊 Melhor qualidade de dados
- 💼 Recomendada para uso profissional

**Como usar:**
```bash
streamlit run app_enriquecimento_avancado.py
```

## 🔑 APIs Recomendadas (Opcional)

### Hunter.io
- **Para:** Encontrar emails corporativos
- **Grátis:** 50 buscas/mês
- **Como obter:** https://hunter.io/users/sign_up

### Serper
- **Para:** Melhorar qualidade das buscas
- **Grátis:** 2.500 buscas/mês
- **Como obter:** https://serper.dev/

## 🎯 Fluxo de Trabalho Recomendado

1. **Preparar dados:**
   - Arquivo Excel com colunas: name, city, state
   - Verificar se nomes estão corretos

2. **Primeira rodada (10 empresas):**
   - Testar com amostra pequena
   - Validar qualidade dos resultados
   - Ajustar configurações se necessário

3. **Processamento completo:**
   - Processar em lotes de 20-30 empresas
   - Fazer pausas entre lotes (evita bloqueios)

4. **Validação:**
   - Revisar dados encontrados
   - Complementar manualmente quando necessário
   - Verificar LinkedIn dos decisores

5. **Ação:**
   - Importar para CRM
   - Iniciar cadência de prospecção

## 🆘 Resolução de Problemas

### "Comando não encontrado"
```bash
# Windows
python -m streamlit run app_enriquecimento.py

# Mac/Linux
python3 -m streamlit run app_enriquecimento.py
```

### "Módulo não encontrado"
```bash
pip install --upgrade -r requirements.txt
```

### "Erro de permissão"
```bash
# Windows: Execute como Administrador
# Mac/Linux:
pip install --user -r requirements.txt
```

### Processamento lento
- Reduza o número de empresas por lote
- Aumente o delay entre buscas
- Verifique sua conexão de internet

## 💡 Dicas de Pre Sales

### Para Maximizar Resultados:
1. ✅ Use nomes completos das empresas
2. ✅ Confirme cidade e estado corretos
3. ✅ Processe empresas similares juntas
4. ✅ Valide todos os dados encontrados
5. ✅ Complemente com LinkedIn Sales Navigator

### Dados de Qualidade:
- 📞 Telefones: Valide antes de ligar
- 📧 Emails: Use verificador (NeverBounce, ZeroBounce)
- 💼 LinkedIn: Confirme que é a pessoa certa
- 🎯 Decisores: Pesquise mais sobre o cargo

## 📊 Benchmarks

### Taxa de Sucesso Esperada:

| Dado | Versão Básica | Versão Avançada |
|------|---------------|-----------------|
| Telefone | 30-40% | 50-60% |
| Email | 20-30% | 40-50% |
| Website | 40-50% | 60-70% |
| LinkedIn Empresa | 30-40% | 50-60% |
| LinkedIn Decisor | 10-20% | 30-40% |

### Tempo de Processamento:
- Versão Básica: ~8-10 seg/empresa
- Versão Avançada: ~12-15 seg/empresa

## 🔒 LGPD e Privacidade

⚠️ **IMPORTANTE:**
- Use apenas para prospecção B2B legítima
- Ofereça sempre opção de opt-out
- Não compartilhe dados pessoais
- Respeite pedidos de remoção
- Mantenha dados seguros

## 📞 Próximos Passos

Após enriquecer seus dados:

1. **Validação** (mesmo dia)
   - Conferir dados manualmente
   - Remover duplicatas
   - Priorizar leads quentes

2. **Enriquecimento adicional** (dia seguinte)
   - LinkedIn Sales Navigator
   - Apollo.io
   - Clearbit

3. **Preparação para contato** (2-3 dias)
   - Pesquisar sobre as empresas
   - Personalizar mensagens
   - Definir cadência

4. **Ação** (início da semana)
   - Importar para CRM
   - Iniciar prospecção
   - Acompanhar métricas

## ✅ Checklist de Uso

Antes de começar:
- [ ] Python instalado
- [ ] Dependências instaladas
- [ ] Arquivo Excel preparado
- [ ] Nomes das empresas verificados
- [ ] Cidade e estado confirmados

Durante o processo:
- [ ] Começar com amostra pequena
- [ ] Monitorar qualidade dos dados
- [ ] Fazer pausas entre lotes
- [ ] Salvar resultados frequentemente

Após o processamento:
- [ ] Validar todos os dados
- [ ] Complementar informações
- [ ] Remover duplicatas
- [ ] Importar para CRM
- [ ] Iniciar cadência

## 🎓 Recursos Adicionais

- 📖 [Documentação Streamlit](https://docs.streamlit.io)
- 🔍 [Hunter.io API Docs](https://hunter.io/api-documentation)
- 💼 [Melhores práticas de Pre Sales](https://www.gartner.com/en/sales)

---

**Desenvolvido para profissionais de Pre Sales** 🎯

Sucesso na sua prospecção! 🚀
