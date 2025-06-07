from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3
import os
from datetime import datetime, time, date
import calendar
import sys

print("\n*** DIAGNOSTIC VERSION - kintaikanri/app.py (JUNE 8 07:45) ***\n")
print(f"Python version: {sys.version}")
print(f"Running from: {os.path.abspath(__file__)}")

app = Flask(__name__)
app.secret_key = os.urandom(24)

DATABASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
DATABASE_PATH = os.path.join(DATABASE_DIR, 'attendance.db')

if not os.path.exists(DATABASE_DIR):
    os.makedirs(DATABASE_DIR)

def get_db_connection():
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL UNIQUE, -- YYYY-MM-DD
            clock_in TEXT,          -- HH:MM
            clock_out TEXT,         -- HH:MM
            rounding_method TEXT,   -- "切り上げ" or "切り下げ"
            pre_eight_category TEXT,-- "自己学習" or "勤務"
            memo TEXT,
            total_hours REAL,       -- 丸め後
            overtime_hours REAL     -- 丸め後・8-17 超過分
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    now = datetime.now()
    year = now.year
    month = now.month

    month_name = now.strftime("%B")
    cal = calendar.Calendar()
    calendar_weeks = cal.monthdayscalendar(year, month)

    stats = {
        'total_hours_month': 0, # Placeholder
        'total_overtime_month': 0 # Placeholder
    }

    # This was the test string from before simplification
    test_string_from_app = "APP.PY IS UPDATED AND THIS STRING IS FROM HOME ROUTE JUNE 8 0700"
    return render_template('index.html',
                           year=year,
                           month_num=month,
                           month_name=month_name,
                           calendar_weeks=calendar_weeks,
                           stats=stats,
                           test_string=test_string_from_app,
                           app_name='大輔専用勤怠管理',
                           primary_color='#0065ff',
                           icon='clock')

@app.route('/record/<string:record_date>', methods=['GET', 'POST'])
def record_page(record_date):
    # This is a placeholder, actual implementation needed
    return render_template('record.html', record_date=record_date, app_name='勤怠マネージャー', primary_color='#0065ff', icon='clock')

@app.route('/test_direct')
def test_direct_output():
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    # This was the test route from before simplification
    return f"これはapp.pyからの直接出力テストです。 (kintaikanri/app.py) 現在時刻: {current_time}"

# シンプル版のルートは削除して競合を避ける

# ルートのレジスタ状況を確認するヘルパー関数
def print_registered_routes():
    print("\n==== REGISTERED ROUTES ====")
    for rule in app.url_map.iter_rules():
        print(f"{rule.endpoint}: {rule}")
    print("============================\n")

if __name__ == '__main__':
    print(f"\nFlask app object: {app}")
    print(f"Secret key set: {'Yes' if app.secret_key else 'No'}")
    
    # 現在のURLマップを出力
    print_registered_routes()
    
    print("\nAttempting to initialize database...")
    try:
        init_db()
        print("✅ Database initialized successfully")
    except Exception as e:
        print(f"❌ CRITICAL ERROR during init_db: {str(e)}")
    
    # 明示的に各ルートを確認
    print("\nConfirming routes are registered properly:")
    routes = [
        ('/', 'home'),
        ('/test_direct', 'test_direct_output'),
        ('/record/<date>', 'record_page')
    ]
    
    for path, endpoint in routes:
        try:
            url = url_for(endpoint, date='2025-06-08' if '<date>' in path else None)
            print(f"✅ Route '{path}' -> {endpoint} is registered (URL: {url})")
        except Exception as e:
            print(f"❌ Route '{path}' -> {endpoint} is NOT properly registered: {str(e)}")
    
    # URLマップの最終確認
    print_registered_routes()
    
    # デバッグモードを無効にし、ポートを5002に変更して明示的に起動
    print("\n🚀 Starting Flask app on port 5002 (NO debug mode for clean startup)...")
    try:
        # 重要: デバッグモードを一時的に無効化して、リロードの問題を回避
        app.run(host='127.0.0.1', port=5002, debug=False) 
    except Exception as e:
        print(f"❌ CRITICAL ERROR during app.run: {str(e)}")