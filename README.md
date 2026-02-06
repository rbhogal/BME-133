![Alt text](./SJSU_Primary_mark_Web.png)


# BME-133 Lab

This repo is designed for our team to **collaborate on Jupyter notebooks** for our lab exercises. Each team member will work on their own branch and push changes to GitHub so we can all stay in sync.

---

## **Repository Structure**

```
BME-133/
│
├── lab-notebooks/       # Jupyter notebooks (.ipynb) for each lab
│   ├── Lab0.ipynb
│   ├── Lab1.ipynb
│
├── exports/             # Optional: PDFs, HTML exports
│   ├── Lab0.pdf
│   └── Lab0.html
│
├── README.md
└── .gitignore
```

---

## **Branch Naming Format**

Use this format for all branches:

```
lab_<number>_exercise_<number>
```

**Examples:**
- `lab_1_exercise_1`
- `lab_2_exercise_3`
- `lab_3_exercise_2`

---

## **INITIAL SETUP (Do This Once)**

### **Step 1: Navigate to where you want the project**

Open VS Code terminal or any terminal, then navigate to your desired folder:

```
cd ~/<folder-name>
```

* Replace `~/<folder-name>` with wherever you want to store the project.
* Common locations: `~/repos` or `~/projects`

### **Step 2: Clone the repository**

```
git clone https://github.com/yourusername/BME-133.git
cd BME-133
```

* `git clone` copies the GitHub repo to your computer.
* `cd` changes into the repo folder.

**✅ Setup complete!** You only need to do this once. Now follow the "Regular Workflow" below every time you work on the project.

---

## **REGULAR WORKFLOW (Do This Every Time You Work)**

### **Step 1: Navigate to your project folder**

```
cd <path>/BME-133
```

* Replace `path/to/BME-133` with the actual path to your project folder.
* Example: `cd ~/repos/BME-133`

---

### **Step 2: Switch to main and pull latest changes**

```bash
git checkout main
git pull origin main
```

* This ensures you have the latest code from your team before starting new work.
* **Always do this first!**

---

### **Step 3: Create a new branch for your exercise**

```bash
git checkout -b lab_1_exercise_1
```

* Replace `lab_1_exercise_1` with the correct lab and exercise number.
* This creates a new branch and switches to it.

Check your branch:

```bash
git branch
```

* `*` indicates your current branch.

---

### **Step 4: Work on your notebook**

* Open notebooks in the `lab-notebooks/` folder in VS Code.
* Make your changes or complete exercises.

---

### **Step 5: Stage your changes**

```bash
git add lab-notebooks/Lab1.ipynb
```

* Replace `Lab1.ipynb` with the file you worked on.
* Or use `git add .` to stage all changed files.

---

### **Step 6: Commit your changes**

```bash
git commit -m "Completed Lab 1 Exercise 1"
```

* Write a clear commit message so others know what you changed.
* Commit frequently as you make progress!

---

### **Step 7: Push your branch to GitHub**

**First time pushing this branch:**
```bash
git push origin lab_1_exercise_1
```

**Subsequent pushes (after the first):**
```bash
git push
```

* This uploads your work to GitHub so others can see it.

---

### **Step 8: Merge your branch into main (when exercise is complete)**

Once your work is ready:

```bash
git checkout main
git pull origin main
git merge lab_1_exercise_1
git push origin main
```

* This merges your completed exercise into the main branch.
* Always pull before merging to avoid conflicts!

---

### **Step 9: Keep working or start a new exercise**

**To start a new exercise:**
- Go back to Step 2 (pull main) and create a new branch.

**To continue working on your current branch:**
```bash
git checkout lab_1_exercise_1
git pull origin main
```

* This updates your branch with any changes others have made to main.

---

## **Quick Reference: Git Commands**

