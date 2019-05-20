import math
import matplotlib.pyplot as plt
import numpy as np

def koch(n, a, b, l):
    if n == 0:
        return
    s, t, u = {}, {}, {}
    th = math.pi * 60.0 / 180.0

    # abを三等分
    s['x'] = (2.0 * a['x'] + 1.0 * b['x']) / 3.0
    s['y'] = (2.0 * a['y'] + 1.0 * b['y']) / 3.0
    t['x'] = (1.0 * a['x'] + 2.0 * b['x']) / 3.0
    t['y'] = (1.0 * a['y'] + 2.0 * b['y']) / 3.0
    # ベクトル演算
    u['x'] = (t['x'] - s['x']) * math.cos(th) - (t['y'] - s['y']) * math.sin(th) + s['x']
    u['y'] = (t['x'] - s['x']) * math.sin(th) + (t['y'] - s['y']) * math.cos(th) + s['y']

    koch(n-1, a, s, l)
    l.append((s['x'], s['y']))
    koch(n-1, s, u, l)
    l.append((u['x'], u['y']))
    koch(n-1, u, t, l)
    l.append((t['x'], t['y']))
    koch(n-1, t, b, l)

def main():
    n = int(input())
    a = {'x':0, 'y':0}
    b = {'x':100, 'y':0}
    l = []

    l.append((a['x'], a['y']))
    koch(n, a, b, l)
    l.append((b['x'], b['y']))

    l = np.array(l)
    
    plt.figure(figsize=(8, 5))
    plt.plot(l[:,0], l[:,1])
    plt.title('Koch Curve')
    plt.savefig('ch06/koch.png')
    


if __name__ == "__main__":
    main()