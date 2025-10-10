import json
import os
from typing import List
from langchain.schema.document import Document

def exportar_para_json(chunks: List[Document], vetores: List[List[float]], caminho_arquivo_original: str):
    """
    Exporta os chunks de texto e seus vetores correspondentes para um arquivo JSON.

    Args:
        chunks (List[Document]): A lista de chunks de texto (objetos Document do LangChain).
        vetores (List[List[float]]): A lista de embeddings (vetores).
        caminho_arquivo_original (str): O caminho do arquivo que foi processado.
    """
    # Prepara a lista de dados para serialização em JSON.
    dados_para_salvar = []
    
    # Combina cada chunk de texto com seu respectivo vetor.
    for chunk, vetor in zip(chunks, vetores):
        dados_para_salvar.append({
            'fonte': chunk.metadata.get('source', 'N/A'),
            'texto': chunk.page_content,
            'vetor': vetor  # O vetor já é uma lista de floats, perfeita para JSON.
        })
    
    # Define o nome do arquivo de saída. Ex: 'meu_doc.pdf' -> 'meu_doc.pdf.json'
    nome_base_arquivo = os.path.basename(caminho_arquivo_original)
    caminho_saida = f"{nome_base_arquivo}.json"
    
    print(f"Exportando {len(dados_para_salvar)} chunks vetorizados para o arquivo: '{caminho_saida}'...")

    try:
        with open(caminho_saida, 'w', encoding='utf-8') as f:
            # json.dump escreve a lista de dicionários no arquivo.
            # indent=4 formata o JSON para ser legível por humanos.
            # ensure_ascii=False garante que caracteres acentuados (pt-BR) sejam salvos corretamente.
            json.dump(dados_para_salvar, f, indent=4, ensure_ascii=False)
        
        print(f"Arquivo '{caminho_saida}' salvo com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro ao salvar o arquivo JSON: {e}")