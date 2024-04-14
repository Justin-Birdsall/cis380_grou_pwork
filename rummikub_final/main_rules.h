#ifndef BASE_RULES_H
#define BASE_RULES_H

class BaseRules {
public:
    BaseRules();
    virtual ~BaseRules();
    bool isFirstHandValid(const std::vector<int>& tilesPlayed);

    // Add shared rule-checking functions here
};

#endif

