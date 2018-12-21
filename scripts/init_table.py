import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from manage import db

if __name__ == "__main__":
    db.create_all()
