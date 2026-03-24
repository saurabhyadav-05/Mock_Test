# 🚀 Student Performance System

A mini end-to-end project combining **Data Analysis, Machine Learning, FastAPI, Testing, and Docker**.

---

## 🧩 Modules Overview

### 📊 1. Analysis (`analysis.py`)

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

**Output:**

* RMSE → `2.37`
* Prediction → `5 hrs = 74 marks`

**Insight:**
Model is reasonably accurate with low prediction error.

---

### ⚡ 3. FastAPI Backend

Provides REST APIs for student management.

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

**Result:**

* ✅ 1 test passed
* ⏱ Execution time: 0.96s

---

### 📈 5. Graphs

* Bar Chart → Course-wise average
* Line Chart → Score trend

**Observation:**

* Peak score ~91
* Final drop to ~55 → performance inconsistency

---

### 🐳 6. Docker

* Built container images for deployment

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
