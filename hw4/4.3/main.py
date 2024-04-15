from typing import List

def buildWall(self, height: int, width: int, bricks: List[int]) -> int:
        def build_layer(current_width):
            nonlocal count
            if current_width > width:
                return
            if current_width == width:
                count += 1
                return
            for brick in bricks:
                layer.append(brick)
                build_layer(current_width + brick)
                layer.pop()

        count = 0
        layer = []
        build_layer(0)
        return count

if __name__ == "__main__":
    # num_tests = int(input())
    # while num_tests:
    #     height, width = map(int,input().split)


    height = 1
    width = 5
    bricks = [1, 2]
    print(buildWall(height, width, bricks))  # Output: 3
