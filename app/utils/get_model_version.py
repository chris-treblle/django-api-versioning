from importlib import import_module


class ObjectNotFound(Exception):
    pass


def get_model_version(api_version: str, object_name: str):
    try:
        object_module = import_module(f'app.{api_version}.models.{object_name}')
        object_class = getattr(object_module, object_name)

        return object_class
    except ImportError:
        try:
            object_module = import_module(f'app.models.{object_name}')
            object_class = getattr(object_module, object_name)

            return object_class
        except ImportError:
            raise ObjectNotFound(f"{object_name} not found in API version '{api_version}' or base version.")
