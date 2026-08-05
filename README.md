Markdown
# 🟢 Real-Time Crypto WebSocket Terminal

Bu proje, harici bir API katmanına ihtiyaç duymadan, **Binance WebSocket** akışını doğrudan arayüze bağlayan asenkron ve hafif bir canlı borsa takip terminalidir. 

## 🚀 Projenin Amacı
Sistem; veri tabanı yükü veya HTTP sorgu gecikmeleri (latency) yaratmaksızın, seçilen kripto para birimlerinin (BTC, ETH, SOL vb.) anlık fiyat değişimlerini saniyeden kısa sürede arayüze yansıtmak amacıyla geliştirilmiştir.

## 🛠️ Kullanılan Teknolojiler
* **Python** (Core & Concurrency / Threading)
* **Streamlit** (Real-time Frontend & Reactive UI)
* **Websocket-Client** (Binance Stream Tüneli)

## ⚙️ Kurulum ve Çalıştırma

Projeyi yerel ortamınıza (local) kurmak için sırasıyla şu adımları izleyin:

1. Depoyu klonlayın:
   ```bash
   git clone [https://github.com/KULLANICI_ADINIZ/REPO_ADINIZ.git](https://github.com/KULLANICI_ADINIZ/REPO_ADINIZ.git)
   cd REPO_ADINIZ
Sanal ortam (venv) oluşturun ve aktif edin:  

Bash
python -m venv .venv
# Windows için:
.\.venv\Scripts\activate
# macOS/Linux için:
source .venv/bin/activate
Gerekli kütüphaneleri yükleyin:  

Bash
pip install -r requirements.txt
Sistemi başlatın:

Bash
python run.py
(Alternatif olarak doğrudan streamlit run app.py komutuyla da çalıştırabilirsiniz.)

💡 Mimari Detay
Uygulama, arayüzün kilitlenmesini (blocking) önlemek amacıyla arka planda Daemon Threading yapısı kullanır. Seçilen sembol değiştiğinde eski WebSocket tüneli güvenli bir şekilde kapatılır (close()) ve yeni sembol için Asenkron akış tetiklenir.
