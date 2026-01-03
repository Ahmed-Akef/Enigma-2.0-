# Enigma 2.0 🔐

A modern cipher tool based on linear algebra and matrix transformations. Inspired by the historic WWII Enigma machine, this project implements a mathematical encryption system using matrix operations.

## 🌐 Live Demo

**[View Live Site](https://[your-username].github.io/enigma-website/)** *(Update this link after deployment)*

## ✨ Features

- **Matrix-Based Encryption**: Uses linear algebra transformations for encoding messages
- **Client-Side Processing**: All encryption/decryption happens in your browser
- **Cyberpunk UI**: Modern, animated interface with neon aesthetics
- **Copy to Clipboard**: Easy sharing of encrypted messages and H-vectors
- **Responsive Design**: Works on desktop and mobile devices

## 🔬 How It Works

The cipher uses a mathematical transformation based on matrix operations:

1. **Encryption**:
   - Each character is mapped to a position `i` in the character set (space + a-z + 0-9)
   - For each character at position `j`, a vector is created: `[i, 2i + j + key, 2i + 2j]`
   - Matrix multiplication with `[1, 1, 1]` produces: `5i + 3j + key`
   - The result is split into encrypted character and H-value using modulo operation

2. **Decryption**:
   - Reconstructs the original value from encrypted character and H-value
   - Reverses the transformation: `i = (value - 3j - key) / 5`
   - Maps back to the original character

## 🚀 Local Development

Simply open `index.html` in your web browser. No server required!

```bash
# Clone the repository
git clone https://github.com/[your-username]/enigma-website.git

# Navigate to the directory
cd enigma-website

# Open in browser
start index.html  # Windows
open index.html   # macOS
xdg-open index.html  # Linux
```

## 📁 Project Structure

```
enigma-website/
├── index.html          # Main HTML file (static version)
├── cipher.js           # JavaScript cipher implementation
├── static/
│   └── style.css       # Cyberpunk styling
├── templates/          # Original Flask templates (reference)
├── app.py             # Flask backend (reference)
├── cipher.py          # Python implementation (reference)
└── README.md          # This file
```

## 🔒 Security Note

> **⚠️ Educational Purpose Only**
> 
> This cipher is designed for educational and demonstration purposes. It is **NOT** suitable for encrypting sensitive or confidential information. The algorithm and key are visible in the browser's source code.

## 🛠️ Technologies Used

- **HTML5** - Structure
- **CSS3** - Styling with animations and glassmorphism
- **Vanilla JavaScript** - Cipher logic and UI interactions
- **Google Fonts** - Orbitron, Share Tech Mono, Inter

## 📦 Deployment

This site is deployed on **GitHub Pages**. To deploy your own version:

1. Fork this repository
2. Go to Settings → Pages
3. Select `main` branch as source
4. Your site will be live at `https://[your-username].github.io/enigma-website/`

## 🎨 Design Credits

- Cyberpunk aesthetic inspired by modern UI/UX trends
- Glitch effects and neon styling
- Responsive grid layout

## 📄 License

This project is open source and available for educational purposes.

## 🤝 Contributing

Feel free to fork this project and submit pull requests for improvements!

---

**Made with 💚 for cryptography enthusiasts**
