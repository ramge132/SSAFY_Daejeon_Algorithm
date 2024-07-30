DIRECTION = {
    1: [-1, 0],
    2: [1, 0],
    3: [0, -1],
    4: [0, 1]
}
 
 
def change_direction(in_direction):
    if in_direction == 1:
        return 2
    elif in_direction == 2:
        return 1
    elif in_direction == 3:
        return 4
    else:
        return 3
 
 
class Cluster:
    def __init__(self, N, x, y, num_of_microbe, direction):
        self.map_size = N
        self.location_x = x
        self.location_y = y
        self.num_of_microbe = num_of_microbe
        self.direction = direction
        self.is_alive = True
 
    def move_cluster(self):
        dx, dy = DIRECTION[self.direction]
 
        self.location_x = self.location_x + dx
        self.location_y = self.location_y + dy
 
        if self.location_x < 1 or self.location_x > self.map_size - 2:
            self.num_of_microbe = int(self.num_of_microbe / 2)
            self.direction = change_direction(self.direction)
        elif self.location_y < 1 or self.location_y > self.map_size - 2:
            self.num_of_microbe = int(self.num_of_microbe / 2)
            self.direction = change_direction(self.direction)
 
        if self.num_of_microbe == 0:
            self.is_alive = False
 
 
def merge_cluster(clusters):
    new_cluster = Cluster(
        N=clusters[0].map_size,
        x=clusters[0].location_x,
        y=clusters[0].location_y,
        num_of_microbe=clusters[0].num_of_microbe,
        direction=0
    )
 
    num_of_microbe_for_each_cluster = [c.num_of_microbe for c in clusters]
 
    max_idx = num_of_microbe_for_each_cluster.index(max(num_of_microbe_for_each_cluster))
 
    new_cluster.num_of_microbe = sum(num_of_microbe_for_each_cluster)
    new_cluster.direction = clusters[max_idx].direction
 
    return new_cluster
 
 
# main
T = int(input())
 
for t_iter in range(1, T+1):
    N, M, K = list(map(int, input().split()))
 
    cluster_lists = []
    for k_iter in range(K):
        x, y, num_of_microbe, direction = list(map(int, input().split()))
        cluster_lists.append(Cluster(N=N, x=x, y=y, num_of_microbe=num_of_microbe, direction=direction))
 
    for m_iter in range(M):
        loc_of_clusters = []
 
        # 군집 이동 후 위치 저장
        for idx, cluster in enumerate(cluster_lists):
            cluster.move_cluster()
            loc_of_clusters.append("000"+str(cluster.location_x)+"_"+str(cluster.location_y)+"000")
 
            # if not cluster.is_alive:
            #     del cluster_lists[idx]
            #     del loc_of_clusters[idx]
 
        # 저장된 위치 기반 동일한 위치 추출
        loc_dict = {loc: [] for loc in loc_of_clusters}
        for idx, loc in enumerate(loc_of_clusters):
            loc_dict[loc].append(idx)
 
        # 동일한 위치에 있는 군집 합치기
        temp_cluster_lists = []
        for dict_idx, loc_dict_key in enumerate(loc_dict.keys()):
            if len(loc_dict[loc_dict_key]) > 1:
                clusters_to_merge = []
                for idx in loc_dict[loc_dict_key]:
                    clusters_to_merge.append(cluster_lists[idx])
 
                temp_cluster_lists.append(merge_cluster(clusters_to_merge))
            else:
                for idx in loc_dict[loc_dict_key]:
                    temp_cluster_lists.append(cluster_lists[idx])
 
        cluster_lists = temp_cluster_lists
 
    sum_of_microbe = 0
    for cluster in cluster_lists:
        sum_of_microbe = sum_of_microbe + cluster.num_of_microbe
 
    print(f"#{t_iter} {sum_of_microbe}")