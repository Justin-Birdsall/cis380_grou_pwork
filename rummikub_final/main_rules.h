#ifndef BASE_RULES_H
#define BASE_RULES_H
#include <vector>

class BaseRules {
public:
    BaseRules();
    virtual ~BaseRules();
    bool isFirstHandValid(const std::vector<int>& tilesPlayed);
    bool drawOrNot()
    // Add shared rule-checking functions here
};

#endif

