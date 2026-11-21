
import os
from flask import Flask, render_template, request

app = Flask(__name__)


# HOME PAGE
@app.route('/')
def home():
    return render_template('index.html')


# FOOD ANALYSIS
@app.route('/submit', methods=['POST'])
def submit():

    food = request.form.get('food', '')
    quantity = request.form.get('quantity', '')
    expiry = int(request.form.get('expiry', 0))
    storage = request.form.get('storage', '')
    category = request.form.get('category', '')

    # FOOD WASTE RISK ANALYSIS
    if expiry <= 2:
        status = "High Risk"
        recommendation = "Donate Immediately"
        waste_score = 90
        color = "#ff4d4d"

    elif expiry <= 5:
        status = "Medium Risk"
        recommendation = "Use Quickly"
        waste_score = 60
        color = "#ffb347"

    else:
        status = "Safe"
        recommendation = "Store Properly"
        waste_score = 20
        color = "#00cc66"

    # RESULT PAGE
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Food Waste Analysis</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <style>
            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }}

            body {{
                font-family: Arial, sans-serif;
                background: linear-gradient(to right, #141e30, #243b55);
                min-height: 100vh;
                padding: 20px;
                color: white;
            }}

            .container {{
                width: 100%;
                max-width: 900px;
                margin: auto;
            }}

            .main-card {{
                background: rgba(255,255,255,0.08);
                backdrop-filter: blur(12px);
                border-radius: 25px;
                padding: 30px;
                box-shadow: 0 0 30px rgba(0,0,0,0.4);
            }}

            .top-section {{
                text-align: center;
            }}

            h1 {{
                font-size: clamp(28px, 5vw, 45px);
                margin-bottom: 15px;
            }}

            .risk-score {{
                font-size: clamp(45px, 10vw, 75px);
                font-weight: bold;
                color: {color};
                margin-top: 10px;
            }}

            .status {{
                font-size: 28px;
                margin-top: 10px;
                color: {color};
            }}

            .progress-bar {{
                width: 100%;
                background: #ddd;
                border-radius: 20px;
                overflow: hidden;
                margin-top: 25px;
            }}

            .progress {{
                width: {waste_score}%;
                background: {color};
                padding: 15px;
                text-align: center;
                font-weight: bold;
            }}

            .grid {{
                display: grid;
                grid-template-columns: repeat(2, 1fr);
                gap: 20px;
                margin-top: 30px;
            }}

            .card {{
                background: rgba(255,255,255,0.08);
                border-radius: 20px;
                padding: 25px;
                overflow-wrap: anywhere;
            }}

            .card h2,
            .recommend-box h2 {{
                color: #00ffcc;
                margin-bottom: 18px;
            }}

            .card p {{
                margin-top: 12px;
                font-size: 16px;
                line-height: 1.6;
            }}

            .recommend-box {{
                margin-top: 30px;
                background: rgba(255,255,255,0.08);
                padding: 25px;
                border-radius: 20px;
            }}

            .tips-container {{
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 15px;
                margin-top: 20px;
            }}

            .tip {{
                background: rgba(255,255,255,0.08);
                padding: 20px 10px;
                border-radius: 20px;
                text-align: center;
                font-size: 16px;
            }}

            .footer {{
                margin-top: 30px;
                text-align: center;
            }}

            .back-btn {{
                display: inline-block;
                background: {color};
                color: white;
                text-decoration: none;
                padding: 14px 28px;
                border-radius: 12px;
                font-weight: bold;
            }}

            @media (max-width: 600px) {{
                body {{
                    padding: 12px;
                }}

                .main-card {{
                    padding: 20px 15px;
                }}

                .grid,
                .tips-container {{
                    grid-template-columns: 1fr;
                }}

                .card,
                .recommend-box {{
                    padding: 20px;
                }}

                .back-btn {{
                    display: block;
                    width: 100%;
                }}
            }}
        </style>
    </head>

    <body>
        <div class="container">
            <div class="main-card">

                <div class="top-section">
                    <h1>🍱 Food Waste Analysis</h1>

                    <div class="risk-score">
                        {waste_score}%
                    </div>

                    <div class="status">
                        {status}
                    </div>

                    <div class="progress-bar">
                        <div class="progress">
                            Waste Prediction Score
                        </div>
                    </div>
                </div>

                <div class="grid">

                    <div class="card">
                        <h2>📋 Food Details</h2>
                        <p><b>Food Name:</b> {food}</p>
                        <p><b>Quantity:</b> {quantity}</p>
                        <p><b>Expiry Days:</b> {expiry}</p>
                        <p><b>Storage:</b> {storage}</p>
                        <p><b>Category:</b> {category}</p>
                    </div>

                    <div class="card">
                        <h2>🤖 AI Recommendation</h2>
                        <p>{recommendation}</p>
                        <p>
                            The system estimates food waste risk
                            based on the expiry period.
                        </p>
                        <p>
                            <b>Suggested Action:</b>
                            Store and handle food properly
                            to reduce wastage.
                        </p>
                    </div>

                </div>

                <div class="recommend-box">
                    <h2>💡 Smart Waste Reduction Tips</h2>

                    <div class="tips-container">
                        <div class="tip">
                            ❄️<br><br>
                            Store Food Properly
                        </div>

                        <div class="tip">
                            🍲<br><br>
                            Reuse Extra Food
                        </div>

                        <div class="tip">
                            ❤️<br><br>
                            Donate Excess Food
                        </div>
                    </div>
                </div>

                <div class="footer">
                    <a href="/" class="back-btn">
                        ⬅ Back to Home
                    </a>
                </div>

            </div>
        </div>
    </body>
    </html>
    """


# RUN APPLICATION - KEEP THIS AT THE VERY BOTTOM
if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=int(os.environ.get('PORT', 5000)),
        debug=False
    )
