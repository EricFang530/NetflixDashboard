NetflixDashboard transforms raw Netflix data into an interactive, visually coherent dashboard. Built with Flask and Plotly, it guides users through exploratory prompts and curated visualizations to uncover patterns in global content consumption.
Each chart and label is refined for clarity, balance, and explanatory purpose. This repo showcases genre, country, and rating modules with minimal, elegant fixes—emphasizing reproducibility and onboarding clarity.
# 1. Clone the repo
git clone https://github.com/EricFang530/NetflixDashboard.git
cd NetflixDashboard

# 2. Create and activate Conda environment
conda create -n netflixenv python=3.11
conda activate netflixenv

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python app.py

Visit http://127.0.0.1:5000 to explore the dashboard.




