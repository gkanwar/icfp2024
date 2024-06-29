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
