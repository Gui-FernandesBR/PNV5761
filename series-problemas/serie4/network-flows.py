import numpy as np
from ortools.graph.python import min_cost_flow


def main():
    """MinCostFlow simple interface example."""
    # Instantiate a SimpleMinCostFlow solver.
    smcf = min_cost_flow.SimpleMinCostFlow()

    # Define four parallel arrays: sources, destinations, capacities,
    # and unit costs between each pair. For instance, the arc from node 0
    # to node 1 has a capacity of 15.
    start_nodes = np.array([1, 2, 2, 2, 3, 3, 3, 3, 4, 5, 6, 6, 6, 6, 7])
    end_nodes = np.array([4, 1, 5, 8, 2, 1, 5, 8, 3, 6, 4, 7, 3, 8, 4])
    unit_costs = np.array([3, 8, 5, 0, 3, 4, 1, 0, 5, 2, 6, 5, 3, 0, 4])

    # define uma capacidade infinita
    capacities = np.array([1000]) * np.ones(len(start_nodes))

    # Define an array of supplies at each node.
    supplies = [
        -5,  # b1
        6,  # b2
        4,  # b3
        -3,  # b4
        -4,  # b5
        6,  # b6
        -2,  # b7
        -2,  # b8
    ]

    # Add arcs, capacities and costs in bulk using numpy.
    all_arcs = smcf.add_arcs_with_capacity_and_unit_cost(
        start_nodes, end_nodes, capacities, unit_costs
    )

    # Add supply for each nodes.
    smcf.set_nodes_supplies(np.arange(0, len(supplies)), supplies)

    # Find the min cost flow.
    status = smcf.solve()

    if status != smcf.OPTIMAL:
        print("There was an issue with the min cost flow input.")
        print(f"Status: {status}")
        exit(1)
    print(f"Minimum cost: {smcf.optimal_cost()}")
    print("")
    print(" Arc    Flow / Capacity Cost")
    solution_flows = smcf.flows(all_arcs)
    costs = solution_flows * unit_costs
    for arc, flow, cost in zip(all_arcs, solution_flows, costs):
        print(
            f"{smcf.tail(arc):1} -> {smcf.head(arc)}  {flow:3}  / {smcf.capacity(arc):3}       {cost}"
        )


if __name__ == "__main__":
    main()
