from flask import Flask,request,jsonify
from flask_cors import CORS
import pymysql

app=Flask(__name__)

CORS(app)

db = pymysql.connect(
        host = "multitierprojectdb.ap-south-1.rds.amazonaws.com",
        user = "admin",
        password = "",
        database = "Multi_Tier_Project_DB",
        port = 3306
)

@app.route("/")
def home():
    return "Backend Running Successfully"

@app.route("/register", methods=["POST"])
def register():

    data = request.json

    print(data)

    cursor = db.cursor()

    sql = """ 
    Insert Into Employee(empID, name, email, Dept)
    VALUES(%s, %s, %s, %s)
    """

    cursor.execute(sql,(
        data["empID"],
        data["name"],
        data["email"],
        data["Dept"]
    ))

    db.commit()

    return jsonify({
        "message":"Successfully Registered"
    })

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port=5000, debug=True)