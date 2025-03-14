def DF(board: str):
    
    rows = board.strip().split("\n")
    n = len(rows)  

    
    king_pos = None
    for i in range(n):
        for j in range(n):
            if rows[i][j] == "K":
                king_pos = (i, j)
                break
        if king_pos:
            break

    if not king_pos:
        print("Error")
        return

    kx, ky = king_pos  

    
    pawns = []
    for i in range(n):
        for j in range(n):
            if rows[i][j] == "P":
                pawns.append((i, j))  

    
    for px, py in pawns:
        if (py - 1, px - 1) == (kx, ky) or (py - 1, px + 1) == (kx, ky): 
            return

    
    directions = {
        "R": [(1, 0), (-1, 0), (0, 1), (0, -1)],  
        "B": [(1, 1), (-1, -1), (1, -1), (-1, 1)],  
        "Q": [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)],  
    }


    for piece, moves in directions.items():
        for i in range(n): 
            for j in range(n):
                if rows[i][j] == piece:
                    
                    for dx, dy in moves:
                        x, y = i + dx, j + dy
                        while 0 <= x < n and 0 <= y < n:
                            if (x, y) == (kx, ky): 
                                print("Success")
                                return
                            elif rows[x][y] != ".":  # เจอหมากตัวอื่นขวาง
                                break
                            x += dx
                            y += dy

    print("Fail")  # ถ้าไม่มีตัวไหน Check ได้