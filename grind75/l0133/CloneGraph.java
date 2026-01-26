package grind75.l0133;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class CloneGraph {
    public Node cloneGraph(Node node) {
        if (node ==null) {
            return node;
        }

        HashMap<Node, Node> visited = new HashMap<>();
        visited.put(node, new Node(node.val));

        Queue<Node> que = new LinkedList<>();
        que.offer(node);

        while (! que.isEmpty()) {
            Node nd = que.poll();
            for (Node neighbor: nd.neighbors) {
                if (!visited.containsKey(neighbor)) {
                    visited.put(neighbor, new Node(neighbor.val));
                    que.offer(neighbor);
                }
                visited.get(nd).neighbors.add(visited.get(neighbor));
            }

        }
        return visited.get(node);
    }
    
}


class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
