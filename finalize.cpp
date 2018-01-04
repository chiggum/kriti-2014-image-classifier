#include <iostream>
#include <fstream>
#include <cstdlib>
using namespace std;

int main(int argc, char **argv) {
	ifstream myf1(argv[1]);
	ifstream myf2(argv[2]);
	ifstream myf3(argv[3]);
	int numTest = atoi(argv[4]);
	int numK = atoi(argv[5]);

	int cnt = 0;
	for(int i = 1; i <= numTest; ++i) {
		int x, y, z, x1, y1, z1;
		string st, st1, st2;
		getline(myf1, st);
		getline(myf2, st1);
		getline(myf3, st2);
		x = st[0] - '0';
		x1 = st1[0] - '0';
		y = st[2] - '0';
		y1 = st1[2] - '0';
		st = st.substr(3, -1);
		st1 = st1.substr(3, -1);
		z = atoi(st.c_str());
		z1 = atoi(st1.c_str());
		cout << st2;
		if(x == 1) {
			cout << " Photo " << endl;
		} else if(x1 == 0) {
			cout << " Art " << endl;
		} else {
			if(numK-z >= z1) {
				cout << " Art " << endl;
			} else {
				cout << " Photo " << endl;
			}
		}
	}
	return 0;
}