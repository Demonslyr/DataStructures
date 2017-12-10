#ifndef BRTree_H
#define BRTree_H

#include "stdafx.h"

class BRTree {
private:
	BRNode* root;
	void GenerateTree();
public:
	BRTree();
	BRTree(int* initData, bool allowDuplicates);
	bool Contains(int value);
	int TryGet(int value);
	int* TryGetAll(int value);
	void Insert(int value);
	void InsertSet(int* values);
	void Remove(int value);
	void RemoveAll(int value);
	void RemoveSet(int value);
	// Try cut operations
};
#endif
