from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3
import os
from datetime import datetime, time, date

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
    # TODO: Fetch data for calendar and stats
    return render_template('index.html', app_name='勤怠マネージャー', primary_color='#0065ff', icon='clock')

@app.route('/record/<string:record_date>', methods=['GET', 'POST'])
def record_page(record_date):
    # TODO: Implement record creation/update logic
    return render_template('record.html', record_date=record_date, app_name='勤怠マネージャー', primary_color='#0065ff', icon='clock')

# --- Utility functions (to be implemented based on prompt) ---

def rounded_time(t_str, rounding_method):
    # TODO: Implement rounding logic
    pass

def calculate_hours(clock_in_str, clock_out_str, rounding_method):
    # TODO: Implement hour calculation
    pass

def generate_monthly_pdf_data(month_year_str):
    # TODO: Implement PDF data generation
    pass 

if __name__ == '__main__':
    init_db() # Initialize database and table if they don't exist
    app.run(debug=True)
