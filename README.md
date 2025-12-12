# ZEUS • Copiloto Local (RAG + Ollama + Qdrant)

O **ZEUS** é um copiloto local, seguro e totalmente offline, baseado em:

- 🔹 **FastAPI**  
- 🔹 **Qdrant (Vector Database)**  
- 🔹 **Sentence Transformers (MiniLM)**  
- 🔹 **Ollama (Modelos locais)**  
- 🔹 **Extensão Tampermonkey**  

O objetivo do ZEUS é fornecer um assistente que responde com base em uma **Base de Conhecimento interna** (arquivos `.md`), de forma similar ao *Salesforce Einstein Copilot*, mas **100% local e privado**.

---

# 🚀 Arquitetura Geral



Usuário → Extensão Tampermonkey → Backend FastAPI → RAG (Qdrant) → Ollama → Resposta + Fontes


---

# 📦 Estrutura do Projeto



Zeus00/
├─ articles/ # Base de conhecimento (.md)
├─ backend/
│ ├─ app/
│ │ ├─ main.py # Rotas /chat e /rag
│ │ ├─ rag.py # Inteligência RAG
│ │ ├─ chat.py
│ │ ├─ embedder.py
│ │ ├─ qclient.py
│ │ ├─ ollama_client.py
│ │ └─ templates/static
│ ├─ venv/ # Ambiente virtual (ignorado no Git)
│ └─ requirements.txt
├─ indexador/
│ └─ indexar.py # Indexação dos artigos no Qdrant
├─ docker-compose.yml # Banco vetorial (Qdrant)
├─ start_zeus.bat # Inicialização completa (opcional)
├─ .gitignore
└─ README.md


---

# 🛠 Instalação Completa (Windows)

## 1️⃣ Clone o repositório

```bash
git clone https://github.com/mvsaraujo-ti/zeus_00
cd zeus_00

2️⃣ Subir o Qdrant (banco vetorial)

O Qdrant é responsável por armazenar embeddings da base de conhecimento.

docker compose up -d


Verifique se está rodando:

docker ps


Você deve ver algo como:

qdrant/qdrant:latest   Up   0.0.0.0:6333->6333/tcp

3️⃣ Instalar dependências do backend
cd backend
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt

4️⃣ Rodar o backend
uvicorn app.main:app --host 0.0.0.0 --port 8000


Acesse a documentação:

➡ http://localhost:8000/docs

📚 Base de Conhecimento

Coloque seus artigos em:

/articles


Formato:

articles/
 ├─ vpn.md
 ├─ sentinela_perfis.md
 ├─ senhas.md
 └─ sistemas.md


Arquivo exemplo (vpn.md):

Para acessar a VPN:

1. Abra o Global Protect.
2. Selecione "VPN".
3. Informe usuário e senha.
4. Clique em "Conectar".

🔍 Indexação da Base de Conhecimento

Depois de adicionar ou alterar artigos:

cd indexador
python indexar.py


Você verá:

Indexando: vpn.md
Indexação concluída!


Isso envia todos os arquivos .md para o Qdrant.

🤖 API / RAG
POST /rag

Busca artigos relevantes e gera resposta usando o Ollama.

Exemplo de requisição:

{
  "message": "Como acesso a VPN?"
}


Exemplo de resposta:

{
  "answer": "Para acessar a VPN, abra o Global Protect...",
  "sources": ["vpn.md"]
}

🧩 Extensão Tampermonkey

O frontend do ZEUS funciona com um script Tampermonkey que:

injeta um painel estilo ChatGPT

envia mensagens para o backend /chat ou /rag

exibe respostas em tempo real

Basta instalar o script fornecido em:

extension/zeus.user.js

📌 Status Atual do Projeto

✔ RAG funcionando
✔ Qdrant funcionando (Docker)
✔ Indexador funcional
✔ Backend estável
✔ Extensão funcionando
✔ Base inicial criada

🛠 Próximos Passos

Painel web para edição da Knowledge Base

Personalização da interface da extensão

Criar instalador automatizado (PowerShell)

Log e auditoria de perguntas

Controle de permissões por usuário

📄 Licença

Projeto de uso privado e educacional.
Não destinado à distribuição pública.

Autor

Maxwell Araújo
💼 mvsaraujo-ti
📧 maxwellaraujoti@gmail.com
# zeus_01
