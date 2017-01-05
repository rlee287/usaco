class LinkedList:
    def __init__(self,start_list=None):
        self.list_struct=list()
        self.current_index=0
        before=False
        if start_list is not None:
            for element in start_list:
                if not before:
                    new=len(self.list_struct) # Will be len-1 after appending
                    self.list_struct.append([None,element,None])
                    self.current_index=new
                    before=True
                else:
                    self.add_element(element)
            # start_list.reverse()
            # for i,element in enumerate(start_list):
            #     self.list_struct.append([before,element,None])
            #     if i!=0:
            #         self.list_struct[i-1][0]=i
        else:
            self.list_struct.append([None,None,None])

    def add_element(self,element):
        old=self.current_index
        new=len(self.list_struct) # Will be len-1 after appending
        self.list_struct.append([old,element,None])
        self.list_struct[old][2]=new
        self.current_index=new

    def search(self,obj):
        index_track=self.current_index
        while True:
            ref_obj=self.list_struct[index_track][1]
            if ref_obj==obj:
                break
            index_track=self.list_struct[index_track][0]
            if index_track is None:
                index_track=-1
                break
        return index_track

    def delete(self,obj):
        index=self.search(obj)
        if index==-1:
            return False
        before_index=self.list_struct[index][0]
        after_index=self.list_struct[index][2]
        self.list_struct[before_index][2]=after_index
        self.list_struct[after_index][0]=before_index
        self.list_struct[index][0]=None
        self.list_struct[index][2]=None

if __name__=="__main__":
    import pprint
    q=LinkedList(["a","b","c","d","e"])
    q.add_element("f")
    pprint.pprint(q.list_struct)
    ind=q.search("c")
    print("index of c:",ind)
    ind=q.search("p")
    print("index of p:",ind)
    q.delete("c")
    pprint.pprint(q.list_struct)
    ind=q.search("c")
    print("index of c:",ind)
