# GenAI for MCQ Creator

## 📌 Project Overview

GenAI-for-MCQ-Creator is an AI-powered application designed to automatically generate high-quality Multiple Choice Questions (MCQs) from text content, PDF files, lecture notes, or user input. The system utilizes state-of-the-art Generative AI models (GPT-based) to create concept-based, difficulty-level-specific MCQs suitable for exams, quizzes, corporate training, and e-learning platforms.

This project aims to assist teachers, content creators, and students by reducing manual effort in question creation while ensuring accuracy and relevance.

---

## 🚀 Key Features

* 🧠 **Automated MCQ Generation** using GenAI
* ✍️ **Input Methods**: Text, PDF upload, or manual paste
* 🎯 **Difficulty Levels**: Easy, Medium, Hard (if applicable)
* ✅ **Answer Key Generation**
* 📄 **Artifacts Folder to Store MCQ Files**
* 🌐 **Web Interface with Frontend & Backend Integration**

---

## 📁 Project Structure

```
GenAI-for-MCQ-Creator/
│
├── artifacts/           # Stores generated MCQs and related files
├── src/                 # Backend logic, AI integration, data processing
├── static/              # CSS, JS, image assets
├── templates/           # HTML pages (UI components)
├── app.py               # Main application entry point
├── requirements.txt     # Python dependencies
├── LICENSE              # License details
└── README.md            # Project documentation
```

---

## 🛠️ Technologies Used

| Component        | Technology             |
| ---------------- | ---------------------- |
| Frontend         | HTML, CSS, JavaScript  |
| Backend          | Python (Flask/FastAPI) |
| AI Model         | GPT-based GenAI model  |
| PDF/Text Parsing | PyPDF2, pdfplumber     |
| Deployment Ready | Azure / Docker ready   |

---

## 📦 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/GenAI-for-MCQ-Creator.git
cd GenAI-for-MCQ-Creator
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Configure API Keys

Create a `.env` file and add your API credentials:

```
OPENAI_API_KEY=your_api_key_here
```

### 4️⃣ Run the Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## ▶️ How to Use

1. Upload a PDF or paste text.
2. Select difficulty level (if enabled).
3. Click **Generate MCQs**.
4. View or download generated questions with answer keys.

---

## 📌 Use Cases

* 🎓 Educational Institutions
* 🏢 Corporate Training & Assessments
* 📖 Self-study & Exam Preparation
* 🌐 EdTech Platforms

---

## 🧪 Future Enhancements

* ✅ Support for Bloom's Taxonomy-based MCQ generation
* ✅ Export options: PDF, DOCX, Excel
* ✅ Interactive quizzes
* ✅ Integration with LMS platforms

---

## 🤝 Contributing

Contributions, suggestions, and feedback are welcome! Feel free to open issues or submit PRs to enhance this project.

---

## 📜 License

This project is licensed under the **MIT License**. See the `LICENSE` file for more info.

---

## ⭐ Support

If you find this project helpful, please ⭐ the repository to support its growth!

When the user's Input was incorrect.
![image](https://github.com/user-attachments/assets/38d60779-8d10-4958-83a0-14f0d030c69b)

When the user's Input was correct.
![image](https://github.com/user-attachments/assets/5e30362d-94c5-4739-9d8c-259e08aee640)

Kindly download the ZIP file, which contains sample input JSON files.
This will help you quickly test and run the MCQ Creator App without generating your own data.
