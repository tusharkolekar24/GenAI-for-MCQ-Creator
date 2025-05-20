import os
import secrets
import pandas as pd
import numpy as np

import warnings
warnings.filterwarnings('ignore')

from flask import (Flask, flash, jsonify, redirect, render_template, request,
                   send_file, session, url_for)

from datetime import datetime, timedelta
from src.rag import retrival_info
from src.genai import generate_mcq

# from langchain.prompts import PromptTemplate
# from langchain.llms import OpenAI 
# from langchain.chains import LLMChain

retrival_db = retrival_info()

current_date = str(datetime.now()).split(" ")[0]
date_obj = datetime.strptime(current_date, "%Y-%m-%d")

one_year_ago = date_obj + timedelta(days=1)  # 365, 450
current_date_info = one_year_ago.strftime("%Y-%m-%d")

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", secrets.token_hex(24))

# metainfo
metainfo = dict()
metainfo['rag_content']    = ''
metainfo['mcq_content']    = ''
metainfo['question']       = ''
metainfo['username']       = ''
metainfo['username']       = "admin"

# User data for Demonstration
USERS               = {"admin": "1234"}

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if USERS.get(username) == password:
            session["username"] = username
            flash("Login successful!", "success")
            return redirect(url_for("home"))
        else:
            flash("Invalid credentials, please try again.", "danger")
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("username", None)
    session.pop("home_form_data", None)  # Clear home form data from the session
    session.pop("page_form_data", None)  # Clear page form data from the session
    flash("You have been logged out.", "info")
    return redirect(url_for("login"))

# Define a route for the sectoral page
@app.route('/')
def home():
    if "username" in session:
        # info  = {'rag_content':metainfo['rag_content'],'mcq_content':metainfo['mcq_content']}
        metainfo['username']       = session["username"]
        return render_template(
            "home.html",
            username=session["username"],
            form_data=metainfo,
            current_date=current_date,
        )
    
    return redirect(url_for("login"))

@app.route("/submit_home_form", methods=["POST"])
def submit_home_form():
    # Retrieve form data from home.html

    # prompt_info      = request.form.get('type_prompt')
    # prompt_type_list = [prompt_info]
    # for cols in ['Educational','Sales']:
    #     if cols not in prompt_type_list:
    #         prompt_type_list.append(cols)
    # metainfo['type_prompt']       = prompt_type_list

    flash("Form submitted successfully for Home page!", "success")
    return redirect(url_for("home"))

@app.route("/process_input", methods=["POST"])
def process_input():
    question_info = request.form.get("user-input")
    
    # print(question_info,"question_info")
    docs             = retrival_db.get_relevant_documents(question_info)
    combined_content = " ".join(doc.page_content for doc in docs)

    outcome          = generate_mcq(content  = combined_content,
                                    question = question_info)
    
    # print(outcome["response"].strip())
    
    if 'Invalid question asked by user'==outcome["response"].strip():
        metainfo['rag_content'] = "Content Not Found"
    
    if 'Invalid question asked by user'!=outcome["response"].strip():
        metainfo['rag_content'] = outcome["content"]

    metainfo['mcq_content'] = outcome["response"].strip()
    metainfo['question']    = question_info

    return render_template(
            "home.html",
            username=metainfo["username"],
            form_data=metainfo,
            current_date=current_date,
        )
    
if __name__ == '__main__':
    app.run(debug=True)