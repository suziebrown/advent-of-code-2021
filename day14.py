from typing import List, Dict
import utils


class Rule:
    def __init__(self, from_pair: str, to_add: str):
        self.from_pair = from_pair
        self.to_add = to_add
        self.to_left = from_pair[0] + to_add
        self.to_right = to_add + from_pair[1]


def fast_forward(number_of_steps: int):
    for _ in range(number_of_steps):
        polymerise()


def polymerise():
    # TODO: go through polymer (i.e. pair counts) & apply update to each consecutive pair
    # Take a copy of the counts first so updates don't interfere with original counts
    pass


def update_one_pair(rule: Rule):
    pair_counts[rule.from_pair] -= 1
    pair_counts[rule.to_left] += 1
    pair_counts[rule.to_right] += 1
    element_counts[rule.to_add] += 1


def get_score():
    return max(element_counts.values()) - min(element_counts.values())

            
def main():
    (template, rules) = parse_input()
    
    global pair_counts
    global element_counts
    pair_counts = get_initial_pair_counts(template, rules)
    element_counts = get_initial_element_counts(template)
    
    # Part 1
    print("=== Part 1 ===")
    fast_forward(10)
    answer = get_score()
    print("Answer:", answer)

    # Part 2
    print("=== Part 2 ===")
    answer = "?"
    print("Answer:", answer)


def parse_input() -> tuple[str, Dict[str, Rule]]:
    input_file = open("day14_input.txt", "r")
    input_parts = input_file.read().strip().split("\n\n")
    input_file.close()
    
    template = input_parts[0]
    rules_raw = input_parts[1].split("\n")
    
    rules = dict[str, Rule]()
    for rule in rules_raw:
        rule_split = rule.strip().split(" -> ")
        rules.update({rule_split[0]: Rule(rule_split[0], rule_split[1])})
    
    return (template, rules)


def get_initial_element_counts(template: str) -> Dict[str, int]:
    element_counts = dict[str, int]()
    for element in template:
        if element in element_counts.keys():
            element_counts[element] += 1
        else:
            element_counts.update({element: 1})

    return element_counts
    

def get_initial_pair_counts(template: str, rules: Dict[str, Rule]) -> Dict[str, int]:
    pair_counts = dict[str, int]()
    unique_pairs = get_unique_pairs(rules)
    
    for pair in unique_pairs:
        pair_counts.update({pair: 0})
        
    for index in range(0, len(template) - 1):
        pair_here = template[index : index + 2]
        if template[index : index + 2] in pair_counts.keys():
            pair_counts[pair_here] += 1

    return pair_counts


def get_unique_pairs(rules: Dict[str, Rule]) -> List[str]:
    rules_as_list_of_lists = [[rule.from_pair, rule.to_left, rule.to_right] for rule in rules.values()]
    return utils.unique(utils.flatten(rules_as_list_of_lists))


if __name__ == "__main__":
    main()
