from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# MySQL configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '8198'
app.config['MYSQL_DB'] = 'ride_share_hub_db'

# Initialize MySQL connection
mysql = mysql.connector.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    database=app.config['MYSQL_DB']
)

@app.route('/')  # home page
def home():
    return render_template('index.html')

@app.route('/Log-In/login.html')  # login page
def login():
    return render_template('login.html')

@app.route('/submit_login', methods=['GET', 'POST'])
def submit_login():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    cursor = mysql.cursor()
    cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", (username, email, password))
    mysql.commit()
    cursor.close()
    return redirect('/Log-In/login.html')

@app.route('/contactus')  # contact page
def contact_us():
    return render_template('contactus.html')

@app.route('/submit_contactus', methods=['POST'])
def submit_contactus():
    full_name = request.form['full_name']
    email_address = request.form['email_address']
    phone_no = request.form['phone_no']
    subject = request.form['subject']
    message = request.form['message']
    cursor = mysql.cursor()
    cursor.execute("INSERT INTO contact_us (full_name, email_address, phone_no, subject, message) VALUES (%s, %s, %s, %s, %s)", (full_name, email_address, phone_no, subject, message))
    mysql.commit()
    cursor.close()
    return redirect('/contactus')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    full_name = request.form['full_name']
    mobile = request.form['mobile']
    email = request.form['mail']
    password = request.form['password']
    address = request.form['address']
    cursor = mysql.cursor()
    cursor.execute("INSERT INTO register (username, full_name, mobile, email, password, address) VALUES (%s, %s, %s, %s, %s, %s)", (username, full_name, mobile, email, password, address))
    mysql.commit()
    cursor.close()
    return redirect('/')

@app.route('/order_taxi')
def order_taxi():
    return render_template('order_taxi.html')


if __name__ == '__main__':
    app.run(debug=True)
