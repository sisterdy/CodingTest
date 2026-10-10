/*
'원본' 배열을 왼쪽부터 순회하면서 answer 배열의 마지막 값이랑 비교하기
*/
#include <vector>

using namespace std;

vector<int> solution(vector<int> arr) {
    vector<int> answer;

    // 원본 배열을 앞에서부터 하나씩 순회
    for (int value : arr) {

        // answer 배열이 비어 있거나 or answer 배열의 마지막 원소와 현재 값이 다르면 추가
        if (answer.empty() || answer.back() != value) {
            answer.push_back(value);
        }
    }

    return answer;
}