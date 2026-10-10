#include <vector>
#include <unordered_set>
#include <algorithm>

using namespace std;

int solution(vector<int> nums) {
    // nums의 모든 원소를 unordered_set에 저장 -> 중복 방지
    unordered_set<int> kinds(nums.begin(), nums.end());

    // 선택할 수 있는 폰켓몬의 최대 마릿수
    int limit = nums.size() / 2;

    // 중복 제거 후 남은 종류 개수 카운팅
    int distinct_count = kinds.size();

    // 종류의 수와 선택 가능한 마릿수 중 작은 값 반환
    return min(limit, distinct_count);
}