#! /usr/bin/python3

import sys, getopt
import random

offsets={'0':[], '1':[], '2':[], '3':[], '4':[], '5':[], '6':[], '7':[], '8':[], '9':[], 'A':[], 'B':[], 'C':[], 'D':[], 'E':[], 'F':[]}

def usage():
    print("\n=================================================================");
    print("Digital Book Cipher Tool");
    print("Usage:");
    print("digibook.py -b book -p plaintext|-c ciphertext -o outfile");
    print("----------");
    print("-b | --book <file>                        ### book file");
    print("-p | --plain <file>                       ### plaintext file");
    print("-c | --cipher <file>                      ### ciphertext file");
    print("-o | --outfile <file>                    ### output file");
    print("=================================================================\n");

# create book table
# for each matched char in string, append char index to offset list
def initialize(book):
    for i in range(len(book)):
        offsets[book[i]].append(i);

# encrypt
def encrypt(plaintext):
    ciphertext="";
    for i in range(len(plaintext)):
        ciphertext = ciphertext + str(offsets[plaintext[i]][random.randrange(0,len(offsets[plaintext[i]]))]) + " ";

    return ciphertext;

# decrypt
def decrypt(ciphertext):
    plaintext="";
    for c_char in ciphertext:
        for i in offsets.keys():
            if (c_char != ""):
                if (offsets[i].count(int(c_char)) > 0 ):
                    plaintext = plaintext + str(i);

    return plaintext;

def main(argv):
    isEncrypt = False;
    isDecrypt = False;
    isBook = False;

    if (len(argv)<1):
        print("Missing Arguments");
        usage();
        sys.exit(2);
    try:
        opts, args = getopt.getopt(argv, 'hb:p:c:o:', ["book=", "plain=", "cipher=", "outfile="]);
    except getopt.GetoptError as err:
        print(err);
        usage();
        sys.exit(2);

    for opt, arg in opts:
        if opt == '-h':
            usage();
            sys.exit();
        elif opt in ('-b', "--book"):
            isBook = True
            b_file = arg;
        elif (opt in ('-p', "--plain")) and (not isDecrypt) and isBook:
            isEncrypt = True;
            p_file = arg;
        elif (opt in ('-c', "--cipher")) and (not isEncrypt) and isBook:
            isDecrypt = True;
            c_file = arg;
        elif opt in ('-o' "--outfile"):
            o_file = arg;
        else:
            print("what?, how did this happen?");
            usage();
            sys.exit(2);
    
    # initialize
    book = open(b_file, "rb").read().hex().upper();
    initialize(book);
    
    # encrypt
    if isEncrypt:
        outfile = open(o_file, "w");
        plaintext = open(p_file, "rb").read().hex().upper();
        ciphertext = encrypt(plaintext);
        outfile.write(ciphertext);
        outfile.close()

    # decrypt
    if isDecrypt:
        outfile = open(o_file,"wb");
        ciphertext = open(c_file, "r").read().split(" ");
        plaintext = decrypt(ciphertext);
        outfile.write(bytearray.fromhex(plaintext));
        outfile.close();


if __name__ == "__main__":
    main(sys.argv[1:]);
 
##END##