| Command                         | Description                                                                   |
| ------------------------------- | ----------------------------------------------------------------------------- |
| `git clone <repo_url>`          | Make a local copy of the repository from GitHub (one-time setup).             |
| `git status`                    | Check which files have changed, which are staged, and which branch you're on. |
| `git branch`                    | See all local branches. `*` indicates your current branch.                    |
| `git checkout -b <branch_name>` | Create a new branch and switch to it.                                         |
| `git switch <branch_name>`      | Switch to an existing branch.                                                 |
| `git add <file>`                | Stage a file for commit.                                                      |
| `git add .`                     | Stage ALL changed files in the current directory and subdirectories.          |
| `git commit -m "message"`       | Commit staged files with a descriptive message.                               |
| `git push origin <branch_name>` | Push your branch to GitHub (first time).                                      |
| `git push`                      | Push subsequent commits (after upstream is set).                              |
| `git pull origin main`          | Pull the latest changes from the main branch.                                 |
| `git pull`                      | Pull subsequent changes (after upstream is set).                              |
| `git merge <branch_name>`       | Merge another branch into your current branch.                                |
| `git rm <file>`                 | Remove file from your working directory.                                      |
| `git log`                       | See a history of commits for the current branch.                              |

---

## **Preventing and Resolving Merge Conflicts**

### **What is a Merge Conflict?**

A merge conflict happens when two people edit the same part of the same file, and Git doesn't know which change to keep. This is common with Jupyter notebooks!

---

### **How to PREVENT Merge Conflicts**

✅ **Always pull main before creating a new branch**
```bash
git checkout main
git pull origin main
git checkout -b lab_1_exercise_1
```

✅ **Work on different notebooks when possible**
- If doing different exercises, use separate notebook files
- Example: Person A works on Lab1.ipynb, Person B works on Lab2.ipynb

✅ **Communicate with your team**
- Let others know which notebook/exercise you're working on
- Use Slack/Discord to coordinate who's working on what

✅ **Commit and push frequently**
- Small, frequent commits are easier to merge than large ones
- Push your work regularly so others can see what you've done

✅ **Pull main regularly into your branch**
```bash
git checkout lab_1_exercise_1
git pull origin main
```
- Do this every time before you start working
- Keeps your branch up-to-date with team changes

---

### **What to Do If You Get a Merge Conflict**

#### **Step 1: Don't panic!**
Merge conflicts are normal and fixable. You'll see a message like:
```
CONFLICT (content): Merge conflict in lab-notebooks/Lab1.ipynb
```

#### **Step 2: Check which files have conflicts**
```bash
git status
```
- Files with conflicts will be listed under "Unmerged paths"

#### **Step 3: Open the conflicted file**

Open the file in VS Code. You'll see conflict markers like this:

```
<<<<<<< HEAD
Your changes
=======
Their changes (from main)
>>>>>>> main
```

**For Jupyter notebooks**, conflicts look messy because notebooks are JSON files. You have two options:

**Option A: Keep your version**
```bash
git checkout --ours lab-notebooks/Lab1.ipynb
git add lab-notebooks/Lab1.ipynb
```

**Option B: Keep their version (from main)**
```bash
git checkout --theirs lab-notebooks/Lab1.ipynb
git add lab-notebooks/Lab1.ipynb
```

**Option C: Manually edit the file**
- Open the file and delete the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`)
- Keep the code you want
- Save the file
- Stage it with `git add`

#### **Step 4: Complete the merge**
```bash
git commit -m "Resolved merge conflict in Lab1.ipynb"
git push
```

#### **Step 5: Test your notebook**
- Open the notebook in Jupyter/VS Code
- Run the cells to make sure everything works
- If something broke, you can always ask a teammate for help

---

## **Tips for Beginners**

* Press **`q`** to exit `(END)` screens in the terminal (like after `git log`).
* **Always pull main before creating a new branch** to avoid conflicts.
* Commit **small changes frequently** to make merging easier.
* If you see merge conflicts, don't panic—follow the steps above or ask for help!

---

**This workflow helps everyone work independently, keeps history clear, and teaches real Git/GitHub collaboration skills!**
