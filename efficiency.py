from ir import *

# problem 1
eff1 = [Str("solve efficiency1 17592186044416")]

# problem 2
# y = (L1 B$ L2 B$ v1 B$ v2 v2 L2 B$ v1 B$ v2 v2)
eff2 = [Str("solve efficiency2 2134")]
'''
(B+ 2134 B* B$ B$ y L3 L4 if (v4 == 0) 1 else (1 + (B$ v3 v4-1)) I":c1+0(9345873499) I!(0)
(2134 + (0 * (B$ B$ y L3 L4 if (v4 == 0) 1 else (1 + (B$ v3 (v4 - 1))) 9345873499)))
human interpretation
2134 + 0 * f(9345873499)
where f(x) = x+1
'''

# problem 3
# same as problem 3 but * 1 instead of * 0
'''
B+ I7c(2134) B* B$ B$ L1 B$ L2 B$ v1 B$ v2 v2 L2 B$ v1 B$ v2 v2 L3 L4 ? B= v4 I!(0) I"(1) B+ I"(1) B$ v3 B- v4 I"(1) I":c1+0(9345873499) I"(1)
'''
# 2134 + (9345873499+1) =
eff3 = [Str("solve efficiency3 9345875634")]

# problem 4
'''
B$ B$ y L3 L4 if (v4 < 2) 1 else (+ (v3 (v4 - 1)) (v3 (v4 - 2))) 40
human interpretation
fib(40)
def fib(x):
    if x < 2: return 1
    return fib(x - 1) + fib(x - 2)
= F(41) as defined in A000045
'''
eff4 = [Str("solve efficiency4 165580141")]

# problem 5
'''
B$ L6 B$ L7 B$ B$ y L3 L4 ? B& B> v4 I"41=(1000000) B& B$ v6 v4 B$ v7 B+ v4 I"(1) v4 B$ v3 B+ v4 I"(1) I#(2) B$ y L3 L4 ? B= v4 I"(1) T ? B= B% v4 I#(2) I"(1) F B$ v3 B/ v4 I#(2) L5 B$ B$ y L3 L4 ? B= v4 v5 T ? B= B% v5 v4 I!(0) F B$ v3 B+ v4 I"(1) I#(2)

(L6 (L7 (B$ B$ y L3 L4
if (v4 > 1000000 and v6(v4) and v7(v4+1)) v4
else
v3(v4+1)
2)
# v7 - "is power of two"
B$ y L3 L4
if (v4 == 1) T
else if (v4 % 2 == 1) F
else
v3(v4/2)
# v6 - "is prime"
L5 B$ B$ y L3 L4
if (v4 == v5) T
else if ((v5%v4) == 0) F
else
v3(v4+1)
# called on 2

human interpretation
first Mersenne prime x > 1000000
'''
eff5 = [Str("solve efficiency5 2147483647")]

# problem 6
'''
B$ L6 B$ L7
B$ B$ y L3 L4
if (v4 > 30 and v6(v7(v4))) v4
else
v3(v4+1)
# applied to 2

# v7 -- Fib(x+1) again
B$ y L3 L4
if (v4 < 2) 1
else (+ v3(v4-1) v3(v4-2))

# v6 -- "is prime" again
L5 B$ B$ y L3 L4
if (v4==v5) T
else if (v5%v4 == 0) F
else v3(v4+1)
# applied to 2

human interpretation
first x > 30 such that Fib(x+1) is prime
'''
eff6 = [Str("solve efficiency6 42")]

# problem 7
'''
B$ B$ y L42 L41
B$ L1 B$ L2 B$ L3 B$ L4 B$ L5 B$ L6 B$ L7 B$ L8 B$ L9 B$ L10 B$ L11 B$ L12 B$ L13 B$ L14 B$ L15 B$ L16 B$ L17 B$ L18 B$ L19 B$ L20 B$ L21 B$ L22 B$ L23 B$ L24 B$ L25 B$ L26 B$ L27 B$ L28 B$ L29 B$ L30 B$ L31 B$ L32 B$ L33 B$ L34 B$ L35 B$ L36 B$ L37 B$ L38 B$ L39 B$ L40
? B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B&
### SAT conditions on bits
(B| U! v18 U! v15
B| U! v14 U! v9
B| B| U! v19 v37 v12)
(U! v39)
(B| U! v20 v18)
(B| B| U! v8 v16 U! v24)
(B| U! v29 U! v39)
(B| U! v2 v19)
(v15)
(B| B| U! v37 v19 U! v6)
(B| v25 U! v23)
(B| B| U! v17 v40 v21)
(B| B| U! v23 v35 v24)
(B| U! v30 U! v28)
(v15)
(B| B| U! v37 v19 v6)
(B| U! v3 U! v11)
(B| U! v35 U! v3)
(B| B| U! v29 v39 v22)
(B| U! v27 U! v10)
(B| v28 U! v8)
(B| U! v4 v39)
(B| v10 v26)
(B| B| v22 v14 v15)
(U! v13)
(B| B| v36 v28 U! v35)
(B| B| U! v8 v16 v24)
(B| B| U! v7 v3 U! v40)
(B| B| v22 v14 v15)
(U! v13)
(B| B| U! v8 v16 v24)
(B| B| U! v19 v37 v12)
(B| v10 U! v26)
(B| U! v20 U! v18)
(B| U! v8 U! v16)
(B| B| U! v3 v11 U! v23)
(B| U! v16 v37)
(B| U! v38 U! v11)
(B| B| U! v31 v13 v14)
(B| U! v33 v19)
(B| B| U! v14 v9 U! v29)
(B| v6 v16)
(B| B| v36 v28 v35)
(B| U! v19 U! v37)
(B| U! v5 v6)
(B| v10 v26)
(B| B| U! v3 v11 v23)
(B| B| v26 v37 U! v16)
(B| B| v22 v14 U! v15 )
(B| B| v25 v23 v38 )
(B| v36 U! v28 )
(B| U! v35 v3 )
(B| B| U! v34 v35 U! v37 )
(B| U! v5 U! v6 )
(B| U! v33 U! v19 )
(B| B| U! v17 v40 v21 )
(B| B| U! v30 v28 v4 )
(B| B| U! v34 v35 v37 )
(B| B| v28 v8 v29 U! v21 )
(B| B| U! v18 v15 v39)
(v40 )
(B| B| U! v3 v11 v23 )
(B| U! v17 U! v40 )
(B| U! v35 v3 )
(B| U! v33 v19 )
(B| B| v25 v23 U! v38 )
(B| U! v27 v10 )
(B| B| v36 v28 v35 )
(B| B| U! v7 v3 v40 )
(B| U! v11 v35 )
(B| v6 v16 )
(B| B| U! v30 v28 v4 )
(B| U! v11 U! v35 )
(B| U! v32 v19 )
(B| U! v37 U! v19 )
(B| v26 U! v37 )
(B| B| U! v30 v28 U! v4)
(U! v21 )
(B| U! v20 v18 )
(B| U! v9 v31 )
(B| B| v28 v8 v29 )
(B| B| U! v31 v13 U! v14 )
(B| B| U! v24 v32 v35 )
(B| v12 v16 )
(B| B| U! v29 v39 v22 )
(B| B| U! v14 v9 v29 )
(U! v39 )
(B| U! v4 U! v39 )
(B| B| U! v37 v19 v6 )
(B| U! v23 U! v35 )
(B| B| U! v29 v39 U! v22 )
(B| U! v5 v6)
(v40 )
(B| B| v25 v23 v38 )
(B| U! v2 v19)
(B| v12 v16 )
(B| B| U! v23 v35 v24 )
(B| U! v31 U! v13 )
(B| U! v34 U! v35 )
(B| U! v32 v19 )
(B| B| U! v24 v32 v35 )
(B| B| v26 v37 v16 )
(B| U! v38 v11 )
(B| U! v16 v37 )
(B| B| U! v7 v3 v40 )
(B| U! v4 v39 )
(B| U! v7 U! v3 )
(B| B| U! v24 v32 U! v35 )
(B| B| U! v34 v35 v37 )
(B| U! v11 v35 v1 )
(B| U! v27 v10 )
(B| B| U! v23 v35 U! v24 )
(B| B| U! v18 v15 U! v39 )
(B| B| U! v19 v37 U! v12 )
(B| B| v26 v37 v16 )
(B| v6 U! v16 )
(B| B| U! v17 v40 U! v21 )
(B| U! v9 U! v31 )
(B| U! v32 U! v19 )
(B| U! v38 v11 )
(B| U! v9 v31 )
(B| B| U! v14 v9 v29 )
(B| B| U! v18 v15 v39 )
(B| v12 U! v16 )
(B| U! v16 U! v37 )
(B| v22 U! v14 )
(B| B| v28 v8 U! v29)
(v1 )
(B| U! v24 U! v32 )
(B| U! v2 U! v19 )
(B| B| U! v31 v13 v14 )
# return x
v41
# f(x+1)
B$ v42(v41+1)

# extract bits 1-40 of v41
B< I!(0) (v41/2**39 % 2)
B< I!(0) (v41/274877906944 % 2)
B< I!(0) B% (v41/137438953472 % 2)
B< I!(0) (v41/68719476736 % 2)
B< I!(0) B% (v41/34359738368) I#(2)
B< I!(0) B% (v41/17179869184) I#(2)
B< I!(0) B% (v41/8589934592) I#(2)
B< I!(0) B% B/ v41 IX""|K(4294967296) I#(2)
B< I!(0) B% B/ v41 I<PP}e(2147483648) I#(2)
B< I!(0) B% B/ v41 I.gg~C(1073741824) I#(2)
B< I!(0) B% B/ v41 I'sDOa(536870912) I#(2)
B< I!(0) B% B/ v41 I$J2gA(268435456) I#(2)
B< I!(0) B% B/ v41 I"dXs1(134217728) I#(2)
B< I!(0) B% B/ v41 Iqky)(67108864) I#(2)
B< I!(0) B% B/ v41 IIFM%(33554432) I#(2)
B< I!(0) B% B/ v41 I53f#(16777216) I#(2)
B< I!(0) B% B/ v41 I+*CQ(8388608) I#(2)
B< I!(0) B% B/ v41 I&%a9(4194304) I#(2)
B< I!(0) B% B/ v41 I#RA-(2097152) I#(2)
B< I!(0) B% B/ v41 I"9`'(1048576) I#(2)
B< I!(0) B% B/ v41 I(524288) I#(2)
B< I!(0) B% B/ v41 I>_i(262144) I#(2)
B< I!(0) B% B/ v41 I/oE(131072) I#(2)
B< I!(0) B% B/ v41 I(H3(65536) I#(2)
B< I!(0) B% B/ v41 I$cY(32768) I#(2)
B< I!(0) B% B/ v41 I"q=(16384) I#(2)
B< I!(0) B% B/ v41 Ix/(8192) I#(2)
B< I!(0) B% B/ v41 ILW(4096) I#(2)
B< I!(0) B% B/ v41 I6k(2048) I#(2)
B< I!(0) B% B/ v41 I+u(1024) I#(2)
B< I!(0) B% B/ v41 I&K(512) I#(2)
B< I!(0) B% B/ v41 I#e(256) I#(2)
B< I!(0) B% B/ v41 I"C(128) I#(2)
B< I!(0) B% B/ v41 Ia(64) I#(2)
B< I!(0) B% B/ v41 IA(32) I#(2)
B< I!(0) B% B/ v41 I1(16) I#(2)
B< I!(0) B% B/ v41 I)(8) I#(2)
B< I!(0) B% B/ v41 I%(4) I#(2)
B< I!(0) B% B/ v41 I#(2) I#(2)
B< I!(0) B% B/ v41 I"(1) I#(2)
I"(1)
'''
eff7 = [Str("solve efficiency7 584302217761")]


