import os
from src.chunking import processar_documentos
from src.embedding import obter_modelo_embedding
from src.vector_store import criar_e_armazenar_vetores, realizar_busca_por_similaridade

# Define os caminhos principais usados pelo programa
CAMINHO_DOCUMENTOS_RAW = "data/raw"
CAMINHO_DB = "chroma_db"

def exibir_menu():
    """Exibe o menu de opções para o usuário."""
    print("\n--- MENU DE FERRAMENTAS RAG ---")
    print("1. Processar e Vetorizar Documentos")
    print("2. Fazer uma Pergunta (Busca por Similaridade)")
    print("3. Sair")
    return input("Escolha uma opção: ")

def main():
    """
    Função principal que executa o loop do menu interativo.
    """
    # Garante que o diretório de dados brutos exista
    if not os.path.exists(CAMINHO_DOCUMENTOS_RAW):
        os.makedirs(CAMINHO_DOCUMENTOS_RAW)
        print(f"Pasta '{CAMINHO_DOCUMENTOS_RAW}' criada.")
        print("Por favor, adicione seus arquivos .txt ou .pdf nesta pasta antes de processar.")

    # Carrega o modelo de embedding uma vez para reutilizá-lo
    modelo_embedding = obter_modelo_embedding()

    while True:
        escolha = exibir_menu()

        if escolha == '1':
            # --- Opção 1: Processar e Vetorizar ---
            chunks = processar_documentos()
            if chunks:
                criar_e_armazenar_vetores(chunks, modelo_embedding)
            else:
                print("Nenhum chunk gerado. Verifique se há documentos na pasta 'data/raw'.")

        elif escolha == '2':
            # --- Opção 2: Fazer uma Pergunta ---
            if not os.path.exists(CAMINHO_DB):
                print("\n[ERRO] O banco de dados vetorial não existe.")
                print("Por favor, execute a opção '1' primeiro para criar o banco de dados.")
                continue

            pergunta = input("\nDigite sua pergunta: ")
            if not pergunta:
                print("Pergunta não pode ser vazia.")
                continue
                
            resultados = realizar_busca_por_similaridade(pergunta, modelo_embedding)
            
            print("\n--- Resultados da Busca ---")
            if not resultados:
                print("Nenhum resultado relevante encontrado.")
            else:
                for i, doc in enumerate(resultados):
                    print(f"\n--- Documento Relevante #{i+1} ---")
                    print(f"Fonte: {doc.metadata.get('source', 'N/A')}")
                    print(f"Conteúdo:\n{doc.page_content}")
                    print("-" * 30)
        
        elif escolha == '3':
            # --- Opção 3: Sair ---
            print("Saindo do programa. Até mais!")
            break
        
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()