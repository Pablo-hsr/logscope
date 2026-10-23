# LogScope

Analisador de logs de autenticação SSH escrito em Python. Lê um arquivo `auth.log`, identifica tentativas de login falhas, mostra quais IPs mais tentaram e salva os eventos em um banco SQLite.

## Funcionalidades

- Detecta tentativas de login falhas (`Failed password`), inclusive para usuários inválidos
- Extrai data/hora, usuário e IP de cada tentativa
- Mostra o ranking de IPs com mais falhas
- Salva os eventos em um banco SQLite (`logscope.db`) para consultas posteriores

## Requisitos

- Python 3.8 ou superior
- Nenhuma dependência externa (usa apenas a biblioteca padrão: `re`, `sys`, `sqlite3`, `collections`)

## Como usar

```bash
cd logscope
python3 logscope.py sample_logs/auth.log
```
```estou trabalhando para colocar essa funcionalidade´´´
Para analisar um log do seu próprio sistema (pode exigir permissão de leitura):

```bash
sudo python3 logscope.py /var/log/auth.log
```