# problem 8
# similar SAT problem, it seems
'''
B$ B$ y L52 L51
B$ L1 B$ L2 B$ L3 B$ L4 B$ L5 B$ L6 B$ L7 B$ L8 B$ L9 B$ L10 B$ L11 B$ L12 B$ L13 B$ L14 B$ L15 B$ L16 B$ L17 B$ L18 B$ L19 B$ L20 B$ L21 B$ L22 B$ L23 B$ L24 B$ L25 B$ L26 B$ L27 B$ L28 B$ L29 B$ L30 B$ L31 B$ L32 B$ L33 B$ L34 B$ L35 B$ L36 B$ L37 B$ L38 B$ L39 B$ L40 B$ L41 B$ L42 B$ L43 B$ L44 B$ L45 B$ L46 B$ L47 B$ L48 B$ L49 B$ L50
? B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B&
B| B| U! v3 v36 v7 B| B| U! v3 U! v42 U! v48 B| B| U! v49 U! v47 U! v41 B| B| v8 U! v40 v17 B| B| U! v21 U! v31 U! v39 B| B| v36 U! v22 v49 B| B| v27 v38 v14 B| B| v15 U! v18 v6 B| B| v6 v7 U! v43 B| B| v34 U! v7 v23 B| B| v2 v14 U! v13 B| B| v2 v47 U! v42 B| B| U! v33 U! v35 v3 B| B| v44 v40 v49 B| B| v50 v36 v31 B| B| U! v36 U! v3 U! v37 B| B| v26 U! v29 v43 B| B| v15 v29 U! v45 B| B| v24 U! v11 v18 B| B| U! v47 U! v26 v6 B| B| U! v50 U! v33 U! v10 B| B| v32 v6 v16 B| B| U! v34 v37 v41 B| B| v7 U! v28 U! v17 B| B| U! v44 v46 v19 B| B| v7 v22 U! v48 B| B| v3 v39 v34 B| B| v31 v46 U! v43 B| B| U! v27 v32 v23 B| B| v37 U! v50 U! v18 B| B| v20 v5 v11 B| B| U! v45 U! v24 v6 B| B| U! v34 U! v23 U! v14 B| B| U! v22 v21 v20 B| B| U! v17 v50 v24 B| B| U! v25 U! v24 U! v27 B| B| v3 v35 v21 B| B| U! v26 v47 U! v36 B| B| U! v28 U! v45 v49 B| B| U! v21 U! v6 v12 B| B| U! v17 U! v15 U! v39 B| B| v41 v2 U! v14 B| B| v25 v36 U! v23 B| B| U! v39 U! v3 U! v40 B| B| v50 v20 v35 B| B| v27 v31 U! v39 B| B| v45 U! v15 U! v40 B| B| v34 v50 v35 B| B| U! v1 U! v48 v12 B| B| v18 U! v35 U! v30 B| B| v27 U! v24 U! v25 B| B| U! v4 U! v33 U! v12 B| B| U! v43 U! v24 U! v37 B| B| U! v37 v31 U! v44 B| B| U! v9 U! v38 v14 B| B| v33 U! v16 v34 B| B| v4 U! v35 U! v5 B| B| U! v3 U! v21 U! v19 B| B| U! v35 U! v36 U! v29 B| B| v7 U! v43 v36 B| B| v30 v14 v41 B| B| U! v35 U! v24 U! v7 B| B| v35 U! v42 v6 B| B| U! v1 U! v15 v39 B| B| v27 v49 U! v16 B| B| U! v37 v49 U! v10 B| B| v50 U! v46 U! v3 B| B| U! v41 v20 v34 B| B| U! v1 v23 v28 B| B| U! v12 U! v30 U! v20 B| B| U! v24 v29 U! v37 B| B| v12 v5 U! v44 B| B| U! v6 U! v2 v48 B| B| U! v2 U! v49 U! v43 B| B| v1 U! v50 v24 B| B| U! v7 U! v50 U! v44 B| B| U! v41 v43 v4 B| B| v13 v15 U! v11 B| B| U! v3 U! v11 v23 B| B| v33 v48 v41 B| B| v9 v23 U! v49 B| B| U! v43 v47 v1 B| B| U! v40 v16 U! v29 B| B| v30 v19 v3 B| B| v19 U! v34 v48 B| B| U! v16 U! v44 v14 B| B| v38 U! v45 U! v12 B| B| U! v4 U! v14 U! v31 B| B| U! v48 v35 U! v1 B| B| v45 U! v13 v19 B| B| v9 v42 U! v7 B| B| U! v1 U! v15 v8 B| B| U! v13 U! v44 U! v14 B| B| U! v43 U! v37 U! v31 B| B| U! v27 U! v29 v47 B| B| v7 v4 v17 B| B| v7 v10 v35 B| B| U! v25 v20 v17 B| B| v35 U! v5 U! v42 B| B| U! v50 v24 U! v5 B| B| U! v21 U! v26 v2 B| B| U! v8 v45 U! v21 B| B| U! v16 v33 v49 B| B| U! v38 v6 v16 B| B| v5 v21 v37 B| B| v8 v38 v31 B| B| U! v21 v33 v14 B| B| v20 v40 U! v5 B| B| U! v29 U! v9 v31 B| B| U! v7 v42 U! v22 B| B| U! v48 v8 v26 B| B| v48 U! v38 v33 B| B| U! v34 v49 v46 B| B| U! v14 U! v46 v25 B| B| U! v46 v4 v18 B| B| v36 U! v12 U! v31 B| B| v12 U! v18 v14 B| B| U! v7 v46 U! v16 B| B| v9 U! v8 v7 B| B| v49 U! v42 U! v22 B| B| v22 U! v15 v38 B| B| v34 U! v41 v47 B| B| v22 U! v26 v32 B| B| U! v25 U! v45 U! v21 B| B| U! v26 v32 U! v11 B| B| v15 v26 U! v25 B| B| U! v1 v46 v25 B| B| U! v14 U! v31 v30 B| B| U! v9 U! v22 v12 B| B| U! v18 v26 U! v35 B| B| U! v16 U! v32 U! v21 B| B| v31 U! v49 U! v21 B| B| v11 v9 v41 B| B| U! v13 U! v30 v19 B| B| U! v10 v4 v6 B| B| U! v4 v3 U! v22 B| B| U! v25 U! v50 U! v18 B| B| U! v40 v4 v9 B| B| v37 v20 v46 B| B| U! v27 v22 U! v29 B| B| v34 v14 v3 B| B| v3 U! v31 v20 B| B| U! v50 v2 U! v26 B| B| v17 U! v29 v38 B| B| U! v49 v12 U! v41 B| B| v15 U! v35 U! v43 B| B| U! v22 U! v23 U! v49 B| B| U! v9 v33 v48 B| B| v26 v29 v35 B| B| v27 U! v50 v37 B| B| U! v7 v46 U! v43 B| B| U! v46 U! v37 U! v8 B| B| U! v40 v36 U! v24 B| B| U! v44 v46 v15 B| B| U! v3 v36 U! v16 B| B| U! v48 v9 v43 B| B| U! v25 U! v4 v44 B| B| U! v22 v37 U! v7 B| B| U! v31 U! v17 U! v22 B| B| U! v11 U! v48 v17 B| B| v23 v34 U! v28 B| B| v23 U! v48 U! v39 B| B| U! v37 U! v1 U! v23 B| B| U! v19 v27 v14 B| B| U! v22 v33 U! v6 B| B| U! v6 U! v32 U! v26 B| B| v18 U! v20 U! v46 B| B| v43 v22 v27 B| B| U! v13 v34 v49 B| B| U! v35 U! v46 v3 B| B| v32 v39 U! v43 B| B| v6 U! v39 U! v9 B| B| v27 v39 U! v16 B| B| v25 U! v17 U! v15 B| B| U! v43 v27 v34 B| B| U! v6 v49 v5 B| B| U! v38 v11 v14 B| B| v40 U! v38 v47 B| B| v37 U! v14 v17 B| B| v39 v29 v36 B| B| U! v39 U! v28 v1 B| B| U! v18 v14 U! v16 B| B| U! v40 v50 v15 B| B| v37 U! v42 v18 B| B| U! v13 v31 v33 B| B| v2 U! v42 v33 B| B| v8 U! v3 U! v22 B| B| v1 v23 U! v31 B| B| U! v20 U! v45 v26 B| B| v42 v11 v49 B| B| v29 v11 U! v43 B| B| U! v20 U! v21 v30 B| B| v23 v45 U! v35 B| B| v38 U! v30 U! v14 B| B| U! v9 v48 U! v29 B| B| v11 U! v18 U! v23 B| B| U! v41 U! v1 U! v29 B| B| v5 v41 v26 B| B| v44 U! v30 U! v7 B| B| v38 U! v6 U! v41 B| B| v46 v48 U! v15 B| B| U! v18 U! v10 U! v47 B| B| v38 v46 U! v32 B| B| U! v32 v46 v12 B| B| v31 v40 v14 B| B| U! v18 v2 v49 B| B| v28 U! v38 v27 B| B| U! v16 U! v21 v14 B| B| U! v29 v15 v12 B| B| v49 v34 v5 B| B| v14 v22 U! v12 B| B| v30 v33 v20 B| B| U! v24 v22 v25 B| B| v4 U! v48 U! v23 B| B| U! v30 U! v36 v9 B| B| v44 v12 U! v35 B| B| v38 v3 U! v21 B| B| U! v11 v33 v49
# return x
v51
# return f(x+1)
B$ v52 B+ v51 I"(1)
# feed bits as input
B< I!(0) B% B/ v51 I)a#4]ts)(562949953421312) I#(2)
B< I!(0) B% B/ v51 I%A"*nJy%(281474976710656) I#(2)
B< I!(0) B% B/ v51 I#1!Tvd|#(140737488355328) I#(2)
B< I!(0) B% B/ v51 I")!:zq}Q(70368744177664) I#(2)
B< I!(0) B% B/ v51 IT!-|xO9(35184372088832) I#(2)
B< I!(0) B% B/ v51 I:P'N{g-(17592186044416) I#(2)
B< I!(0) B% B/ v51 I-gS7}D'(8796093022208) I#(2)
B< I!(0) B% B/ v51 I'D:,O2S(4398046511104) I#(2)
B< I!(0) B% B/ v51 I(2199023255552) I#(2)
B< I!(0) B% B/ v51 I"XmjD%E(1099511627776) I#(2)
B< I!(0) B% B/ v51 IkvEaR3(549755813888) I#(2)
B< I!(0) B% B/ v51 IFKbA9Y(274877906944) I#(2)
B< I!(0) B% B/ v51 I3eA`-=(137438953472) I#(2)
B< I!(0) B% B/ v51 I*C1@V/(68719476736) I#(2)
B< I!(0) B% B/ v51 I%a)0jW(34359738368) I#(2)
B< I!(0) B% B/ v51 I#A%(tk(17179869184) I#(2)
B< I!(0) B% B/ v51 I"1#$yu(8589934592) I#(2)
B< I!(0) B% B/ v51 IX""|K(4294967296) I#(2)
B< I!(0) B% B/ v51 I<PP}e(2147483648) I#(2)
B< I!(0) B% B/ v51 I.gg~C(1073741824) I#(2)
B< I!(0) B% B/ v51 I'sDOa(536870912) I#(2)
B< I!(0) B% B/ v51 I$J2gA(268435456) I#(2)
B< I!(0) B% B/ v51 I"dXs1(134217728) I#(2)
B< I!(0) B% B/ v51 Iqky)(67108864) I#(2)
B< I!(0) B% B/ v51 IIFM%(33554432) I#(2)
B< I!(0) B% B/ v51 I53f#(16777216) I#(2)
B< I!(0) B% B/ v51 I+*CQ(8388608) I#(2)
B< I!(0) B% B/ v51 I&%a9(4194304) I#(2)
B< I!(0) B% B/ v51 I#RA-(2097152) I#(2)
B< I!(0) B% B/ v51 I"9`'(1048576) I#(2)
B< I!(0) B% B/ v51 I(524288) I#(2)
B< I!(0) B% B/ v51 I>_i(262144) I#(2)
B< I!(0) B% B/ v51 I/oE(131072) I#(2)
B< I!(0) B% B/ v51 I(H3(65536) I#(2)
B< I!(0) B% B/ v51 I$cY(32768) I#(2)
B< I!(0) B% B/ v51 I"q=(16384) I#(2)
B< I!(0) B% B/ v51 Ix/(8192) I#(2)
B< I!(0) B% B/ v51 ILW(4096) I#(2)
B< I!(0) B% B/ v51 I6k(2048) I#(2)
B< I!(0) B% B/ v51 I+u(1024) I#(2)
B< I!(0) B% B/ v51 I&K(512) I#(2)
B< I!(0) B% B/ v51 I#e(256) I#(2)
B< I!(0) B% B/ v51 I"C(128) I#(2)
B< I!(0) B% B/ v51 Ia(64) I#(2)
B< I!(0) B% B/ v51 IA(32) I#(2)
B< I!(0) B% B/ v51 I1(16) I#(2)
B< I!(0) B% B/ v51 I)(8) I#(2)
B< I!(0) B% B/ v51 I%(4) I#(2)
B< I!(0) B% B/ v51 I#(2) I#(2)
B< I!(0) B% B/ v51 I"(1) I#(2)

I"(1)
'''
eff8 = [Str("solve efficiency8 422607674157562")]


