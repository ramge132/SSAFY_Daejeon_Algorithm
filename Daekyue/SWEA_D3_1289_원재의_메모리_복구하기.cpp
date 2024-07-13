#include <bits/stdc++.h>

using namespace std;

int mem[50];
int main(int argc, char** argv)
{
	int test_case;
	int T;
	cin >> T;
	for (test_case = 1; test_case <= T; ++test_case)
	{
		string str;
		cin >> str;
		int cnt = 0;
		int pre = 0;
		for (int i = 0; i < str.length(); i++)
		{
			mem[i] = str[i] - '0';
			if (mem[i] != pre)
			{
				cnt++;
				if (mem[i] == 0)
					pre = 0;
				else
					pre = 1;
			}
		}
		cout << "#" << test_case << " " << cnt << "\n";
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}
