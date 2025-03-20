# from flask import Flask,render_template,request
# from pipeline.prediction_pipeline import hybrid_recommendation

# app = Flask(__name__)

# @app.route('/' , methods=['GET','POST'])
# def home():
#     recommendations = None

#     if request.method == 'POST':
#         try:
#             user_id = int(request.form["userID"])

#             recommendations = hybrid_recommendation(user_id)
#         except Exception as e:
#             print("Erorr occured....")

#     return render_template('index.html' , recommendations=recommendations)

# if __name__=="__main__":
#     app.run(debug=True,host='0.0.0.0',port=5000)

from flask import Flask, render_template, request
import traceback
from pipeline.prediction_pipeline import hybrid_recommendation

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    recommendations = None

    if request.method == 'POST':
        try:
            user_id = request.form.get("userID")
            if not user_id:
                raise ValueError("Missing userID in request form")

            user_id = int(user_id)  # Ensure valid integer input
            print(f"Received user_id: {user_id}")

            recommendations = hybrid_recommendation(user_id)
            print(f"Generated recommendations: {recommendations}")

        except Exception as e:
            print("Error occurred:", str(e))
            traceback.print_exc()  # Print full error details

    return render_template('index.html', recommendations=recommendations)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
