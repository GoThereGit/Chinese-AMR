# !/usr/bin/env python
# -*- coding:utf-8 -*-
from collections import defaultdict

def id_anchor(node_name):
    """
    :param node_name: nid with '_', like "x1_x2", "x1_2"
    :return: anchor split 'x', like "1_2", "1.2"
    """
    joint = node_name.split('_')
    joint_word = ''
    if node_name.count('x') == node_name.count('_') + 1:
        joint = node_name.split('x')
        for words in joint:
            joint_word += words
    elif node_name.count('x') <= node_name.count('_'):
        joint_list = []
        if node_name.count('x') == 1:
            for words in joint[1:]:
                joint_word = joint[0][1:] + '.' + words
                joint_list.append(joint_word)
        else:
            joint = node_name.split('_x')
            for mx in joint:
                if mx[0] != 'x':
                    mx = 'x' + mx
                if '_' in mx:
                    nj = mx.split('_')
                    for words in nj[1:]:
                        joint_word = nj[0][1:] + '.' + words
                        joint_list.append(joint_word)
                else:
                    joint_list.append(mx[1:])
        joint_word = '_'.join(joint_list)
    return joint_word


def add_anchor(nid, limit):
    """
    :param nid: nid, like "x1", "x1_x2", "x1_1", "x100"
    :param limit: max length of a sentence
    :return: anchor
    """
    if '_' not in nid:
        if nid != 'x0' and int(nid[1:]) <= limit:
            return nid[1:]
        else:
            return None
    else:
        return id_anchor(nid)


