import functools


def make_html(tag=None):
    def make_html_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if tag:
                return f'<{tag}>{func(*args, **kwargs)}</{tag}>'
            else:
                return func(*args, **kwargs)
        return wrapper
    return make_html_decorator


@make_html('del')
def get_text(text):
    return text


print(get_text('Python'))


@make_html('i')
@make_html('del')
def get_text(text):
    return text


print(get_text(text='decorators are so cool!'))