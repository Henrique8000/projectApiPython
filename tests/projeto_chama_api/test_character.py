import requests
from src.projeto_chama_api.main import (
    fetch_data
)


def test_todos_retornos_certos():
    characters = fetch_data('character')
    local = fetch_data('location')
    episodios = fetch_data('episode')
    assert characters["status"] == 200
    assert local["status"] == 200
    assert episodios["status"] == 200


def test_todos_retornos_errados():
    characters = fetch_data('Henrique')
    local = fetch_data('carro')
    episodios = fetch_data('pizza')
    assert characters is None
    assert local is None
    assert episodios is None
