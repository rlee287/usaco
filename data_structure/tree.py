class BinTreeNode:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
        self.height=1

    def iter_children(self):
        yield self.left
        yield self.right

class Tree:
    def __init__(self,data):
        if len(data)==0:
            raise ValueError("data must have at least one element")
        first=True
        for element in data:
            if first:
                self.root=BinTreeNode(element,None,None)
            else:
                # inline add_element so as to call fix_heights only once
                node=self.root
                while True:
                    if element<=node.data:
                        if node.left is None:
                            node.left=BinTreeNode(element,None,None)
                            break
                        else:
                            node=node.left
                    else: #element>nodedata
                        if node.right is None:
                            node.right=BinTreeNode(element,None,None)
                            break
                        else:
                            node=node.right
            first=False

    def add_element(self,element):
        node=self.root
        height=node.height
        while True:
            if element<=node.data:
                if node.left is None:
                    node.left=BinTreeNode(element,None,None)
                    node.left.height=height
                    node.height+=1
                    break
                else:
                    node=node.left
            else: #element>nodedata
                if node.right is None:
                    node.right=BinTreeNode(element,None,None)
                    node.right.height=height
                    node.height+=1
                    break
                else:
                    node=node.right

    def dft(self,start=None,hook=None,*args,**kwargs):
        if start is None:
            node=self.root
        else:
            node=start
        list_visited=list()
        list_visited.append(node)
        if hook is not None:
            hook(node,*args,**kwargs)
        if node.left is not None:
            self.dft(node.left,hook,*args,**kwargs)
        if node.right is not None:
            self.dft(node.right,hook,*args,**kwargs)

    def print_val(self):
        def hookfunc(node):
            if node.left is not None:
                leftdata=node.left.data
            else:
                leftdata=None
            if node.right is not None:
                rightdata=node.right.data
            else:
                rightdata=None
            if (leftdata is None) and (rightdata is None):
                print("data: {0} leaf height: {1}"
                    .format(node.data,node.height))
            else:
                print("data: {0} leftdata: {1} rightdata: {2} height: {3}"
                    .format(node.data,leftdata,rightdata,node.height))
        self.dft(hook=hookfunc)

if __name__ == '__main__':
    test=Tree([3,1,2,5,4,7,6,8])
    test.print_val()
