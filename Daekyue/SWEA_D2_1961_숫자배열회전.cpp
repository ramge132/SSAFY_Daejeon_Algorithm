#include<iostream>
#include<bits/stdc++.h>

using namespace std;

string arr[8][8];
string answer[8][4];

int main(int argc, char** argv)
{
	int test_case;
	int T;

	//freopen("input.txt", "r", stdin);
	cin >> T;

	for (test_case = 1; test_case <= T; ++test_case)
	{
		for (int i = 0; i < 8; i++)
			for (int j = 0; j < 3; j++)
				answer[i][j] = "";
		
		int n;
		cin >> n;
		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++)
				cin >> arr[i][j];
		for (int k = 0; k < n; k++)
		{
			for (int i = 0; i < n; i++)
			{
				for (int j = 0; j < 3; j++)
				{
					if (j == 0)
						answer[i][j].append(arr[n - 1 - k][i]);
					else if (j == 1)
						answer[i][j].append(arr[n - 1 - i][n - k - 1]);
					else if(j == 2)
						answer[i][j].append(arr[k][n - i - 1]);
				}
			}
		}
		
		cout << "#" << test_case << endl;
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < 3; j++)
				cout << answer[i][j] << " ";
			cout << endl;
		}
	}

	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}
