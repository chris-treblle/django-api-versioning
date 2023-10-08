import os
import importlib

config_dir = os.path.dirname(__file__) + '/../config'

module_files = [file[:-3] for file in os.listdir(config_dir) if file.endswith('.py')]

for module_name in module_files:
    module = importlib.import_module(f'config.{module_name}')
    globals().update(vars(module))