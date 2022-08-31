def http_methods_enable(*methods):
    def decorator(cls):
        cls.http_method_names = [method for method in cls.http_method_names if method in methods]
        return cls
    return decorator

    