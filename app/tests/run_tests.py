import time
import subprocess


if __name__ == "__main__":
    subprocess.call("python -m pytest --html=report.html --self-contained-html")

