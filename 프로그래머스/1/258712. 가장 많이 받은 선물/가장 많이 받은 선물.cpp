#include <bits/stdc++.h>

using namespace std;

vector<string> split(string input, char delimiter) {
    vector<string> answer;
    stringstream ss(input);
    
    string temp;
    while (getline(ss, temp, delimiter))
        answer.push_back(temp);
    
    return answer;
}

int solution(vector<string> friends, vector<string> gifts) {
    int num_of_friends = friends.size();
    map<string, int> index_dict;
    
    // index 사전 생성
    for (int i = 0; i < num_of_friends; i++)
        index_dict[friends[i]] = i;
    
    // give-take 및 지수 생성
    vector<vector<int>> table(num_of_friends, vector<int>(num_of_friends, 0));
    vector<int> factors(num_of_friends);
    for (const auto gift : gifts) {
        auto pkts = split(gift, ' ');
        int from = index_dict[pkts[0]];
        int to = index_dict[pkts[1]];
        
        table[from][to]++;
        factors[from]++;
        factors[to]--;
    }
    
    int answer = 0;    
    for (int i = 0; i < num_of_friends; i++) {
        
        int cnt = 0;
        for (int j = 0; j < num_of_friends; j++) {
            if (table[i][j] > table[j][i]) {
                cnt++;
            }
            else if (table[i][j] == table[j][i]) {
                if (factors[i] > factors[j])
                    cnt++;
            }
        }
        
        answer = max(answer, cnt);
    }
    
    return answer;
}

