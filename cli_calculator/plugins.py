import importlib
import os

def load_plugins():
    plugins = {}
    for filename in os.listdir('plugins'):
        if filename.endswith('.py'):
            module_name = filename[:-3]
            module = importlib.import_module(f'plugins.{module_name}')
            plugins[module_name] = module.PluginCommand()
    return plugins
