# 🚀 GitHub Pages Deployment Guide for Enigma 2.0

This guide will walk you through deploying your Enigma 2.0 website to GitHub Pages, making it accessible online for free!

## Prerequisites

- A GitHub account ([Sign up here](https://github.com/join) if you don't have one)
- Git installed on your computer ([Download here](https://git-scm.com/downloads))

---

## Step 1: Initialize Git Repository

Open PowerShell in your project directory and run:

```powershell
cd "c:\Users\MF\.gemini\antigravity\scratch\enigma_website"
git init
```

## Step 2: Add All Files to Git

```powershell
git add .
```

## Step 3: Create Your First Commit

```powershell
git commit -m "Initial commit: Enigma 2.0 static website"
```

## Step 4: Create a GitHub Repository

1. Go to [GitHub](https://github.com) and log in
2. Click the **"+"** icon in the top right corner
3. Select **"New repository"**
4. Fill in the details:
   - **Repository name**: `enigma-website` (or any name you prefer)
   - **Description**: "A modern cipher tool based on linear algebra"
   - **Visibility**: Choose **Public** (required for free GitHub Pages)
   - **DO NOT** initialize with README, .gitignore, or license (we already have these)
5. Click **"Create repository"**

## Step 5: Connect Your Local Repository to GitHub

GitHub will show you commands to run. Copy the commands under **"…or push an existing repository from the command line"**. They will look like this:

```powershell
git remote add origin https://github.com/YOUR-USERNAME/enigma-website.git
git branch -M main
git push -u origin main
```

**Replace `YOUR-USERNAME` with your actual GitHub username**, then run these commands in PowerShell.

## Step 6: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **"Settings"** (top menu)
3. Click **"Pages"** in the left sidebar
4. Under **"Source"**, select:
   - Branch: **main**
   - Folder: **/ (root)**
5. Click **"Save"**

## Step 7: Wait for Deployment

GitHub will take 1-3 minutes to build and deploy your site. You'll see a message like:

> ✅ Your site is live at `https://YOUR-USERNAME.github.io/enigma-website/`

## Step 8: Update README with Live Link

Once your site is live, update the `README.md` file:

1. Open `README.md`
2. Find the line: `**[View Live Site](https://[your-username].github.io/enigma-website/)**`
3. Replace `[your-username]` with your actual GitHub username
4. Save the file
5. Commit and push the change:

```powershell
git add README.md
git commit -m "Update README with live site link"
git push
```

---

## 🎉 You're Done!

Your Enigma 2.0 website is now live on the internet! Share the link with friends and colleagues.

## Making Updates

Whenever you want to update your website:

```powershell
# Make your changes to the files
git add .
git commit -m "Description of your changes"
git push
```

GitHub Pages will automatically rebuild and deploy your changes within 1-3 minutes.

---

## Troubleshooting

### Site not loading?
- Make sure you selected the **main** branch and **/ (root)** folder in GitHub Pages settings
- Wait a few minutes - deployment can take time
- Check that your repository is **Public**

### CSS not loading?
- Verify that `index.html` has the correct path: `<link rel="stylesheet" href="static/style.css">`
- Check that the `static` folder is in your repository

### JavaScript errors?
- Open browser Developer Tools (F12)
- Check the Console tab for errors
- Verify that `cipher.js` is in the root directory

---

## What You Should Put on GitHub

Your repository should include:

✅ **Include these files:**
- `index.html` (root)
- `cipher.js`
- `static/style.css`
- `README.md`
- `.gitignore`

❌ **These are optional (for reference only):**
- `app.py` (Flask backend - not used by static site)
- `cipher.py` (Python implementation - not used by static site)
- `requirements.txt` (Python dependencies - not used by static site)
- `templates/` folder (Flask templates - not used by static site)

The `.gitignore` file will automatically exclude Python cache files and virtual environments.

---

## Need Help?

If you encounter any issues:
1. Check the [GitHub Pages documentation](https://docs.github.com/en/pages)
2. Verify all files are committed and pushed to GitHub
3. Make sure your repository is public
4. Check the Actions tab in your repository for build errors

**Happy encrypting! 🔐**
