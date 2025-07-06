# 🚀 60 Days DevOps Challenge - Day 2

## 📚 Topic: Linux Shell Scripting & Automation

### ✅ What I Did
- Created a shell script to automate:
  - Greeting the user
  - Showing the current date
  - Showing the current directory
  - Listing files in the current directory

### 💻 Shell Script

```bash
#!/bin/bash

echo "Hello, $USER!"
echo "Today is: $(date)"
echo "Current directory is: $(pwd)"
echo "Here are your files:"
ls -l
