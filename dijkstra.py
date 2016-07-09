import pprint

def find_neighbors(pos):
    row,column=pos
    list_pos=list()
    for dr in [-1,0,1]:
        for dc in [-1,0,1]:
            list_pos.append((row+dr,column+dc))
    return list_pos

class Dijkstra_solver:
    def __init__(self, filepath):
        """Zero based with
           <space>=open
           s=start
           f=finish
           anything else=wall"""
        self.filepath=filepath
        # Map characters in file to initial distances or walls
        map_char={"s": 0,
                  "w": float("inf"),
                  " ": float("inf")}
        self.distmatrix=dict()
        # Read file contents, row by row
        with open(self.filepath,"r") as file_handle:
            row=0
            for line in file_handle:
                column=0
                for element in line:
                    if element=="f":
                        self.finish=(row,column)
                    if element=="s":
                        self.start=(row,column)
                    init_dist=map_char.get(element,"wall")
                    visited=True if init_dist=="wall" else False
                    self.distmatrix[(row, column)]={"dist": init_dist,
                                                    "parent": None,
                                                    "visited": visited}
                    column+=1
                row+=1
        try:
            self.finish
        except:
            raise ValueError("File does not contain end point")
        try:
            self.start
        except:
            raise ValueError("File does not contain start point")


if __name__=="__main__":
    q=Dijkstra_solver("test.txt")
    pprint.pprint(q.distmatrix)
    print("Start node is:", q.start)
    print("Finish node is:", q.finish)
