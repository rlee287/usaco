import pprint
import math
import pdb

def find_neighbors(pos):
    row,col=pos
    list_pos=list()
    for dr in [-1,0,1]:
        for dc in [-1,0,1]:
            list_pos.append((row+dr,col+dc))
    del list_pos[list_pos.index((row,col))]
    return list_pos

def find_distance(pos1,pos2):
    row1,col1=pos1
    row2,col2=pos2
    return math.sqrt(pow(row1-row2,2)+pow(col1-col2,2))

class DijkstraSolver:
    def __init__(self, filepath):
        """Zero based with
           <space>=open
           s=start
           f=finish
           anything else=wall"""
        self.filepath=filepath
        # Map characters in file to initial distances or walls
        map_char={"s": 0,
                  "f": float("inf"),
                  " ": float("inf")}
        self.distmatrix=dict()
        # Read file contents, row by row
        with open(self.filepath,"r") as file_handle:
            has_start=False
            has_finish=False
            row=0
            for line in file_handle:
                column=0
                for element in line:
                    if element=="f":
                        if not has_finish:
                            self.finish=(row,column)
                            has_finish=True
                        else:
                            raise ValueError("File contains multiple end points")
                    if element=="s":
                        if not has_start:
                            self.start=(row,column)
                            has_start=True
                        else:
                            raise ValueError("File contains multiple start points")
                    init_dist=map_char.get(element,"wall")
                    visited=(init_dist=="wall" or element==has_start)
                    self.distmatrix[(row, column)]={"dist": init_dist,
                                                    "parent": None,
                                                    "visited": visited}
                    column+=1
                row+=1
            if not has_finish:
                raise ValueError("File does not contain end point")
            if not has_start:
                raise ValueError("File does not contain start point")

    def find_path(self):
        current=self.start
        current_point=self.distmatrix[self.start]
        outside={'dist': 'wall', 'parent': None, 'visited': True}
        while self.distmatrix[self.finish].get("visited") is False:
            print("Currently on", current)
            for neighbor in find_neighbors(current):
                print("  Checking neighbor",neighbor)
                neighbor_point=self.distmatrix.get(neighbor,outside)
                if not neighbor_point["visited"]:
                    print("    Neighbor",neighbor,"is not visited")
                    neighbor_dist=current_point["dist"]
                    neighbor_dist+=find_distance(current,neighbor)
                    if not isinstance((neighbor_point["dist"]), str) and \
                                    neighbor_point["dist"]>neighbor_dist:
                            neighbor_point["dist"]=neighbor_dist
                            neighbor_point["parent"]=current
                            print("    Neighbor distance is",neighbor_dist)
                            print("    Neighbor parent is",current)
                else:
                    print("    Neighbor",neighbor,"is visited")
            current_point["visited"]=True
            print("  Point",current,"is visited")
            print("  ",end="")
            pprint.pprint(current_point)
            mindist=float("inf")
            minpoint=None
            for point in self.distmatrix:
                point_dict=self.distmatrix[point]
                point_dist=point_dict["dist"]
                if point != current and not point_dict["visited"]:
                    if not isinstance(point_dist,str) and \
                                mindist>point_dist:
                            mindist=point_dist
                            minpoint=point
            if minpoint is None:
                exit_while=True
                break
            else:
                exit_while=False
            current=minpoint
            current_point=self.distmatrix[current]
        #endwhile
        if exit_while:
            return "There is no pathway"
        else:
            next_point=self.finish
            pathway=[next_point]
            while next_point != self.start:
                next_point=self.distmatrix[next_point]["parent"]
                pathway.append(next_point)
            return pathway

if __name__=="__main__":
    filename=input("Please enter a filename:")
    q=DijkstraSolver(filename)
    pprint.pprint(q.distmatrix)
    print("Start node is:", q.start)
    print("Finish node is:", q.finish)
    path=q.find_path()
    print(path)
