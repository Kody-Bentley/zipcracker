import zipfile
import sys
from tqdm import tqdm
from threading import Thread, active_count

print(f'Number of arguments: {len(sys.argv)}, arguments')
print(f'Argument list is: {str(sys.argv)}')
found = []

def extract_file(z_file, password):
    try:
        z_file.extractall(pwd=password.strip())
        #print(f'Password Found: {password}')
        found.append(password)
        if len(found) > 0:
            print(f'Password Found: {password}')
            sys.exit()
            # exit(0)
    except:
        pass

def main():
    z_file = zipfile.ZipFile(sys.argv[1])
    passfile = str(sys.argv[2])
    n_words = len(list(open(passfile, "rb")))
    t = []
    # print the total number of passwords
    print("Total passwords to test:", n_words)
    with open(passfile, "rb") as wordlist:
        for word in tqdm(wordlist, total=n_words, unit="word"):
            # z_file.extractall(pwd=word.strip())
            # t = Thread(target=extract_file, args=(z_file, word.strip()))
            t.append(Thread(target=extract_file, args=(z_file, word.strip())))
            # t.start()
        for thread in t:
            thread.start()
        for thread in t:
            thread.join()
if __name__ == '__main__':
    main()
