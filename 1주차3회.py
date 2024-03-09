
def solution(bridge_length, weight, truck_weights):
    time = 0
    curr_weight = 0
    on_bridge = []
    crossed = []
    truck_weight_list = []
    
    for n in range(len(truck_weights)):
        truck_weight_list.append(truck_weights[n])
    on_bridge.append(truck_weight_list[0])
    
    curr_weight = curr_weight + on_bridge[0]
    time += 1
    
    while (curr_weight + truck_weight_list[0] < weight and truck_weight_list):
        on_bridge.append(truck_weights.pop(0))
        curr_weight = curr_weight + int(on_bridge[0])
        time += 1
    time = time + bridge_length 

    return time
bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]
solution(bridge_length, weight, truck_weights)
