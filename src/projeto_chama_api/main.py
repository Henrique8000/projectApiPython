"""
Documentação da API do Rick and Morry --> https://rickandmortyapi.com/documentation/
"""

import requests


def main():
    l_ops = ["1", "2", "3", "4"]
    roda_programa = True

    while roda_programa:
        op_menu = menu()
        roda_programa = trata_opcao(op_menu, l_ops, roda_programa)


def menu():
    print("\nQual endpoint você deseja usar?")
    print("1 - Characters")
    print("2 - Locations")
    print("3 - Episodes")
    print("4 - Sair")
    option = input("--> ")
    return option


def trata_opcao(op_menu, l_ops, roda_programa):
    if op_menu == l_ops[3]:
        print("Finalizando o programa....")
        roda_programa = False
        return roda_programa

    elif op_menu == l_ops[0]:
        characters = fetch_data("character")
        return exibe_resposta_ou_erro_api(characters), roda_programa

    elif op_menu == l_ops[1]:
        locais = fetch_data("location")
        return exibe_resposta_ou_erro_api(locais), roda_programa

    elif op_menu == l_ops[2]:
        epsodios = fetch_data("episode")
        return exibe_resposta_ou_erro_api(epsodios), roda_programa

    else:
        print("\n====SELECIONE UMA OPÇÃO VÁLIDA====")
        return roda_programa


def fetch_data(endpoint):
    url = f"https://rickandmortyapi.com/api/{endpoint}"
    response = requests.get(url)

    detalhe_resposta = {
        "endpoint": endpoint,
        "status": response.status_code,
        "json": response.json()
    }

    return detalhe_resposta if detalhe_resposta["status"] == 200 else None


def exibe_resposta_ou_erro_api(detalhe_resposta=dict):
    if detalhe_resposta:
        print(detalhe_resposta["json"])
    else:
        print("Failed to fetch data")


if __name__ == "__main__":
    main()
