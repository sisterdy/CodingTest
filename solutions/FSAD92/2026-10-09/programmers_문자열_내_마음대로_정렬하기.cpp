/*
대놓고 람다를 쓰라는 문제
*/

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<string> solution(vector<string> strings, int n) {
    sort(strings.begin(), strings.end(),
        [n](const string& a, const string& b){
            // n번째 문자가 같으면 문자열 '전체'를 사전순으로 정렬
            if (a[n] == b[n]) {
                return a < b;
            }
            // n번째 문자가 다르면 n번째 문자가 작은 문자열이 앞으로
            return a[n] < b[n];
        });
    return strings;
}