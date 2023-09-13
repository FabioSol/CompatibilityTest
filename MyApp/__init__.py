import sys
import os

# Get the base directory when running as an executable
base_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))

# Construct the database file path
db_file_path = os.path.join(base_dir, 'testing.db')