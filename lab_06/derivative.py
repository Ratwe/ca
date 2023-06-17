def one_side_left_dif_derivative(h, ys_i, ys_i_l_1 = None):
    if ys_i_l_1 != None:
        return '{0:.3f}'.format((ys_i - ys_i_l_1) / h)
    else:
        return "None"

def center_dif_derivative(h, ys_p_1 = None, ys_m_1 = None):
    if ys_p_1 != None and ys_m_1 != None:
        return '{0:.3f}'.format((ys_p_1 - ys_m_1) / 2 / h)
    else:
        return "None"

def second_runge_formula(left_dif_derivative_s_1, left_dif_derivative_s_2,  m, p):
    return '{0:.3f}'.format(left_dif_derivative_s_1 + (left_dif_derivative_s_1 - left_dif_derivative_s_2) / (m ** p - 1))

def derivative_with_align_vars(teta1, teta2, xsi1, xsi2, y1, x1):
    return '{0:.3f}'.format(((teta2 - teta1) / (xsi2 - xsi1) - 1 / y1) / (- x1 / (y1 ** 2)))

def second_dif_derivative(h, ys_p_1 = None, ys = None, ys_m_1 = None):
    if ys_p_1 != None and ys_m_1 != None:
        return '{0:.3f}'.format((ys_p_1 - 2 * ys + ys_m_1) / (h ** 2))
    else:
        return "None"
