#include <iostream>
#include <stack>
#include <fstream>

using namespace std;

int main(int argc, char const *argv[])
{
	// freopen("input.txt", "r", stdin);
	int noTestCases;

	cin >> noTestCases;

	while (noTestCases--)
	{
		string inputLine;
		string outputLine;

		stack<char> operationStack;

		cin >> inputLine;

		for (char& c : inputLine)
		{
			if (c == '(' || c == '+' || c == '-' || c == '*' || c == '^' || c == '/')
			{
				operationStack.push(c);
			}
			else if (c == ')')
			{
				//here we need to pop elements from operationStack until we get a matching opening bracket

				char poppedElement;

				while (!operationStack.empty())
				{
					poppedElement = operationStack.top();
					operationStack.pop();

					if (poppedElement == '(')	//we have got a matching opening bracket - so we need to break here
					{
						break;
					}
					else
					{
						outputLine += poppedElement;
					}
				}
			}
			else
			{
				outputLine += c;	
			}
		}

		cout << outputLine << "\n";

	}

	return 0;
}