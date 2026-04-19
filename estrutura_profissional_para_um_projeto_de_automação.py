#Estrutura profissional para um projeto de automação
#automacao/
#├── tasks/
#│   ├── __init__.py
#│   ├── arquivos.py      # mover, renomear, limpar
#│   ├── relatorios.py    # gerar Excel/PDF
#│   └── notificacoes.py  # email, Telegram
#├── config.py            # paths, credenciais via .env
#├── scheduler.py         # agenda todas as tarefas
#├── main.py              # entrypoint
#└── tests/
#    └── test_tasks.py


# config.py — nunca hardcode credenciais!
from dotenv import load_dotenv
import os

load_dotenv()

#Bibliotecas essenciais para instalar

EMAIL_PASS = os.getenv("EMAIL_PASS")
BASE_DIR   = Path(os.getenv("BASE_DIR", "./dados"))
pip install schedule playwright httpx beautifulsoup4 pandas openpyxl python-dotenv
playwright install chromium
