# define the llm and llm2

from langchain_core.messages import AIMessage, HumanMessage

from langchain_groq import ChatGroq
# this llm1 is only for basil
llm1 = ChatGroq(
    model="deepseek-r1-distill-llama-70b",
    temperature=0.5,
    max_tokens=None,
    timeout=None,
    groq_api_key="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",
    # other params...
)

#this llm for everyone
llm2 = ChatGroq(
    model="deepseek-r1-distill-llama-70b",
    temperature=0.5,
    max_tokens=None,
    timeout=60,
    groq_api_key="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",
    # other params...
)


# create the bunch of tool for llm

# create the bunch of tool for llm


import socket
# featch the ip address
from typing import List
import requests

#only for basil 
def featch_ip(ip:str) -> str:
    """it only featch the ip address from the meachine to get the public ip"""
    try:
        ip_address = requests.get("https://api.ipify.org").text
        return ip_address
    except requests.RequestException:
        return "Unable to fetch IP address"


#only for basil to get the what are the port are the localmeachine 

# def scanning_port(port_start:int,port_end:int)-> str:
#     """get the port details from the local meachine
#     args:
#     prot_start: staring number of port eg:4
#     prot_end: ending number of port eg:90
#     """
#     t_IP = gethostbyname("127.0.0.1")
#     values = []
#     for i in range(50, 500):
#       s = socket(port_start, port_end)
      
#       conn = s.connect_ex((t_IP, i))
#       if(conn == 0) :
#          print ('Port %d: OPEN' % (i,))
#          values+=[f"Port: OPEN' % {(i,)}"]
#       s.close()
#     return values

def scanning_port(port_start: int, port_end: int) -> List[str]:
    """
    Scans a range of ports on localhost to check if they are open.

    Args:
        port_start (int): Starting port number.
        port_end (int): Ending port number.

    Returns:
        List[str]: List of open ports with messages.
    """
    t_IP = socket.gethostbyname("127.0.0.1")
    open_ports = []

    for port in range(port_start, port_end + 1):  # range should include end
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # s.settimeout(0.5)  # Add timeout to avoid hanging
        conn = s.connect_ex((t_IP, port))
        if conn == 0:
            msg = f"Port {port}: OPEN"
            print(msg)
            open_ports.append(msg)
        s.close()

    return open_ports


#for other user function
#that only for addiciton and subraction

def addiction(a:int, b:int)-> int:
    """this function was perform the addicion and give the output in int
    args:
    a: number eg:44
    b: number eg:3
    """
    return a + b

def subraction(a:int, b:int)-> int:
    """this function was perform the subraction and give the output in int
    args:
    a: number eg:44
    b: number eg:3
    """
    return a - b




#for other user function
#that only for addiciton and subraction

def addiction(a:int, b:int)-> int:
    """this function was perform the addicion and give the output in int
    args:
    a: number eg:44
    b: number eg:3
    """
    return a + b

def subraction(a:int, b:int)-> int:
    """this function was perform the subraction and give the output in int
    args:
    a: number eg:44
    b: number eg:3
    """
    return a - b


#binindg the along with two llms

llm1 = llm1.bind_tools([featch_ip,scanning_port])
llm2 = llm2.bind_tools([addiction,subraction])

# define the node and condictionss
from typing import Annotated
from langgraph.graph.message import add_messages
from typing_extensions import TypedDict
from langchain_core.messages import AnyMessage
from typing import Literal  
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

sys_msg = SystemMessage(content="You are a helpful assistant tasked with using search and performing arithmetic on a set of inputs. and also perfoem the tool exicuction ")


class Multi_llm_state(TypedDict):
    """State to store messages."""

    messages: Annotated[list[AnyMessage], add_messages]
    name: str | None


from IPython.display import Image, display
from langgraph.graph import StateGraph, START, END

# condiiction ediges

def routing_based_on_names(state:Multi_llm_state)-> Literal["llm1","llm2"]:
    if state["name"] == "basil":
        return "llm1"
    return "llm2"


#greeding card:

def greeting(state:Multi_llm_state):
    print("_____greeting_______")
    print(f"Hello {state["name"]}")
    return {"messages":state["messages"], "name":state["name"]}
graph = StateGraph(Multi_llm_state)
#define the nodes


# node for llm1 and llm2

def llm_1(state:Multi_llm_state):
    print("------llm1 for basil------")
    return {"messages": llm1.invoke(state["messages"])}

def llm_2(state:Multi_llm_state):
    print("------llm2 for other member------")
    return {"messages": llm2.invoke(state["messages"])}