# problem 9
'''
B$ B$ y L2 L1
B$ L11 B$ L12 B$ L13 B$ L14 B$ L15 B$ L16 B$ L17 B$ L18 B$ L19
B$ L21 B$ L22 B$ L23 B$ L24 B$ L25 B$ L26 B$ L27 B$ L28 B$ L29
B$ L31 B$ L32 B$ L33 B$ L34 B$ L35 B$ L36 B$ L37 B$ L38 B$ L39
B$ L41 B$ L42 B$ L43 B$ L44 B$ L45 B$ L46 B$ L47 B$ L48 B$ L49
B$ L51 B$ L52 B$ L53 B$ L54 B$ L55 B$ L56 B$ L57 B$ L58 B$ L59
B$ L61 B$ L62 B$ L63 B$ L64 B$ L65 B$ L66 B$ L67 B$ L68 B$ L69
B$ L71 B$ L72 B$ L73 B$ L74 B$ L75 B$ L76 B$ L77 B$ L78 B$ L79
B$ L81 B$ L82 B$ L83 B$ L84 B$ L85 B$ L86 B$ L87 B$ L88 B$ L89
B$ L91 B$ L92 B$ L93 B$ L94 B$ L95 B$ L96 B$ L97 B$ L98 B$ L99
? B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B&
U! B= v11 v12 U! B= v11 v13 U! B= v11 v14 U! B= v11 v15 U! B= v11 v16 U! B= v11 v17 U! B= v11 v18 U! B= v11 v19 U! B= v11 v21 U! B= v11 v22 U! B= v11 v23 U! B= v11 v31 U! B= v11 v32 U! B= v11 v33 U! B= v11 v41 U! B= v11 v51 U! B= v11 v61 U! B= v11 v71 U! B= v11 v81 U! B= v11 v91 U! B= v12 v13 U! B= v12 v14 U! B= v12 v15 U! B= v12 v16 U! B= v12 v17 U! B= v12 v18 U! B= v12 v19 U! B= v12 v21 U! B= v12 v22 U! B= v12 v23 U! B= v12 v31 U! B= v12 v32 U! B= v12 v33 U! B= v12 v42 U! B= v12 v52 U! B= v12 v62 U! B= v12 v72 U! B= v12 v82 U! B= v12 v92 U! B= v13 v14 U! B= v13 v15 U! B= v13 v16 U! B= v13 v17 U! B= v13 v18 U! B= v13 v19 U! B= v13 v21 U! B= v13 v22 U! B= v13 v23 U! B= v13 v31 U! B= v13 v32 U! B= v13 v33 U! B= v13 v43 U! B= v13 v53 U! B= v13 v63 U! B= v13 v73 U! B= v13 v83 U! B= v13 v93 U! B= v14 v15 U! B= v14 v16 U! B= v14 v17 U! B= v14 v18 U! B= v14 v19 U! B= v14 v24 U! B= v14 v25 U! B= v14 v26 U! B= v14 v34 U! B= v14 v35 U! B= v14 v36 U! B= v14 v44 U! B= v14 v54 U! B= v14 v64 U! B= v14 v74 U! B= v14 v84 U! B= v14 v94 U! B= v15 v16 U! B= v15 v17 U! B= v15 v18 U! B= v15 v19 U! B= v15 v24 U! B= v15 v25 U! B= v15 v26 U! B= v15 v34 U! B= v15 v35 U! B= v15 v36 U! B= v15 v45 U! B= v15 v55 U! B= v15 v65 U! B= v15 v75 U! B= v15 v85 U! B= v15 v95 U! B= v16 v17 U! B= v16 v18 U! B= v16 v19 U! B= v16 v24 U! B= v16 v25 U! B= v16 v26 U! B= v16 v34 U! B= v16 v35 U! B= v16 v36 U! B= v16 v46 U! B= v16 v56 U! B= v16 v66 U! B= v16 v76 U! B= v16 v86 U! B= v16 v96 U! B= v17 v18 U! B= v17 v19 U! B= v17 v27 U! B= v17 v28 U! B= v17 v29 U! B= v17 v37 U! B= v17 v38 U! B= v17 v39 U! B= v17 v47 U! B= v17 v57 U! B= v17 v67 U! B= v17 v77 U! B= v17 v87 U! B= v17 v97 U! B= v18 v19 U! B= v18 v27 U! B= v18 v28 U! B= v18 v29 U! B= v18 v37 U! B= v18 v38 U! B= v18 v39 U! B= v18 v48 U! B= v18 v58 U! B= v18 v68 U! B= v18 v78 U! B= v18 v88 U! B= v18 v98 U! B= v19 v27 U! B= v19 v28 U! B= v19 v29 U! B= v19 v37 U! B= v19 v38 U! B= v19 v39 U! B= v19 v49 U! B= v19 v59 U! B= v19 v69 U! B= v19 v79 U! B= v19 v89 U! B= v19 v99 U! B= v21 v22 U! B= v21 v23 U! B= v21 v24 U! B= v21 v25 U! B= v21 v26 U! B= v21 v27 U! B= v21 v28 U! B= v21 v29 U! B= v21 v31 U! B= v21 v32 U! B= v21 v33 U! B= v21 v41 U! B= v21 v51 U! B= v21 v61 U! B= v21 v71 U! B= v21 v81 U! B= v21 v91 U! B= v22 v23 U! B= v22 v24 U! B= v22 v25 U! B= v22 v26 U! B= v22 v27 U! B= v22 v28 U! B= v22 v29 U! B= v22 v31 U! B= v22 v32 U! B= v22 v33 U! B= v22 v42 U! B= v22 v52 U! B= v22 v62 U! B= v22 v72 U! B= v22 v82 U! B= v22 v92 U! B= v23 v24 U! B= v23 v25 U! B= v23 v26 U! B= v23 v27 U! B= v23 v28 U! B= v23 v29 U! B= v23 v31 U! B= v23 v32 U! B= v23 v33 U! B= v23 v43 U! B= v23 v53 U! B= v23 v63 U! B= v23 v73 U! B= v23 v83 U! B= v23 v93 U! B= v24 v25 U! B= v24 v26 U! B= v24 v27 U! B= v24 v28 U! B= v24 v29 U! B= v24 v34 U! B= v24 v35 U! B= v24 v36 U! B= v24 v44 U! B= v24 v54 U! B= v24 v64 U! B= v24 v74 U! B= v24 v84 U! B= v24 v94 U! B= v25 v26 U! B= v25 v27 U! B= v25 v28 U! B= v25 v29 U! B= v25 v34 U! B= v25 v35 U! B= v25 v36 U! B= v25 v45 U! B= v25 v55 U! B= v25 v65 U! B= v25 v75 U! B= v25 v85 U! B= v25 v95 U! B= v26 v27 U! B= v26 v28 U! B= v26 v29 U! B= v26 v34 U! B= v26 v35 U! B= v26 v36 U! B= v26 v46 U! B= v26 v56 U! B= v26 v66 U! B= v26 v76 U! B= v26 v86 U! B= v26 v96 U! B= v27 v28 U! B= v27 v29 U! B= v27 v37 U! B= v27 v38 U! B= v27 v39 U! B= v27 v47 U! B= v27 v57 U! B= v27 v67 U! B= v27 v77 U! B= v27 v87 U! B= v27 v97 U! B= v28 v29 U! B= v28 v37 U! B= v28 v38 U! B= v28 v39 U! B= v28 v48 U! B= v28 v58 U! B= v28 v68 U! B= v28 v78 U! B= v28 v88 U! B= v28 v98 U! B= v29 v37 U! B= v29 v38 U! B= v29 v39 U! B= v29 v49 U! B= v29 v59 U! B= v29 v69 U! B= v29 v79 U! B= v29 v89 U! B= v29 v99 U! B= v31 v32 U! B= v31 v33 U! B= v31 v34 U! B= v31 v35 U! B= v31 v36 U! B= v31 v37 U! B= v31 v38 U! B= v31 v39 U! B= v31 v41 U! B= v31 v51 U! B= v31 v61 U! B= v31 v71 U! B= v31 v81 U! B= v31 v91 U! B= v32 v33 U! B= v32 v34 U! B= v32 v35 U! B= v32 v36 U! B= v32 v37 U! B= v32 v38 U! B= v32 v39 U! B= v32 v42 U! B= v32 v52 U! B= v32 v62 U! B= v32 v72 U! B= v32 v82 U! B= v32 v92 U! B= v33 v34 U! B= v33 v35 U! B= v33 v36 U! B= v33 v37 U! B= v33 v38 U! B= v33 v39 U! B= v33 v43 U! B= v33 v53 U! B= v33 v63 U! B= v33 v73 U! B= v33 v83 U! B= v33 v93 U! B= v34 v35 U! B= v34 v36 U! B= v34 v37 U! B= v34 v38 U! B= v34 v39 U! B= v34 v44 U! B= v34 v54 U! B= v34 v64 U! B= v34 v74 U! B= v34 v84 U! B= v34 v94 U! B= v35 v36 U! B= v35 v37 U! B= v35 v38 U! B= v35 v39 U! B= v35 v45 U! B= v35 v55 U! B= v35 v65 U! B= v35 v75 U! B= v35 v85 U! B= v35 v95 U! B= v36 v37 U! B= v36 v38 U! B= v36 v39 U! B= v36 v46 U! B= v36 v56 U! B= v36 v66 U! B= v36 v76 U! B= v36 v86 U! B= v36 v96 U! B= v37 v38 U! B= v37 v39 U! B= v37 v47 U! B= v37 v57 U! B= v37 v67 U! B= v37 v77 U! B= v37 v87 U! B= v37 v97 U! B= v38 v39 U! B= v38 v48 U! B= v38 v58 U! B= v38 v68 U! B= v38 v78 U! B= v38 v88 U! B= v38 v98 U! B= v39 v49 U! B= v39 v59 U! B= v39 v69 U! B= v39 v79 U! B= v39 v89 U! B= v39 v99 U! B= v41 v42 U! B= v41 v43 U! B= v41 v44 U! B= v41 v45 U! B= v41 v46 U! B= v41 v47 U! B= v41 v48 U! B= v41 v49 U! B= v41 v51 U! B= v41 v52 U! B= v41 v53 U! B= v41 v61 U! B= v41 v62 U! B= v41 v63 U! B= v41 v71 U! B= v41 v81 U! B= v41 v91 U! B= v42 v43 U! B= v42 v44 U! B= v42 v45 U! B= v42 v46 U! B= v42 v47 U! B= v42 v48 U! B= v42 v49 U! B= v42 v51 U! B= v42 v52 U! B= v42 v53 U! B= v42 v61 U! B= v42 v62 U! B= v42 v63 U! B= v42 v72 U! B= v42 v82 U! B= v42 v92 U! B= v43 v44 U! B= v43 v45 U! B= v43 v46 U! B= v43 v47 U! B= v43 v48 U! B= v43 v49 U! B= v43 v51 U! B= v43 v52 U! B= v43 v53 U! B= v43 v61 U! B= v43 v62 U! B= v43 v63 U! B= v43 v73 U! B= v43 v83 U! B= v43 v93 U! B= v44 v45 U! B= v44 v46 U! B= v44 v47 U! B= v44 v48 U! B= v44 v49 U! B= v44 v54 U! B= v44 v55 U! B= v44 v56 U! B= v44 v64 U! B= v44 v65 U! B= v44 v66 U! B= v44 v74 U! B= v44 v84 U! B= v44 v94 U! B= v45 v46 U! B= v45 v47 U! B= v45 v48 U! B= v45 v49 U! B= v45 v54 U! B= v45 v55 U! B= v45 v56 U! B= v45 v64 U! B= v45 v65 U! B= v45 v66 U! B= v45 v75 U! B= v45 v85 U! B= v45 v95 U! B= v46 v47 U! B= v46 v48 U! B= v46 v49 U! B= v46 v54 U! B= v46 v55 U! B= v46 v56 U! B= v46 v64 U! B= v46 v65 U! B= v46 v66 U! B= v46 v76 U! B= v46 v86 U! B= v46 v96 U! B= v47 v48 U! B= v47 v49 U! B= v47 v57 U! B= v47 v58 U! B= v47 v59 U! B= v47 v67 U! B= v47 v68 U! B= v47 v69 U! B= v47 v77 U! B= v47 v87 U! B= v47 v97 U! B= v48 v49 U! B= v48 v57 U! B= v48 v58 U! B= v48 v59 U! B= v48 v67 U! B= v48 v68 U! B= v48 v69 U! B= v48 v78 U! B= v48 v88 U! B= v48 v98 U! B= v49 v57 U! B= v49 v58 U! B= v49 v59 U! B= v49 v67 U! B= v49 v68 U! B= v49 v69 U! B= v49 v79 U! B= v49 v89 U! B= v49 v99 U! B= v51 v52 U! B= v51 v53 U! B= v51 v54 U! B= v51 v55 U! B= v51 v56 U! B= v51 v57 U! B= v51 v58 U! B= v51 v59 U! B= v51 v61 U! B= v51 v62 U! B= v51 v63 U! B= v51 v71 U! B= v51 v81 U! B= v51 v91 U! B= v52 v53 U! B= v52 v54 U! B= v52 v55 U! B= v52 v56 U! B= v52 v57 U! B= v52 v58 U! B= v52 v59 U! B= v52 v61 U! B= v52 v62 U! B= v52 v63 U! B= v52 v72 U! B= v52 v82 U! B= v52 v92 U! B= v53 v54 U! B= v53 v55 U! B= v53 v56 U! B= v53 v57 U! B= v53 v58 U! B= v53 v59 U! B= v53 v61 U! B= v53 v62 U! B= v53 v63 U! B= v53 v73 U! B= v53 v83 U! B= v53 v93 U! B= v54 v55 U! B= v54 v56 U! B= v54 v57 U! B= v54 v58 U! B= v54 v59 U! B= v54 v64 U! B= v54 v65 U! B= v54 v66 U! B= v54 v74 U! B= v54 v84 U! B= v54 v94 U! B= v55 v56 U! B= v55 v57 U! B= v55 v58 U! B= v55 v59 U! B= v55 v64 U! B= v55 v65 U! B= v55 v66 U! B= v55 v75 U! B= v55 v85 U! B= v55 v95 U! B= v56 v57 U! B= v56 v58 U! B= v56 v59 U! B= v56 v64 U! B= v56 v65 U! B= v56 v66 U! B= v56 v76 U! B= v56 v86 U! B= v56 v96 U! B= v57 v58 U! B= v57 v59 U! B= v57 v67 U! B= v57 v68 U! B= v57 v69 U! B= v57 v77 U! B= v57 v87 U! B= v57 v97 U! B= v58 v59 U! B= v58 v67 U! B= v58 v68 U! B= v58 v69 U! B= v58 v78 U! B= v58 v88 U! B= v58 v98 U! B= v59 v67 U! B= v59 v68 U! B= v59 v69 U! B= v59 v79 U! B= v59 v89 U! B= v59 v99 U! B= v61 v62 U! B= v61 v63 U! B= v61 v64 U! B= v61 v65 U! B= v61 v66 U! B= v61 v67 U! B= v61 v68 U! B= v61 v69 U! B= v61 v71 U! B= v61 v81 U! B= v61 v91 U! B= v62 v63 U! B= v62 v64 U! B= v62 v65 U! B= v62 v66 U! B= v62 v67 U! B= v62 v68 U! B= v62 v69 U! B= v62 v72 U! B= v62 v82 U! B= v62 v92 U! B= v63 v64 U! B= v63 v65 U! B= v63 v66 U! B= v63 v67 U! B= v63 v68 U! B= v63 v69 U! B= v63 v73 U! B= v63 v83 U! B= v63 v93 U! B= v64 v65 U! B= v64 v66 U! B= v64 v67 U! B= v64 v68 U! B= v64 v69 U! B= v64 v74 U! B= v64 v84 U! B= v64 v94 U! B= v65 v66 U! B= v65 v67 U! B= v65 v68 U! B= v65 v69 U! B= v65 v75 U! B= v65 v85 U! B= v65 v95 U! B= v66 v67 U! B= v66 v68 U! B= v66 v69 U! B= v66 v76 U! B= v66 v86 U! B= v66 v96 U! B= v67 v68 U! B= v67 v69 U! B= v67 v77 U! B= v67 v87 U! B= v67 v97 U! B= v68 v69 U! B= v68 v78 U! B= v68 v88 U! B= v68 v98 U! B= v69 v79 U! B= v69 v89 U! B= v69 v99 U! B= v71 v72 U! B= v71 v73 U! B= v71 v74 U! B= v71 v75 U! B= v71 v76 U! B= v71 v77 U! B= v71 v78 U! B= v71 v79 U! B= v71 v81 U! B= v71 v82 U! B= v71 v83 U! B= v71 v91 U! B= v71 v92 U! B= v71 v93 U! B= v72 v73 U! B= v72 v74 U! B= v72 v75 U! B= v72 v76 U! B= v72 v77 U! B= v72 v78 U! B= v72 v79 U! B= v72 v81 U! B= v72 v82 U! B= v72 v83 U! B= v72 v91 U! B= v72 v92 U! B= v72 v93 U! B= v73 v74 U! B= v73 v75 U! B= v73 v76 U! B= v73 v77 U! B= v73 v78 U! B= v73 v79 U! B= v73 v81 U! B= v73 v82 U! B= v73 v83 U! B= v73 v91 U! B= v73 v92 U! B= v73 v93 U! B= v74 v75 U! B= v74 v76 U! B= v74 v77 U! B= v74 v78 U! B= v74 v79 U! B= v74 v84 U! B= v74 v85 U! B= v74 v86 U! B= v74 v94 U! B= v74 v95 U! B= v74 v96 U! B= v75 v76 U! B= v75 v77 U! B= v75 v78 U! B= v75 v79 U! B= v75 v84 U! B= v75 v85 U! B= v75 v86 U! B= v75 v94 U! B= v75 v95 U! B= v75 v96 U! B= v76 v77 U! B= v76 v78 U! B= v76 v79 U! B= v76 v84 U! B= v76 v85 U! B= v76 v86 U! B= v76 v94 U! B= v76 v95 U! B= v76 v96 U! B= v77 v78 U! B= v77 v79 U! B= v77 v87 U! B= v77 v88 U! B= v77 v89 U! B= v77 v97 U! B= v77 v98 U! B= v77 v99 U! B= v78 v79 U! B= v78 v87 U! B= v78 v88 U! B= v78 v89 U! B= v78 v97 U! B= v78 v98 U! B= v78 v99 U! B= v79 v87 U! B= v79 v88 U! B= v79 v89 U! B= v79 v97 U! B= v79 v98 U! B= v79 v99 U! B= v81 v82 U! B= v81 v83 U! B= v81 v84 U! B= v81 v85 U! B= v81 v86 U! B= v81 v87 U! B= v81 v88 U! B= v81 v89 U! B= v81 v91 U! B= v81 v92 U! B= v81 v93 U! B= v82 v83 U! B= v82 v84 U! B= v82 v85 U! B= v82 v86 U! B= v82 v87 U! B= v82 v88 U! B= v82 v89 U! B= v82 v91 U! B= v82 v92 U! B= v82 v93 U! B= v83 v84 U! B= v83 v85 U! B= v83 v86 U! B= v83 v87 U! B= v83 v88 U! B= v83 v89 U! B= v83 v91 U! B= v83 v92 U! B= v83 v93 U! B= v84 v85 U! B= v84 v86 U! B= v84 v87 U! B= v84 v88 U! B= v84 v89 U! B= v84 v94 U! B= v84 v95 U! B= v84 v96 U! B= v85 v86 U! B= v85 v87 U! B= v85 v88 U! B= v85 v89 U! B= v85 v94 U! B= v85 v95 U! B= v85 v96 U! B= v86 v87 U! B= v86 v88 U! B= v86 v89 U! B= v86 v94 U! B= v86 v95 U! B= v86 v96 U! B= v87 v88 U! B= v87 v89 U! B= v87 v97 U! B= v87 v98 U! B= v87 v99 U! B= v88 v89 U! B= v88 v97 U! B= v88 v98 U! B= v88 v99 U! B= v89 v97 U! B= v89 v98 U! B= v89 v99 U! B= v91 v92 U! B= v91 v93 U! B= v91 v94 U! B= v91 v95 U! B= v91 v96 U! B= v91 v97 U! B= v91 v98 U! B= v91 v99 U! B= v92 v93 U! B= v92 v94 U! B= v92 v95 U! B= v92 v96 U! B= v92 v97 U! B= v92 v98 U! B= v92 v99 U! B= v93 v94 U! B= v93 v95 U! B= v93 v96 U! B= v93 v97 U! B= v93 v98 U! B= v93 v99 U! B= v94 v95 U! B= v94 v96 U! B= v94 v97 U! B= v94 v98 U! B= v94 v99 U! B= v95 v96 U! B= v95 v97 U! B= v95 v98 U! B= v95 v99 U! B= v96 v97 U! B= v96 v98 U! B= v96 v99 U! B= v97 v98 U! B= v97 v99 U! B= v98 v99
# return x
v1
# return f(x+1)
B$ v2 B+ v1 I(1)

# inputs: digits base 9 plus 1 ([1-10])
B+ I(1) B% B/ v1 I(1) I(9)
B+ I(1) B% B/ v1 I(9) I(9)
B+ I(1) B% B/ v1 I(81) I(9)
B+ I(1) B% B/ v1 I(729) I(9)
B+ I(1) B% B/ v1 I(6561) I(9)
B+ I(1) B% B/ v1 I(59049) I(9)
B+ I(1) B% B/ v1 I(531441) I(9)
B+ I(1) B% B/ v1 I(4782969) I(9)
B+ I(1) B% B/ v1 I(43046721) I(9)
B+ I(1) B% B/ v1 I(387420489) I(9)
B+ I(1) B% B/ v1 I(3486784401) I(9)
B+ I(1) B% B/ v1 I(31381059609) I(9)
B+ I(1) B% B/ v1 I(282429536481) I(9)
B+ I(1) B% B/ v1 I(2541865828329) I(9)
B+ I(1) B% B/ v1 I(22876792454961) I(9)
B+ I(1) B% B/ v1 I(205891132094649) I(9)
B+ I(1) B% B/ v1 I(1853020188851841) I(9)
B+ I(1) B% B/ v1 I(16677181699666569) I(9)
B+ I(1) B% B/ v1 I(150094635296999121) I(9)
B+ I(1) B% B/ v1 I(1350851717672992089) I(9)
B+ I(1) B% B/ v1 I(12157665459056928801) I(9)
B+ I(1) B% B/ v1 I(109418989131512359209) I(9)
B+ I(1) B% B/ v1 I(984770902183611232881) I(9)
B+ I(1) B% B/ v1 I(8862938119652501095929) I(9)
B+ I(1) B% B/ v1 I(79766443076872509863361) I(9)
B+ I(1) B% B/ v1 I(717897987691852588770249) I(9)
B+ I(1) B% B/ v1 I(6461081889226673298932241) I(9)
B+ I(1) B% B/ v1 I(58149737003040059690390169) I(9)
B+ I(1) B% B/ v1 I(523347633027360537213511521) I(9)
B+ I(1) B% B/ v1 I(4710128697246244834921603689) I(9)
B+ I(1) B% B/ v1 I(42391158275216203514294433201) I(9)
B+ I(1) B% B/ v1 I(381520424476945831628649898809) I(9)
B+ I(1) B% B/ v1 I(3433683820292512484657849089281) I(9)
B+ I(1) B% B/ v1 I(30903154382632612361920641803529) I(9)
B+ I(1) B% B/ v1 I(278128389443693511257285776231761) I(9)
B+ I(1) B% B/ v1 I(2503155504993241601315571986085849) I(9)
B+ I(1) B% B/ v1 I(22528399544939174411840147874772641) I(9)
B+ I(1) B% B/ v1 I(202755595904452569706561330872953769) I(9)
B+ I(1) B% B/ v1 I(1824800363140073127359051977856583921) I(9)
B+ I(1) B% B/ v1 I(16423203268260658146231467800709255289) I(9)
B+ I(1) B% B/ v1 I(147808829414345923316083210206383297601) I(9)
B+ I(1) B% B/ v1 I(1330279464729113309844748891857449678409) I(9)
B+ I(1) B% B/ v1 I(11972515182562019788602740026717047105681) I(9)
B+ I(1) B% B/ v1 I(107752636643058178097424660240453423951129) I(9)
B+ I(1) B% B/ v1 I(969773729787523602876821942164080815560161) I(9)
B+ I(1) B% B/ v1 I(8727963568087712425891397479476727340041449) I(9)
B+ I(1) B% B/ v1 I(78551672112789411833022577315290546060373041) I(9)
B+ I(1) B% B/ v1 I(706965049015104706497203195837614914543357369) I(9)
B+ I(1) B% B/ v1 I(6362685441135942358474828762538534230890216321) I(9)
B+ I(1) B% B/ v1 I(57264168970223481226273458862846808078011946889) I(9)
B+ I(1) B% B/ v1 I(515377520732011331036461129765621272702107522001) I(9)
B+ I(1) B% B/ v1 I(4638397686588101979328150167890591454318967698009) I(9)
B+ I(1) B% B/ v1 I(41745579179292917813953351511015323088870709282081) I(9)
B+ I(1) B% B/ v1 I(375710212613636260325580163599137907799836383538729) I(9)
B+ I(1) B% B/ v1 I(3381391913522726342930221472392241170198527451848561) I(9)
B+ I(1) B% B/ v1 I(30432527221704537086371993251530170531786747066637049) I(9)
B+ I(1) B% B/ v1 I(273892744995340833777347939263771534786080723599733441) I(9)
B+ I(1) B% B/ v1 I(2465034704958067503996131453373943813074726512397600969) I(9)
B+ I(1) B% B/ v1 I(22185312344622607535965183080365494317672538611578408721) I(9)
B+ I(1) B% B/ v1 I(199667811101603467823686647723289448859052847504205678489) I(9)
B+ I(1) B% B/ v1 I(1797010299914431210413179829509605039731475627537851106401) I(9)
B+ I(1) B% B/ v1 I(16173092699229880893718618465586445357583280647840659957609) I(9)
B+ I(1) B% B/ v1 I(145557834293068928043467566190278008218249525830565939618481) I(9)
B+ I(1) B% B/ v1 I(1310020508637620352391208095712502073964245732475093456566329) I(9)
B+ I(1) B% B/ v1 I(11790184577738583171520872861412518665678211592275841109096961) I(9)
B+ I(1) B% B/ v1 I(106111661199647248543687855752712667991103904330482569981872649) I(9)
B+ I(1) B% B/ v1 I(955004950796825236893190701774414011919935138974343129836853841) I(9)
B+ I(1) B% B/ v1 I(8595044557171427132038716315969726107279416250769088168531684569) I(9)
B+ I(1) B% B/ v1 I(77355401014542844188348446843727534965514746256921793516785161121) I(9)
B+ I(1) B% B/ v1 I(696198609130885597695136021593547814689632716312296141651066450089) I(9)
B+ I(1) B% B/ v1 I(6265787482177970379256224194341930332206694446810665274859598050801) I(9)
B+ I(1) B% B/ v1 I(56392087339601733413306017749077372989860250021295987473736382457209) I(9)
B+ I(1) B% B/ v1 I(507528786056415600719754159741696356908742250191663887263627442114881) I(9)
B+ I(1) B% B/ v1 I(4567759074507740406477787437675267212178680251724974985372646979033929) I(9)
B+ I(1) B% B/ v1 I(41109831670569663658300086939077404909608122265524774868353822811305361) I(9)
B+ I(1) B% B/ v1 I(369988485035126972924700782451696644186473100389722973815184405301748249) I(9)
B+ I(1) B% B/ v1 I(3329896365316142756322307042065269797678257903507506764336659647715734241) I(9)
B+ I(1) B% B/ v1 I(29969067287845284806900763378587428179104321131567560879029936829441608169) I(9)
B+ I(1) B% B/ v1 I(269721605590607563262106870407286853611938890184108047911269431464974473521) I(9)
B+ I(1) B% B/ v1 I(2427494450315468069358961833665581682507450011656972431201424883184770261689) I(9)
B+ I(1) B% B/ v1 I(21847450052839212624230656502990235142567050104912751880812823948662932355201) I(9)

I(1)

human translation: find a 9-coloring of the given graph
human translation': wait a minute... it's a sudoku grid, just need the
lexicographically smallest sudoku grid
https://possiblywrong.wordpress.com/2013/11/03/sudoku-solver/
'''
eff9 = [Str("solve efficiency9 3072297283032850841637141056325154790039828427723724157541484782406577456068")]


