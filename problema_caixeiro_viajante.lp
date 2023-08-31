\* Problema_Caixeiro_Viajante *\
Minimize
OBJ: 435 visitada_0_1 + 294 visitada_0_2 + 413 visitada_0_3 + 435 visitada_1_0
 + 141 visitada_1_2 + 85 visitada_1_3 + 294 visitada_2_0 + 141 visitada_2_1
 + 131 visitada_2_3 + 413 visitada_3_0 + 85 visitada_3_1 + 131 visitada_3_2
Subject To
_C1: visitada_0_1 + visitada_0_2 + visitada_0_3 = 1
_dummy: __dummy = 0
_C10: __dummy <= 0
_C11: __dummy <= 0
_C12: __dummy <= 0
_C13: visitada_0_1 + visitada_1_0 <= 1
_C14: visitada_0_2 + visitada_2_0 <= 1
_C15: visitada_0_3 + visitada_3_0 <= 1
_C16: visitada_1_2 + visitada_2_1 <= 1
_C17: visitada_1_3 + visitada_3_1 <= 1
_C18: visitada_2_3 + visitada_3_2 <= 1
_C19: visitada_0_1 + visitada_0_2 + visitada_1_0 + visitada_1_2 + visitada_2_0
 + visitada_2_1 <= 2
_C2: visitada_1_0 + visitada_2_0 + visitada_3_0 = 1
_C20: visitada_0_1 + visitada_0_3 + visitada_1_0 + visitada_1_3 + visitada_3_0
 + visitada_3_1 <= 2
_C21: visitada_0_2 + visitada_0_3 + visitada_2_0 + visitada_2_3 + visitada_3_0
 + visitada_3_2 <= 2
_C22: visitada_1_2 + visitada_1_3 + visitada_2_1 + visitada_2_3 + visitada_3_1
 + visitada_3_2 <= 2
_C23: visitada_0_1 + visitada_0_2 + visitada_0_3 + visitada_1_0 + visitada_1_2
 + visitada_1_3 + visitada_2_0 + visitada_2_1 + visitada_2_3 + visitada_3_0
 + visitada_3_1 + visitada_3_2 <= 3
_C3: visitada_1_0 + visitada_1_2 + visitada_1_3 = 1
_C4: visitada_0_1 + visitada_2_1 + visitada_3_1 = 1
_C5: visitada_2_0 + visitada_2_1 + visitada_2_3 = 1
_C6: visitada_0_2 + visitada_1_2 + visitada_3_2 = 1
_C7: visitada_3_0 + visitada_3_1 + visitada_3_2 = 1
_C8: visitada_0_3 + visitada_1_3 + visitada_2_3 = 1
_C9: __dummy <= 0
Bounds
 __dummy = 0
Binaries
visitada_0_1
visitada_0_2
visitada_0_3
visitada_1_0
visitada_1_2
visitada_1_3
visitada_2_0
visitada_2_1
visitada_2_3
visitada_3_0
visitada_3_1
visitada_3_2
End
