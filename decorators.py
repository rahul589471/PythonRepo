def smart_div(fn):
    def inner_div(m, n):
        if m < n:
            m, n = n, m;
        return fn(m, n);

    return inner_div;


@smart_div
def div(a, b):
    return a / b;


res = div(2, 4);

print(res);
