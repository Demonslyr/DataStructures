#ifndef BRLeaf_H
#define BRLeaf_H

#include "stdafx.h"

class BRLeaf {
	public:
		int value;
		char color = 'b';
		BRLeaf();
		BRLeaf(int value);
		int GetValue();

};
#endif