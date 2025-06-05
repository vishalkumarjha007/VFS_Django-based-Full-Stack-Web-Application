# VS-FORCE

How to Push Your Project to GitHub
1. Initialize Git in your project folder
bash
Copy
Edit
git init
2. Add all files to staging
bash
Copy
Edit
git add .
3. Commit your changes
bash
Copy
Edit
git commit -m "Initial commit"
4. Add your GitHub repository as a remote
bash
Copy
Edit
git remote add origin https://github.com/<username>/<repo-name>.git
Replace <username> and <repo-name> with your GitHub username and repository name.

5. Pull remote changes (if any exist, like README)
bash
Copy
Edit
git pull origin main --allow-unrelated-histories
6. Push your local commits to GitHub
bash
Copy
Edit
git push -u origin main
