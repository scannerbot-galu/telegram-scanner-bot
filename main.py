import logging
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# 1. Mengaktifkan log untuk memantau aktivitas bot di server
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# 2. Fungsi merespons ketika Anda mengetik /start di Telegram
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Halo! Scanner bot Anda berhasil aktif 24 jam di server cloud tanpa mati."
    )

# 3. Fungsi Logika Scanner Otomatis Anda
async def tugas_scanner(context: ContextTypes.DEFAULT_TYPE):
    # --- TEMPATKAN LOGIKA SCANNER ANDA DI SINI ---
    # Contoh: cek website, cek harga saham, atau cek data berkala
    
    chat_id = "8576284120" # Ganti dengan ID Chat / Group Anda
    await context.bot.send_message(
        chat_id=chat_id, 
        text="[Sinyal Scanner]: Sistem berjalan mendeteksi data baru!"
    )

def main():
    # 4. Masukkan Token Bot dari BotFather
    TOKEN = "8903614216:AAEZc-6Ut3ZAQuIAwEDjKvEYezliAuFBkvg"
    
    # 5. Bangun Aplikasi Bot
    app = ApplicationBuilder().token(TOKEN).build()
    
    # Registrasi perintah manual /start
    app.add_handler(CommandHandler("start", start))
    
    # 6. Mengatur Scanner agar otomatis berjalan berkala (Contoh: setiap 60 detik)
    job_queue = app.job_queue
    job_queue.run_repeating(tugas_scanner, interval=60, first=10)
    
    # 7. Jalankan Bot
    print("Bot Scanner Telegram telah aktif...")
    app.run_polling()

if __name__ == '__main__':
    main()
  
