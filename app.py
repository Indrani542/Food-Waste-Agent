import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


# HOME PAGE
@app.route('/')
def home():
    return render_template('index.html')


# AI FOOD IMAGE SCANNER
@app.route('/scanner')
def scanner():
    return render_template('scanner.html')


# FOOD ANALYSIS SUBMISSION
@app.route('/submit', methods=['POST'])
def submit():
    food = request.form.get('food', '').strip()
    quantity = request.form.get('quantity', '').strip()
    expiry_raw = request.form.get('expiry', '0').strip()
    storage = request.form.get('storage', 'Room Temperature').strip()
    category = request.form.get('category', 'General').strip()

    try:
        expiry = int(expiry_raw)
    except (ValueError, TypeError):
        expiry = 0

    # RISK ANALYSIS ENGINE
    if expiry <= 2:
        status = "High Risk - Immediate Attention"
        recommendation = "Consume Today or Donate Immediately"
        waste_score = 90
        color = "#ef4444"
        action_text = "Prioritize using this item in today's meals, cook and freeze, or drop off at a local community pantry."
    elif expiry <= 5:
        status = "Medium Risk - Approaching Expiry"
        recommendation = "Plan Meals & Use Soon"
        waste_score = 55
        color = "#f59e0b"
        action_text = "Inspect quality, store in sealed airtight containers, and plan into your weekly meal prep."
    else:
        status = "Safe - Good Condition"
        recommendation = "Store Under Proper Conditions"
        waste_score = 15
        color = "#10b981"
        action_text = "Maintain optimal temperature and humidity to prolong freshness."

    return render_template(
        'result.html',
        food=food or "Food Item",
        quantity=quantity or "1 unit",
        expiry=expiry,
        storage=storage,
        category=category,
        status=status,
        recommendation=recommendation,
        waste_score=waste_score,
        color=color,
        action_text=action_text
    )


# RENDER & LOCAL EXECUTION
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
