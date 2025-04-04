<!-- PROJECT LOGO -->
<div align="center">
  <img src="images/BookSearch.svg" alt="Logo" width="256" height="256">
  <h3 align="center">BookSearch</h3>
  <p align="center">
    Book Searching program using the Amazon API and ML.
    <br />
    <a href="https://github.com/SP-SDU/BookSearch"><strong>View Project »</strong></a>
    <br />
    <br />
    <a href="https://github.com/SP-SDU/BookSearch/issues">Issues</a>
    ·
    <a href="https://github.com/orgs/SP-SDU/projects/8">Board</a>
  </p>
</div>

## Getting Started 🚀

# 📂 Large Files Storage
To keep the repository lightweight, large `.csv` files are stored externally.

🔗 **Download Files:**  
- [merged_dataframe.csv](https://drive.google.com/your-file-link)  
After downloading, place the files in:
BookSearch

Running the Preprocessing Script

The preprocessing script takes raw book data and transforms it into a structured format.

Run the Script
python preprocessing.py

Output

The processed dataset is saved as data/processed_books.csv.

Logs and progress updates are printed to the console.


### Prerequisites
- Python 3.12 or higher
- pip (Python package manager)
- Download [merged_dataframe.csv](https://drive.google.com/file/d/1MVRHs_CwKTBR2Rpakx920f277IcJ0q6X/view) and place it in the `src/data` directory.

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/SP-SDU/BookSearch.git
   cd BookSearch
   ```

2. Create and activate a virtual environment:
   ```bash
   # Windows
   python -m venv .venv
   .\.venv\Scripts\activate

   # Linux/MacOS
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```
   pip install -r src/requirements.txt
   ```

### Running the Application (Or debug F5 in VSCode)

1. Ensure virtual environment is activated (you should see `(.venv)` in your terminal)

2. Start the Flask server:
   ```
   python src/app.py
   ```

3. Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

## Contributing 🤝

1. **Clone** Open [GitHub Desktop](https://desktop.github.com/), go to `File > Clone Repository`, and enter:
     ```
     hhttps://github.com/SP-SDU/BookSearch
     ```
2. **Branch**: In GitHub Desktop, switch to `main` and create a new branch (e.g., `add-login-feature`).
3. **Commit & Push**: Commit changes in GitHub Desktop, then click `Push origin`.
4. **Pull Request**: Open a pull request on GitHub, choosing `main` as the base branch, and tag a teammate for review.

For more details, see [GitHub Flow](https://githubflow.github.io/).

## Communication 🗂️

Join the [Discord server](https://discord.gg/a2ARm52WwE) for discussions and updates.

## License 📝

Distributed under the Apache 2.0 License. See [LICENSE](LICENSE) for details.

