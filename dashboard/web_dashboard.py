from flask import Flask, render_template("index.html",prices=latest_prices), request
import csv

app = Flask(__name__)

TEMPLATE = '''
<html>
<head>
    <title>Trade Log Dashboard</title>
    <meta http-equiv="refresh" content="30">
    <style>
        table { width: 100%%; border-collapse: collapse; }
        th, td { padding: 8px; text-align: left; border: 1px solid #ddd; }
        th { background-color: #f2f2f2; }
        body { font-family: Arial, sans-serif; margin: 20px; }
        input { margin-bottom: 10px; padding: 6px; width: 200px; }
    </style>
</head>
<body>
<h2>Trade Log Dashboard</h2>
<form method="get">
    <label for="asset">Filter by asset:</label>
    <input type="text" id="asset" name="asset" value="{{ filter_asset }}">
    <input type="submit" value="Filter">
</form>
<table>
    <tr>
        <th>Timestamp</th><th>Asset</th><th>Side</th><th>Quantity</th>
        <th>Price</th><th>Order ID</th><th>Fee</th><th>Status</th>
    </tr>
    {% for row in trades %}
    <tr>
        {% for col in row %}
        <td>{{ col }}</td>
        {% endfor %}
    </tr>
    {% endfor %}
</table>
<p>Auto-refreshes every 30 seconds</p>
</body>
</html>
'''

@app.route('/')
def index():
    filter_asset = request.args.get('asset', '').upper()
    trades = []
    try:
        with open('trade_log.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader)  # skip header
            for row in reader:
                if filter_asset and row[1].upper() != filter_asset:
                    continue
                trades.append(row)
    except FileNotFoundError:
        trades = [['No trades logged yet.'] * 8]
    return render_template_string(TEMPLATE, trades=trades, filter_asset=filter_asset)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