class CAMR(object):
    def __init__(self, node_list=None, node_value_list=None, relation_list=None, attribute_list=None, sentence_id=None):
        """
        node_list: names of nodes in CAMR graph, e.g. CAMR of "我 爱 你" has three nodes "x1", "x2" and "x3"
        node_value_list: values(concepts) of nodes in CAMR graph, e.g. concept "我" of node "x1"
        relation_list: list of relations and alignment of relations between two nodes
        attribute_list: list of attributes between node and its alignment
        sentence_id: str of sentence id
        """
        # initialize CAMR graph nodes using list of nodes name
        # root, by default, is the first in node_list

        if node_list is None:
            self.nodes = []
            self.root = None
        else:
            self.nodes = node_list[:]
            if len(node_list) != 0:
                self.root = node_list[0]
            else:
                self.root = None
        if node_value_list is None:
            self.node_values = []
        else:
            self.node_values = node_value_list[:]
        if relation_list is None:
            self.relations = []
        else:
            self.relations = relation_list[:]
        if attribute_list is None:
            self.attributes = []
        else:
            self.attributes = attribute_list[:]
        if sentence_id is None:
            self.sid = None
        else:
            self.sid = str(sentence_id).strip()

    def rename_node(self, prefix):
        """
        Rename CAMR graph nodes to prefix + node_index to avoid nodes with the same name in two different CAMRs.
        """
        node_map_dict = {}
        # map each node to its new name (e.g. "a1")
        for i in range(0, len(self.nodes)):
            node_map_dict[self.nodes[i]] = prefix + str(i)
        # update node name
        for i, v in enumerate(self.nodes):
            self.nodes[i] = node_map_dict[v]
        # update node name in relations
        for node_relations in self.relations:
            for i, l in enumerate(node_relations):
                node_relations[i][1] = node_map_dict[l[1]]

    def get_triples(self):
        """
        Get the triples in three lists.
        instance_triple: a triple representing an instance. E.g. instance(a0, 爱-01), instance(a1, name)
        attribute triple: links of attributes, e.g. anchor(a0, x2), op1(a1, 北京)
        and relation triple, e.g. arg1(a0, a1),
        """
        instance_triple = []
        relation_triple = []
        attribute_triple = []
        for i in range(len(self.nodes)):
            instance_triple.append(("instance", self.nodes[i], self.node_values[i]))
            # l[0] is relation name
            # l[1] is the other node this node has relation with
            for l in self.relations[i]:
                relation_triple.append((l[0], self.nodes[i], l[1]))
            # l[0] is the attribute name
            # l[1] is the attribute value
            for l in self.attributes[i]:
                attribute_triple.append((l[0], self.nodes[i], l[1]))
        return instance_triple, attribute_triple, relation_triple

    @staticmethod
    def get_CAMR(input_f, len_dict=None, smatch=True):
        """
        :param input_f: content of CAMR tuples
        :param len_dict: a dict with max length of each sentence for Align-smatch
        :param smatch: True for Smatch and False for Align-smatch
        :return: a CAMR class
        """
        def match_node_concept(nid, concept, coref, limit):
            if nid not in node_dict:
                node_dict[nid] = concept
                if not smatch:
                    my_anchor = add_anchor(nid, limit)
                    if my_anchor != None:
                        anchor_dict[nid] = my_anchor
            else:
                if node_dict[nid] != concept:
                    for i in range(1, 11):
                        node = 'x' * i + nid
                        if node not in node_dict:
                            node_dict[node] = concept
                            if not smatch:
                                my_anchor = add_anchor(nid, limit)
                            nid = node
                            if not smatch:
                                if my_anchor != None:
                                    anchor_dict[nid] = my_anchor
                            break
            if nid not in node_list:
                node_list.append(nid)
            if coref != '-' and ('coref', coref) not in relation_dict[nid]:
                relation_dict[nid].append(('coref', coref))
            return nid

        def update_relation(u, r, v):
            if r.endswith('-of') and r != 'consist-of':
                relation_dict[v].append((r[:-3], u))
            else:
                relation_dict[u].append((r, v))

        def add_ralign(u, r, id, fc, v):
            if r.endswith('-of') and r != 'consist-of':
                relation_dict[v].append(((id, fc), u))
            else:
                relation_dict[u].append(((id, fc), v))
        # key:nid, value:concept
        node_dict = {}
        # key:source nid, value:[relation, target nid]
        relation_dict = defaultdict(list)
        # key:nid, value:anchor
        anchor_dict = {}
        # nid
        node_list = []
        limit = 0
        for line in input_f:
            line = line.strip()
            if line != '':
                [sid, nid1, concept1, coref1, rel, rid, ralign, nid2, concept2, coref2] = line.split('\t')
                if sid == '句子编号' or sid == 'sid':
                    continue
                if not smatch:
                    limit = int(len_dict[sid])
                # skip concept "root"
                if concept1 == 'root' and rel == ':top':
                    _ = match_node_concept(nid2, concept2, coref2, limit)
                    continue
                nid1 = match_node_concept(nid1, concept1, coref1, limit)
                nid2 = match_node_concept(nid2, concept2, coref2, limit)
                update_relation(nid1, rel[1:], nid2)
                if not smatch:
                    if rid != '-' and ralign != '-':
                        add_ralign(nid1, rel[1:], rid, ralign, nid2)
            else:
                if node_list == []:
                    continue
                node_value_list = []
                relation_list = []
                anchor_list = []
                for v in node_list:
                    if v not in node_dict:
                        print("Error: Node name not found" + v)
                    else:
                        node_value_list.append(node_dict[v])
                    node_rel_list = []
                    node_attr_list = []
                    if v in relation_dict:
                        for v0 in relation_dict[v]:
                            node_rel_list.append([v0[0], v0[1]])
                    if v in anchor_dict:
                        node_attr_list.append(['anchor', anchor_dict[v]])
                    relation_list.append(node_rel_list)
                    anchor_list.append(node_attr_list)
                if smatch:
                    anchor_list[0].append(["top", 'TOP'])
                else:
                    relation_list[0].append(["top", node_list[0]])
                result_camr = CAMR(node_list, node_value_list, relation_list, anchor_list, sid)
                return result_camr
