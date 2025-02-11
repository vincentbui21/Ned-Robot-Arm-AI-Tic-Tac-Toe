# Ned Robot Arm - AI Tic-Tac-Toe

🔹 **A 1v1 Tic-Tac-Toe Game between Human and AI, powered by the Ned 6-axis robot arm.**

## 📌 Overview
This project implements a **3x3 Tic-Tac-Toe game**, where a **human player** competes against an **AI-controlled opponent**. The AI uses the **Ned robot arm** to pick up and place game pieces, which are distinguished by color. No matter how the human plays, the **AI is designed to always win or force a draw**.

## 🎥 Video Demonstration
📌 Watch the project in action on youtube here: <br>
[![Watch the video](https://img.youtube.com/vi/MdAdJVFdFAE/0.jpg)](https://www.youtube.com/watch?v=MdAdJVFdFAE)



## 🛠️ Features
- ✅ **AI-powered gameplay** – Uses optimal Tic-Tac-Toe strategies to guarantee a win or draw.
- ✅ **Robotic interaction** – The Ned arm physically picks and places game pieces.
- ✅ **Computer vision** – Pieces are recognized by color for accurate placement.
- ✅ **User-friendly interface** – Simple controls for human players.

## 🖥️ Technologies Used
- **Python** – Core programming language
- **OpenCV** – For color-based piece detection
- **ROS (Robot Operating System)** – Handles robotic control
- **Niryo Studio** – For setting up the Ned arm

## 🛠️ Installation & Setup
### Prerequisites
- **Ned Robot Arm** with Niryo Studio installed
- **Python 3.x** installed
- **ROS environment set up**
- Required Python packages:
  ```bash
  pip install opencv-python numpy pyniryo
  ```

### Running the Program
1. **Power on the Ned robot and connect it to your PC.**
2. **Run the main Python script:**
   ```bash
   python aicode.py
   ```
3. **Follow on-screen instructions to start playing.**

## 🔗Set up physical board
1. After you run the program, a window will pop up on screen with grid <br>
![image](https://github.com/user-attachments/assets/215d6e24-a76c-4474-a02c-1b4cc124b376)
2. Move the board that until all edges match the grid
3. Make sure there is no pieces on the board

## 🎮 How to Play
1. The **human player goes first**, selecting a valid move.
2. The AI calculates its move and **commands the Ned robot** to place the piece.
3. The game continues until a **draw or an AI win** occurs.
4. The **final result** is displayed.

## 📜 License
This project is open-source under the **MIT License**. Feel free to use, modify, and contribute!

## 🙌 Credits
Developed by **Vincent Bui** and team.
