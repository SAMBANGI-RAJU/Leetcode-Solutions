class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        paths=dict(paths)
        print(paths)
        for i in paths:
            if paths[i] not in paths:
                return paths[i]