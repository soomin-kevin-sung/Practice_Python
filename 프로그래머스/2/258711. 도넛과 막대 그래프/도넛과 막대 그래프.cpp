#include <bits/stdc++.h>
//#define debug printf
#define debug

using namespace std;

map<int, bool> _visited;
map<int, set<int>> _edge_table;
map<int, int> _in_table;
map<int, int> _out_table;

void SetTablesAndCenterNode(vector<vector<int>> edges,
                           set<int> &nodes,
                           int &center_node) {        
    // _edge_table, _inout_table 생성
    for (auto edge : edges) {
        // nodes에 노드 추가
        nodes.insert(edge[0]);
        nodes.insert(edge[1]);
        
        // edge_table에 삽입
        _edge_table[edge[0]].insert(edge[1]);   
        
        // inout_table 갱신
        _out_table[edge[0]]++;
        _in_table[edge[1]]++;
    }
    
    // center node 구하기
    int max_for_center_node = -1;
    for (int node : nodes) {
        if (_in_table[node] == 0 &&
            _out_table[node] > max_for_center_node) {
            center_node = node;   
            max_for_center_node = _out_table[node];
        }
    }
    
    // center node 방문 설정
    _visited.insert({center_node, true});
    // nodes 에서 center_node 제거
    nodes.erase(center_node);
    
    // center node의 in을 빼줌
    for (int node : _edge_table[center_node])
        _in_table[node]--;
}

int GetGraphShape(int root) {    
    queue<int> q;
    q.push(root);
    
    bool flag_stick = false, flag_sand = false;
    
    // 연관 노드 방문
    while (!q.empty()) {
        int node = q.front();
        _visited[node] = root;
        
        q.pop();
        
        if (_in_table[node] == 2 && _out_table[node] == 2)
            flag_sand = true;
        else if (_out_table[node] == 0)
            flag_stick = true;
        
        for (int next_node : _edge_table[node])
        {
            if (_visited[next_node])
                continue;
            
            q.push(next_node);
        }
    }
    
    debug("%d: %d %d %d\n", root, !flag_stick && !flag_sand, flag_stick, flag_sand);
    
    if (flag_sand)
        return 3;
    else if (flag_stick)
        return 2;
    else
        return 1;
}

vector<int> solution(vector<vector<int>> edges) {    
    vector<int> answer(4);
    set<int> nodes;
    int center_node;
    
    // edge_table, in_table, out_table, nodes, center_node 설정
    SetTablesAndCenterNode(edges, nodes, center_node);
    
    debug("center: %d\n", center_node);
    
    // in이 없는 노드 순회
    for (int node : nodes)
    {
        // 이미 방문된 노드거나 in이 있는 노드라면
        if (_visited[node] ||
            _in_table[node] > 0)
            continue;
        
        // 그래프 찾고 마킹
        int graph = GetGraphShape(node);
        answer[graph]++;
    }
    
    // 나머지 노드 순회
    for (int node : nodes) {
        // 이미 방문된 노드라면
        if (_visited[node])
            continue;
        
        // 그래프 찾고 마킹
        int graph = GetGraphShape(node);
        answer[graph]++;
    }
    
    // answer 처번째에 center_node 지정
    answer[0] = center_node;
    
    return answer;
}