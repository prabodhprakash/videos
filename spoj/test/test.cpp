#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char const *argv[])
{

	//1. taking input from a text file
	// freopen("input.txt", "r", stdin);

	//2. printing output to text file
	// freopen("output.txt", "w", stdout);

	std::ios::sync_with_stdio(false);

	int number;

	while (true)
	{
		cin >> number;
		
		if (number == 42)
		{
			break;
		}	

		cout << number << "\n";
	}

	return 0;
}