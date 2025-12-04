import os
import json
import time
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env para o ambiente
load_dotenv()

# Importa apenas a função de embedding
from src.embedding_gemini import obter_modelo_embedding_gemini

# Nome do arquivo JSON de entrada
ARQUIVO_ENTRADA = "data/raw/REGRA_DE_VIDA_EM_ADORACAO_FINAL.json"
# Nome do arquivo de saída (pode ser o mesmo se quiser sobrescrever)
ARQUIVO_SAIDA = "data/raw/REGRA_DE_VIDA_EM_ADORACAO_VETORIZADO.json"

def carregar_json(caminho):
    """Carrega os dados do arquivo JSON."""
    if not os.path.exists(caminho):
        print(f"Erro: O arquivo '{caminho}' não foi encontrado.")
        return None
    
    with open(caminho, 'r', encoding='utf-8') as f:
        return json.load(f)

def salvar_json(dados, caminho):
    """Salva os dados em um arquivo JSON."""
    try:
        with open(caminho, 'w', encoding='utf-8') as f:
            json.dump(dados, f, ensure_ascii=False, indent=4)
        print(f"Arquivo salvo com sucesso em: {caminho}")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")

def processar_json_existente():
    """
    Lê o JSON existente, gera embeddings para os textos e salva o resultado.
    """
    print(f"Lendo arquivo: {ARQUIVO_ENTRADA}")
    dados = carregar_json(ARQUIVO_ENTRADA)
    
    if not dados:
        return

    print(f"Total de chunks encontrados: {len(dados)}")

    # Inicializa o modelo do Gemini
    try:
        modelo_embedding = obter_modelo_embedding_gemini()
    except Exception as e:
        print(f"Erro ao inicializar o modelo Gemini: {e}")
        return

    # Prepara a lista de textos para vetorização
    textos_para_vetorizar = [item['texto'] for item in dados]
    
    print("Gerando embeddings com Gemini... (Isso pode levar alguns segundos)")
    
    try:
        # Gera os vetores em lote
        # Nota: O LangChain/Gemini geralmente lida bem com lotes, 
        # mas se o arquivo for muito grande, pode ser necessário processar em partes menores.
        vetores = modelo_embedding.embed_documents(textos_para_vetorizar)
        
        if len(vetores) != len(dados):
            print(f"Erro: Quantidade de vetores gerados ({len(vetores)}) difere da quantidade de chunks ({len(dados)}).")
            return

        # Atribui os vetores de volta aos objetos originais
        for i, item in enumerate(dados):
            item['vetor'] = vetores[i]
            
        print("Embeddings gerados e atribuídos com sucesso.")
        
        # Salva o novo JSON mantendo toda a estrutura original
        salvar_json(dados, ARQUIVO_SAIDA)

    except Exception as e:
        print(f"Ocorreu um erro durante a geração dos embeddings: {e}")

def exibir_menu():
    """Exibe o menu de opções."""
    print("\n--- GERADOR DE EMBEDDINGS PARA JSON (GEMINI) ---")
    print(f"Arquivo alvo: {ARQUIVO_ENTRADA}")
    print("1. Processar JSON e Gerar Vetores")
    print("2. Sair")
    return input("Escolha uma opção: ")

def main():
    while True:
        escolha = exibir_menu()

        if escolha == '1':
            processar_json_existente()
        elif escolha == '2':
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()