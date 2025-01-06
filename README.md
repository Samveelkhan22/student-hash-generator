## 🚀 Student Hash Generator

## 📋 Overview
This repository contains a hash function tailored to uniquely map student seat numbers to a fixed range. It is specifically designed for CS and SE students enrolled between the years 2000 and 2099. The hash function minimizes collisions and ensures fast and efficient indexing.

## 🧮 Hash Function Logic

### Extract the Enrollment Year
- The first two digits of the seat number represent the year of enrollment.
- Example: For B22110004016, the year is 22 (i.e., 2022).

### Extract the Roll Number
- The remaining digits of the seat number are the student's roll number.
- Example: From B22110004016, the roll number is 110004016.

## 🛠 Features
✔️ Efficient Mapping: Minimal collisions for unique seat numbers.
✔️ Year-Driven Logic: Supports enrollment years from 2000 to 2099.
✔️ Customizable Table Size: Adaptable to different hash table sizes for various use cases.
✔️ Scalable Design: Designed for large datasets with minimal computational overhead.

## 🛠 Applications
- Student Management Systems: Efficient storage and retrieval of student records.
- Hash Table Data Structures: Perfect for quick lookup in large datasets.

