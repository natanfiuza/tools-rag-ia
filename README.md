# Ferramentas para RAG com IA

 Bem-vindo ao repositório **tools-rag-ia**\! Este projeto é uma coleção de ferramentas e scripts em Python desenvolvidos para facilitar a implementação e experimentação com o padrão **RAG (Retrieval-Augmented Generation)** utilizando modelos de linguagem (LLMs).

O objetivo é fornecer uma base sólida e didática para desenvolvedores, especialmente aqueles que estão começando a explorar o fascinante mundo da Inteligência Artificial Generativa.

## O que é RAG?

Antes de mergulhar nas ferramentas, vamos entender o conceito principal.

**RAG (Retrieval-Augmented Generation)** é uma arquitetura de IA que combina a força de um modelo de linguagem pré-treinado (como o GPT) com um sistema de recuperação de informação.

**Como funciona de forma simples?**

1.  **Pergunta do Usuário:** O usuário faz uma pergunta.
2.  **Busca (Retrieval):** Em vez de ir direto para o LLM, o sistema primeiro busca em uma base de conhecimento específica (documentos, PDFs, sites, etc.) as informações mais relevantes para a pergunta.
3.  **Acréscimo (Augmentation):** As informações encontradas são inseridas no *prompt* que será enviado ao LLM, junto com a pergunta original do usuário. Isso dá ao modelo um contexto preciso e atualizado.
4.  **Geração (Generation):** O LLM, agora com o contexto adicional, gera uma resposta muito mais precisa, detalhada e baseada nos fatos encontrados, reduzindo drasticamente as "alucinações" (informações incorretas).

Essa abordagem é poderosa para criar chatbots, assistentes de Q\&A e sistemas que precisam responder com base em um conhecimento privado ou muito específico.

## Sobre este Repositório

Este projeto nasceu da necessidade de simplificar o processo de construção de sistemas RAG. Aqui você encontrará scripts para:

  * **Processamento de Documentos:** Ferramentas para ler diferentes formatos de arquivo (como `.txt` e `.pdf`), limpá-los e dividi-los em pedaços menores (`chunks`).
  * **Geração de Embeddings:** Scripts para converter os `chunks` de texto em vetores numéricos (embeddings), que é como a IA entende a semântica do texto.
  * **Armazenamento e Busca Vetorial:** Exemplos de como usar bancos de dados vetoriais (como o ChromaDB) para armazenar esses embeddings e realizar buscas de similaridade de forma eficiente.

## Estrutura do Projeto

```
/
├── data/ # Pasta para colocar seus documentos (PDFs, TXTs, etc)
│   └── raw/ # Documentos brutos
├── notebooks/ # Jupyter notebooks com exemplos práticos (se aplicável)
├── src/ # Código fonte principal
│   ├── chunking.py # Lógica para dividir os textos
│   ├── embedding.py # Lógica para gerar os embeddings
│   └── vector_store.py # Lógica para interagir com o banco vetorial
└── main.py # Script principal para orquestrar o processo
```

## Tecnologias Utilizadas

  * **Python 3.10+**
  * **LangChain:** Para orquestrar os componentes do RAG.
  * **ChromaDB:** Para o armazenamento e busca vetorial local.
  * **SentenceTransformers:** Para a geração dos embeddings.
  * **PyPDF2:** Para a leitura de arquivos PDF.

## Como Começar

Siga os passos abaixo para configurar e executar o projeto em sua máquina local.

### Pré-requisitos

  * Python 3.10 ou superior instalado.
  * Pip (gerenciador de pacotes do Python).

### 1\. Clone o Repositório

```bash
git clone https://github.com/natanfiuza/tools-rag-ia.git
cd tools-rag-ia
```

### 2\. Crie um Ambiente Virtual (Recomendado)

É uma boa prática isolar as dependências do projeto para evitar conflitos.

```bash
# Para Linux/macOS
python3 -m venv .venv
source .venv/bin/activate

# Para Windows
python -m venv .venv
.\.venv\Scripts\activate
```

### 3\. Instale as Dependências

Todos os pacotes necessários estão listados no arquivo `requirements.txt`.

```bash
pip install -r requirements.txt
```

### 4\. Adicione seus Documentos

Coloque os arquivos (`.pdf`, `.txt`, etc.) que você deseja usar como base de conhecimento dentro da pasta `data/raw/`.

### 5\. Execute o Projeto

O script principal irá processar os documentos, gerar os embeddings e armazená-los no banco de dados vetorial.

```bash
python main.py
```

Após a execução, uma pasta `chroma_db` será criada na raiz do projeto, contendo os vetores gerados. Agora você está pronto para fazer consultas\!

## Casos de Uso

Você pode adaptar estas ferramentas para diversos cenários, como:

  * **Chatbot de Atendimento ao Cliente:** Treine-o com manuais de produtos, políticas da empresa e FAQs para responder perguntas dos clientes com precisão.
  * **Assistente de Documentação Técnica:** Alimente o sistema com a documentação de uma API ou software para ajudar desenvolvedores a encontrar a informação que precisam rapidamente.
  * **Análise de Contratos:** Use o RAG para fazer perguntas específicas sobre cláusulas e termos em longos documentos jurídicos.

## Como Contribuir

A sua contribuição é muito bem-vinda\! Se você tem ideias para novas ferramentas, melhorias nos scripts existentes ou encontrou algum bug, sinta-se à vontade para:

1.  **Abrir uma Issue:** Descreva a sua sugestão ou o problema encontrado.
2.  **Fazer um Fork:** Crie uma cópia do repositório para a sua conta.
3.  **Criar uma Branch:** Crie uma nova branch para a sua feature (`git checkout -b feature/minha-feature`).
4.  **Commitar suas Mudanças:** (`git commit -m 'Adiciona minha feature'`).
5.  **Enviar um Pull Request:** Abra um Pull Request para que possamos revisar e integrar sua contribuição.

Vamos construir juntos uma ferramenta incrível para a comunidade\!

## Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](https://www.google.com/search?q=LICENSE) para mais detalhes.

