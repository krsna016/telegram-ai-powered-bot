
# SSH Setup Guide for Project Management

## 1. **How to Get Started with `venv` in SSH**

- **Step 1:** Connect to your SSH instance:
  ```bash
  ssh g016_krsna@instance-20250509-050625
  ```

- **Step 2:** Install `python3` and `venv` if not installed:
  ```bash
  sudo apt update
  sudo apt install python3 python3-venv python3-pip
  ```

- **Step 3:** Create a virtual environment:
  ```bash
  python3 -m venv myenv
  ```

- **Step 4:** Activate the virtual environment:
  ```bash
  source myenv/bin/activate
  ```

- **Step 5:** Once activated, install the required dependencies (e.g., `pip install -r requirements.txt`).

---

## 2. **Using `tmux` for Session Management in SSH**

- **Step 1:** Install `tmux` if it's not already installed:
  ```bash
  sudo apt update
  sudo apt install tmux
  ```

- **Step 2:** Start a new tmux session:
  ```bash
  tmux
  ```

- **Step 3:** To detach from the tmux session, press:
  ```
  Ctrl + B, then D
  ```

- **Step 4:** To list active sessions:
  ```bash
  tmux ls
  ```

- **Step 5:** Reattach to an active session:
  ```bash
  tmux attach -t <session_name>
  ```

- **Step 6:** To kill a session:
  ```bash
  tmux kill-session -t <session_name>
  ```

---

## 3. **Getting Database from Google Cloud Instance**

- **Step 1:** Ensure you have SSH access to your Google Cloud instance.

- **Step 2:** Use the following command to copy the database file (`db.sqlite3`) from the remote server to your local machine:
  ```bash
  gcloud compute scp g016_krsna@instance-20250509-050625:~/telegram-ai-powered-bot/db.sqlite3 ~/Desktop/
  ```

- This command will securely copy the `db.sqlite3` file to the `Desktop` of your local machine.

---

## 4. **Updating Anything from Local to SSH Instance Using Git Pull**

- **Step 1:** Ensure your SSH instance is in the project directory where the git repository is initialized:
  ```bash
  cd ~/telegram-ai-powered-bot
  ```

- **Step 2:** Use `git pull` to pull the latest changes from the remote repository to your SSH instance:
  ```bash
  git pull origin main
  ```

- This will fetch the latest changes from the `main` branch of your repository and merge them into your current branch. Make sure to replace `main` with the branch name you are using.
