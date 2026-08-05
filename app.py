import streamlit as st
import websocket
import json
import threading
import time
from streamlit.runtime.scriptrunner import add_script_run_ctx

st.set_page_config(page_title="Canlı Piyasa", page_icon="🟢", layout="wide")
st.title("Gerçek Zamanlı Kripto Takibi")
st.caption("Binance WebSocket üzerinden doğrudan ve kesintisiz veri akışı sağlanmaktadır.")
st.divider()

SEMBOL_LISTESI = ["btcusdt", "ethusdt", "solusdt", "avaxusdt", "bnbusdt", "xrpusdt", "adausdt"]

if 'aktif_sembol' not in st.session_state:
    st.session_state['aktif_sembol'] = "btcusdt"
if 'anlik_fiyat' not in st.session_state:
    st.session_state['anlik_fiyat'] = "Veri Bekleniyor..."
if 'ws_app' not in st.session_state:
    st.session_state['ws_app'] = None

secilen_sembol = st.selectbox(
    "Takip Etmek İstediğiniz Birimi Seçin:",
    SEMBOL_LISTESI,
    index=SEMBOL_LISTESI.index(st.session_state['aktif_sembol'])
)


def baslat_websocket(sembol):
    def on_message(ws, message):
        data = json.loads(message)
        st.session_state['anlik_fiyat'] = float(data['p'])

    socket_url = f"wss://stream.binance.com:9443/ws/{sembol}@trade"
    ws = websocket.WebSocketApp(socket_url, on_message=on_message)

    st.session_state['ws_app'] = ws
    ws.run_forever()


if secilen_sembol != st.session_state['aktif_sembol'] or st.session_state['ws_app'] is None:

    if st.session_state['ws_app'] is not None:
        st.session_state['ws_app'].close()
        st.session_state['anlik_fiyat'] = "Yeni veriye bağlanılıyor..."
        time.sleep(0.5)

    st.session_state['aktif_sembol'] = secilen_sembol
    t = threading.Thread(target=baslat_websocket, args=(secilen_sembol,), daemon=True)
    add_script_run_ctx(t)
    t.start()

st.subheader(f"{secilen_sembol.upper()} Canlı Fiyat")
st.metric(label="Anlık Fiyat", value=f"{st.session_state['anlik_fiyat']} $")
time.sleep(1)
st.rerun()