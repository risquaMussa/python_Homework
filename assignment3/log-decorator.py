#Task 1: Writing and Testing a Decorator
import logging

logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a"))



def logger_decorator(func):
    def wrapper(*args, **kwargs):
        logger.info(f"function: {func.__name__}")
        if args:
            logger.info(f"positional parameters: {args}")
        else:
            logger.info("positional parameters: none")
            
        if kwargs:
            logger.info(f"keyword parameters: {kwargs}")
        else:
            logger.info("keyword parameters: none")

        result = func(*args, **kwargs)
    
        logger.info(f"return: {result}")

        return result
    return wrapper

@logger_decorator
def hello():
    return "Hello, World!"



@logger_decorator
def add(a, b):
    return a + b


@logger_decorator
def variable_args(*args):
    return True


@logger_decorator
def keyword_args(**kwargs):
    return kwargs
                  


print(hello())
print(add(3, 5))
print(variable_args(1, 2, 3, 4, 5))
print(keyword_args(name="Alice", age=30))

