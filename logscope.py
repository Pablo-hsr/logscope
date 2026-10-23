import re
import sys
from collections import Counter
from logbase import criar_banco, salvar_falha, listar_eventos

PADRAO_FALHA = re.compile(
    r"^(?P<timestamp>\w{3}\s+\d+\s+\d{2}:\d{2}:\d{2})\s+"
    r".*Failed password for (?:invalid user )?(?P<usuario>\S+) "
    r"from (?P<ip>\d+\.\d+\.\d+\.\d+)"
)

def analisar(caminho):
    falhas = []

    with open(caminho, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            resultado = PADRAO_FALHA.search(linha)

            if resultado:
                falhas.append({
                    "timestamp": resultado.group("timestamp"),
                    "usuario": resultado.group("usuario"),
                    "ip": resultado.group("ip"),
                    "linha": linha.strip(),
                })
    return falhas

def top_ips(falhas, limite=10):
    contador = Counter(f["ip"] for f in falhas)
    return contador.most_common(limite)

def main():
    if len(sys.argv)<2:
        print("Uso: python3 logscope.py <arquivo_log>")
        sys.exit(1)

    falhas = analisar(sys.argv[1])

    print(f"Tentativas de login falhas: {len(falhas)}")

    for falha in falhas:
         print(
            f"- Data: {falha['timestamp']} | "
            f"Usuario: {falha['usuario']} | "
            f"IP: {falha['ip']}"
        )

    print("\nIPs com mais tentativas de falhas: ")
    for ip, total in top_ips(falhas):
        print(f"- {ip}: {total} tentativa(s)")

    if falhas:
        conexao = criar_banco()

        for falha in falhas:
            salvar_falha(conexao, falha)

        print("\nEventos salvos no banco: ")
        for evento in listar_eventos(conexao):
            print(evento)
        conexao.close()

    
if __name__ == "__main__":
    main()