# conn = pymysql.connect(
#     host='localhost',
#     user='root',
#     password='udmysql@@2005',
#     database='Retail_store',
#     port=3306
# )


from flask import Flask, render_template, request, redirect, url_for
import pymysql

app = Flask(__name__)

# Connect to MySQL database
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='udmysql@@2005',
    database='Retail_store',
    port=3306
)

@app.route('/')
def index():
    return render_template('wow.html')

@app.route('/admin', methods=['GET', 'POST'])
def login():
    print("camehere1")
    if request.method == 'POST':
        print("camehere2")
        # role = request.form['adminForm']
        username = request.form['adminUsername']
        password = request.form['adminPassword']
        print("camehere2")
        role = 'admin'
        table='Admin'
        #     table = 'Admin'
        # elif role == 'vendor':
        #     table = 'Vendor'
        # elif role == 'customer':
        #     table = 'Customer'
        # else:
        #     return 'Invalid role'
        try:
            if conn.open:
                with conn.cursor() as cursor:
                    query = f"SELECT * FROM {table} WHERE Mail=%s AND Pass=%s"
                    cursor.execute(query, (username, password))
                    user = cursor.fetchone()
                    if user:
                        print("camehere2")
                        # Redirect to dashboard or specific page based on role
                        return  redirect('/admin_dashboard')
                    else:
                        return 'Invalid credentials'
            else:
                return 'Connection to database failed'
        except Exception as e:
            print("Error:", e)
        finally:
            conn.close()

    return render_template('wow.html') #

@app.route('/admin_dashboard')
def admin_dashboard():
    # Add logic for admin dashboard
    print("camehere3")
    return render_template('adminpage.html')

@app.route('/vendor_dashboard')
def vendor_dashboard():
    # Add logic for vendor dashboard
    return 'Vendor Dashboard'

@app.route('/customer_dashboard')
def customer_dashboard():
    # Add logic for customer dashboard
    return 'Customer Dashboard'

if __name__ == '__main__':
    app.run(debug=True)
