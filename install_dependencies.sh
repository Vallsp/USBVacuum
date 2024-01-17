#Install packages
sudo apt install python3 python3-tk python3-venv python3-pip -y

# Create a Python virtual environment
python3 -m venv env

# Activate the virtual environment
source env/bin/activate

# Install requirements
pip install -r requirements.txt
