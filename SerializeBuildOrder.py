def  serialize_build_order(relations):
    child = {}
    for rel in relations:
        if rel[1] in child:
            child[rel[1]].append(rel[0])
        else:
            child[rel[1]] = [rel[0]]
    q = deque()
    masters = child['ubuntu']
    q.extend(masters)
    deps = []
    while q:
        node = q.popleft()
        if node in child:
            node_child = child[node]
            q.extend(node_child)
        deps.append(node)
    return deps