# problem 10
# probably a sudoku with some numbers filled in?
'''
B$ B$ y L2 L1
B$ L11 B$ L12 B$ L13 B$ L14 B$ L15 B$ L16 B$ L17 B$ L18 B$ L19 B$ L21 B$ L22 B$ L23 B$ L24 B$ L25 B$ L26 B$ L27 B$ L28 B$ L29 B$ L31 B$ L32 B$ L33 B$ L34 B$ L35 B$ L36 B$ L37 B$ L38 B$ L39 B$ L41 B$ L42 B$ L43 B$ L44 B$ L45 B$ L46 B$ L47 B$ L48 B$ L49 B$ L51 B$ L52 B$ L53 B$ L54 B$ L55 B$ L56 B$ L57 B$ L58 B$ L59 B$ L61 B$ L62 B$ L63 B$ L64 B$ L65 B$ L66 B$ L67 B$ L68 B$ L69 B$ L71 B$ L72 B$ L73 B$ L74 B$ L75 B$ L76 B$ L77 B$ L78 B$ L79 B$ L81 B$ L82 B$ L83 B$ L84 B$ L85 B$ L86 B$ L87 B$ L88 B$ L89 B$ L91 B$ L92 B$ L93 B$ L94 B$ L95 B$ L96 B$ L97 B$ L98 B$ L99
? B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B&
U! B= v11 v12 U! B= v11 v13 U! B= v11 v14 U! B= v11 v15 U! B= v11 v16 U! B= v11 v17 U! B= v11 v18 U! B= v11 v19 U! B= v11 v21 U! B= v11 v22 U! B= v11 v23 U! B= v11 v31 U! B= v11 v32 U! B= v11 v33 U! B= v11 v41 U! B= v11 v51 U! B= v11 v61 U! B= v11 v71 U! B= v11 v81 U! B= v11 v91 U! B= v12 v13 U! B= v12 v14 U! B= v12 v15 U! B= v12 v16 U! B= v12 v17 U! B= v12 v18 U! B= v12 v19 U! B= v12 v21 U! B= v12 v22 U! B= v12 v23 U! B= v12 v31 U! B= v12 v32 U! B= v12 v33 U! B= v12 v42 U! B= v12 v52 U! B= v12 v62 U! B= v12 v72 U! B= v12 v82 U! B= v12 v92 U! B= v13 v14 U! B= v13 v15 U! B= v13 v16 U! B= v13 v17 U! B= v13 v18 U! B= v13 v19 U! B= v13 v21 U! B= v13 v22 U! B= v13 v23 U! B= v13 v31 U! B= v13 v32 U! B= v13 v33 U! B= v13 v43 U! B= v13 v53 U! B= v13 v63 U! B= v13 v73 U! B= v13 v83 U! B= v13 v93 U! B= v14 v15 U! B= v14 v16 U! B= v14 v17 U! B= v14 v18 U! B= v14 v19 U! B= v14 v24 U! B= v14 v25 U! B= v14 v26 U! B= v14 v34 U! B= v14 v35 U! B= v14 v36 U! B= v14 v44 U! B= v14 v54 U! B= v14 v64 U! B= v14 v74 U! B= v14 v84 U! B= v14 v94 U! B= v15 v16 U! B= v15 v17 U! B= v15 v18 U! B= v15 v19 U! B= v15 v24 U! B= v15 v25 U! B= v15 v26 U! B= v15 v34 U! B= v15 v35 U! B= v15 v36 U! B= v15 v45 U! B= v15 v55 U! B= v15 v65 U! B= v15 v75 U! B= v15 v85 U! B= v15 v95 U! B= v16 v17 U! B= v16 v18 U! B= v16 v19 U! B= v16 v24 U! B= v16 v25 U! B= v16 v26 U! B= v16 v34 U! B= v16 v35 U! B= v16 v36 U! B= v16 v46 U! B= v16 v56 U! B= v16 v66 U! B= v16 v76 U! B= v16 v86 U! B= v16 v96 U! B= v17 v18 U! B= v17 v19 U! B= v17 v27 U! B= v17 v28 U! B= v17 v29 U! B= v17 v37 U! B= v17 v38 U! B= v17 v39 U! B= v17 v47 U! B= v17 v57 U! B= v17 v67 U! B= v17 v77 U! B= v17 v87 U! B= v17 v97 U! B= v18 v19 U! B= v18 v27 U! B= v18 v28 U! B= v18 v29 U! B= v18 v37 U! B= v18 v38 U! B= v18 v39 U! B= v18 v48 U! B= v18 v58 U! B= v18 v68 U! B= v18 v78 U! B= v18 v88 U! B= v18 v98 U! B= v19 v27 U! B= v19 v28 U! B= v19 v29 U! B= v19 v37 U! B= v19 v38 U! B= v19 v39 U! B= v19 v49 U! B= v19 v59 U! B= v19 v69 U! B= v19 v79 U! B= v19 v89 U! B= v19 v99 U! B= v21 v22 U! B= v21 v23 U! B= v21 v24 U! B= v21 v25 U! B= v21 v26 U! B= v21 v27 U! B= v21 v28 U! B= v21 v29 U! B= v21 v31 U! B= v21 v32 U! B= v21 v33 U! B= v21 v41 U! B= v21 v51 U! B= v21 v61 U! B= v21 v71 U! B= v21 v81 U! B= v21 v91 U! B= v22 v23 U! B= v22 v24 U! B= v22 v25 U! B= v22 v26 U! B= v22 v27 U! B= v22 v28 U! B= v22 v29 U! B= v22 v31 U! B= v22 v32 U! B= v22 v33 U! B= v22 v42 U! B= v22 v52 U! B= v22 v62 U! B= v22 v72 U! B= v22 v82 U! B= v22 v92 U! B= v23 v24 U! B= v23 v25 U! B= v23 v26 U! B= v23 v27 U! B= v23 v28 U! B= v23 v29 U! B= v23 v31 U! B= v23 v32 U! B= v23 v33 U! B= v23 v43 U! B= v23 v53 U! B= v23 v63 U! B= v23 v73 U! B= v23 v83 U! B= v23 v93 U! B= v24 v25 U! B= v24 v26 U! B= v24 v27 U! B= v24 v28 U! B= v24 v29 U! B= v24 v34 U! B= v24 v35 U! B= v24 v36 U! B= v24 v44 U! B= v24 v54 U! B= v24 v64 U! B= v24 v74 U! B= v24 v84 U! B= v24 v94 U! B= v25 v26 U! B= v25 v27 U! B= v25 v28 U! B= v25 v29 U! B= v25 v34 U! B= v25 v35 U! B= v25 v36 U! B= v25 v45 U! B= v25 v55 U! B= v25 v65 U! B= v25 v75 U! B= v25 v85 U! B= v25 v95 U! B= v26 v27 U! B= v26 v28 U! B= v26 v29 U! B= v26 v34 U! B= v26 v35 U! B= v26 v36 U! B= v26 v46 U! B= v26 v56 U! B= v26 v66 U! B= v26 v76 U! B= v26 v86 U! B= v26 v96 U! B= v27 v28 U! B= v27 v29 U! B= v27 v37 U! B= v27 v38 U! B= v27 v39 U! B= v27 v47 U! B= v27 v57 U! B= v27 v67 U! B= v27 v77 U! B= v27 v87 U! B= v27 v97 U! B= v28 v29 U! B= v28 v37 U! B= v28 v38 U! B= v28 v39 U! B= v28 v48 U! B= v28 v58 U! B= v28 v68 U! B= v28 v78 U! B= v28 v88 U! B= v28 v98 U! B= v29 v37 U! B= v29 v38 U! B= v29 v39 U! B= v29 v49 U! B= v29 v59 U! B= v29 v69 U! B= v29 v79 U! B= v29 v89 U! B= v29 v99 U! B= v31 v32 U! B= v31 v33 U! B= v31 v34 U! B= v31 v35 U! B= v31 v36 U! B= v31 v37 U! B= v31 v38 U! B= v31 v39 U! B= v31 v41 U! B= v31 v51 U! B= v31 v61 U! B= v31 v71 U! B= v31 v81 U! B= v31 v91 U! B= v32 v33 U! B= v32 v34 U! B= v32 v35 U! B= v32 v36 U! B= v32 v37 U! B= v32 v38 U! B= v32 v39 U! B= v32 v42 U! B= v32 v52 U! B= v32 v62 U! B= v32 v72 U! B= v32 v82 U! B= v32 v92 U! B= v33 v34 U! B= v33 v35 U! B= v33 v36 U! B= v33 v37 U! B= v33 v38 U! B= v33 v39 U! B= v33 v43 U! B= v33 v53 U! B= v33 v63 U! B= v33 v73 U! B= v33 v83 U! B= v33 v93 U! B= v34 v35 U! B= v34 v36 U! B= v34 v37 U! B= v34 v38 U! B= v34 v39 U! B= v34 v44 U! B= v34 v54 U! B= v34 v64 U! B= v34 v74 U! B= v34 v84 U! B= v34 v94 U! B= v35 v36 U! B= v35 v37 U! B= v35 v38 U! B= v35 v39 U! B= v35 v45 U! B= v35 v55 U! B= v35 v65 U! B= v35 v75 U! B= v35 v85 U! B= v35 v95 U! B= v36 v37 U! B= v36 v38 U! B= v36 v39 U! B= v36 v46 U! B= v36 v56 U! B= v36 v66 U! B= v36 v76 U! B= v36 v86 U! B= v36 v96 U! B= v37 v38 U! B= v37 v39 U! B= v37 v47 U! B= v37 v57 U! B= v37 v67 U! B= v37 v77 U! B= v37 v87 U! B= v37 v97 U! B= v38 v39 U! B= v38 v48 U! B= v38 v58 U! B= v38 v68 U! B= v38 v78 U! B= v38 v88 U! B= v38 v98 U! B= v39 v49 U! B= v39 v59 U! B= v39 v69 U! B= v39 v79 U! B= v39 v89 U! B= v39 v99 U! B= v41 v42 U! B= v41 v43 U! B= v41 v44 U! B= v41 v45 U! B= v41 v46 U! B= v41 v47 U! B= v41 v48 U! B= v41 v49 U! B= v41 v51 U! B= v41 v52 U! B= v41 v53 U! B= v41 v61 U! B= v41 v62 U! B= v41 v63 U! B= v41 v71 U! B= v41 v81 U! B= v41 v91 U! B= v42 v43 U! B= v42 v44 U! B= v42 v45 U! B= v42 v46 U! B= v42 v47 U! B= v42 v48 U! B= v42 v49 U! B= v42 v51 U! B= v42 v52 U! B= v42 v53 U! B= v42 v61 U! B= v42 v62 U! B= v42 v63 U! B= v42 v72 U! B= v42 v82 U! B= v42 v92 U! B= v43 v44 U! B= v43 v45 U! B= v43 v46 U! B= v43 v47 U! B= v43 v48 U! B= v43 v49 U! B= v43 v51 U! B= v43 v52 U! B= v43 v53 U! B= v43 v61 U! B= v43 v62 U! B= v43 v63 U! B= v43 v73 U! B= v43 v83 U! B= v43 v93 U! B= v44 v45 U! B= v44 v46 U! B= v44 v47 U! B= v44 v48 U! B= v44 v49 U! B= v44 v54 U! B= v44 v55 U! B= v44 v56 U! B= v44 v64 U! B= v44 v65 U! B= v44 v66 U! B= v44 v74 U! B= v44 v84 U! B= v44 v94 U! B= v45 v46 U! B= v45 v47 U! B= v45 v48 U! B= v45 v49 U! B= v45 v54 U! B= v45 v55 U! B= v45 v56 U! B= v45 v64 U! B= v45 v65 U! B= v45 v66 U! B= v45 v75 U! B= v45 v85 U! B= v45 v95 U! B= v46 v47 U! B= v46 v48 U! B= v46 v49 U! B= v46 v54 U! B= v46 v55 U! B= v46 v56 U! B= v46 v64 U! B= v46 v65 U! B= v46 v66 U! B= v46 v76 U! B= v46 v86 U! B= v46 v96 U! B= v47 v48 U! B= v47 v49 U! B= v47 v57 U! B= v47 v58 U! B= v47 v59 U! B= v47 v67 U! B= v47 v68 U! B= v47 v69 U! B= v47 v77 U! B= v47 v87 U! B= v47 v97 U! B= v48 v49 U! B= v48 v57 U! B= v48 v58 U! B= v48 v59 U! B= v48 v67 U! B= v48 v68 U! B= v48 v69 U! B= v48 v78 U! B= v48 v88 U! B= v48 v98 U! B= v49 v57 U! B= v49 v58 U! B= v49 v59 U! B= v49 v67 U! B= v49 v68 U! B= v49 v69 U! B= v49 v79 U! B= v49 v89 U! B= v49 v99 U! B= v51 v52 U! B= v51 v53 U! B= v51 v54 U! B= v51 v55 U! B= v51 v56 U! B= v51 v57 U! B= v51 v58 U! B= v51 v59 U! B= v51 v61 U! B= v51 v62 U! B= v51 v63 U! B= v51 v71 U! B= v51 v81 U! B= v51 v91 U! B= v52 v53 U! B= v52 v54 U! B= v52 v55 U! B= v52 v56 U! B= v52 v57 U! B= v52 v58 U! B= v52 v59 U! B= v52 v61 U! B= v52 v62 U! B= v52 v63 U! B= v52 v72 U! B= v52 v82 U! B= v52 v92 U! B= v53 v54 U! B= v53 v55 U! B= v53 v56 U! B= v53 v57 U! B= v53 v58 U! B= v53 v59 U! B= v53 v61 U! B= v53 v62 U! B= v53 v63 U! B= v53 v73 U! B= v53 v83 U! B= v53 v93 U! B= v54 v55 U! B= v54 v56 U! B= v54 v57 U! B= v54 v58 U! B= v54 v59 U! B= v54 v64 U! B= v54 v65 U! B= v54 v66 U! B= v54 v74 U! B= v54 v84 U! B= v54 v94 U! B= v55 v56 U! B= v55 v57 U! B= v55 v58 U! B= v55 v59 U! B= v55 v64 U! B= v55 v65 U! B= v55 v66 U! B= v55 v75 U! B= v55 v85 U! B= v55 v95 U! B= v56 v57 U! B= v56 v58 U! B= v56 v59 U! B= v56 v64 U! B= v56 v65 U! B= v56 v66 U! B= v56 v76 U! B= v56 v86 U! B= v56 v96 U! B= v57 v58 U! B= v57 v59 U! B= v57 v67 U! B= v57 v68 U! B= v57 v69 U! B= v57 v77 U! B= v57 v87 U! B= v57 v97 U! B= v58 v59 U! B= v58 v67 U! B= v58 v68 U! B= v58 v69 U! B= v58 v78 U! B= v58 v88 U! B= v58 v98 U! B= v59 v67 U! B= v59 v68 U! B= v59 v69 U! B= v59 v79 U! B= v59 v89 U! B= v59 v99 U! B= v61 v62 U! B= v61 v63 U! B= v61 v64 U! B= v61 v65 U! B= v61 v66 U! B= v61 v67 U! B= v61 v68 U! B= v61 v69 U! B= v61 v71 U! B= v61 v81 U! B= v61 v91 U! B= v62 v63 U! B= v62 v64 U! B= v62 v65 U! B= v62 v66 U! B= v62 v67 U! B= v62 v68 U! B= v62 v69 U! B= v62 v72 U! B= v62 v82 U! B= v62 v92 U! B= v63 v64 U! B= v63 v65 U! B= v63 v66 U! B= v63 v67 U! B= v63 v68 U! B= v63 v69 U! B= v63 v73 U! B= v63 v83 U! B= v63 v93 U! B= v64 v65 U! B= v64 v66 U! B= v64 v67 U! B= v64 v68 U! B= v64 v69 U! B= v64 v74 U! B= v64 v84 U! B= v64 v94 U! B= v65 v66 U! B= v65 v67 U! B= v65 v68 U! B= v65 v69 U! B= v65 v75 U! B= v65 v85 U! B= v65 v95 U! B= v66 v67 U! B= v66 v68 U! B= v66 v69 U! B= v66 v76 U! B= v66 v86 U! B= v66 v96 U! B= v67 v68 U! B= v67 v69 U! B= v67 v77 U! B= v67 v87 U! B= v67 v97 U! B= v68 v69 U! B= v68 v78 U! B= v68 v88 U! B= v68 v98 U! B= v69 v79 U! B= v69 v89 U! B= v69 v99 U! B= v71 v72 U! B= v71 v73 U! B= v71 v74 U! B= v71 v75 U! B= v71 v76 U! B= v71 v77 U! B= v71 v78 U! B= v71 v79 U! B= v71 v81 U! B= v71 v82 U! B= v71 v83 U! B= v71 v91 U! B= v71 v92 U! B= v71 v93 U! B= v72 v73 U! B= v72 v74 U! B= v72 v75 U! B= v72 v76 U! B= v72 v77 U! B= v72 v78 U! B= v72 v79 U! B= v72 v81 U! B= v72 v82 U! B= v72 v83 U! B= v72 v91 U! B= v72 v92 U! B= v72 v93 U! B= v73 v74 U! B= v73 v75 U! B= v73 v76 U! B= v73 v77 U! B= v73 v78 U! B= v73 v79 U! B= v73 v81 U! B= v73 v82 U! B= v73 v83 U! B= v73 v91 U! B= v73 v92 U! B= v73 v93 U! B= v74 v75 U! B= v74 v76 U! B= v74 v77 U! B= v74 v78 U! B= v74 v79 U! B= v74 v84 U! B= v74 v85 U! B= v74 v86 U! B= v74 v94 U! B= v74 v95 U! B= v74 v96 U! B= v75 v76 U! B= v75 v77 U! B= v75 v78 U! B= v75 v79 U! B= v75 v84 U! B= v75 v85 U! B= v75 v86 U! B= v75 v94 U! B= v75 v95 U! B= v75 v96 U! B= v76 v77 U! B= v76 v78 U! B= v76 v79 U! B= v76 v84 U! B= v76 v85 U! B= v76 v86 U! B= v76 v94 U! B= v76 v95 U! B= v76 v96 U! B= v77 v78 U! B= v77 v79 U! B= v77 v87 U! B= v77 v88 U! B= v77 v89 U! B= v77 v97 U! B= v77 v98 U! B= v77 v99 U! B= v78 v79 U! B= v78 v87 U! B= v78 v88 U! B= v78 v89 U! B= v78 v97 U! B= v78 v98 U! B= v78 v99 U! B= v79 v87 U! B= v79 v88 U! B= v79 v89 U! B= v79 v97 U! B= v79 v98 U! B= v79 v99 U! B= v81 v82 U! B= v81 v83 U! B= v81 v84 U! B= v81 v85 U! B= v81 v86 U! B= v81 v87 U! B= v81 v88 U! B= v81 v89 U! B= v81 v91 U! B= v81 v92 U! B= v81 v93 U! B= v82 v83 U! B= v82 v84 U! B= v82 v85 U! B= v82 v86 U! B= v82 v87 U! B= v82 v88 U! B= v82 v89 U! B= v82 v91 U! B= v82 v92 U! B= v82 v93 U! B= v83 v84 U! B= v83 v85 U! B= v83 v86 U! B= v83 v87 U! B= v83 v88 U! B= v83 v89 U! B= v83 v91 U! B= v83 v92 U! B= v83 v93 U! B= v84 v85 U! B= v84 v86 U! B= v84 v87 U! B= v84 v88 U! B= v84 v89 U! B= v84 v94 U! B= v84 v95 U! B= v84 v96 U! B= v85 v86 U! B= v85 v87 U! B= v85 v88 U! B= v85 v89 U! B= v85 v94 U! B= v85 v95 U! B= v85 v96 U! B= v86 v87 U! B= v86 v88 U! B= v86 v89 U! B= v86 v94 U! B= v86 v95 U! B= v86 v96 U! B= v87 v88 U! B= v87 v89 U! B= v87 v97 U! B= v87 v98 U! B= v87 v99 U! B= v88 v89 U! B= v88 v97 U! B= v88 v98 U! B= v88 v99 U! B= v89 v97 U! B= v89 v98 U! B= v89 v99 U! B= v91 v92 U! B= v91 v93 U! B= v91 v94 U! B= v91 v95 U! B= v91 v96 U! B= v91 v97 U! B= v91 v98 U! B= v91 v99 U! B= v92 v93 U! B= v92 v94 U! B= v92 v95 U! B= v92 v96 U! B= v92 v97 U! B= v92 v98 U! B= v92 v99 U! B= v93 v94 U! B= v93 v95 U! B= v93 v96 U! B= v93 v97 U! B= v93 v98 U! B= v93 v99 U! B= v94 v95 U! B= v94 v96 U! B= v94 v97 U! B= v94 v98 U! B= v94 v99 U! B= v95 v96 U! B= v95 v97 U! B= v95 v98 U! B= v95 v99 U! B= v96 v97 U! B= v96 v98 U! B= v96 v99 U! B= v97 v98 U! B= v97 v99 U! B= v98 v99
# fixed digits
B= v17 I(6) B= v18 I(8) B= v25 I(7) B= v26 I(3) B= v29 I(9) B= v31 I(3) B= v33 I(9) B= v38 I(4) B= v39 I(5) B= v41 I(4) B= v42 I(9) B= v51 I(8) B= v53 I(3) B= v55 I(5) B= v57 I(9) B= v59 I(2) B= v68 I(3) B= v69 I(6) B= v71 I(9) B= v72 I(6) B= v77 I(3) B= v79 I(8) B= v81 I(7) B= v84 I(6) B= v85 I(8) B= v92 I(2) B= v93 I(8)
# return x
v1
# return f(x+1)
B$ v2 B+ v1 I(1)
# digit decomposition
B+ I(1) B% B/ v1 I(1) I(9) B+ I(1) B% B/ v1 I(9) I(9) B+ I(1) B% B/ v1 I(81) I(9) B+ I(1) B% B/ v1 I(729) I(9) B+ I(1) B% B/ v1 I(6561) I(9) B+ I(1) B% B/ v1 I(59049) I(9) B+ I(1) B% B/ v1 I(531441) I(9) B+ I(1) B% B/ v1 I(4782969) I(9) B+ I(1) B% B/ v1 I(43046721) I(9) B+ I(1) B% B/ v1 I(387420489) I(9) B+ I(1) B% B/ v1 I(3486784401) I(9) B+ I(1) B% B/ v1 I(31381059609) I(9) B+ I(1) B% B/ v1 I(282429536481) I(9) B+ I(1) B% B/ v1 I(2541865828329) I(9) B+ I(1) B% B/ v1 I(22876792454961) I(9) B+ I(1) B% B/ v1 I(205891132094649) I(9) B+ I(1) B% B/ v1 I(1853020188851841) I(9) B+ I(1) B% B/ v1 I(16677181699666569) I(9) B+ I(1) B% B/ v1 I(150094635296999121) I(9) B+ I(1) B% B/ v1 I(1350851717672992089) I(9) B+ I(1) B% B/ v1 I(12157665459056928801) I(9) B+ I(1) B% B/ v1 I(109418989131512359209) I(9) B+ I(1) B% B/ v1 I(984770902183611232881) I(9) B+ I(1) B% B/ v1 I(8862938119652501095929) I(9) B+ I(1) B% B/ v1 I(79766443076872509863361) I(9) B+ I(1) B% B/ v1 I(717897987691852588770249) I(9) B+ I(1) B% B/ v1 I(6461081889226673298932241) I(9) B+ I(1) B% B/ v1 I(58149737003040059690390169) I(9) B+ I(1) B% B/ v1 I(523347633027360537213511521) I(9) B+ I(1) B% B/ v1 I(4710128697246244834921603689) I(9) B+ I(1) B% B/ v1 I(42391158275216203514294433201) I(9) B+ I(1) B% B/ v1 I(381520424476945831628649898809) I(9) B+ I(1) B% B/ v1 I(3433683820292512484657849089281) I(9) B+ I(1) B% B/ v1 I(30903154382632612361920641803529) I(9) B+ I(1) B% B/ v1 I(278128389443693511257285776231761) I(9) B+ I(1) B% B/ v1 I(2503155504993241601315571986085849) I(9) B+ I(1) B% B/ v1 I(22528399544939174411840147874772641) I(9) B+ I(1) B% B/ v1 I(202755595904452569706561330872953769) I(9) B+ I(1) B% B/ v1 I(1824800363140073127359051977856583921) I(9) B+ I(1) B% B/ v1 I(16423203268260658146231467800709255289) I(9) B+ I(1) B% B/ v1 I(147808829414345923316083210206383297601) I(9) B+ I(1) B% B/ v1 I(1330279464729113309844748891857449678409) I(9) B+ I(1) B% B/ v1 I(11972515182562019788602740026717047105681) I(9) B+ I(1) B% B/ v1 I(107752636643058178097424660240453423951129) I(9) B+ I(1) B% B/ v1 I(969773729787523602876821942164080815560161) I(9) B+ I(1) B% B/ v1 I(8727963568087712425891397479476727340041449) I(9) B+ I(1) B% B/ v1 I(78551672112789411833022577315290546060373041) I(9) B+ I(1) B% B/ v1 I(706965049015104706497203195837614914543357369) I(9) B+ I(1) B% B/ v1 I(6362685441135942358474828762538534230890216321) I(9) B+ I(1) B% B/ v1 I(57264168970223481226273458862846808078011946889) I(9) B+ I(1) B% B/ v1 I(515377520732011331036461129765621272702107522001) I(9) B+ I(1) B% B/ v1 I(4638397686588101979328150167890591454318967698009) I(9) B+ I(1) B% B/ v1 I(41745579179292917813953351511015323088870709282081) I(9) B+ I(1) B% B/ v1 I(375710212613636260325580163599137907799836383538729) I(9) B+ I(1) B% B/ v1 I(3381391913522726342930221472392241170198527451848561) I(9) B+ I(1) B% B/ v1 I(30432527221704537086371993251530170531786747066637049) I(9) B+ I(1) B% B/ v1 I(273892744995340833777347939263771534786080723599733441) I(9) B+ I(1) B% B/ v1 I(2465034704958067503996131453373943813074726512397600969) I(9) B+ I(1) B% B/ v1 I(22185312344622607535965183080365494317672538611578408721) I(9) B+ I(1) B% B/ v1 I(199667811101603467823686647723289448859052847504205678489) I(9) B+ I(1) B% B/ v1 I(1797010299914431210413179829509605039731475627537851106401) I(9) B+ I(1) B% B/ v1 I(16173092699229880893718618465586445357583280647840659957609) I(9) B+ I(1) B% B/ v1 I(145557834293068928043467566190278008218249525830565939618481) I(9) B+ I(1) B% B/ v1 I(1310020508637620352391208095712502073964245732475093456566329) I(9) B+ I(1) B% B/ v1 I(11790184577738583171520872861412518665678211592275841109096961) I(9) B+ I(1) B% B/ v1 I(106111661199647248543687855752712667991103904330482569981872649) I(9) B+ I(1) B% B/ v1 I(955004950796825236893190701774414011919935138974343129836853841) I(9) B+ I(1) B% B/ v1 I(8595044557171427132038716315969726107279416250769088168531684569) I(9) B+ I(1) B% B/ v1 I(77355401014542844188348446843727534965514746256921793516785161121) I(9) B+ I(1) B% B/ v1 I(696198609130885597695136021593547814689632716312296141651066450089) I(9) B+ I(1) B% B/ v1 I(6265787482177970379256224194341930332206694446810665274859598050801) I(9) B+ I(1) B% B/ v1 I(56392087339601733413306017749077372989860250021295987473736382457209) I(9) B+ I(1) B% B/ v1 I(507528786056415600719754159741696356908742250191663887263627442114881) I(9) B+ I(1) B% B/ v1 I(4567759074507740406477787437675267212178680251724974985372646979033929) I(9) B+ I(1) B% B/ v1 I(41109831670569663658300086939077404909608122265524774868353822811305361) I(9) B+ I(1) B% B/ v1 I(369988485035126972924700782451696644186473100389722973815184405301748249) I(9) B+ I(1) B% B/ v1 I(3329896365316142756322307042065269797678257903507506764336659647715734241) I(9) B+ I(1) B% B/ v1 I(29969067287845284806900763378587428179104321131567560879029936829441608169) I(9) B+ I(1) B% B/ v1 I(269721605590607563262106870407286853611938890184108047911269431464974473521) I(9) B+ I(1) B% B/ v1 I(2427494450315468069358961833665581682507450011656972431201424883184770261689) I(9) B+ I(1) B% B/ v1 I(21847450052839212624230656502990235142567050104912751880812823948662932355201) I(9) I(1)
'''
eff10 = [Str("solve efficiency10 14967753016278151754281739121556345272360285170537031718346799308781591772932")]


