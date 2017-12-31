#ifndef BRNode_H
#define BRNode_H

#include "stdafx.h"

class BRNode : public BRLeaf {
private:
	BRNode* BRTree;
	BRLeaf* left;
	BRLeaf* right;
	BRLeaf* parent;
	char color = 'b';
	int value;
	BRNode();
public:
	BRNode(int value, char color);
	int GetValue();
};
#endif