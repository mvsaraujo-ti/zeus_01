ZEUS — GUIA DE INSTALAÇÃO E INICIALIZAÇÃO
=======================================

Este documento descreve como instalar e iniciar o ZEUS
(Copiloto Local com RAG + Ollama + Qdrant),
integrado à Wiki NHD.

-------------------------------------------------------
PRÉ-REQUISITOS (LINUX / UBUNTU)
-------------------------------------------------------

- Ubuntu 20.04 ou superior
- Python 3.10 ou superior
- Docker e Docker Compose
- Ollama instalado
- Git

-------------------------------------------------------
PRÉ-REQUISITOS (WINDOWS)
-------------------------------------------------------

- Windows 10 ou superior
- Python 3.10 ou superior
- Docker Desktop
- Ollama para Windows
- Git

Instalar Ollama:
https://ollama.com

-------------------------------------------------------
1. CLONAR O REPOSITÓRIO
-------------------------------------------------------

git clone https://github.com/mvsaraujo-ti/zeus_00
cd zeus_00

-------------------------------------------------------
2. SUBIR O QDRANT (BANCO VETORIAL)
-------------------------------------------------------

O Qdrant armazena os embeddings da base de conhecimento.

docker-compose up -d

Verificar se está rodando:

docker ps

Esperado:
qdrant/qdrant:latest   Up   0.0.0.0:6333->6333/tcp

Painel do Qdrant:
http://localhost:6333/dashboard

-------------------------------------------------------
3. INSTALAR DEPENDÊNCIAS DO BACKEND (LINUX)
-------------------------------------------------------

cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

-------------------------------------------------------
3. INSTALAR DEPENDÊNCIAS DO BACKEND (WINDOWS)
-------------------------------------------------------

cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

-------------------------------------------------------
4. VERIFICAR O OLLAMA
-------------------------------------------------------

Verificar se o Ollama está rodando:

ollama list

Modelo recomendado:

ollama pull qwen2.5:3b-instruct

O Ollama deve escutar em:
http://localhost:11434

-------------------------------------------------------
5. CONFIGURAR BASE DE CONHECIMENTO
-------------------------------------------------------

O ZEUS utiliza os artigos da Wiki NHD:

/home/zeus/DEV/Wiki-NHD/articles

Todos os arquivos devem estar em formato .md

Exemplo:
vpn.md
sistema-sentinela-tjma.md
contatos-oficiais.md

-------------------------------------------------------
6. INDEXAR A BASE DE CONHECIMENTO
-------------------------------------------------------

Sempre que alterar ou criar artigos:

cd ~/DEV/zeus_00/indexador
python3 indexar.py

Saída esperada:
Indexando: vpn.md
Indexação concluída!

-------------------------------------------------------
7. INICIAR O BACKEND DO ZEUS
-------------------------------------------------------

cd ~/DEV/zeus_00/backend
uvicorn app.main:app --host 0.0.0.0 --port 8601

Documentação da API:
http://localhost:8601/docs

-------------------------------------------------------
8. INTEGRAÇÃO COM A WIKI NHD
-------------------------------------------------------

A Wiki NHD consome o ZEUS via HTTP.

Endpoint principal:
/chat  -> chat híbrido (RAG + LLM)
/rag   -> somente RAG

Porta padrão do ZEUS:
8601

-------------------------------------------------------
9. FLUXO DE FUNCIONAMENTO
-------------------------------------------------------

1. Usuário acessa a Wiki NHD
2. Clica no botão Zeus
3. Pergunta é enviada ao backend da Wiki
4. Wiki chama o ZEUS (/chat)
5. ZEUS:
   - tenta responder via RAG (Wiki NHD)
   - se não houver contexto suficiente, usa o Ollama
6. Resposta retorna ao chat da Wiki

-------------------------------------------------------
10. OBSERVAÇÕES IMPORTANTES
-------------------------------------------------------

- O ZEUS NÃO aprende automaticamente
- Sempre reindexar após alterar artigos
- O desempenho depende do modelo Ollama escolhido
- Todo o processamento é LOCAL
- Nenhum dado sai da máquina

-------------------------------------------------------
STATUS FINAL ESPERADO
-------------------------------------------------------

[OK] Qdrant rodando
[OK] Ollama rodando
[OK] Base indexada
[OK] Backend ZEUS ativo
[OK] Wiki integrada

-------------------------------------------------------
AUTOR
-------------------------------------------------------

Maxwell Araújo
GitHub: mvsaraujo-ti
E-mail: maxwellaraujoti@gmail.com
