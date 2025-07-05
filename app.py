from flask import Flask,render_template,request
import mysql.connector
app=Flask(__name__)
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="flaskuser",
        password="flaskpass",
        database="contactdb"
    ) 
@app.route('/')
def home():
    return render_template('index.html') #shows html form
@app.route('/sumbit',methods=['POST'])
def sumbit():
    name=request.form['name']
    email=request.form['email']
    message=request.form['message']
    connection = mysql.connector.connect(
        host="localhost",
        user="flaskuser",
        password="flaskpass",
        database="contactdb"
    )
    print("connected successfully")
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS contact(
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        email VARCHAR(100),
        message TEXT
    )
    ''')
    cursor.execute("INSERT INTO contact (name,email,message) VALUES (%s,%s,%s)",(name, email ,message))
    connection.commit()
    cursor.close()
    conn.close()
    print("Inserted into MySQL")
    print("Data received from user:")
    print("Name",name)
    print("Email",email)
    print("Message",message)
    
    return f"Super da Thailee,{name}.We recieved your message!"

if __name__ == '__main__':
    app.run(debug=True)
    

    
    