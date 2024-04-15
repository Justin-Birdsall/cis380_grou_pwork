#include "base_rules.h"

BaseRules::BaseRules() {
    // Constructor implementation
}

BaseRules::~BaseRules() {
    // Destructor implementation
}

bool BaseRules::isFirstHandValid(const std::vector<int>& tilesPlayed) {
    int totalValue = 0;
    for (int tile : tilesPlayed) {
        totalValue += tile;
    }
    return totalValue >= 30;
}