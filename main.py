from config import kList, roundNum, samples
from app import App
import hashlib

if __name__ == "__main__":
    app = App(kList, roundNum, samples)
    app.hashTest(hashlib.sha1)
    app.hashTest(hashlib.sha256)
    app.hashTest(hashlib.sha512)