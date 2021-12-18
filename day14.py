from typing import List, Dict, Tuple
import utils


class Rule:
    def __init__(self, from_pair: str, to_add: str):
        self.from_pair = from_pair
        self.to_add = to_add
        self.to_left = from_pair[0] + to_add
        self.to_right = to_add + from_pair[1]


def fast_forward(number_of_steps: int, rules: Dict[str, Rule]):
    for _ in range(number_of_steps):
        polymerise(rules)


def polymerise(rules: Dict[str, Rule]):
    pair_counts_before = pair_counts.copy()
    for (pair, count) in pair_counts_before.items():
        update_one_pair_n_times(count, rules[pair])


def update_one_pair_n_times(n: int, rule: Rule):
    pair_counts[rule.from_pair] -= n
    pair_counts[rule.to_left] += n
    pair_counts[rule.to_right] += n
    element_counts[rule.to_add] += n


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
    fast_forward(10, rules)
    answer = get_score()
    print("Answer:", answer)

    # If running immediately after Part 1, reduce number of steps to 30
    # Part 2
    print("=== Part 2 ===")
    fast_forward(40, rules)
    answer = get_score()
    print("Answer:", answer)


def parse_input() -> Tuple[str, Dict[str, Rule]]:
    input_file = open("day14_input.txt", "r")
    input_parts = input_file.read().strip().split("\n\n")
    input_file.close()
    
    template = input_parts[0]
    rules_raw = input_parts[1].split("\n")
    
    rules = dict()
    for rule in rules_raw:
        rule_split = rule.strip().split(" -> ")
        rules.update({rule_split[0]: Rule(rule_split[0], rule_split[1])})
    
    return template, rules


def get_initial_element_counts(template: str) -> Dict[str, int]:
    element_counts = dict()
    for element in template:
        if element in element_counts.keys():
            element_counts[element] += 1
        else:
            element_counts.update({element: 1})

    return element_counts
    

def get_initial_pair_counts(template: str, rules: Dict[str, Rule]) -> Dict[str, int]:
    pair_counts = dict()
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
