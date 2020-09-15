class GraphNode:

    def __init__(self, position_in_map, robot_pose):
        self.position_in_map = position_in_map
        self.robot_pose = robot_pose
    
    def __eq__(self,other):
        return self.position_in_map == other.position_in_map 

class MapGraphBase:

    def __init__(self):
        self._vertices = []
        self._edges    = {}

    def has_vertex(map_node):
        if map_node in self._vertices:
            return True 
        else:
            return False

    def is_edge(map_nodeA, map_nodeB):
        if (map_nodeA,map_nodeB) in self._edges:
            return True
        else:
            return False
    
################## HELPER FUNCTIONS #########################################

def frontier_points(position):
    '''
    Finds frontier points in the current localmap
    '''
    return frontier

def get_local_bounding_area(robot_position):
    '''
    Returns a bounding area for the local exploration
    '''
    bounding_length = 100
    bounding_width = 100
    r_x = robot_position.x
    r_y = robot_position.y
    xLeft = r_x - (bounding_width/2)
    yBottom = r_y - (bounding_length/2)
    # draw rectangle and publish as marker array
    return bounds


def get_radial_nodes(map_node, radius, num_nodes=8):
    '''
    Given a point on the map, returns #num_nodes radial points for exploration
    Input : geometry_msgs Point - map_node
            float - radius
    Returns : list() radial points
    '''
    pass

def check_nodes_feasiblity(radial_nodes):
    '''
    Given a list of radial nodes, check if the node is a feasible exploration point
    Check if a node is occupied or unknown, in which case the node is ignored
    For free nodes the cost (distance) to the  node is calculated
    
    Returns : A sorted list of feasible nodes accroding to cost (higher cost is prefered)
    '''
    pass

