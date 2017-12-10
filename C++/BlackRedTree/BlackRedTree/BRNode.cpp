#include "stdafx.h"
BRNode::BRNode() {

}

BRNode::BRNode(int value) {
	this->value = value;
}

int BRNode::GetValue() {
	return this->value;
}
