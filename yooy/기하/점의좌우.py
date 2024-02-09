def LR(A, B, C):  # A = [0,1]
    result = (A[0] * B[1] - A[1] * B[0]) + (B[0] * C[1] - B[1] * C[0]) + (C[0] * A[1] - C[1] * A[0])
    if result > 0:
        return "Left"
    elif result < 0:
        return "Right"
    else:
        return "Same"


def cross(A, B, C, D):
    if LR(A, B, C) != LR(A, B, D):
        if LR(C, D, A) != LR(C, D, B):
            print("Cross")
            return True
    return False
