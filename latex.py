import sympy as sp
from sympy import latex
import re

def latex_to_sympy_matrix(latex_str):
    pattern = r'\\begin\{pmatrix\}(.*?)\\end\{pmatrix\}'
    match = re.search(pattern, latex_str, re.DOTALL)
    if not match:
        raise ValueError("Не удалось найти матрицу в формате pmatrix.")
    
    matrix_content = match.group(1)
    
    rows = re.split(r'\\\\', matrix_content)
    
    matrix = []
    for row in rows:
        row = row.strip().replace('\n', '')
        if not row:
            continue  
        elements = row.split('&')
        numeric_elements = [sp.sympify(elem.strip()) for elem in elements]
        matrix.append(numeric_elements)
    
    return sp.Matrix(matrix)

def fixed_latex(ans):
    return latex(ans).replace("matrix", "pmatrix")\
                     .replace('\\' + "right]", "")\
                     .replace('\\' + "left[", "")