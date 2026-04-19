import schedule
import time

def backup_diario():
    shutil.copytree("projetos", f"backup_{date.today()}")
    print("Backup feito!")

schedule.every().day.at("08:00").do(backup_diario)
schedule.every(30).minutes.do(checar_emails)
schedule.every().monday.do(gerar_relatorio)

while True:
    schedule.run_pending()
    time.sleep(1)
