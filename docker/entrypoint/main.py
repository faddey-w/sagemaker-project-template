import torch
import sys
import os
import pprint


def main():
    print(sys.argv)
    pprint.pprint(os.environ)
    print("CUDA available =", torch.cuda.is_available())


if __name__ == "__main__":
    main()
