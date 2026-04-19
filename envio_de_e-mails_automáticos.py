import smtplib
from email.mime.text import MIMEText

def enviar_alerta(destinatario: str, mensagem: str):
    msg = MIMEText(mensagem, "html")
    msg["Subject"] = "Alerta automático"
    msg["From"] = "bot@seudominio.com"
    msg["To"] = destinatario

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login("bot@seudominio.com", "app-password")
        smtp.send_message(msg)
