#include <iostream>
#include <vector>

int countWays(std::vector<int>& bricks, int Ltotal) {
    int N = bricks.size();
    std::vector<std::vector<int>> dp(N + 1, std::vector<int>(Ltotal + 1, 0));

    // Base case: 1 way to achieve length 0
    for (int i = 0; i <= N; ++i) {
        dp[i][0] = 1;
    }

    for (int i = 1; i <= N; ++i) {
        for (int j = 1; j <= Ltotal; ++j) {
            dp[i][j] = dp[i - 1][j];
            if (j >= bricks[i - 1]) {
                dp[i][j] += dp[i][j - bricks[i - 1]];
            }
        }
    }

    return dp[N][Ltotal];
}

int main() {
    int T;
    std::cin >> T;

    for (int t = 0; t < T; ++t) {
        int N, Ltotal;
        std::cin >> N >> Ltotal;

        std::vector<int> bricks(N);
        for (int i = 0; i < N; ++i) {
            std::cin >> bricks[i];
        }

        int ways = countWays(bricks, Ltotal);
        std::cout << ways << std::endl;
    }

    return 0;
}