# problem 11
# another sudoku??
'''
B$ B$ y L2 L1
B$ L11 B$ L12 B$ L13 B$ L14 B$ L15 B$ L16 B$ L17 B$ L18 B$ L19 B$ L21 B$ L22 B$ L23 B$ L24 B$ L25 B$ L26 B$ L27 B$ L28 B$ L29 B$ L31 B$ L32 B$ L33 B$ L34 B$ L35 B$ L36 B$ L37 B$ L38 B$ L39 B$ L41 B$ L42 B$ L43 B$ L44 B$ L45 B$ L46 B$ L47 B$ L48 B$ L49 B$ L51 B$ L52 B$ L53 B$ L54 B$ L55 B$ L56 B$ L57 B$ L58 B$ L59 B$ L61 B$ L62 B$ L63 B$ L64 B$ L65 B$ L66 B$ L67 B$ L68 B$ L69 B$ L71 B$ L72 B$ L73 B$ L74 B$ L75 B$ L76 B$ L77 B$ L78 B$ L79 B$ L81 B$ L82 B$ L83 B$ L84 B$ L85 B$ L86 B$ L87 B$ L88 B$ L89 B$ L91 B$ L92 B$ L93 B$ L94 B$ L95 B$ L96 B$ L97 B$ L98 B$ L99
? B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B& B&
U! B= v11 v12 U! B= v11 v13 U! B= v11 v14 U! B= v11 v15 U! B= v11 v16 U! B= v11 v17 U! B= v11 v18 U! B= v11 v19 U! B= v11 v21 U! B= v11 v22 U! B= v11 v23 U! B= v11 v31 U! B= v11 v32 U! B= v11 v33 U! B= v11 v41 U! B= v11 v51 U! B= v11 v61 U! B= v11 v71 U! B= v11 v81 U! B= v11 v91 U! B= v12 v13 U! B= v12 v14 U! B= v12 v15 U! B= v12 v16 U! B= v12 v17 U! B= v12 v18 U! B= v12 v19 U! B= v12 v21 U! B= v12 v22 U! B= v12 v23 U! B= v12 v31 U! B= v12 v32 U! B= v12 v33 U! B= v12 v42 U! B= v12 v52 U! B= v12 v62 U! B= v12 v72 U! B= v12 v82 U! B= v12 v92 U! B= v13 v14 U! B= v13 v15 U! B= v13 v16 U! B= v13 v17 U! B= v13 v18 U! B= v13 v19 U! B= v13 v21 U! B= v13 v22 U! B= v13 v23 U! B= v13 v31 U! B= v13 v32 U! B= v13 v33 U! B= v13 v43 U! B= v13 v53 U! B= v13 v63 U! B= v13 v73 U! B= v13 v83 U! B= v13 v93 U! B= v14 v15 U! B= v14 v16 U! B= v14 v17 U! B= v14 v18 U! B= v14 v19 U! B= v14 v24 U! B= v14 v25 U! B= v14 v26 U! B= v14 v34 U! B= v14 v35 U! B= v14 v36 U! B= v14 v44 U! B= v14 v54 U! B= v14 v64 U! B= v14 v74 U! B= v14 v84 U! B= v14 v94 U! B= v15 v16 U! B= v15 v17 U! B= v15 v18 U! B= v15 v19 U! B= v15 v24 U! B= v15 v25 U! B= v15 v26 U! B= v15 v34 U! B= v15 v35 U! B= v15 v36 U! B= v15 v45 U! B= v15 v55 U! B= v15 v65 U! B= v15 v75 U! B= v15 v85 U! B= v15 v95 U! B= v16 v17 U! B= v16 v18 U! B= v16 v19 U! B= v16 v24 U! B= v16 v25 U! B= v16 v26 U! B= v16 v34 U! B= v16 v35 U! B= v16 v36 U! B= v16 v46 U! B= v16 v56 U! B= v16 v66 U! B= v16 v76 U! B= v16 v86 U! B= v16 v96 U! B= v17 v18 U! B= v17 v19 U! B= v17 v27 U! B= v17 v28 U! B= v17 v29 U! B= v17 v37 U! B= v17 v38 U! B= v17 v39 U! B= v17 v47 U! B= v17 v57 U! B= v17 v67 U! B= v17 v77 U! B= v17 v87 U! B= v17 v97 U! B= v18 v19 U! B= v18 v27 U! B= v18 v28 U! B= v18 v29 U! B= v18 v37 U! B= v18 v38 U! B= v18 v39 U! B= v18 v48 U! B= v18 v58 U! B= v18 v68 U! B= v18 v78 U! B= v18 v88 U! B= v18 v98 U! B= v19 v27 U! B= v19 v28 U! B= v19 v29 U! B= v19 v37 U! B= v19 v38 U! B= v19 v39 U! B= v19 v49 U! B= v19 v59 U! B= v19 v69 U! B= v19 v79 U! B= v19 v89 U! B= v19 v99 U! B= v21 v22 U! B= v21 v23 U! B= v21 v24 U! B= v21 v25 U! B= v21 v26 U! B= v21 v27 U! B= v21 v28 U! B= v21 v29 U! B= v21 v31 U! B= v21 v32 U! B= v21 v33 U! B= v21 v41 U! B= v21 v51 U! B= v21 v61 U! B= v21 v71 U! B= v21 v81 U! B= v21 v91 U! B= v22 v23 U! B= v22 v24 U! B= v22 v25 U! B= v22 v26 U! B= v22 v27 U! B= v22 v28 U! B= v22 v29 U! B= v22 v31 U! B= v22 v32 U! B= v22 v33 U! B= v22 v42 U! B= v22 v52 U! B= v22 v62 U! B= v22 v72 U! B= v22 v82 U! B= v22 v92 U! B= v23 v24 U! B= v23 v25 U! B= v23 v26 U! B= v23 v27 U! B= v23 v28 U! B= v23 v29 U! B= v23 v31 U! B= v23 v32 U! B= v23 v33 U! B= v23 v43 U! B= v23 v53 U! B= v23 v63 U! B= v23 v73 U! B= v23 v83 U! B= v23 v93 U! B= v24 v25 U! B= v24 v26 U! B= v24 v27 U! B= v24 v28 U! B= v24 v29 U! B= v24 v34 U! B= v24 v35 U! B= v24 v36 U! B= v24 v44 U! B= v24 v54 U! B= v24 v64 U! B= v24 v74 U! B= v24 v84 U! B= v24 v94 U! B= v25 v26 U! B= v25 v27 U! B= v25 v28 U! B= v25 v29 U! B= v25 v34 U! B= v25 v35 U! B= v25 v36 U! B= v25 v45 U! B= v25 v55 U! B= v25 v65 U! B= v25 v75 U! B= v25 v85 U! B= v25 v95 U! B= v26 v27 U! B= v26 v28 U! B= v26 v29 U! B= v26 v34 U! B= v26 v35 U! B= v26 v36 U! B= v26 v46 U! B= v26 v56 U! B= v26 v66 U! B= v26 v76 U! B= v26 v86 U! B= v26 v96 U! B= v27 v28 U! B= v27 v29 U! B= v27 v37 U! B= v27 v38 U! B= v27 v39 U! B= v27 v47 U! B= v27 v57 U! B= v27 v67 U! B= v27 v77 U! B= v27 v87 U! B= v27 v97 U! B= v28 v29 U! B= v28 v37 U! B= v28 v38 U! B= v28 v39 U! B= v28 v48 U! B= v28 v58 U! B= v28 v68 U! B= v28 v78 U! B= v28 v88 U! B= v28 v98 U! B= v29 v37 U! B= v29 v38 U! B= v29 v39 U! B= v29 v49 U! B= v29 v59 U! B= v29 v69 U! B= v29 v79 U! B= v29 v89 U! B= v29 v99 U! B= v31 v32 U! B= v31 v33 U! B= v31 v34 U! B= v31 v35 U! B= v31 v36 U! B= v31 v37 U! B= v31 v38 U! B= v31 v39 U! B= v31 v41 U! B= v31 v51 U! B= v31 v61 U! B= v31 v71 U! B= v31 v81 U! B= v31 v91 U! B= v32 v33 U! B= v32 v34 U! B= v32 v35 U! B= v32 v36 U! B= v32 v37 U! B= v32 v38 U! B= v32 v39 U! B= v32 v42 U! B= v32 v52 U! B= v32 v62 U! B= v32 v72 U! B= v32 v82 U! B= v32 v92 U! B= v33 v34 U! B= v33 v35 U! B= v33 v36 U! B= v33 v37 U! B= v33 v38 U! B= v33 v39 U! B= v33 v43 U! B= v33 v53 U! B= v33 v63 U! B= v33 v73 U! B= v33 v83 U! B= v33 v93 U! B= v34 v35 U! B= v34 v36 U! B= v34 v37 U! B= v34 v38 U! B= v34 v39 U! B= v34 v44 U! B= v34 v54 U! B= v34 v64 U! B= v34 v74 U! B= v34 v84 U! B= v34 v94 U! B= v35 v36 U! B= v35 v37 U! B= v35 v38 U! B= v35 v39 U! B= v35 v45 U! B= v35 v55 U! B= v35 v65 U! B= v35 v75 U! B= v35 v85 U! B= v35 v95 U! B= v36 v37 U! B= v36 v38 U! B= v36 v39 U! B= v36 v46 U! B= v36 v56 U! B= v36 v66 U! B= v36 v76 U! B= v36 v86 U! B= v36 v96 U! B= v37 v38 U! B= v37 v39 U! B= v37 v47 U! B= v37 v57 U! B= v37 v67 U! B= v37 v77 U! B= v37 v87 U! B= v37 v97 U! B= v38 v39 U! B= v38 v48 U! B= v38 v58 U! B= v38 v68 U! B= v38 v78 U! B= v38 v88 U! B= v38 v98 U! B= v39 v49 U! B= v39 v59 U! B= v39 v69 U! B= v39 v79 U! B= v39 v89 U! B= v39 v99 U! B= v41 v42 U! B= v41 v43 U! B= v41 v44 U! B= v41 v45 U! B= v41 v46 U! B= v41 v47 U! B= v41 v48 U! B= v41 v49 U! B= v41 v51 U! B= v41 v52 U! B= v41 v53 U! B= v41 v61 U! B= v41 v62 U! B= v41 v63 U! B= v41 v71 U! B= v41 v81 U! B= v41 v91 U! B= v42 v43 U! B= v42 v44 U! B= v42 v45 U! B= v42 v46 U! B= v42 v47 U! B= v42 v48 U! B= v42 v49 U! B= v42 v51 U! B= v42 v52 U! B= v42 v53 U! B= v42 v61 U! B= v42 v62 U! B= v42 v63 U! B= v42 v72 U! B= v42 v82 U! B= v42 v92 U! B= v43 v44 U! B= v43 v45 U! B= v43 v46 U! B= v43 v47 U! B= v43 v48 U! B= v43 v49 U! B= v43 v51 U! B= v43 v52 U! B= v43 v53 U! B= v43 v61 U! B= v43 v62 U! B= v43 v63 U! B= v43 v73 U! B= v43 v83 U! B= v43 v93 U! B= v44 v45 U! B= v44 v46 U! B= v44 v47 U! B= v44 v48 U! B= v44 v49 U! B= v44 v54 U! B= v44 v55 U! B= v44 v56 U! B= v44 v64 U! B= v44 v65 U! B= v44 v66 U! B= v44 v74 U! B= v44 v84 U! B= v44 v94 U! B= v45 v46 U! B= v45 v47 U! B= v45 v48 U! B= v45 v49 U! B= v45 v54 U! B= v45 v55 U! B= v45 v56 U! B= v45 v64 U! B= v45 v65 U! B= v45 v66 U! B= v45 v75 U! B= v45 v85 U! B= v45 v95 U! B= v46 v47 U! B= v46 v48 U! B= v46 v49 U! B= v46 v54 U! B= v46 v55 U! B= v46 v56 U! B= v46 v64 U! B= v46 v65 U! B= v46 v66 U! B= v46 v76 U! B= v46 v86 U! B= v46 v96 U! B= v47 v48 U! B= v47 v49 U! B= v47 v57 U! B= v47 v58 U! B= v47 v59 U! B= v47 v67 U! B= v47 v68 U! B= v47 v69 U! B= v47 v77 U! B= v47 v87 U! B= v47 v97 U! B= v48 v49 U! B= v48 v57 U! B= v48 v58 U! B= v48 v59 U! B= v48 v67 U! B= v48 v68 U! B= v48 v69 U! B= v48 v78 U! B= v48 v88 U! B= v48 v98 U! B= v49 v57 U! B= v49 v58 U! B= v49 v59 U! B= v49 v67 U! B= v49 v68 U! B= v49 v69 U! B= v49 v79 U! B= v49 v89 U! B= v49 v99 U! B= v51 v52 U! B= v51 v53 U! B= v51 v54 U! B= v51 v55 U! B= v51 v56 U! B= v51 v57 U! B= v51 v58 U! B= v51 v59 U! B= v51 v61 U! B= v51 v62 U! B= v51 v63 U! B= v51 v71 U! B= v51 v81 U! B= v51 v91 U! B= v52 v53 U! B= v52 v54 U! B= v52 v55 U! B= v52 v56 U! B= v52 v57 U! B= v52 v58 U! B= v52 v59 U! B= v52 v61 U! B= v52 v62 U! B= v52 v63 U! B= v52 v72 U! B= v52 v82 U! B= v52 v92 U! B= v53 v54 U! B= v53 v55 U! B= v53 v56 U! B= v53 v57 U! B= v53 v58 U! B= v53 v59 U! B= v53 v61 U! B= v53 v62 U! B= v53 v63 U! B= v53 v73 U! B= v53 v83 U! B= v53 v93 U! B= v54 v55 U! B= v54 v56 U! B= v54 v57 U! B= v54 v58 U! B= v54 v59 U! B= v54 v64 U! B= v54 v65 U! B= v54 v66 U! B= v54 v74 U! B= v54 v84 U! B= v54 v94 U! B= v55 v56 U! B= v55 v57 U! B= v55 v58 U! B= v55 v59 U! B= v55 v64 U! B= v55 v65 U! B= v55 v66 U! B= v55 v75 U! B= v55 v85 U! B= v55 v95 U! B= v56 v57 U! B= v56 v58 U! B= v56 v59 U! B= v56 v64 U! B= v56 v65 U! B= v56 v66 U! B= v56 v76 U! B= v56 v86 U! B= v56 v96 U! B= v57 v58 U! B= v57 v59 U! B= v57 v67 U! B= v57 v68 U! B= v57 v69 U! B= v57 v77 U! B= v57 v87 U! B= v57 v97 U! B= v58 v59 U! B= v58 v67 U! B= v58 v68 U! B= v58 v69 U! B= v58 v78 U! B= v58 v88 U! B= v58 v98 U! B= v59 v67 U! B= v59 v68 U! B= v59 v69 U! B= v59 v79 U! B= v59 v89 U! B= v59 v99 U! B= v61 v62 U! B= v61 v63 U! B= v61 v64 U! B= v61 v65 U! B= v61 v66 U! B= v61 v67 U! B= v61 v68 U! B= v61 v69 U! B= v61 v71 U! B= v61 v81 U! B= v61 v91 U! B= v62 v63 U! B= v62 v64 U! B= v62 v65 U! B= v62 v66 U! B= v62 v67 U! B= v62 v68 U! B= v62 v69 U! B= v62 v72 U! B= v62 v82 U! B= v62 v92 U! B= v63 v64 U! B= v63 v65 U! B= v63 v66 U! B= v63 v67 U! B= v63 v68 U! B= v63 v69 U! B= v63 v73 U! B= v63 v83 U! B= v63 v93 U! B= v64 v65 U! B= v64 v66 U! B= v64 v67 U! B= v64 v68 U! B= v64 v69 U! B= v64 v74 U! B= v64 v84 U! B= v64 v94 U! B= v65 v66 U! B= v65 v67 U! B= v65 v68 U! B= v65 v69 U! B= v65 v75 U! B= v65 v85 U! B= v65 v95 U! B= v66 v67 U! B= v66 v68 U! B= v66 v69 U! B= v66 v76 U! B= v66 v86 U! B= v66 v96 U! B= v67 v68 U! B= v67 v69 U! B= v67 v77 U! B= v67 v87 U! B= v67 v97 U! B= v68 v69 U! B= v68 v78 U! B= v68 v88 U! B= v68 v98 U! B= v69 v79 U! B= v69 v89 U! B= v69 v99 U! B= v71 v72 U! B= v71 v73 U! B= v71 v74 U! B= v71 v75 U! B= v71 v76 U! B= v71 v77 U! B= v71 v78 U! B= v71 v79 U! B= v71 v81 U! B= v71 v82 U! B= v71 v83 U! B= v71 v91 U! B= v71 v92 U! B= v71 v93 U! B= v72 v73 U! B= v72 v74 U! B= v72 v75 U! B= v72 v76 U! B= v72 v77 U! B= v72 v78 U! B= v72 v79 U! B= v72 v81 U! B= v72 v82 U! B= v72 v83 U! B= v72 v91 U! B= v72 v92 U! B= v72 v93 U! B= v73 v74 U! B= v73 v75 U! B= v73 v76 U! B= v73 v77 U! B= v73 v78 U! B= v73 v79 U! B= v73 v81 U! B= v73 v82 U! B= v73 v83 U! B= v73 v91 U! B= v73 v92 U! B= v73 v93 U! B= v74 v75 U! B= v74 v76 U! B= v74 v77 U! B= v74 v78 U! B= v74 v79 U! B= v74 v84 U! B= v74 v85 U! B= v74 v86 U! B= v74 v94 U! B= v74 v95 U! B= v74 v96 U! B= v75 v76 U! B= v75 v77 U! B= v75 v78 U! B= v75 v79 U! B= v75 v84 U! B= v75 v85 U! B= v75 v86 U! B= v75 v94 U! B= v75 v95 U! B= v75 v96 U! B= v76 v77 U! B= v76 v78 U! B= v76 v79 U! B= v76 v84 U! B= v76 v85 U! B= v76 v86 U! B= v76 v94 U! B= v76 v95 U! B= v76 v96 U! B= v77 v78 U! B= v77 v79 U! B= v77 v87 U! B= v77 v88 U! B= v77 v89 U! B= v77 v97 U! B= v77 v98 U! B= v77 v99 U! B= v78 v79 U! B= v78 v87 U! B= v78 v88 U! B= v78 v89 U! B= v78 v97 U! B= v78 v98 U! B= v78 v99 U! B= v79 v87 U! B= v79 v88 U! B= v79 v89 U! B= v79 v97 U! B= v79 v98 U! B= v79 v99 U! B= v81 v82 U! B= v81 v83 U! B= v81 v84 U! B= v81 v85 U! B= v81 v86 U! B= v81 v87 U! B= v81 v88 U! B= v81 v89 U! B= v81 v91 U! B= v81 v92 U! B= v81 v93 U! B= v82 v83 U! B= v82 v84 U! B= v82 v85 U! B= v82 v86 U! B= v82 v87 U! B= v82 v88 U! B= v82 v89 U! B= v82 v91 U! B= v82 v92 U! B= v82 v93 U! B= v83 v84 U! B= v83 v85 U! B= v83 v86 U! B= v83 v87 U! B= v83 v88 U! B= v83 v89 U! B= v83 v91 U! B= v83 v92 U! B= v83 v93 U! B= v84 v85 U! B= v84 v86 U! B= v84 v87 U! B= v84 v88 U! B= v84 v89 U! B= v84 v94 U! B= v84 v95 U! B= v84 v96 U! B= v85 v86 U! B= v85 v87 U! B= v85 v88 U! B= v85 v89 U! B= v85 v94 U! B= v85 v95 U! B= v85 v96 U! B= v86 v87 U! B= v86 v88 U! B= v86 v89 U! B= v86 v94 U! B= v86 v95 U! B= v86 v96 U! B= v87 v88 U! B= v87 v89 U! B= v87 v97 U! B= v87 v98 U! B= v87 v99 U! B= v88 v89 U! B= v88 v97 U! B= v88 v98 U! B= v88 v99 U! B= v89 v97 U! B= v89 v98 U! B= v89 v99 U! B= v91 v92 U! B= v91 v93 U! B= v91 v94 U! B= v91 v95 U! B= v91 v96 U! B= v91 v97 U! B= v91 v98 U! B= v91 v99 U! B= v92 v93 U! B= v92 v94 U! B= v92 v95 U! B= v92 v96 U! B= v92 v97 U! B= v92 v98 U! B= v92 v99 U! B= v93 v94 U! B= v93 v95 U! B= v93 v96 U! B= v93 v97 U! B= v93 v98 U! B= v93 v99 U! B= v94 v95 U! B= v94 v96 U! B= v94 v97 U! B= v94 v98 U! B= v94 v99 U! B= v95 v96 U! B= v95 v97 U! B= v95 v98 U! B= v95 v99 U! B= v96 v97 U! B= v96 v98 U! B= v96 v99 U! B= v97 v98 U! B= v97 v99 U! B= v98 v99
# filled squares
B= v12 I(6) B= v13 I(4) B= v17 I(7) B= v25 I(2) B= v28 I(3) B= v29 I(6) B= v33 I(1) B= v41 I(2) B= v42 I(3) B= v45 I(8) B= v54 I(7) B= v57 I(1) B= v59 I(4) B= v71 I(9) B= v81 I(8) B= v88 I(2) B= v94 I(4)
# return x
v1
# return f(x+1)
B$ v2 B+ v1 I(1)
# decompose into digits
B+ I(1) B% B/ v1 I(1) I(9) B+ I(1) B% B/ v1 I(9) I(9) B+ I(1) B% B/ v1 I(81) I(9) B+ I(1) B% B/ v1 I(729) I(9) B+ I(1) B% B/ v1 I(6561) I(9) B+ I(1) B% B/ v1 I(59049) I(9) B+ I(1) B% B/ v1 I(531441) I(9) B+ I(1) B% B/ v1 I(4782969) I(9) B+ I(1) B% B/ v1 I(43046721) I(9) B+ I(1) B% B/ v1 I(387420489) I(9) B+ I(1) B% B/ v1 I(3486784401) I(9) B+ I(1) B% B/ v1 I(31381059609) I(9) B+ I(1) B% B/ v1 I(282429536481) I(9) B+ I(1) B% B/ v1 I(2541865828329) I(9) B+ I(1) B% B/ v1 I(22876792454961) I(9) B+ I(1) B% B/ v1 I(205891132094649) I(9) B+ I(1) B% B/ v1 I(1853020188851841) I(9) B+ I(1) B% B/ v1 I(16677181699666569) I(9) B+ I(1) B% B/ v1 I(150094635296999121) I(9) B+ I(1) B% B/ v1 I(1350851717672992089) I(9) B+ I(1) B% B/ v1 I(12157665459056928801) I(9) B+ I(1) B% B/ v1 I(109418989131512359209) I(9) B+ I(1) B% B/ v1 I(984770902183611232881) I(9) B+ I(1) B% B/ v1 I(8862938119652501095929) I(9) B+ I(1) B% B/ v1 I(79766443076872509863361) I(9) B+ I(1) B% B/ v1 I(717897987691852588770249) I(9) B+ I(1) B% B/ v1 I(6461081889226673298932241) I(9) B+ I(1) B% B/ v1 I(58149737003040059690390169) I(9) B+ I(1) B% B/ v1 I(523347633027360537213511521) I(9) B+ I(1) B% B/ v1 I(4710128697246244834921603689) I(9) B+ I(1) B% B/ v1 I(42391158275216203514294433201) I(9) B+ I(1) B% B/ v1 I(381520424476945831628649898809) I(9) B+ I(1) B% B/ v1 I(3433683820292512484657849089281) I(9) B+ I(1) B% B/ v1 I(30903154382632612361920641803529) I(9) B+ I(1) B% B/ v1 I(278128389443693511257285776231761) I(9) B+ I(1) B% B/ v1 I(2503155504993241601315571986085849) I(9) B+ I(1) B% B/ v1 I(22528399544939174411840147874772641) I(9) B+ I(1) B% B/ v1 I(202755595904452569706561330872953769) I(9) B+ I(1) B% B/ v1 I(1824800363140073127359051977856583921) I(9) B+ I(1) B% B/ v1 I(16423203268260658146231467800709255289) I(9) B+ I(1) B% B/ v1 I(147808829414345923316083210206383297601) I(9) B+ I(1) B% B/ v1 I(1330279464729113309844748891857449678409) I(9) B+ I(1) B% B/ v1 I(11972515182562019788602740026717047105681) I(9) B+ I(1) B% B/ v1 I(107752636643058178097424660240453423951129) I(9) B+ I(1) B% B/ v1 I(969773729787523602876821942164080815560161) I(9) B+ I(1) B% B/ v1 I(8727963568087712425891397479476727340041449) I(9) B+ I(1) B% B/ v1 I(78551672112789411833022577315290546060373041) I(9) B+ I(1) B% B/ v1 I(706965049015104706497203195837614914543357369) I(9) B+ I(1) B% B/ v1 I(6362685441135942358474828762538534230890216321) I(9) B+ I(1) B% B/ v1 I(57264168970223481226273458862846808078011946889) I(9) B+ I(1) B% B/ v1 I(515377520732011331036461129765621272702107522001) I(9) B+ I(1) B% B/ v1 I(4638397686588101979328150167890591454318967698009) I(9) B+ I(1) B% B/ v1 I(41745579179292917813953351511015323088870709282081) I(9) B+ I(1) B% B/ v1 I(375710212613636260325580163599137907799836383538729) I(9) B+ I(1) B% B/ v1 I(3381391913522726342930221472392241170198527451848561) I(9) B+ I(1) B% B/ v1 I(30432527221704537086371993251530170531786747066637049) I(9) B+ I(1) B% B/ v1 I(273892744995340833777347939263771534786080723599733441) I(9) B+ I(1) B% B/ v1 I(2465034704958067503996131453373943813074726512397600969) I(9) B+ I(1) B% B/ v1 I(22185312344622607535965183080365494317672538611578408721) I(9) B+ I(1) B% B/ v1 I(199667811101603467823686647723289448859052847504205678489) I(9) B+ I(1) B% B/ v1 I(1797010299914431210413179829509605039731475627537851106401) I(9) B+ I(1) B% B/ v1 I(16173092699229880893718618465586445357583280647840659957609) I(9) B+ I(1) B% B/ v1 I(145557834293068928043467566190278008218249525830565939618481) I(9) B+ I(1) B% B/ v1 I(1310020508637620352391208095712502073964245732475093456566329) I(9) B+ I(1) B% B/ v1 I(11790184577738583171520872861412518665678211592275841109096961) I(9) B+ I(1) B% B/ v1 I(106111661199647248543687855752712667991103904330482569981872649) I(9) B+ I(1) B% B/ v1 I(955004950796825236893190701774414011919935138974343129836853841) I(9) B+ I(1) B% B/ v1 I(8595044557171427132038716315969726107279416250769088168531684569) I(9) B+ I(1) B% B/ v1 I(77355401014542844188348446843727534965514746256921793516785161121) I(9) B+ I(1) B% B/ v1 I(696198609130885597695136021593547814689632716312296141651066450089) I(9) B+ I(1) B% B/ v1 I(6265787482177970379256224194341930332206694446810665274859598050801) I(9) B+ I(1) B% B/ v1 I(56392087339601733413306017749077372989860250021295987473736382457209) I(9) B+ I(1) B% B/ v1 I(507528786056415600719754159741696356908742250191663887263627442114881) I(9) B+ I(1) B% B/ v1 I(4567759074507740406477787437675267212178680251724974985372646979033929) I(9) B+ I(1) B% B/ v1 I(41109831670569663658300086939077404909608122265524774868353822811305361) I(9) B+ I(1) B% B/ v1 I(369988485035126972924700782451696644186473100389722973815184405301748249) I(9) B+ I(1) B% B/ v1 I(3329896365316142756322307042065269797678257903507506764336659647715734241) I(9) B+ I(1) B% B/ v1 I(29969067287845284806900763378587428179104321131567560879029936829441608169) I(9) B+ I(1) B% B/ v1 I(269721605590607563262106870407286853611938890184108047911269431464974473521) I(9) B+ I(1) B% B/ v1 I(2427494450315468069358961833665581682507450011656972431201424883184770261689) I(9) B+ I(1) B% B/ v1 I(21847450052839212624230656502990235142567050104912751880812823948662932355201) I(9) I(1)
'''
eff11 = [Str("solve efficiency11 100573847453233330105890470844482405072957615231969369459908387717689164043268")]


