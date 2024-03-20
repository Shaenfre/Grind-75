from typing import List


class Node:
    def __init__(self):
        self.directories = {}
        self.files = {}


class FileSystem:
    def __init__(self):
        self.root = Node()

    def ls(self, path: str) -> List[str]:
        p = path[1:].split("/")

        current = self.root

        for d in p:
            if d == "":
                continue

            if d in current.directories:
                current = current.directories[d]
            else:
                assert d in current.files
                return [d]
        else:
            return sorted(
                [str(k) for k in current.directories.keys()]
                + [str(k) for k in current.files.keys()]
            )

    def mkdir(self, path: str) -> None:
        p = path[1:].split("/")

        current = self.root

        for d in p:
            if d not in current.directories:
                current.directories[d] = Node()
            current = current.directories[d]

    def addContentToFile(self, path: str, content: str) -> None:
        *p, f = path[1:].split("/")

        current = self.root

        for d in p:
            assert d in current.directories
            current = current.directories[d]

        if f not in current.files:
            current.files[f] = ""

        current.files[f] += content

    def readContentFromFile(self, filePath: str) -> str:
        *p, f = filePath[1:].split("/")

        current = self.root

        for d in p:
            assert d in current.directories
            current = current.directories[d]

        if f not in current.files:
            current.files[f] = ""

        return current.files[f]


def main():
    f = FileSystem()
    print(f.ls("/"))
    f.mkdir("/a/b/c")
    f.addContentToFile("/a/b/c/d", "hello")
    print(f.ls("/"))
    print(f.readContentFromFile("/a/b/c/d"))


if __name__ == "__main__":
    main()