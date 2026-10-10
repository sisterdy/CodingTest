/*
기존 파이썬 코드를 cpp로 옮기기
*/
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;

    // 각 명령은 start, stop, nth
    for (const auto& command : commands) {
        int start = command[0];
        int stop = command[1];
        int nth = command[2];

        // start번째부터 stop번째까지 배열 복사
        vector<int> sliced(array.begin() + start - 1, array.begin() + stop);

        // sliced를 오름차순으로 정렬
        sort(sliced.begin(), sliced.end());

        // 정렬된 sliced의 nth번째 원소 선택하고 정답 배열에 추가
        answer.push_back(sliced[nth - 1]);
    }

    return answer;
}