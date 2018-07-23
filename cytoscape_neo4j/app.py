# coding=utf-8
from flask import Flask, jsonify, render_template
from py2neo import Graph

app = Flask(__name__)
# graph = Graph("http://172.168.1.7:7474", user="neo4j", password="123456")
graph = Graph()
def buildNodes(nodeRecord):
    # data = {"id": str(nodeRecord.n._id), "label": next(iter(nodeRecord.n.labels))}
    data = {"id":str(hash(nodeRecord['n'])) , "label": next(iter(nodeRecord['n'].labels()))}
    data.update(nodeRecord['n'].properties)

    return {"data": data}

def buildEdges(relationRecord):
    data = {"source": str(hash(relationRecord['r'].start_node())),
            "target": str(hash(relationRecord['r'].end_node())),
            "relationship": relationRecord['r'].type()}

    return {"data": data}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/graph')
def get_graph():
    # nodes = map(buildNodes, graph.cypher.execute('MATCH (n) RETURN n'))

    nodes = list(map(buildNodes, graph.run('MATCH (n) RETURN n').data()))
    # edges = map(buildEdges, graph.cypher.execute('MATCH ()-[r]->() RETURN r'))
    # print(graph.run('MATCH ()-[r]->() RETURN r').data())
    # ssss  =graph.run('MATCH ()-[r]->() RETURN r').data()
    # ddd  = walk(ssss[0]['r'].start_node())
    # print(ddd)
    edges = list(map(buildEdges, graph.run('MATCH ()-[r]->() RETURN r').data()))
    return jsonify(elements = {"nodes": nodes, "edges": edges})    

if __name__ == '__main__':
    app.run(debug = True)
