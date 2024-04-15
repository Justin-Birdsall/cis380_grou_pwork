#include <iostream>
#include <string>
#include <cstring>
/**Specs:
 * Input:
 *      - First Line: N: number of smart bricks in the row
 *      - Second Line: N values: separated by spaces, indicating the
 *        speed of each smart brick
 *
 * Output:
 *      - A single number indicating the maximum total speed possible
 *
 * Specs:
 *      - Given a series of N smart bricks where brick, i, in order, has speed
 *        Si, determine the maximum total speed that can be obtained.
 *      - Choose which subset of bricks to target to maximize total brick speed
 *        without choosing any two that are neighbors.
 */

int main()
{
    int num_bricks;
    std::cin >> num_bricks;
    char* brick_speeds;
    std::cin >> brick_speeds;

    char* strtok(brick_speeds, " ") 
}
