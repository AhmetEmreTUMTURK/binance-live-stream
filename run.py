import subprocess
import sys

if __name__ == "__main__":
    print("Canlı Piyasa Terminali Başlatılıyor...")
    try:
        subprocess.run([sys.executable, "-m", "streamlit", "run", "app.py"])
    except KeyboardInterrupt:
        print("\n Sistem başarıyla durduruldu.")