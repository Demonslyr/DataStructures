// BlackRedTree.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

using namespace std;

int* GenerateRandomData(int size) {
	srand(time(NULL));
	int* randIntArr = new int[size];
	for (int i = size; i--;) {
		randIntArr[i] = rand() % size + 1;
	}
	return randIntArr;
}

void EvalTree(BRTree* brtree) {
}

int main()
{
	// User input
	string arraySize;
	cin >> arraySize;

	// Generate Mock Data
	int* randomData = GenerateRandomData(stoi(arraySize));

	//Initialize Tree
	BRTree* brTreeStore = new BRTree(randomData,false);

	//Evaluate
	EvalTree(brTreeStore);
}
