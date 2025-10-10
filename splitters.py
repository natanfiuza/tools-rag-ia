import sys
# Importa a classe necessária para a divisão de texto.
from langchain_text_splitters import RecursiveCharacterTextSplitter

def criar_chunks_de_texto(caminho_do_arquivo: str):
    """
    Lê um arquivo de texto e o divide em chunks semânticos usando uma estratégia recursiva.

    Args:
        caminho_do_arquivo: O caminho para o arquivo .txt a ser processado.

    Returns:
        Uma lista de strings, onde cada string é um chunk de texto, ou uma lista vazia em caso de erro.
    """
    try:
        with open(caminho_do_arquivo, 'r', encoding='utf-8') as arquivo:
            texto_completo = arquivo.read()
            print(f"Arquivo '{caminho_do_arquivo}' lido com sucesso.")
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_do_arquivo}' não foi encontrado.")
        return []
    except Exception as e:
        print(f"Ocorreu um erro inesperado ao ler o arquivo: {e}")
        return []

    # 1. Escolha da Estratégia: RecursiveCharacterTextSplitter
    # Esta é a estratégia mais robusta, pois tenta manter os parágrafos e frases juntos.
    meu_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", ". ", " ", ""],
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
        is_separator_regex=False,
    )

    # 2. Execução da Divisão
    print("Dividindo o texto em chunks...")
    lista_de_chunks = meu_splitter.split_text(texto_completo)
    print(f"O documento foi dividido em {len(lista_de_chunks)} chunks.")

    return lista_de_chunks

def salvar_chunks_em_arquivo(lista_de_chunks: list, caminho_original: str):
    """
    Salva uma lista de chunks de texto em um novo arquivo com a extensão .chunk.

    Args:
        lista_de_chunks: A lista de strings (chunks) a serem salvas.
        caminho_original: O caminho do arquivo original para determinar o nome do arquivo de saída.
    """
    # Gera o nome do arquivo de saída adicionando .chunk ao nome original.
    caminho_saida = f"{caminho_original}.chunk"
    
    print(f"Salvando os chunks no arquivo: '{caminho_saida}'...")
    
    try:
        with open(caminho_saida, 'w', encoding='utf-8') as arquivo_saida:
            for i, chunk in enumerate(lista_de_chunks):
                arquivo_saida.write(f"--- CHUNK {i + 1} (Tamanho: {len(chunk)} caracteres) ---\n")
                arquivo_saida.write(chunk)
                # Adiciona um separador visual entre os chunks para clareza
                if i < len(lista_de_chunks) - 1:
                    arquivo_saida.write("\n\n" + "="*80 + "\n\n")
        
        print("Arquivo de chunks salvo com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro ao salvar o arquivo de chunks: {e}")


# --- Ponto de Entrada do Script ---
if __name__ == "__main__":
    # 1. Validação do Argumento da Linha de Comando
    # sys.argv é uma lista que contém os argumentos passados para o script.
    # sys.argv[0] é sempre o nome do script (splitters.py).
    # sys.argv[1] é o primeiro argumento que passamos (o caminho do arquivo).
    if len(sys.argv) < 2:
        print("Erro: Nenhum arquivo informado.")
        print("Uso: python splitters.py <caminho_para_o_arquivo.txt>")
        sys.exit(1) # Encerra o script com um código de erro

    # Pega o caminho do arquivo a partir do primeiro argumento.
    caminho_arquivo_original = sys.argv[1]
    
    # 2. Processamento
    chunks_resultantes = criar_chunks_de_texto(caminho_arquivo_original)

    # 3. Salvamento do Resultado
    # Apenas tenta salvar se a criação de chunks foi bem-sucedida (não retornou uma lista vazia).
    if chunks_resultantes:
        salvar_chunks_em_arquivo(chunks_resultantes, caminho_arquivo_original)