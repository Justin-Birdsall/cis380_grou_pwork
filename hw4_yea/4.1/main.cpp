#include <iostream>
#include <vector>
#include <algorithm>
//bottom up dp 
int main() {
    //declare int to take in how many nums 
    int nums;
    std::cin >> nums;
    //create the vector to the size of the nums 
    std::vector<int> numbers(nums);
    //process input for our chain up blocks ex 20 10 1 10 20
    for (int i = 0; i < nums; ++i) { std::cin >> numbers[i]; }
    //create a dp vector thats the size of our vector plus one 
    std::vector<int> dp(nums + 1, 0);
    //making our input 0 20 0 0 0 0 base case
    dp[1] = numbers[0];
    //take our slider and essentially take the best max option of taking versus skipping 
    for (int i = 2; i <= nums; ++i) { dp[i] = std::max(dp[i - 1], dp[i - 2] + numbers[i - 1]); }
    //print out our sum
    std::cout << dp[nums] << std::endl;
    return 0;
}
