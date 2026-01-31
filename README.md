# BME-133 Lab

This repo is designed for our team to **collaborate on Jupyter notebooks** for our lab exercises. Each team member will work on their own branch and push changes to GitHub so we can all stay in sync.

---

## **Repository Structure**

```
BME133/
│
├── lab-notebooks/ # Jupyter notebooks (.ipynb) for each lab
│ ├── Lab0.ipynb
│ ├── Lab1.ipynb
│
├── outputs/ # Optional: PDFs, HTML exports
│ ├── pdf/
│ └── html/
│
├── README.md
└── .gitignore
```

---

## **Git Workflow Overview**

We will follow a **branch-per-person workflow**:

1. Clone the repo.
2. Create your own branch.
3. Work on your assigned exercises in your branch.
4. Commit your changes often.
5. Push your branch to GitHub.
6. Merge into `main` when your work is ready.
7. Pull updates from `main` regularly.

---

## **Git Commands Cheat Sheet**

Here’s a quick guide to all the Git commands we’ll be using:

| Command                         | Description                                                                   |
| ------------------------------- | ----------------------------------------------------------------------------- |
| `git clone <repo_url>`          | Make a local copy of the repository from GitHub.                              |
| `git status`                    | Check which files have changed, which are staged, and which branch you’re on. |
| `git branch`                    | See all local branches. `*` indicates your current branch.                    |
| `git checkout -b <branch_name>` | Create a new branch and switch to it.                                         |
| `git switch <branch_name>`      | Switch to an existing branch.                                                 |
| `git add <file>`                | Stage a file for commit.                                                      |
| `git add .`                     | Stage ALL changed files in teh current directory and subdirectories           |
| `git commit -m "message"`       | Commit staged files with a descriptive message.                               |
| `git push origin <branch_name>` | Push your branch and commits to GitHub.                                       |
| `git push`                      | Subsequent pushes on a branch that already has an upstream                    |
| `git pull origin main`          | Pull the latest changes from the main branch into your local main branch.     |
| `git pull`                      | Subsequent pulls on a branch that already has an upstream                     |
| `git merge <branch_name>`       | Merge another branch into your current branch. Usually done on `main`.        |
| `git rm <file>`                 | Remove file from your working directory (your computer)                       |
| `git log`                       | See a history of commits for the current branch.                              |

---

## **Tips for Working with Jupyter Notebooks**

- Try to **commit changes frequently**—small commits are easier to merge.
- Keep exercises in **separate notebooks** if possible to avoid merge conflicts.
- Avoid editing the same cell at the same time as someone else in your branch.
- Use `.gitignore` to **exclude exported PDFs and HTML files**:

## **Repository Structure**

```
BME-133/
│
├── notebooks/       # Jupyter notebooks (.ipynb) for each lab
│   ├── Lab0.ipynb
│   ├── Lab1.ipynb
│
├── outputs/         # Optional: PDFs, HTML exports
│   ├── Lab0.pdf
│   └── Lab0.html
│
├── README.md
└── .gitignore       # ignore files
```

---

## **Git Workflow (Step-by-Step)**

We will use a **branch-per-exercise workflow**. Each team member works on their own branch for a specific exercise and merges into `main` when ready.

Branch naming format:

```
lab_<number>_exercise_<number>
```

Example:

```
lab_1_exercise_1
lab_2_exercise_3
lab_3_exercise_2
```

---

### **Step 1: Clone the repository**

Open VS Code terminal or any terminal, then run:

```bash
git clone https://github.com/yourusername/BME-133.git
cd BME-133
```

* `git clone` copies the GitHub repo to your computer.
* `cd` changes into the repo folder.

---

### **Step 2: Create a branch for your exercise**

```bash
git checkout -b lab_1_exercise_1
```

* Replace `lab_1_exercise_1` with the correct lab and exercise number.
* This creates a new branch and switches to it.
* You will do your work in this branch, **not in main**.

Check your branch:

```bash
git branch
```

* `*` indicates your current branch.

---

### **Step 3: Work on your notebook**

* Open notebooks in the `notebooks/` folder in VS Code.
* Make your changes or complete exercises.

---

### **Step 4: Stage your changes**

```bash
git add notebooks/Lab1.ipynb
```

* Replace `Lab1.ipynb` with the file you worked on.
* `git add` tells Git “I want to save this change.”

---

### **Step 5: Commit your changes**

```bash
git commit -m "Completed Exercise 1"
```

* Always write a clear commit message so others know what you changed.

---

### **Step 6: Push your branch to GitHub**

```bash
git push origin lab_1_exercise_1
```

* Pushes your branch and commits to GitHub.
* Now others can see your work.

---

### **Step 7: Pull changes from main**

Before merging or starting new work, get the latest main updates:

```bash
git checkout main
git pull origin main
```

* `git checkout main` switches to main branch.
* `git pull origin main` updates main with the latest changes from GitHub.

---

### **Step 8: Merge your branch into main**

Once your work is ready:

```bash
git checkout main
git merge lab_1_exercise_1
git push origin main
```

* Merges your branch into main.
* Pushes updated main to GitHub.

---

### **Step 9: Keep your branch updated**

If others have merged into main, update your branch:

```bash
git checkout lab_1_exercise_1
git pull origin main
```

---

## **Tips for Beginners**

* Press **`q`** to exit `(END)` screens in the terminal (like after `git log`).
* Avoid editing the same notebook as someone else at the same time.
* Commit **small changes frequently** to make merging easier.

---

This setup helps everyone work independently, keeps history clear, and teaches **real Git/GitHub workflow**.
