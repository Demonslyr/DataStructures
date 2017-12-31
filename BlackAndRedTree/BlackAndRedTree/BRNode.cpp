#include "stdafx.h"
BRNode::BRNode() {

}

BRNode::BRNode(int value, char color) {
	this->value = value;
	this->color = color;
}

int BRNode::GetValue() {
	return this->value;
}
