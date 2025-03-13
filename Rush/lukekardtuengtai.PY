def checkmate(board: str):
    # แปลงกระดานจาก string เป็น list ของ list
    rows = board.strip().split("\n")
    n = len(rows)  # ขนาดของกระดาน (NxN)

    # ค้นหาตำแหน่งของ King (K)
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

    kx, ky = king_pos  # ตำแหน่งของ King

    # ค้นหาตำแหน่งของ Pawn (P)
    pawns = []
    for i in range(n):
        for j in range(n):
            if rows[i][j] == "P":
                pawns.append((i, j))  # เก็บตำแหน่งของ Pawn ทั้งหมด

    # ตรวจสอบ Pawn (P) ว่าสามารถโจมตี King ได้หรือไม่
    for px, py in pawns:
        if (px - 1, py - 1) == (kx, ky) or (px - 1, py + 1) == (kx, ky):  # Pawn โจมตีเฉียงหน้า
            print("Success")
            return

    # การเคลื่อนที่ของตัวหมากต่างๆ (Rook, Bishop, Queen)
    directions = {
        "R": [(1, 0), (-1, 0), (0, 1), (0, -1)],  # Rook (แนวตรง)
        "B": [(1, 1), (-1, -1), (1, -1), (-1, 1)],  # Bishop (แนวทแยง)
        "Q": [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)],  # Queen (รวม Rook + Bishop)
    }

    # ตรวจสอบ Rook, Bishop, Queen โดยเริ่มจากตำแหน่งของตัวมันเอง
    for piece, moves in directions.items():
        for i in range(n):  # วนหาตำแหน่งตัวหมาก
            for j in range(n):
                if rows[i][j] == piece:
                    # ตรวจสอบว่า King อยู่ในแนวโจมตีหรือไม่
                    for dx, dy in moves:
                        x, y = i + dx, j + dy
                        while 0 <= x < n and 0 <= y < n:
                            if (x, y) == (kx, ky):  # ถ้าเจอ King ในเส้นทาง
                                print("Success")
                                return
                            elif rows[x][y] != ".":  # เจอหมากตัวอื่นขวาง
                                break
                            x += dx
                            y += dy

    print("Fail")  # ถ้าไม่มีตัวไหน Check ได้

# ตัวอย่างการใช้งาน
if __name__ == "__main__":
    board = """\
....
....
..K.
....\
"""
    checkmate(board)