# ZEUS • Copiloto Local Integrado à Wiki NHD (RAG + Ollama + Qdrant)

O **ZEUS** é um copiloto local, seguro e totalmente offline, integrado à **Wiki NHD**, baseado em:

- 🔹 **FastAPI**
- 🔹 **Qdrant (Vector Database)**
- 🔹 **Sentence Transformers (Embeddings)**
- 🔹 **Ollama (Modelos de Linguagem Locais)**
- 🔹 **Interface Web integrada à Wiki NHD**

O objetivo do ZEUS é fornecer um assistente que responde com base em uma **Base de Conhecimento institucional** (arquivos `.md` da Wiki NHD), de forma similar ao *Salesforce Einstein Copilot*, porém **100% local, privado e sob controle interno**.

---

# 🚀 Arquitetura Geral

Usuário → Wiki NHD (Botão Zeus) → Backend Wiki (FastAPI) → ZEUS Backend (FastAPI) → RAG (Qdrant) → Ollama → Resposta + Fontes

---

# 📦 Estrutura do Projeto

zeus_00/
├─ backend/
│ ├─ app/
│ │ ├─ main.py              # API principal (/chat híbrido e /rag)
│ │ ├─ rag.py               # Inteligência RAG
│ │ ├─ chat.py              # Fallback LLM (sem RAG)
│ │ ├─ embedder.py          # Geração de embeddings
│ │ ├─ qclient.py           # Cliente Qdrant (search e upsert)
│ │ ├─ ollama_client.py     # Integração com Ollama
│ │ └─ templates/static
│ └─ requirements.txt
│
├─ indexador/
│ └─ indexar.py              # Indexação dos artigos da Wiki NHD
│
├─ docker-compose.yml        # Banco vetorial (Qdrant)
├─ .gitignore
└─ README.md

---

# 🛠 Instalação Completa (Linux / Ubuntu)

## 1️⃣ Clonar o repositório

git clone https://github.com/mvsaraujo-ti/zeus_01  
cd zeus_01

## 2️⃣ Subir o Qdrant (Banco Vetorial)

O Qdrant é responsável por armazenar os embeddings da base de conhecimento.

docker-compose up -d

Verifique se está rodando:

docker ps

Você deve ver algo como:

qdrant/qdrant:latest   Up   0.0.0.0:6333->6333/tcp

Acesse o painel:

http://localhost:6333/dashboard

## 3️⃣ Instalar dependências do backend

cd backend  
python3 -m venv venv  
source venv/bin/activate  
pip install -r requirements.txt

## 4️⃣ Rodar o backend do ZEUS

uvicorn app.main:app --host 0.0.0.0 --port 8601

Acesse a documentação:

http://localhost:8601/docs

---

# 🛠 Instalação Completa (Windows)

## 1️⃣ Pré-requisitos

- Windows 10 ou superior  
- Python 3.10+  
- Docker Desktop  
- Ollama para Windows  

Instale o Ollama em:  
https://ollama.com

## 2️⃣ Clonar o repositório

git clone https://github.com/mvsaraujo-ti/zeus_00  
cd zeus_00

## 3️⃣ Subir o Qdrant (Docker)

docker compose up -d

Verifique:

docker ps

## 4️⃣ Criar ambiente virtual e instalar dependências

cd backend  
python -m venv venv  
venv\Scripts\activate  
pip install -r requirements.txt

## 5️⃣ Rodar o backend

uvicorn app.main:app --host 0.0.0.0 --port 8601

Acesse:

http://localhost:8601/docs

---

# 📚 Base de Conhecimento (Wiki NHD)

A **única fonte de conhecimento do ZEUS** é a **Wiki NHD**, localizada em:

/home/zeus/DEV/Wiki-NHD/articles

Todos os arquivos `.md` dessa pasta são utilizados como base de conhecimento.

Exemplo:

articles/
├─ vpn.md
├─ sistema-sentinela-tjma.md
├─ acesso-brbjus-procedimentos-oficiais.md
├─ contatos-oficiais-suporte-tjma.md

⚠️ Qualquer alteração na Wiki exige reindexação.

---

# 🔍 Indexação da Base de Conhecimento

Sempre que um artigo for criado, alterado ou removido:

cd ~/DEV/zeus_00/indexador  
python3 indexar.py

Você verá algo como:

Indexando: vpn.md  
Indexação concluída!

Isso envia os artigos da Wiki para o Qdrant.

---

# 🤖 API / Chat Híbrido

## POST /chat

O endpoint `/chat` funciona de forma híbrida:

1. O ZEUS tenta responder usando **RAG (Wiki NHD)**  
2. Caso não haja contexto suficiente, utiliza o **LLM local (Ollama)**  
3. O ZEUS não inventa informações fora da base indexada  
4. As respostas são objetivas e profissionais  

Exemplo de requisição:

{
  "message": "O que é VPN?"
}

---

# ⚙️ Modelos de Linguagem (Ollama)

Modelo recomendado:

qwen2.5:3b-instruct

Modelos alternativos:

llama3.2:3b  
llama3.2:1b  

---

# 🔐 Segurança e Privacidade

✔ Execução totalmente local  
✔ Nenhum dado enviado para a nuvem  
✔ Sem APIs externas  
✔ Base de conhecimento controlada internamente  
✔ Adequado para ambientes institucionais  

---

# 📌 Status Atual do Projeto

✔ Wiki NHD integrada  
✔ RAG funcionando  
✔ Qdrant funcionando (Docker)  
✔ Indexador funcional  
✔ Backend estável  
✔ Ollama integrado  

---

# 🛠 Próximos Passos

- Indexação automática da Wiki  
- Controle de permissões por usuário  
- Logs e auditoria de perguntas  
- Métricas de uso  
- Painel administrativo do ZEUS  

---

# 📄 Licença

Projeto de uso privado e educacional.  
Não destinado à distribuição pública.

---

# 👤 Autor

Maxwell Araújo  
GitHub: mvsaraujo-ti  
E-mail: maxwellaraujoti@gmail.com
