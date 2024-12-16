import subprocess
import os

def main():
    os.chdir('alt_cuda_corr')
    subprocess.run(['python', 'setup.py', 'install'], check=True)
    # os.chdir('..')

if __name__ == "__main__":
    main()