from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>Stock Web</title>
        </head>
        <body style="font-family: Arial; text-align: center;">
            <h1>📈 Stock Dashboard</h1>
            <p>Backend đang chạy 🚀</p>

            <button onclick="loadData()">Load VCB Price</button>
            <pre id="data"></pre>

            <script>
                async function loadData() {
                    const res = await fetch('/stock/VCB');
                    const data = await res.json();
                    document.getElementById('data').innerText = JSON.stringify(data, null, 2);
                }
            </script>
        </body>
    </html>
    """
