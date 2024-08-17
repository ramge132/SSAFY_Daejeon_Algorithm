DIRECTION = [[-1, 0], [1, 0], [0, -1], [0, 1]]
from pprint import pprint

class Cell:
    def __init__(self, X, loc_x, loc_y):
        self.X = X
        self.life_count = 2 * self.X
        self.is_active = False
        self.loc_x = loc_x
        self.loc_y = loc_y
    
    def tik(self):
        if self.life_count == self.X:
            self.is_active = True
        elif self.life_count == 0:
            self.is_active = False

        self.life_count -= 1

        ret = []
        if self.is_active:
            # 번식하여 Cell 객체 반환
            for direction in DIRECTION:
                dx, dy = direction
                ret.append(
                    Cell(X=self.X, loc_x=self.loc_x+dx, loc_y=self.loc_y+dy)
                )
        
        return ret
    

class Lab:
    def __init__(self, K, cell_info):
        self.simulation_time = K
        self.cells = [
            Cell(info[0], info[1], info[2]) for info in cell_info
        ]
        self.current_cell_locations = set()
        for cell in self.cells:
            self.current_cell_locations.add((cell.loc_x, cell.loc_y))

    def tik(self):
        for t_iter in range(self.simulation_time):
            to_be_merged_cells = []
            for cell in self.cells:
                to_be_merged_cells.extend(cell.tik())

            new_cell = self.check_merge(to_be_merged_cells)

            self.cells.extend(new_cell)
            for cell in new_cell:
                self.current_cell_locations.add(
                    (cell.loc_x, cell.loc_y)
                )

        # 살아남은 셀 숫자 세기
        ret = 0
        for cell in self.cells:
            if cell.life_count > 0:
                ret += 1
        
        return ret

    def check_merge(self, to_be_merged):
        # 동일한 좌표에 세포가 생기려고 하면, 생존력이 높은 셀이 그 자리를 차지한다. 
        location_dict = {}
        for idx, cell in enumerate(to_be_merged):
            key = (cell.loc_x, cell.loc_y)
            if key in self.current_cell_locations:
                # 이미 셀이 존재하는 곳
                continue
            else:
                value = location_dict.get(key, None)
                if value is None:
                    location_dict[key] = set([idx])
                else:
                    location_dict[key].add(idx)
        # pprint(location_dict)
        result = []
        for location in location_dict.keys():
            if len(location_dict[location]) == 1:
                # 혼자만 위치한 셀이다.
                for cell in location_dict[location]:
                    result.append(to_be_merged[cell])
                self.current_cell_locations.add(key)
            else:
                # 가장 강력한 녀석으로 대체하자.
                powerful_cell_idx = -1
                powerful_X = -1
                for cell_idx in location_dict[location]:
                    if powerful_X < to_be_merged[cell_idx].X:
                        powerful_X = to_be_merged[cell_idx].X
                        powerful_cell_idx = cell_idx
                result.append(to_be_merged[powerful_cell_idx])

        return result
    
T = int(input())
for t_iter in range(1, T+1):
    N, M, K = list(map(int, input().split()))
    cell_info = []
    for x in range(N):
        input_line = list(map(int, input().split()))
        for y, item in enumerate(input_line):
            if item == 0:
                continue
            else:
                cell_info.append(
                    [item, x, y]
                )

    Laboratory = Lab(K, cell_info)
    answer = Laboratory.tik()
    print(f"#{t_iter} {answer}")