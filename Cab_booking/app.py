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
    return render_template('new_index.html')


@app.route('/contactus')  # contact page
def contact_us():
    return render_template('new_contactus.html')

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

@app.route('/privacy')     #privacy page
def privacy():
    return render_template('pri_index.html')

@app.route('/safety')        #safty page
def safety():                   
    return render_template('saf_index.html')

@app.route('/map')       #map
def map():
    return render_template('map.html')


if __name__ == '__main__':
    app.run(debug=True)
