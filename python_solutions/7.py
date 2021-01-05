with open("input_7.txt", "r") as f:
    lines = f.readlines()

input_to_output_bags = {}

for line in lines:
    input_bag, output_bags = line.split("contain")
    input_bag = input_bag.strip()
    input_bag = input_bag.replace(" bags", "")
    output_bags = [bag.strip().replace(" bags", "").replace(" bag", "") for bag in output_bags.strip()[:-1].split(",")]
    
    input_to_output_bags[input_bag] = {}
    for output_bag in output_bags:
        if output_bag == "no other":
            break
        output_bag_count, output_bag_type = output_bag.split(" ", 1)
        input_to_output_bags[input_bag][output_bag_type] = int(output_bag_count)

part_1 = False
if part_1:
    searching_for = ["shiny gold"]
    history = set()
    while len(searching_for) != 0:
        currently_searching = searching_for.pop()
        for input_bag in input_to_output_bags:
            if currently_searching in input_to_output_bags[input_bag]:
                if input_bag not in history:
                    searching_for.append(input_bag)
                    history.add(input_bag)
    print(len(history))
else:
    unrolled_bags = 0
    to_unroll = [("shiny gold", 1)]
    while len(to_unroll) > 0:
        next_unroll = []
        print(to_unroll)
        for unrolling in to_unroll:
            unrolling_type, unrolling_count = unrolling
            unrolled_bags += unrolling_count
            output_bags = input_to_output_bags[unrolling_type]
            for output_bag in output_bags:
                next_unroll.append((output_bag, output_bags[output_bag] * unrolling_count))
        to_unroll = next_unroll
    print(unrolled_bags - 1)