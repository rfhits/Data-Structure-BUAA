node_list.append(Node(input_list[0]))
    for i in range(1,len(input_list)):
        if input_list[i] == 'None':
            node_list.append(None)
            continue
        node_list.append(Node(input_list[i]))  # node_list存入Node型的数据
        if i % 2 == 0:  # 右结点
            k = (i - 2) // 2  # 到node_list中father的索引
            while (node_list[k] == None):
                k += 1
            node_list[k].right = Node(input_list[i])
        else:  # 左结点
            k = (i - 1) // 2  # 到node_list中father的索引
            while (node_list[k] == None):
                k += 1
            node_list[k].left = Node(input_list[i])