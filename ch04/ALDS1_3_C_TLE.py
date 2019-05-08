
# TLE

class DoubleLinkedList:
    def __init__(self):
        self.l = []
    
    def insert(self, x):
        self.l.insert(0, x)
    
    def delete(self, x):
        try:
            self.l.remove(x)
        except ValueError:
            pass

    def deleteFirst(self):
        try:
            self.l.pop(0)
        except IndexError:
            pass
    
    def deleteLast(self):
        try:
            self.l.pop()
        except IndexError:
            pass
    
    def show(self):
        print(" ".join(self.l))

def main():
    N = int(input())
    l = DoubleLinkedList()
    for _ in range(N):
        d = input()
        if d == 'deleteFirst':
            try:
                l.deleteFirst()
            except:
                pass
        elif d == 'deleteLast':
            try:
                l.deleteLast()
            except:
                pass
        else:
            command, x = d.split(' ')
            if command == 'insert':
                l.insert(x)
            elif command == 'delete':
                try:
                    l.delete(x)
                except:
                    pass
    l.show()
if __name__ == "__main__":
    main()