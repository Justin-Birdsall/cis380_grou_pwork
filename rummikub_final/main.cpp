#include <iostream>

#include <cstdlib>
#include <ctime>

const int NUM_PLAYERS = 4;
const int TILES_PER_PLAYER = 14;
const int NUM_TILES = NUM_PLAYERS * TILES_PER_PLAYER;
const int NUM_COLORS = 4;
const int MAX_NUMBER = 13;

int tiles[NUM_PLAYERS][TILES_PER_PLAYER];
// Function to initialize the tile pool
void initializeTilePool() {
    // Seed the random number generator
    srand(time(0));
    // Initialize an array to represent the tile pool
    int tilePool[NUM_COLORS][MAX_NUMBER + 1];
    // Initialize the tile pool with the correct number of each tile
    for (int color = 0; color < NUM_COLORS; color++) {
        for (int number = 1; number <= MAX_NUMBER; number++) {
            tilePool[color][number] = 2; // Each tile appears twice in Rummikub 
            }
    }
    // Randomly draw tiles for each player
    for (int player = 0; player < NUM_PLAYERS; player++) 
    {
        for (int tileIndex = 0; tileIndex < TILES_PER_PLAYER; tileIndex++) 
        {
            // Find a random available tile
            int color, number;
            do 
            {
                color = rand() % NUM_COLORS;
                number = rand() % (MAX_NUMBER + 1);
            } while (tilePool[color][number] == 0);
            // Assign the tile to the player
            tiles[player][tileIndex] = color * (MAX_NUMBER + 1) + number;
            // Reduce the count of available tiles
            tilePool[color][number]--;
        }
    }
}

int main() {
    initializeTilePool();

    // Print out the tiles for each player
    for (int player = 0; player < NUM_PLAYERS; player++) {
        std::cout << "Player " << (player + 1) << " tiles:";
        for (int tileIndex = 0; tileIndex < TILES_PER_PLAYER; tileIndex++) {
            int color = tiles[player][tileIndex] / (MAX_NUMBER + 1);
            int number = tiles[player][tileIndex] % (MAX_NUMBER + 1);
            std::cout << " " << color << "-" << number;
        }
        std::cout << std::endl;
    }

    return 0;
}