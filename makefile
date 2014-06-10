CC = gcc
#The -Ofast might not work with older versions of gcc; in that case, use -O2
# if there is some error like no such instruction: `vfmadd312ss', remove -march=native 
CFLAGS = -lm -pthread -Ofast -Wall -funroll-loops -Wno-unused-result

all: word2vec word2phrase distance word-analogy compute-accuracy distance_byQueryList

word2vec : word2vec.c
	$(CC) word2vec.c -o word2vec $(CFLAGS)
word2phrase : word2phrase.c
	$(CC) word2phrase.c -o word2phrase $(CFLAGS)
distance : distance.c
	$(CC) distance.c -o distance $(CFLAGS)
distance_byQueryList : distance_byQueryList.c
	$(CC) distance_byQueryList.c -o distance_byQueryList -lm
word-analogy : word-analogy.c
	$(CC) word-analogy.c -o word-analogy $(CFLAGS)
compute-accuracy : compute-accuracy.c
	$(CC) compute-accuracy.c -o compute-accuracy $(CFLAGS)
	chmod +x *.sh

clean:
	rm -rf word2vec word2phrase distance word-analogy compute-accuracy
