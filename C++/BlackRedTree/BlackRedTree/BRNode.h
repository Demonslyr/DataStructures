#ifndef BRNode_H
#define BRNode_H

#include "stdafx.h"

class BRNode : public BRLeaf {
private:
	BRNode* BRTree;
	BRLeaf* left;
	BRLeaf* right;
	int value;
public:
	BRNode();
	BRNode(int value);
	int GetValue();
};
#endif