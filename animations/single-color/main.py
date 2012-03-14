import sys
sys.path.append("./osc")
from osc import ColorsOut


if __name__ == "__main__":
    import time
    out = ColorsOut()
    while True:
        pix = [(4.0 * 127.0, 4.0 * 101.0, 4.0 * 30.0)] * 24
        out.write(pix)
        time.sleep(0.2)
