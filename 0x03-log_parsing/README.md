# 0x03-log_parsing

# 📝 Log Parsing Tool

Welcome to the **Log Parsing Tool**, a simple yet powerful script to analyze and summarize web server logs in real-time. Whether you're a developer or a sysadmin, this tool provides instant metrics on log file sizes and HTTP status codes.

---

## 🔍 Features

- **Real-Time Parsing**: Reads log data line by line directly from `stdin`.
- **Accurate Metrics**:
  - Tracks total file size.
  - Counts occurrences of HTTP status codes: `200`, `301`, `400`, `401`, `403`, `404`, `405`, and `500`.
- **Efficient Output**:
  - Prints stats every 10 lines.
  - Handles keyboard interruptions (Ctrl + C) gracefully, showing the final stats before exiting.
- **Error-Tolerant**: Skips invalid or malformed log lines seamlessly.

---

## 📂 Input Format

The tool expects log lines in the following format:

192.168.0.1 - [2024-11-28] "GET /projects/260 HTTP/1.1" 404 512


- **IP Address**: Client's IP address.
- **Date**: Timestamp of the request.
- **HTTP Method and Path**: Always expects `"GET /path HTTP/1.1"`.
- **Status Code**: HTTP response status code (e.g., `200`, `404`).
- **File Size**: Size of the response in bytes.

---

## 🛠 Usage

1. Clone the repository and navigate to the directory.
2. Make the script executable:
   ```bash
   chmod +x 0-stats.py

## Author
* Name: Wilfort Abel
* Email: juiciwhilf@gmail.com