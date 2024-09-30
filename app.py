from flask import Flask, render_template, request, jsonify, send_file
import os
import numpy as np
import kmeans

app = Flask(__name__)

@app.route('/')
def index():
    print(request.view_args)
    return render_template('index.html')

@app.route('/makegraph', methods=['POST'])
def makegraph():
    print(request)
    print(request.form)
    print(request.form["form_k"])
    test_data = [4,2,5,7,8,3,2]
    return jsonify(kmeans.X.tolist())
   


