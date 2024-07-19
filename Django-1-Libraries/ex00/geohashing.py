import sys
import antigravity

if __name__ == "__main__":
    try:
        assert len(sys.argv) == 4, "Wrong number of arguments"
    except Exception as e:
        print("Error: ", e)