# # define the node and condictionss
# from typing import Annotated
# from langgraph.graph.message import add_messages
# from typing_extensions import TypedDict
# from langchain_core.messages import AnyMessage
# from typing import Literal  
# from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

# sys_msg = SystemMessage(content="You are a helpful assistant tasked with using search and performing arithmetic on a set of inputs. and also perfoem the tool exicuction ")


# class Multi_llm_state(TypedDict):
#     """State to store messages."""

#     messages: Annotated[list[AnyMessage], add_messages]
#     name: str | None


# from IPython.display import Image, display
# from langgraph.graph import StateGraph, START, END
# from langgraph.prebuilt import ToolNode
# from langgraph.prebuilt import tools_condition

# # condiiction ediges

# def routing_based_on_names(state:Multi_llm_state)-> Literal["llm1","llm2"]:
#     if state["name"] == "basil":
#         return "llm1"
#     return "llm2"


# #greeding card:

# def greeting(state:Multi_llm_state):
#     print("_____greeting_______")
#     print(f"Hello {state["name"]}")
#     return {"messages":state["messages"], "name":state["name"]}
# graph = StateGraph(Multi_llm_state)
# #define the nodes


# # node for llm1 and llm2

# def llm_1(state:Multi_llm_state):
#     print("------llm1 for basil------")
#     return {"messages": llm1.invoke(state["messages"])}

# def llm_2(state:Multi_llm_state):
#     print("------llm2 for other member------")
#     return {"messages": llm2.invoke(state["messages"])}


# #define the nodes
# graph.add_node("greeting",greeting)
# graph.add_node("llm1",llm_1)
# graph.add_node("llm2",llm_2)
# graph.add_node("tools",ToolNode([featch_ip,scanning_port,addiction,subraction]))
# # graph.add_node("tools2",ToolNode([featch_ip,scanning_port]))


# #add the ediges and condiction ediges

# graph.add_edge(START,"greeting")
# graph.add_conditional_edges("greeting",routing_based_on_names)
# graph.add_conditional_edges("llm1",tools_condition)
# graph.add_conditional_edges("llm2",tools_condition)
# graph.add_edge("tools", END)

# build = graph.compile()




# define the node and condictionss
from typing import Annotated
from langgraph.graph.message import add_messages
from typing_extensions import TypedDict
from langchain_core.messages import AnyMessage
from typing import Literal  
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

sys_msg = SystemMessage(content="You are a helpful assistant tasked with using search and performing arithmetic on a set of inputs. and also perfoem the tool exicuction ")



def tools_condition_for_llm1(state: Multi_llm_state) -> Literal["tools1", END]:
    # some logic to decide if tools1 should run
    # e.g. if a tool call is needed
    if "tool_call" in str(state["messages"][-1]):
        return "tools1"
    return END

def tools_condition_for_llm2(state: Multi_llm_state) -> Literal["tools2", END]:
    if "tool_call" in str(state["messages"][-1]):
        return "tools2"
    return END
class Multi_llm_state(TypedDict):
    """State to store messages."""

    messages: Annotated[list[AnyMessage], add_messages]
    name: str | None


from IPython.display import Image, display
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode
from langgraph.prebuilt import tools_condition

# condiiction ediges

def routing_based_on_names(state:Multi_llm_state)-> Literal["llm1","llm2"]:
    if state["name"] == "basil":
        return "llm1"
    return "llm2"


#greeding card:

def greeting(state:Multi_llm_state):
    print("_____greeting_______")
    print(f"Hello {state["name"]}")
    return {"messages":state["messages"], "name":state["name"]}
graph = StateGraph(Multi_llm_state)
#define the nodes


# node for llm1 and llm2

def llm_1(state:Multi_llm_state):
    print("------llm1 for basil------")
    return {"messages": llm1.invoke(state["messages"])}

def llm_2(state:Multi_llm_state):
    print("------llm2 for other member------")
    return {"messages": llm2.invoke(state["messages"])}


#define the nodes
graph.add_node("greeting",greeting)
graph.add_node("llm1",llm_1)
graph.add_node("llm2",llm_2)
graph.add_node("tools1",ToolNode([featch_ip,scanning_port]))
graph.add_node("tools2",ToolNode([addiction,subraction]))


#add the ediges and condiction ediges

graph.add_edge(START,"greeting")
graph.add_conditional_edges("greeting",routing_based_on_names)
graph.add_conditional_edges("llm1",tools_condition_for_llm1)
graph.add_conditional_edges("llm2",tools_condition_for_llm2)
# graph.add_edge("tools1", END)
# graph.add_edge("tools2", END)

build = graph.compile()
