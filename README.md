# 🚀 Student Performance System

A mini end-to-end project combining **Data Analysis, Machine Learning, FastAPI, Testing, and Docker**.

---

## 🧩 Modules Overview

### 📊 1. Analysis (`analysis.py`)
<img width="851" height="310" alt="Screenshot 2026-03-24 152051" src="https://github.com/user-attachments/assets/3fffa140-933a-4acd-bf26-cb4f1cae96fe" />

* Computes average scores by course
* Generates visual insights

**Results:**

* CSE → 60.66
* ECE → 83.00
* IT → 68.00

**Key Insight:**
ECE students outperform others, while CSE needs improvement.

---

### 🤖 2. Machine Learning (`ml.py`)

* Predicts student score based on study hours
<img width="765" height="84" alt="Screenshot 2026-03-24 151854" src="https://github.com/user-attachments/assets/4b5fb4c8-2ee6-4a53-b6e1-54a671c1cedd" />

**Output:**

* RMSE → `2.37`
* Prediction → `5 hrs = 74 marks`

**Insight:**
Model is reasonably accurate with low prediction error.

---

### ⚡ 3. FastAPI Backend

Provides REST APIs for student management.
<img width="980" height="478" alt="Screenshot 2026-03-24 151312" src="https://github.com/user-attachments/assets/9dc1d333-d11e-48b1-a0d8-6e334892b590" />
**Endpoints:**

* `POST /students` → Create
* `GET /students` → Read all
* `GET /students/{id}` → Read one
* `PUT /students/{id}` → Update
* `DELETE /students/{id}` → Delete

**Behavior:**

* Valid requests → `200 OK`
* Invalid IDs → `404 Not Found`

---

### 🧪 4. Testing (`pytest`)

* Ran unit tests for API
<img width="991" height="370" alt="Screenshot 2026-03-24 152229" src="https://github.com/user-attachments/assets/a6f52448-c92e-4718-a452-1efb9e7c0fed" />

**Result:**

* ✅ 1 test passed
* ⏱ Execution time: 0.96s

---

### 📈 5. Graphs

* Bar Chart → Course-wise average
* Line Chart → Score trend
<img width="640" height="480" alt="Figure_2" src="https://github.com/user-attachments/assets/f7ccf629-8e1f-43ba-a367-f85fcc259577" />
<img width="640" height="480" alt="Figure_1" src="https://github.com/user-attachments/assets/a64d7509-e406-4f70-a385-46000b952e92" />

**Observation:**

* Peak score ~91
* Final drop to ~55 → performance inconsistency

---

### 🐳 6. Docker

* Built container images for deployment
<img width="775" height="107" alt="Screenshot 2026-03-24 154040" src="https://github.com/user-attachments/assets/1b92952a-a51d-41e0-a437-943a5ac9e275" />

**Images:**

* `fastapi-app` → 244MB
* `student-api` → 1.45GB

---

## ⚠️ Issue & Fix

**Problem:**

* AutoGen failed due to missing dependency (`ray`)
* Numpy binary mismatch

**Solution:**

```bash id="a8sk21"
pip install ray
pip install --upgrade numpy
```

---

## 🧠 What You Learn

* Data analysis & visualization
* Regression modeling
* FastAPI development
* API testing with pytest
* Docker basics
* Debugging Python environments

---

## 🔮 Improvements

* Add database integration
* Enhance ML model
* Add authentication
* Increase test coverage
* Reduce Docker image size

---

## 🏁 Summary

This project showcases a **complete pipeline**:

➡️ Data → Analysis → ML → API → Testing → Deployment

A solid base for **SDE + Data-oriented roles**.

---
