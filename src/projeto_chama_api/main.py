"""
Documentação da API do Rick and Morry --> https://rickandmortyapi.com/documentation/
"""

import requests


def main():
    roda_programa = True
    while roda_programa:
        op_menu = menu()
        if op_menu == "4":
            print("Finalizando o programa....")
            roda_programa = False

        elif op_menu == "1":
            characters = fetch_data("character")
            exibe_resposta_ou_erro_api(characters)

        elif op_menu == "2":
            locais = fetch_data("location")
            exibe_resposta_ou_erro_api(locais)

        elif op_menu == "3":
            epsodios = fetch_data("episode")
            exibe_resposta_ou_erro_api(epsodios)

        else:
            op_menu = digitar_op_valida(op_menu)


def menu():
    print("\nQual endpoint você deseja usar?")
    print("1 - Characters")
    print("2 - Locations")
    print("3 - Episodes")
    print("4 - Sair")
    option = input("--> ")
    return option


def trata_opcao(opcao=str):
    cond_programa = True
    if opcao == "4":
        cond_programa = False
        return cond_programa


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


def digitar_op_valida(opcao):
    l_ops = ["1", "2", "3", "4"]
    while opcao not in l_ops:
        opcao = input("Insira uma opção válida! ")
    return opcao


if __name__ == "__main__":
    main()
