# define the state

from typing_extensions import TypedDict

class Experimental(TypedDict):
    messages: str
    is_true: bool # based on the logic on node 4 


# define the node

# defne the fiest node

def node_1(state: Experimental):
    print("-------node1---------")
    if state["is_true"]:
        return {"messages": state["messages"] , "is_true": True}
    else:
        return {"messages": state["messages"] , "is_true": False}


#define rthe second node

def node_2(state: Experimental):
    print("-------node2---------")
    return {"messages": state["messages"] + "i am developer", "is_true": False}

def node_3(state: Experimental):
    print("-------node3---------")
    return {"messages": state["messages"] + "i am cybersecuirty", "is_true": False}

def node_4(state: Experimental):
    print("-------node4---------")
    return {"messages": state["messages"] + "and ", "is_true": True}



# define the ediges based on the condiction do i create the new funciton that deside the which mode you want to go
import random
from typing import Literal   # it was only give those values inside the list


def get_randome_number() -> str:
    if random.random() < 0.5:

        # 50% of the time, we return Node 2
        return "node2"
    
    # 50% of the time, we return Node 3
    return "node3"


def deside_nodes_for_3_node(state:Experimental) -> Literal["node2","node3","node4"]:
    print("-------deside_nodes_loop---------")
    values = random.random()
    print("values: ", values)
    if state["is_true"]:
        return get_randome_number()
    if values > 0.00 and values < 0.25:
        return "node2"
    elif values > 0.25 and values < 0.50:
        return "node4"
    else:
        return "node3"
    
def node_1_condition(state:Experimental) -> Literal["node1"]:
    print("-------node1_condition---------")
    state["is_true"] = True
    print("state: ", state["messages"])
    return "node1"
    

#build the graph 

from langgraph.graph import StateGraph, START, END

#build tge graph

graph = StateGraph(Experimental)
graph.add_node("node1",node_1)
graph.add_node("node2",node_2)
graph.add_node("node3",node_3)
graph.add_node("node4",node_4)

#give the condiction ediges

graph.add_edge(START,"node1")
graph.add_conditional_edges("node1",deside_nodes_for_3_node)
graph.add_conditional_edges("node4",node_1_condition)
graph.add_edge("node2",END)
graph.add_edge("node3",END)
build = graph.compile()