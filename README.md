# Text Summarizer App

A simple, interactive text summarization web application built with **Streamlit** and **Hugging Face Transformers**.  
This app allows users to paste or type long text, process it using a state-of-the-art summarization model, and get a concise summary instantly.

---

## 🚀 Features
- **Easy-to-use UI** powered by Streamlit.
- **Automatic summarization** using Hugging Face Transformers pipeline.
- **Real-time output** with no local setup required when deployed on Hugging Face Spaces.
- **Customizable summarization length** (optional parameter tuning).
- **Future enhancement planned** — download button to save summaries as `.json` or `.txt`.

---

## 🛠️ Tech Stack
- **Python 3.10+**
- **Streamlit**
- **Transformers (Hugging Face)**
- **PyTorch**

---

## 📂 Project Structure

├── app.py # Main Streamlit application file
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── sample_texts/ # (Optional) Folder with sample test cases


---

## 📦 Installation
Clone this repository and install dependencies:

git clone https://huggingface.co/spaces/your-username/text-summarizer
cd text-summarizer
pip install -r requirements.txt

---

##  ▶️ Usage
Run the app locally:

streamlit run app.py

---

## 🌐 Deployment
This app is designed to be deployed on Hugging Face Spaces using the Streamlit template.


---


## 📈 Future Work / Improvements
- Download Button for Summaries:
Add an option to download the generated summary in .json or .txt format directly from the UI.

- Multi-language Support:
Support summarization in multiple languages.

- Model Selection Dropdown:
Allow users to choose from different summarization models.

- Text Preprocessing Options:
Remove stopwords, clean special characters before summarization.


## 📜 License


This project is licensed under the MIT License.
