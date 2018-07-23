from py2neo import Graph,Node,Relationship
test_graph = Graph(
    "http://localhost:7474",
    username="neo4j",
    password="123456"
)

test_node_1 = Node("Person",name = "test_node_1")
test_node_2 = Node("Machine",name = "test_node_2")
test_graph.create(test_node_1)
test_graph.create(test_node_2)

node_1_call_node_2 = Relationship(test_node_1,'CALL',test_node_2)
node_1_call_node_2['count'] = 1

test_graph.create(node_1_call_node_2)
