import sqlite3


def criar_banco(caminho_banco="logscope.db"):
    conexao = sqlite3.connect(caminho_banco)

    conexao.execute("""

        CREATE TABLE IF NOT EXISTS events(
            id INTEGER PRIMARY KEY,
            timestamp  TEXT,
            event_type TEXT,
            username TEXT,
            ip_address TEXT,
            raw_line TEXT
        )
""")
    conexao.commit()
    return conexao

def salvar_falha(conexao, falha):
    conexao.execute(
        """
        INSERT INTO events (timestamp, event_type, username, ip_address, raw_line)
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            falha["timestamp"],
            "failed_login",
            falha["usuario"],
            falha["ip"],
            falha["linha"],
        ),
    )
    conexao.commit()

def listar_eventos(conexao):
    resultado = conexao.execute(
        "SELECT timestamp, event_type, username, ip_address FROM events"
    )

    return resultado.fetchall()