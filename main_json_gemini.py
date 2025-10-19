import os
from dotenv import load_dotenv

# ADICIONADO: Carrega as variáveis do arquivo .env para o ambiente
load_dotenv()

from src.json_exporter import exportar_para_json
from src.chunking import processar_documentos, CAMINHO_DOCUMENTOS_RAW
# ADICIONADO: Importa a nova função de embedding do Gemini
from src.embedding_gemini import obter_modelo_embedding_gemini

# REMOVIDO: O antigo módulo de embedding não será mais usado
# from src.embedding import obter_modelo_embedding

def exibir_menu():
    """Exibe o menu de opções para o usuário."""
    print("\n--- MENU DE FERRAMENTAS RAG (GEMINI) ---")
    print("1. Processar Documentos e Gerar JSON Vetorizado com Gemini")
    print("2. Sair")
    return input("Escolha uma opção: ")

def main():
    """
    Função principal que executa o loop do menu interativo.
    """
    if not os.path.exists(CAMINHO_DOCUMENTOS_RAW):
        os.makedirs(CAMINHO_DOCUMENTOS_RAW)
        print(f"Pasta '{CAMINHO_DOCUMENTOS_RAW}' criada.")
        print("Por favor, adicione seus arquivos .txt ou .pdf nesta pasta antes de processar.")

    # ATUALIZADO: Chama a função para obter o modelo do Gemini
    modelo_embedding = obter_modelo_embedding_gemini()

    while True:
        escolha = exibir_menu()

        if escolha == '1':
            chunks = processar_documentos()
            
            if chunks:
                textos_dos_chunks = [chunk.page_content for chunk in chunks]
                
                print(f"Gerando embeddings com Gemini para os {len(textos_dos_chunks)} chunks...")
                
                # A lógica aqui permanece a mesma, mas agora usa o modelo do Gemini
                vetores = modelo_embedding.embed_documents(textos_dos_chunks)
                
                print("Embeddings gerados com sucesso.")

                if chunks[0].metadata and 'source' in chunks[0].metadata:
                    caminho_original = chunks[0].metadata['source']
                    exportar_para_json(chunks, vetores, caminho_original)
                else:
                    print("Não foi possível determinar o arquivo de origem para nomear o JSON.")

            else:
                print("Nenhum chunk gerado. Verifique se há documentos na pasta 'data/raw'.")

        elif escolha == '2':
            print("Saindo do programa. Até mais!")
            break
        
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()