# problem 12
'''
# raw
B$ B$ y L3 L4
B$ B$ L1 L2
(? B< v1 v2 v1 v2) v4 B+ I(1)
(? (B> v4 I(2)) (B$ B$ B$ y L5 L6 L7
(? (B= v6 v4) v7 (B$ (B$ v5 B+ v6 I(1))
  (? (B> B$ v3 v6 B- v6 I(1))
    (? (B= B% v4 v6 I(0))
      (B* B/ v7 B$ v3 v6 B- B$ v3 v6 I(1))
      v7)
  v7)))
I(2) v4)
v4)
I"Ndb(1234567)

# pseudocode
B$ B$ y L3 L4
# return the minimum of
B$ B$ L1 L2
if (v1 < v2) v1 else v2
# x
v4
# 1 + (x > 2)
(1 +
if (v4 > 2)
  # g(y,z)
  B$ B$ B$ y L5 L6 L7
  # if y == x: return z
  if (v6 == v4) v7
  else
    v5(v6 + 1,
    if (v3(v6) > (v6 - 1))
       if (v4 % v6 == 0) (v7 / v3(v6)) * (v3(v6)-1)
       else v7
    else v7)
  # call g(2,x)
  I(2) v4
else:
  v4
I(1234567)
'''
eff12 = [Str("solve efficiency12 1224721")]

# problem 13
'''
B$ B$ y L3 L4
# strlen
if (v4 == '') return 0
B+ I(1)
v3(v4[1:])
# applied to
B$ L2 B.
# apply f 28 times to 'na'
B$ v2 B$ v2 B$ v2 B$ v2 B$ v2 B$ v2 B$ v2 B$ v2 B$ v2 B$ v2 B$ v2 B$ v2 B$ v2 B$ v2 B$ v2 B$ v2 B$ v2 B$ v2 B$ v2 B$ v2 B$ v2 B$ v2 B$ v2 B$ v2 B$ v2 B$ v2 B$ v2 B$ v2 'na'
# append 'heyjude'
'heyjude'
# f = double string
L1 B. v1 v1
'''
eff13 = [Str("solve efficiency13 536870919")]
